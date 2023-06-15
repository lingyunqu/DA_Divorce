from collections import deque
import pandas as pd
import numpy as np
import random
import copy

#reindex the irregular cases!
def tr_numbers(source_match_dict, source_sort_boy_to_girl, source_sort_girl_to_boy):
    # if the number or the preference is irregular
    # boy_dict = {}
    tr_boy_dict = {}
    # girl_dict = {}
    tr_girl_dict = {}
    count = 1
    for i in range(len(source_sort_boy_to_girl[0])):
        # girl_dict[i+1] = source_sort_boy_to_girl[0][i]
        tr_girl_dict[source_sort_boy_to_girl[0][i]] = i+1
        # boy_dict[i+1] = source_sort_girl_to_boy[0][i]
    for key in source_match_dict.keys():
        tr_boy_dict[key] = count
        count += 1

    match_dict = {}
    sort_boy_to_girl = []
    sort_girl_to_boy = []
    for key,value in source_match_dict.items():
        match_dict[tr_boy_dict[key]] = tr_girl_dict[value] if value!=0 else 0
    for sort_list in source_sort_boy_to_girl:
        sort_boy_to_girl.append([tr_girl_dict[x] for x in sort_list]) 
    for sort_list in source_sort_girl_to_boy:
        sort_girl_to_boy.append([tr_boy_dict[x] for x in sort_list]) 

    return match_dict, sort_boy_to_girl, sort_girl_to_boy
