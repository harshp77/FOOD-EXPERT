from cProfile import label
import cv2 as cv
import numpy as np
import pandas as pd
import random as rng
import os
import math



def prepros(img):
    img = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
    # img = cv.resize(img,(1080,1920),interpolation=cv.INTER_AREA)
    gauss = cv.GaussianBlur(img, (7,7),0)
    ret3,th3 = cv.threshold(gauss,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    dialate = cv.dilate(th3, None, iterations=1)
    erode = cv.erode(dialate, None, iterations=1) 
    canny = cv.Canny(erode,150,200) 
    prepros.contours,prepros.hierarchy=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)


def featstr(contours,img):
    featstr.areacontt = []
    featstr.label=[]
    featstr.MajbyMin = []
    featstr.eccentricity =[]
    featstr.chalkratio = []
    featstr.rgbmean = []


    for t in range(len(contours)):
       areacont = ((cv.contourArea(contours[t]))*0.26*0.26) 
       featstr.areacontt.append(areacont)
    mean_area = round((sum(featstr.areacontt)/len(featstr.areacontt)),2)
    featstr.maxstrech = round((2*mean_area),2)
    featstr.minstrech = round((0.5*mean_area),2)
    featstr.coinarea = max(featstr.areacontt)
    act = 490
    featstr.regu = featstr.coinarea/act
    featstr.areacontt = []

    minEllipse = [None]*len(contours)
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
        if c.shape[0] > 5:
            minEllipse[i] = cv.fitEllipse(c)

    for i, c in enumerate(contours):
        areacont = ((cv.contourArea(contours[i]))*0.26*0.26)
        if featstr.minstrech<areacont<featstr.maxstrech:
            areacont = round((areacont/featstr.regu),2)
            color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
            if c.shape[0] > 5:
                cv.ellipse(img, minEllipse[i], color, 2)
                (xc,yc),(d1,d2),angle = minEllipse[i]

            if angle > 90:
                angle = angle - 90
            else:
                angle = angle + 90
            x,y,w,h = cv.boundingRect(contours[i])
            r,g,b,z = cv.mean(img[y:y+h,x:x+w])
            rgbmean=round(((r+g+b)/3),2)
            rmajor = max(d1,d2)/2
            xtop = int(xc + math.cos(math.radians(angle))*rmajor)
            ytop = int(yc + math.sin(math.radians(angle))*rmajor)
            xbot = int(xc + math.cos(math.radians(angle+180))*rmajor)
            ybot = int(yc + math.sin(math.radians(angle+180))*rmajor)
            cv.line(img, (xtop,ytop), (xbot,ybot), (0, 0, 255), 1)
            major_length  = math.sqrt(((xtop-xbot)**2)+((ytop-ybot)**2))


            rminor = min(d1,d2)/2
            xtop = int(xc + math.cos(math.radians(angle))*rminor)
            ytop = int(yc + math.sin(math.radians(angle))*rminor)
            xbot = int(xc + math.cos(math.radians(angle+180))*rminor)
            ybot = int(yc + math.sin(math.radians(angle+180))*rminor)
            cv.line(img, (xtop,ytop), (xbot,ybot), (0, 0, 255), 1)
            minor_length  = math.sqrt(((xtop-xbot)**2)+((ytop-ybot)**2))
            label = 3
            b = minor_length/major_length
            areacont = round(areacont,2)
            if b>=0.73:
                featstr.MajbyMin.append(round((b),2))
                featstr.eccentricity.append(round((math.sqrt(1-(b)**2)),2))            
                featstr.label.append(label)
                featstr.areacontt.append(areacont)
                featstr.rgbmean.append(rgbmean)
            # featstr.chalkratio.append(round(((areacont)/(math.pi*minor_length*major_length*0.26*0.26*0.26)),2))


        
    # cv.imshow('Contours', img)
    # cv.waitKey(0)


for subdir, dirs, files in os.walk('Arahar Sample'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".png"):
            count  = 0
            img = cv.imread(filepath)
            prepros(img)
            featstr(prepros.contours,img)
            if os.path.isfile('G3-2-araharclr.csv'):
                count =1
            
            if (count==0):
                # df1=pd.DataFrame(featstr.eccentricity, columns=['Eccentricity']) 
                # # df2=pd.DataFrame(featstr.chalkratio, columns=['chalkratio']) 
                # df3=pd.DataFrame(featstr.MajbyMin, columns=['MinbyMaj']) 
                df4=pd.DataFrame(featstr.label,columns=['Label'])
                # df5=pd.DataFrame(featstr.areacontt,columns=["area"])
                df7=pd.DataFrame(featstr.rgbmean,columns=['rgb'])
                result = pd.concat([df7, df4], axis=1)
                result.to_csv('G3-2-araharclr.csv')
            elif (count==1):
                # df1=pd.DataFrame(featstr.eccentricity, columns=['Eccentricity']) 
                # # df2=pd.DataFrame(featstr.chalkratio, columns=['chalkratio']) 
                # df3=pd.DataFrame(featstr.MajbyMin, columns=['MinbyMaj']) 
                df4=pd.DataFrame(featstr.label,columns=['Label'])
                # df5=pd.DataFrame(featstr.areacontt,columns=["area"])
                df7=pd.DataFrame(featstr.rgbmean,columns=['rgb'])
                result2 = pd.concat([df7, df4], axis=1)
                frames = [result,result2]
                df3 = pd.concat(frames,ignore_index=True)
                result = df3
                df3.to_csv('G3-2-araharclr.csv')
                





    