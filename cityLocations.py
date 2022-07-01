#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:58:29 2022

@author: joe
"""

import pandas as pd
import matplotlib.pyplot as plt
import math

cities = pd.read_csv('cities500.csv')

print(cities)

cities = cities[ cities['lat'] >= 0 ]

cities['r'] = cities['elv']**0.4 + 50

cities['x'] = cities.apply(lambda x: ( math.cos(x['lat']) * math.cos(x['lon']) * x['r'] ), axis=1)
cities['y'] = cities.apply(lambda x: ( math.cos(x['lat']) * math.sin(x['lon']) * x['r'] ), axis=1)
cities['z'] = cities.apply(lambda x: ( math.sin(x['lat']) * x['r'] ) * 1.2, axis=1)                       




for angle in range(-180,180,60):

    plt.ioff()
    plt.clf()
                
    fig = plt.figure(figsize=(8,8), dpi=300, constrained_layout=True)
                
    ax1 = fig.add_subplot(projection='3d')
    
    ax1.scatter3D(cities['x'], cities['y'], cities['z'], zdir='z', s=0.2, c=-cities['pop']**0.1, cmap='bone', marker='o', depthshade=True)
                      
    ax1.set_axis_off()
    ax1.view_init(0, angle) # elev, axim
    
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_zticks([])
    ax1.grid(False)
    ax1.set_axis_off()
    
    ax1.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    
    axisMax = 60
    axisMin = -axisMax
    
    ax1.set_xlim3d(axisMin, axisMax)
    ax1.set_ylim3d(axisMin, axisMax)
    ax1.set_zlim3d(axisMin, axisMax)
    
    #ax1.set_aspect(1)
                
    fig.savefig('outputs/test_cities_{}.png'.format(angle))
                
    plt.clf()
    plt.close(fig)