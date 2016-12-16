import copy
from collections import defaultdict
from collections import OrderedDict
import random

import time

mainlist = []

print "\nEnter number of persons : "

N = raw_input()

N = int(N)

for i in range(1,N+1):
    mainlist.append(random.randrange(1, 100, 3))
    
print "Input Generated is : ",mainlist

count = N
star = ['||=========||']

array = copy.copy(mainlist) 

array = array + star

dict_stage_array = {}
priority_queue_child_num = []
priority_queue_cost = []

dict_stage_array[1] = copy.copy(array)

stageNum_tostartarray = 1
stage_num_tocount = 2

child_list = defaultdict(list)

parent_list = {}

def move_front(parent_stage, fwd_count, stage_num_tocount):
    #print ("parent stage is : ",parent_stage)
    
    bkwd_orig_array = array[fwd_count + 1:]
    fwd_orig_array = array[:fwd_count]
    
    for i in range(0, fwd_count):
        for j in range(i+1, fwd_count):
            bkwd_new_array = []
            bkwd_new_array.append(array[i])
            bkwd_new_array.append(array[j])
            fwd_modified_array = copy.copy(fwd_orig_array)
            fwd_modified_array.remove(array[i])
            fwd_modified_array.remove(array[j])
            joined_array = fwd_modified_array + star + bkwd_orig_array + bkwd_new_array
            #print joined_array
            
            dict_stage_array[stage_num_tocount] = copy.copy(joined_array)
            
            cost = max(array[i], array[j])
            child_list[parent_stage].append(str(stage_num_tocount)+'-'+str(cost))
            parent_list[stage_num_tocount] = str(parent_stage)+'-'+str(cost)
            stage_num_tocount = stage_num_tocount + 1
    return stage_num_tocount
            
def move_back(parent_stage, bkwd_count, stage_num_tocount):
    #print ("parent stage is : ",parent_stage)
    
    bkwd_orig_array = array[bkwd_count + 1:]
    fwd_orig_array = array[:bkwd_count]
    
    for i in range(len(bkwd_orig_array)):
        fwd_new_array = []
        fwd_new_array.append(bkwd_orig_array[i])
        bkwd_modified_array = copy.copy(bkwd_orig_array)
        bkwd_modified_array.remove(bkwd_orig_array[i])
        joined_array = fwd_orig_array + fwd_new_array + star + bkwd_modified_array
        #print joined_array
                   
        dict_stage_array[stage_num_tocount] = copy.copy(joined_array)
        
        cost = bkwd_orig_array[i]
        child_list[parent_stage].append(str(stage_num_tocount)+'-'+str(cost))
        parent_list[stage_num_tocount] = str(parent_stage)+'-'+str(cost)
        
        stage_num_tocount = stage_num_tocount + 1
        
    return stage_num_tocount
                   
t0 = time.time()
while(count >= 0):
    #print ("stageNum_tostartarray is ",stageNum_tostartarray)
    #print ("stage_num_tocount is ",stage_num_tocount)

    stage_num_tocount_temp = copy.copy(stage_num_tocount)
    for i in range(stageNum_tostartarray, stage_num_tocount_temp):
        array = dict_stage_array[i]
        stage_num_tocount = move_front(i, count, stage_num_tocount)
        
    print ("stage_num_tocount is ",stage_num_tocount)

    count = count - 2
    
    print ("count is ", count)
    if(count == 0):
        #print ("---------------------------")
        #print "Child list is \n"
        #print child_list
        #print "\n"
        #print "Stage array is \n"
        #print dict_stage_array
        #print "\n"
        #print "Parent list is \n"
        #print parent_list
        break
        
    stageNum_tostartarray = copy.copy(stage_num_tocount_temp)
    stage_num_tocount_temp = copy.copy(stage_num_tocount)
    
    #print ("stageNum_tostartarray is ",stageNum_tostartarray)
    #print ("stage_num_tocount is ",stage_num_tocount)
    
    for i in range(stageNum_tostartarray, stage_num_tocount_temp):
        array = dict_stage_array[i]
        stage_num_tocount = move_back(i, count, stage_num_tocount)
        
    count = count + 1
    #print ("count is ", count)
    stageNum_tostartarray = copy.copy(stage_num_tocount_temp)
    
t1 = time.time()

total = t1-t0

print "\nTime taken by input is - ", total*1000," msec"


current_parent = 1

def dfs(current_parent):
    while(1):
        child = child_list[current_parent][0]
        child_num , cost = child.split('-')
        #print child_num
        child_num = int(child_num)
        cost = int(cost)
        current_parent = child_num
        if(dict_stage_array[current_parent][0] == '||=========||'):
            return current_parent

t0 = time.time()
parent_ret_from_dfs = dfs(current_parent)
t1 = time.time()
total = t1-t0
print "\nTime taken by DFS is - ", total*1000," msec"

bfs_list = []

def bfs(current_parent):
    while(1):
        for i in child_list[current_parent]:
            child_num , cost = i.split('-')
            bfs_list.append(int(child_num))
    
        current_parent = bfs_list.pop(0)
        if(dict_stage_array[current_parent][0] == '||=========||'):
            return current_parent

t0 = time.time()        
parent_ret_from_bfs = bfs(current_parent)
t1 = time.time()
total = t1-t0
print "\nTime taken by BFS is - ", total*1000," msec"

def track_back(parent_ret):
    track_list = []
    cost_total = 0
    cur_child = parent_ret
    track_list.append(cur_child)
    #print "Tracking back from \n"
    #print dict_stage_array[cur_child]
    #print "\n"
    while(1):
        parent, cost = parent_list[cur_child].split('-')
        parent = int(parent)
        cost = int(cost)
        #print "Child is \n"
        #print dict_stage_array[parent]
        #print "\n"
        #print "Cost is \n"
        #print cost
        cost_total = cost_total + cost
        #print "\n"
        cur_child = parent
        track_list.append(cur_child)
        if(cur_child == 1):
            track_list.reverse()
            print "Initial Point is -> ", dict_stage_array[track_list[0]]
            for i in range(len(track_list)):
                if (i != len(track_list) - 1):
                    parent, cost = parent_list[track_list[i+1]].split('-')
                    print "\nNext State is -> ", dict_stage_array[track_list[i+1]]
                    print "\nCost is -> ", cost
                else:
                    print "\nFinal Stage is -> ", dict_stage_array[track_list[i]] 
                    print "\nTotal Cost is -> ", cost_total    
            break


def total_cost(node):
    cost_total = 0
    cur_child = node
    while(1):
        parent, cost = parent_list[cur_child].split('-')
        parent = int(parent)
        cost = int(cost)
        cost_total = cost_total + cost
        cur_child = parent
        if(cur_child == 1):
            return cost_total    

def ucs(current_parent):
    while(1):
        for i in child_list[current_parent]:
            child_num , cost = i.split('-')
            priority_queue_child_num.append(int(child_num))
            priority_queue_cost.append(total_cost(int(child_num)))
            
        least_index = priority_queue_cost.index(min(priority_queue_cost))
        least_cost_node = priority_queue_child_num[least_index]
        
        if(dict_stage_array[least_cost_node][0] == '||=========||'):
            return least_cost_node
        else:
            current_parent = least_cost_node
            #del priority_queue[least_cost_node]
            priority_queue_child_num.pop(least_index)
            priority_queue_cost.pop(least_index)

t0 = time.time()
parent_ret_from_ucs = ucs(current_parent)
t1 = time.time()
total = t1-t0
print "\nTime taken by UCS is - ", total*1000," msec"


print "\nDFS Tracking Path ###################### \n"
track_back(parent_ret_from_dfs)

print "\nBFS Tracking Path ###################### \n"            
track_back(parent_ret_from_bfs)

print "\nUCS Tracking Path ###################### \n"
track_back(parent_ret_from_ucs)