#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:32:53 2024

@author: benhenderson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:45:51 2024

@author: benhenderson
"""

import pandas as pd

data_file = pd.read_csv("for_nitpicker.dat", delimiter = "\t", header = None)
column_names = ["Date", "Time", "Depth (m)", "Temperature", "Salinity (psu)"]
data_file.columns = column_names

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, sharey = True)
ax[0].plot(data_file["Temperature"], data_file["Depth (m)"], color = 'b')
ax[1].plot(data_file["Salinity (psu)"], data_file["Depth (m)"], color = 'r')
ax[0].set_title("Temperature Profile")
ax[1].set_title("Salinity Profile")
ax[0].set_ylabel("Depth (m)")
ax[1].set_ylabel("Depth (m)")
ax[0].set_xlabel("Temperature (degrees c)")
ax[1].set_xlabel("Salinity (psu)")

