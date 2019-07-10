#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:28:22 2019

@author: ocnc
"""

import numpy as np
import matplotlib.pyplot as plt

spkid = np.array(sim.simData['spkid'].to_python())
spkt = np.array(sim.simData['spkt'].to_python())

_, ax = plt.subplots()
ax.plot(spkt, spkid, '|')

# only stimulus
stimt = spkt[spkid==1] #select the spkt which have the spkid 1.
_, ax = plt.subplots()
ax.plot(stimt, np.ones(stimt.size), '|')

# the same result with a different method
stimt = []
for i, spikes in enumerate(spkt):
    if spkid[i]==1:
        stimt.append(spikes)

_, ax = plt.subplots()
ax.plot(stimt, spkid, '|')