#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:14:02 2020

@author: john
"""

#Program for converting .mts files to .mp4 files 
 
import subprocess
import os
import argparse

def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def convert(original_dir,save_dir) :
    
    create_dir(save_dir)    
    list_vid = os.listdir(original_dir)
    
    for vid in list_vid:
        name =  os.path.splitext(vid)[0]
        path_vid = os.path.join(original_dir,vid)
        save_path = os.path.join(save_dir,name+'.mp4')
        subprocess.run(['ffmpeg', '-i', path_vid, save_path])
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--original_dir', default=None, help='directory path of videos')
    args = parser.parse_args()
    parser.add_argument('-o','--save_dir', default=args.original_dir + '_mp4', help='path where converted videos are to be saved')
    args = parser.parse_args()
    convert(args.original_dir,args.save_dir)