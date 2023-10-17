import cv2 as cv
import joblib
import numpy as np
import pandas as pd
import random as rng
import os
import statistics
import math


# img = cv.imread('Arahar Sample\Screenshot 2022-02-18 002719.png')
# img = cv.imread('ref\Screenshot 2022-01-25 005348.png')
# img = cv.imread('Arahar Sample\Screenshot 2022-02-18 002745.png')
img = cv.imread('Screenshot 2022-04-09 021909.png')
model = joblib.load("Model.joblib")


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
    predictt=[]


    for t in range(len(contours)):
       areacont = ((cv.contourArea(contours[t]))*0.26*0.26) 
       featstr.areacontt.append(areacont)
    mean_area = round((sum(featstr.areacontt)/len(featstr.areacontt)),2)
    featstr.maxstrech = round((2*mean_area),2)
    featstr.minstrech = round((0.5*mean_area),2)
    featstr.coinarea = max(featstr.areacontt)
    act = 490
    regu = featstr.coinarea/act
    featstr.areacontt = []


    minEllipse = [None]*len(contours)
    boundRect = [None]*len(contours)
    contours_poly = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
        if c.shape[0] > 5:
            minEllipse[i] = cv.fitEllipse(c)
    ctr=0
    for i, c in enumerate(contours):
        areacont = ((cv.contourArea(contours[i]))*0.26*0.26)
        # if featstr.minstrech<areacont<featstr.maxstrech:
        areacont = round((areacont/regu),2)
        x1,y2=(int(boundRect[i][0]) , int(boundRect[i][1]+boundRect[i][3]))
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        if c.shape[0] > 5:
            cv.ellipse(img, minEllipse[i], color, 2)
            (xc,yc),(d1,d2),angle = minEllipse[i]

        if angle > 90:
            angle = angle - 90
        else:
            angle = angle + 90


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
        b = (minor_length)/(major_length)
        vall = np.array([[ round((math.sqrt(1-(b)**2)),2) , round((math.sqrt(1-(b)**2)),2) ,  round((minor_length/major_length),2) , round((minor_length/major_length),2) , round(areacont), round(areacont) ]])
        df78 = pd.DataFrame(vall, columns = ['Eccentricity','eccen_mean','MinbyMaj','minby_mean','area','area_mean'])
        label = model.predict(df78)
        z=str(label)
        z = z[1::]
        z = z[:-1:]
        
        if (z[1::]) == '.':
            z = z[:-1:]
            z=int(z)
            cv.putText(img, ('Catgory '+str(z)), (x1, y2-40), cv.FONT_HERSHEY_SIMPLEX, 0.30, (color), 1) 
            cv.putText(img, ('length '+str(major_length*regu)), (x1, y2-50), cv.FONT_HERSHEY_SIMPLEX, 0.30, (color), 1)               
            cv.putText(img, ('area '+str(areacont)), (x1, y2-60), cv.FONT_HERSHEY_SIMPLEX, 0.30, (color), 1)               
        else :
            z = int(round(float(z)))
            cv.putText(img, ('Catgory '+str(z)), (x1, y2-40), cv.FONT_HERSHEY_SIMPLEX, 0.30, (color), 1)
            cv.putText(img, ('length '+str(major_length*regu)), (x1, y2-50), cv.FONT_HERSHEY_SIMPLEX, 0.30, (color), 1)
            cv.putText(img, ('area '+str(areacont)), (x1, y2-60), cv.FONT_HERSHEY_SIMPLEX, 0.30, (color), 1)
        predictt.append(z)
        ctr=ctr+1
    # print(ctr)
    cv.imshow('',img)
    cv.waitKey(0)
    c1 ,c2 , c3 = 0,0,0
    for i in predictt:
        if i == 1:
            c1=c1+1
        elif i==2:
            c2=c2+1
        elif i==3:
            c3=c3+1
    cv.putText(img, ('percent grade1 daal is ' + str(round((c1/(len(predictt))),2))), (100-50,100-50), cv.FONT_HERSHEY_SIMPLEX, 0.40, (36,255,12), 1)
    cv.putText(img, ('percent grade2 daal is ' + str(round((c2/(len(predictt))),2))), (120-50,120-50), cv.FONT_HERSHEY_SIMPLEX, 0.40, (36,255,12), 1)
    cv.putText(img, ('percent grade3 daal is ' + str(round((c3/(len(predictt))),2))), (140-50,140-50), cv.FONT_HERSHEY_SIMPLEX, 0.40, (36,255,12), 1)              
    print('percent grade1 daal is ' + str(round((c1/(len(predictt))),2)))
    print('percent grade2 daal is ' + str(round((c2/(len(predictt))),2)))
    print('percent grade3 daal is ' + str(round((c3/(len(predictt))),2)))


prepros(img)
featstr(prepros.contours ,img)
cv.imshow('',img)
cv.imshow('',img)
cv.waitKey(0)






















