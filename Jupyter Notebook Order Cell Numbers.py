# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:38:00 2022

@author: arife
"""

import json

NOTEBOOK_FILE = 'C:/Users/arife/Desktop/a.ipynb'
with open(NOTEBOOK_FILE, 'rt', encoding='utf-8') as f_in:
    doc = json.load(f_in)


cnt = 1

for cell in doc['cells']:
    if 'execution_count' not in cell:
        continue

    cell['execution_count'] = cnt

    for o in cell.get('outputs', []):
        if 'execution_count' in o:
            o['execution_count'] = cnt

    cnt = cnt + 1


with open(NOTEBOOK_FILE, 'wt') as f_out:
    json.dump(doc, f_out, indent=1)
    
    