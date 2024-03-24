#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:46:25 2024

@author: benhenderson
"""

import pandas as pd

import numpy as np

data = pd.read_csv("data/SAA2_WC_2017_metocean_10min_avg.csv")
data["TIME_SERVER"] = pd.to_datetime(data["TIME_SERVER"], format = "%Y/%m/%d %H:%M")
data["TIME_GPS"] = pd.to_datetime(data["TIME_GPS"], format = "%H:%M:%S").dt.time
data.set_index("TIME_SERVER", inplace = True)

def ddmm2dd(ddmm):
    thedeg = np.floor(ddmm/100.)     
    themin = (ddmm-thedeg*100.)/60.     
    return thedeg+themin

data["LONGITUDE"] = ddmm2dd(data["LONGITUDE"])
data["LATITUDE"] = ddmm2dd(data["LATITUDE"])


data_sample = data["2017-06-28 17:10:00":"2017-07-04 23:50:00"]

import matplotlib.pyplot as plt

plt.style.use("grayscale")
fig, ax = plt.subplots()
ax.plot(data_sample.index, data_sample["TSG_TEMP"])
plt.xticks(rotation = 90)
ax.set_title("Temperature over Time")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature (degrees c)")

fig, ax = plt.subplots()
bins = np.arange(30, 35, 0.5)
ax.hist(data_sample["TSG_SALINITY"], bins = bins)
ax.set_xlabel("Salinity")
ax.set_ylabel("# of observations")

data_sample.set_index("LATITUDE", inplace = True)
plt.style.use("default")
fig, ax = plt.subplots()
ax.scatter(data_sample["WIND_SPEED_TRUE"], data_sample["AIR_TEMPERATURE"], c = data_sample.index)
ax.set_xlabel("Wind Speed (m/s)")
ax.set_ylabel("Air Temperature (degrees c)")

fig.savefig("wind_speed-air_temp.png", dpi = 200)












