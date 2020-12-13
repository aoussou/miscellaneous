#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:58:20 2019

@author: next
"""

import cv2
import math
import numpy as np
import os
import copy
import json
import shutil
        
###############################################################################
# CREATE UNEXISTENT FOLDERS
def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
###############################################################################
'''
0'Nose'
1'EyeLeft'
2'EyeRight'
3'EarLeft'
4'EarRight'
5'ShoulderLeft'
6'ShoulderRight'
7'ElbowLeft'
8'ElbowRight'
9'WristLeft'
10'WristRight'
11'HipLeft'
12'HipRight'
13'KneeLeft'
14'KneeRight'
15'AnkleLeft'
16'AnkleRight'
'''

###############################################################################
l_eye_nose = ([0,1],(182, 0, 255))
r_eye_nose = ([0,2], (182, 0, 255))

r_ear_eye = ([1,3], (182, 0, 255))
l_ear_eye = ([2,4],(255, 255, 0))


l_upper_arm = [[5,7],(0, 0, 255)]
r_upper_arm = [[6,8],(255, 0, 125)]

l_lower_arm = [[7,9],(0, 0, 255)]
r_lower_arm = [[8,10],(255, 0, 125)]

l_thigh = [[11,13],(0, 137, 232)]
r_thigh = [[12,14],(86, 232, 12)]

l_calf = [[13,15],(0, 137, 232)]
r_calf = [[14,16],(86, 232, 12)]

l_trunk = [[5,11],(0, 255, 255)]
r_trunk = [[6,12],(0, 255, 255)]

pelvis = [[11,12],(0, 255, 255)]
shoulders = [[5,6],(0, 255, 255)]
 
list_limbs = [l_eye_nose,
              r_eye_nose,
              r_ear_eye,
              l_ear_eye,
              l_upper_arm,
              r_upper_arm,
              l_lower_arm,
              r_lower_arm,
              l_thigh,
              r_thigh,
              l_calf,
              r_calf,
              l_trunk,
              r_trunk,
              pelvis,
              shoulders
              ]

#list_limbs = [r_upper_arm,r_lower_arm]
#list_limbs = [l_thigh,l_calf]
###############################################################################
def drawline(img,pt1,pt2,color,thickness=1,gap=20):
    dist =((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**.5
    pts= []
    for i in  np.arange(0,dist,gap):
        r=i/dist
        x=int((pt1[0]*(1-r)+pt2[0]*r)+.5)
        y=int((pt1[1]*(1-r)+pt2[1]*r)+.5)
        p = (x,y)
        pts.append(p)

    for p in pts:
        cv2.circle(img,p,thickness,color,-1)

###############################################################################
def plot_limbs(img,a,b,color,thickness):
    cv2.line(img, (int(a[0]), int(a[1])), (int(b[0]), int(b[1])), color, thickness)    
    
    
###############################################################################
def plot_limbs_dotted(img,a,b,color,thickness):
    drawline(img,a,b,color,thickness)
###############################################################################

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n*multiplier + 0.5) / multiplier)


colours = [[0,0,255],[255,0,0],[0,255,0]]

colours_vp = [[0,0,0],[255,255,255],[128,128,128]]

plot_joints = True
limb_color = 'by_limb'


kpts_npy = np.load('keypoints2d.npy')
name = 'synth'
save_dir_images = os.path.join('output','kpts_images',name)
shutil.rmtree(save_dir_images)
create_dir(save_dir_images)

for n_array, npy in enumerate(kpts_npy) :
    img = np.ones((720,1280,3))*255
    print(n_array)
    try:
        vp_kps = npy.reshape(30,3)
    except:
        try:
            vp_kps = npy.reshape(30,2)  
        except :
            print('matrix format problem')
    vp_kps = vp_kps[[1,2,3,4,5,8,9,10,11,12,13,22,23,24,25,26,27],] 

        
    if plot_joints:
        for i in range(len(vp_kps)) :
            vp_coords = (round_half_up(vp_kps[i][0]),  round_half_up(vp_kps[i][1]))
            img = cv2.circle(img,vp_coords , 1, colours_vp[0], thickness=3, lineType=1, shift=0) 
            #img = cv2.putText(img, str(scores[i])[:4], vp_coords,cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255))
            
    for limb in list_limbs:

        a = vp_kps[limb[0][0]]
        b = vp_kps[limb[0][1]]
        
        if (a[0] + a[1]!=0) and (b[0] + b[1]!=0) :

            if limb_color == 'by_limb':
                plot_limbs(img,a,b,limb[1],3)
            elif limb_color == 'by_person':
                plot_limbs_dotted(img,a,b,colours[0],3)  

    save_path = os.path.join(save_dir_images,str(n_array).zfill(5) + '.jpg')
    cv2.imwrite(save_path,img)




  