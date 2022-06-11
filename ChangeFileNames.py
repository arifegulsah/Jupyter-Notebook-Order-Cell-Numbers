# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:43:35 2022

@author: arife
"""

import glob
import os

path = r"WHOLE_PATH"
pattern = path + "*.png"

result = glob.glob(pattern)

count = 1
for file_name in result:
    old_name = file_name
    new_name = path + 'NEW_NAME_' + str(count) + ".png"
    os.rename(old_name, new_name)
    count = count + 1

# printing all revenue txt files
res = glob.glob(path + "NEW_NAME" + "*.png")
for name in res:
    print(name)


