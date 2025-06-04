# -*- coding: utf-8 -*-
"""
Created on Mon May 26 22:24:37 2025

@author: Ji
"""

import numpy as np
from collections import Counter


def search(x):
    for i in range(len(drug)):
        if drug[i]==x:
            cluster_type = cluster_result[i]
    return cluster_type

def group_search(x):
    group_list =[]
    for i in range(len(GGI)):
        if GGI[i] ==x:
            group_list.append(alpha[i][2])
    return group_list

#test
clusters = {
     "0": ['AMK', 'GEN', 'TOB', 'SPE'],
     "1": ['CEF', 'OXA'],
     "2": ['CIP', 'LEV'],
     "3": ['CLA', 'ERY'],
     "4": ['TET'],
     "5": ['CHL', 'FUS', 'NAL', 'RIF', 'NIT', 'TRI', 'VAN']
 }

drug = np.loadtxt('drug.txt',dtype=str,delimiter='	')
alpha = np.loadtxt('DDI.txt',dtype=str,delimiter='	',)

cluster_result = []
for i in range(len(drug)):
    for j in range(len(clusters)):
        if str(drug[i]) in clusters[str(j)]:
            cluster_result.append(j)

GGI = []
for i in range(len(alpha)):
    drug1_ID = search(alpha[i][0])
    drug2_ID = search(alpha[i][1])
    if drug1_ID > drug2_ID:
        GGI.append(str(drug1_ID)+'_'+str(drug2_ID))
    else:
        GGI.append(str(drug2_ID)+'_'+str(drug1_ID))


x = 0
y = 0
k = 6  #number of clusters
for i in range(k-1,-1,-1):
    for j in range(i-1,-1,-1):
        name = str(i)+'_'+str(j)
        count = Counter(group_search(name))
        x = x + max(count['1'],count['-1'])
        y= y+ len(group_search(name))
print('edge purity = ',x/y)
