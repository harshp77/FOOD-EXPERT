

from __future__ import print_function
import io,os,sys,time,threading,ctypes,inspect,traceback
from operator import index
from statistics import mode
from PIL import Image as im

def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("Timeout Exception")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
    
def text_thread_run(code):
    try:
        env={}
        exec(code, env, env)
    except Exception as e:
        print(e)
    
#   This is the code to run Text functions...
def mainTextCode(path):
    import cv2 as cv
    import joblib
    import numpy as np
    import pandas as pd
    import random as rng
    import os
    import statistics
    import math
    from os.path import dirname, join

    img_path = path[1:]
    modelSel = path[0:1]



    filename1 = join(dirname(__file__), "arahar.joblib")
    filename3 = join(dirname(__file__), "channa.joblib")
    filename4 = join(dirname(__file__), "masoor.joblib")
    filename2 = join(img_path)

    img = cv.imread(filename2)
    # img = cv.imread('ref\Screenshot 2022-01-25 005348.png')
    # img = cv.imread('Arahar Sample\Screenshot 2022-02-18 002745.png')
    # img = cv.imread('ref\masor brokeen.png')
    # model = joblib.load(filename1)

    if modelSel == 'M':
        model = joblib.load(filename4)
    elif modelSel == 'C':
        model = joblib.load(filename3)
    elif modelSel == 'A':
        model = joblib.load(filename1)



    def prepros(img):
        img = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
        # img = cv.resize(img,(1080,1920),interpolation=cv.INTER_AREA)
        gauss = cv.GaussianBlur(img, (7,7),0)
        ret3,th3 = cv.threshold(gauss,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        dialate = cv.dilate(th3, None, iterations=1)
        erode = cv.erode(dialate, None, iterations=1) 
        canny = cv.Canny(erode,150,200) 
        prepros.contours,prepros.hierarchy=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
        # print(prepros.contours)



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

        for i, c in enumerate(contours):
            areacont = ((cv.contourArea(contours[i]))*0.26*0.26)
            if featstr.minstrech<areacont<featstr.maxstrech:
                areacont = round((areacont/regu),2)
                x1,y2=(int(boundRect[i][0]) , int(boundRect[i][1]+boundRect[i][3]))
                color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
                if c.shape[0] > 5:
                    cv.ellipse(img, minEllipse[i], color, 5)
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
                major_length  = math.sqrt(((xtop-xbot)**2)+((ytop-ybot)**2))


                rminor = min(d1,d2)/2
                xtop = int(xc + math.cos(math.radians(angle))*rminor)
                ytop = int(yc + math.sin(math.radians(angle))*rminor)
                xbot = int(xc + math.cos(math.radians(angle+180))*rminor)
                ybot = int(yc + math.sin(math.radians(angle+180))*rminor)
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
                    cv.putText(img, ('Catgory '+str(z)), (x1, y2-100), cv.FONT_HERSHEY_SIMPLEX, 2, (color), 5)            
                else :
                    z = int(round(float(z)))
                    cv.putText(img, ('Catgory '+str(z)), (x1, y2-100), cv.FONT_HERSHEY_SIMPLEX, 2, (color), 5)
                predictt.append(z)

        featstr.c1 ,featstr.c2 , featstr.c3 = 0,0,0
        for i in predictt:
            if i == 1:
                featstr.c1=featstr.c1+1
            elif i==2:
                featstr.c2=featstr.c2+1
            elif i==3:
                featstr.c3=featstr.c3+1
        featstr.lenn = len(predictt)          



    prepros(img)
    featstr(prepros.contours ,img)
    G1 = int(round((featstr.c1/(featstr.lenn)),2)*100)
    G2 = int(round((featstr.c2/(featstr.lenn)),2)*100)
    G3 = int(round((featstr.c3/(featstr.lenn)),2)*100)
    index = (int(G1*1 +G2*0.7 +G3*0.5))

    print('Percentage of Grade_1 daal ' + str(int(round((featstr.c1/(featstr.lenn)),2)*100)))
    print('Percentage of Grade_2 daal ' + str(int(round((featstr.c2/(featstr.lenn)),2)*100)))
    print('Percentage of Grade_3 daal ' + str(int(round((featstr.c3/(featstr.lenn)),2)*100)))
    print('')
    print('')
    print('Average Daal Quality ' + str(index))
    path = filename2[0:39]+'imgg.png'
    cv.imwrite(path,img)
    