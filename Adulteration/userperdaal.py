import pandas as pd
import numpy as np
import joblib
from prepross import *

img = cv.imread("ref\g1pure2.png")
# model = joblib.load("Color_Model.joblib")


# Image.user_extractor(img,model)
Image.user_extractor(img)


