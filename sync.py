#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:32:07 2022

@author: joe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
import os
import ffmpeg



df = pd.DataFrame()
df['x'] = []
df['y'] = []
df2 = df
df3 = df
df4 = df
df5 = df
df6 = df
df7 = df

x = []
y = []

for i in range(1,100):
    for j in range(1,100):
        x.append(i)
        y.append(j)
        
df['x'] = x
df['y'] = y

dfBase = df

df['p'] = np.random.randint(1, 100, df.shape[0])

images = []

for j in range(1,(6*60+1)):
    df['i'] = 1 / ( 1 + math.e ** ( -1 * ( df['p'] / 20 ) ) )
    df['i'] = df['i'] - 0.5
    df['i'] = df['i'] * 2
    df['i'] = 1 - df['i']
    df['i'] = 12 * df['i']
    
    df['p'] = df['p'] + df['i']
    
    df2 = df[ df['p'] > 100 ]
    bump = df2.size * 24
    
    plt.ioff()
    plt.clf()
    fig = plt.figure(figsize=(4,4), dpi=300, constrained_layout=True)
    fig.set_facecolor('black')
    ax1 = fig.add_subplot()
    ax1.set_facecolor('black')
    # ax1.scatter(dfBase['x'],dfBase['y'],marker="o",s=10,c='snow')
    # ax1.scatter(df7['x'],df7['y'],marker="o",s=5,c='whitesmoke')
    # ax1.scatter(df6['x'],df6['y'],marker="o",s=5,c='lightgray')
    # ax1.scatter(df5['x'],df5['y'],marker="o",s=5,c='silver')
    # ax1.scatter(df4['x'],df4['y'],marker="o",s=5,c='darkgray')
    # ax1.scatter(df3['x'],df3['y'],marker="o",s=5,c='gray')
    # ax1.scatter(df2['x'],df2['y'],marker="o",s=5,c='dimgray')
    ax1.scatter(dfBase['x'],dfBase['y'],marker="o",s=1,c='black')
    ax1.scatter(df7['x'],df7['y'],marker="o",s=1,c='dimgray')
    ax1.scatter(df6['x'],df6['y'],marker="o",s=1,c='darkgoldenrod')
    ax1.scatter(df5['x'],df5['y'],marker="o",s=1,c='goldenrod')
    ax1.scatter(df4['x'],df4['y'],marker="o",s=1,c='gold')
    ax1.scatter(df3['x'],df3['y'],marker="o",s=1,c='palegoldenrod')
    ax1.scatter(df2['x'],df2['y'],marker="o",s=1,c='lightgoldenrodyellow')
    ax1.set_axis_off()
    ax1.set_xlim([1, 99])
    ax1.set_ylim([1, 99])
    
    if j < 10:
        figure = 'outputs/00{}_plot.png'.format(j)
        fig.savefig(figure)
    elif j >= 10 and j < 100:
        figure = 'outputs/0{}_plot.png'.format(j)
        fig.savefig(figure)
    else:
        figure = 'outputs/{}_plot.png'.format(j)
        fig.savefig(figure)
        
    images.append(figure)
    
    plt.clf()
    plt.close(fig)
    
    df7 = df6
    df6 = df5
    df5 = df4
    df4 = df3
    df3 = df2
    
    df.loc[df['p'] > 100, 'p'] = 1
    
print(df)

#

image_folder = 'outputs'
video_name = 'video.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 

#images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, fourcc, 6, (width,height))

for image in images[5:]:
    video.write(cv2.imread(os.path.join(image)))

cv2.destroyAllWindows()
video.release()






