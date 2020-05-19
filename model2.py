import os
from PIL import Image       # Pillow
from pytesseract import *   # pytesseract
import sys
import csv
import cv2                   # OpenCV
import pandas as pd  
import json

def make_table(fname):    
    img   = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)                   
    blur  = cv2.GaussianBlur(img,(5,5),0)                                 # Image Preprocessing
    #blur = cv2.medianBlur(img,5)
    retval, blur = cv2.threshold(img,150,255, cv2.THRESH_BINARY)
    txt   = image_to_string(blur, lang='eng', config='--oem 1 --psm 6 -c preserve_interword_spaces=0')   

    txt   = txt.replace('= ', '')
    txt   = txt.replace('“', '')
    txt   = txt.replace('| ', '')
    txt   = txt.replace(' |', '')
    txt   = txt.replace('|', '')
    txt   = txt.replace('_', ' ')
    txt   = txt.replace('((', '[(')
    txt   = txt.replace(' (', '(')
    txt   = txt.replace('L ', 'L_')
    txt   = txt.replace('R ', 'R_')
    txt   = txt.replace('T ', 'T_')
    txt   = txt.replace('{', '[')
    txt   = txt.replace('ie)', '93')
    txt   = txt.replace('Areacm’]', 'Area[cm^2]')
    txt   = txt.replace('cm’', 'cm^2')
    txt   = txt.replace('k R', 'k_R')
    txt   = txt.replace('e M', 'e_M')
    txt   = txt.replace('$', '8')
    txt   = txt.replace('ES', 'L1,L3')
    txt   = txt.replace('12-13', 'L1-L3')
    txt   = txt.replace('L113', 'L1,L3')
    txt   = txt.replace('L214', 'L2,L4')
    txt   = txt.replace('O85', '95')
    txt   = txt.replace('S519,', '35.17')
    txt   = txt.replace('3339', '33.39')
    txt   = txt.replace('Ll', 'L1')
    txt   = txt.replace('Wis', '71.55')
    txt   = txt.replace('\n\n', '\n')
    txt   = txt.replace('  ', ' ')                
    txt_s = txt.split('\n')                                   # OCR 및 text Preprocessing

    L1    = []                         
    column = ['Region', 'Area[cm^2]', 'BMC[(g)]', 'BMD[g/cm^2]', 'Fat[(g)]', 'Lean[(g)]', 'Lean + BMC[(g)]', 'Total[(g)]', '% Fat[(g)]', 'T-score', 'PR (Peak Reference)', 'Z-score', 'AM (Age Matched)']

    for i in range(len(txt_s)):
        t = txt_s[i].split(' ')    
        L1.append(t)               
    test  = pd.DataFrame(L1[2:], columns=column)
    Path = '{}.csv'.format(fname.replace('img_DB', 'csv_DB'))    
    test.to_csv(Path, encoding='utf-8-sig', header=False, index=False)      # 표 제작 및 excel file로 추출

