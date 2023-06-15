from collections import deque
import pandas as pd
import numpy as np
import random
import copy

## Classical DA! 
def find_free_partner(boys, girls, sort_boy_to_girl, sort_girl_to_boy):
    
    #########################################
    #NOTE: When the number of boys are discrete with gaps
    #      turned into [1,2,3,... ] continuous number
    #########################################
    boy_index_dict = {}
    for i in range(len(boys)):
        boy_index_dict[boys[i]] = i+1
    girl_index_dict = {}
    for i in range(len(girls)):
        girl_index_dict[girls[i]] = i+1
    # old_boys = boys
    # old_girls = girls
    new_boys = list(range(1,len(boys)+1))
    new_girls = list(range(1,len(girls)+1))
    new_sort_boy_to_girl = []
    for items in sort_boy_to_girl:
        tmp = []
        for item in items:
            tmp.append(girl_index_dict[item])
        new_sort_boy_to_girl.append(tmp)
    new_sort_girl_to_boy = []
    for items in sort_girl_to_boy:
        tmp = []
        for item in items:
            tmp.append(boy_index_dict[item])
        new_sort_girl_to_boy.append(tmp)
    ###########################################################
    # print(girl_index_dict)
    # current choice
    # build dict：key: n-th boy，value: current choice of girl，current_boys = {boys[0]:None, boys[1]:None, boys[2]:None, boys[3]:None ... }
    current_boys = dict(zip(new_boys, [None]*len(new_boys)))
    # build dict：key: n-th girl，value: current choice of boy，current_girls = {girls[0]:None, girls[1]:None, girls[2]:None, boys[3]:None ... }
    current_girls = dict(zip(new_girls, [None]*len(new_girls)))
    # sumboys= sum(current_girls)
    count = len(boys)
 
 
    # build dict: next girl to choose for boys
    next_select = dict(zip(new_boys, [None]*len(new_boys)))
    # build sequence for every boy
    for i in range(count):
        # propose to the first girl
        temp = [new_girls[m-1] for m in new_sort_boy_to_girl[i]]
        # next time propose to the second
        next_select[new_boys[i]] = deque(temp)
 
 
    # girl choose boy dict
    sort_girl = dict(zip(new_girls, [None]*len(new_boys)))
    for i in range(count):
        # girl rank boy
        temp = [[new_boys[m-1], 19-ind] for ind, m in enumerate(new_sort_girl_to_boy[i])]
        name = []
        match = []
        # for every girl
        for t in temp:
            # number of matched boy
            name.append(t[0])
            # rank of matched boy
            match.append(t[1])
        # get the ranking of 
        sort_girl[new_girls[i]] = dict(zip(name, match))
 
 
    while None in current_boys.values():
        for i in range(count):
            # i-th boy proposes
            bid = new_boys[i]
            if current_boys[bid]:
                # skip if matched
                continue
            else:
                # choose the next on preference list
                select = next_select[bid][0]
                # if girl is unmatched
                if current_girls[select] == None:
                    # match
                    current_boys[bid] = select
                    current_girls[select] = bid
                    next_select[bid].popleft()
                else:
                    # compare propose boy to the current match
                    # if the current match is preferred to the propose boy
                    # keep status quo 
                    if sort_girl[select][current_girls[select]] > sort_girl[select][bid]:
                        next_select[bid].popleft()
                    # if the reverse
                    # propose boy is preferred to the current match
                    # unmatch
                    # the girl match with propose boy
                    # current match can't propose again
                    else:
                        current_boys[current_girls[select]] = None
                        current_boys[bid] = select
                        current_girls[select] = bid
                        next_select[bid].popleft()
    #NOTE:return to original index
    return_boys = dict()
    for key,value in current_boys.items():
        return_boys[boys[key-1]] = girls[value-1]
    return return_boys
