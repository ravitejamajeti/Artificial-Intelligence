import copy
from collections import OrderedDict
import time

main_matrix = [[1,0,2,0,3],[-1,-1,0,-1,0],[-1,4,0,5,0],[6,-1,7,0,0],[8,0,0,0,0],[0,-1,-1,0,-1]]
main_matrix_copy = copy.deepcopy(main_matrix)

directions = {1: 'a', 2: 'd', 3: 'd', 4: 'a', 5: 'd', 6: 'd', 7: 'a', 8: 'a'}

word_count = {1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 3, 7: 3, 8: 5}

word_finished = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

words_filled = {}

word_constr = {1: 2, 2: 4, 3: 4, 4: 3, 5: 3, 6: 1, 7: 3, 8: 4}

word_constr_num = [2,3,8,4,5,7,1,6]
word_constr_val = [4,4,4,3,3,3,2,1]

word_indexes = {1:[0,0], 2:[0,2], 3:[0,4], 4:[2,1], 5:[2,3], 6:[3,0], 7:[3,2], 8:[4,0]}

word_domain = {1:'e', 2:'e', 3:'e', 4:'f', 5:'f', 6:'g', 7:'g', 8:'e'}

domain_list = {'e':['HOSES','LASER','SAILS','SHEET','STEER'], 'f':['HEEL','HIKE','KEEL','KNOT','LINE'], 'g':['AFT','ALE','EEL','LEE','TIE']}

constraints = {1:{2:[2,0], 3:[4,0]}, 2:{1:[0,2], 7:[3,0], 8:[4,2], 4:[2,1]}, 3:{1:[0,4], 4:[2,3], 7:[3,2], 8:[4,4]}, 4:{2:[1,2], 5:[2,0], 3:[3,2]}, 5:{4:[0,2], 7:[1,1], 8:[2,3]}, 6:{8:[1,0]}, 7:{2:[0,3], 5:[1,1], 3:[2,3]}, 8:{2:[2,4], 5:[3,2], 3:[4,4], 6:[0,1]}}
    
#word_constr = OrderedDict(sorted(word_constr.items(), key=lambda t: t[1], reverse=True))

domain_list_main = copy.deepcopy(domain_list)

def solve_cross(domain_list_func_copy, current_word):
    
    flag = 0
    
    for i in word_finished:
        if(word_finished[i] == 0):
            flag = 1
            
    if(flag == 0):
        return True
    
    domain_list_copy = copy.deepcopy(domain_list_func_copy)
    
    d = 0
    match_count = 0
    
    current_variable = word_constr_num[current_word]
    current_domain = word_domain[current_variable]
    
    for i in domain_list_func_copy[current_domain]:
        match_count = 0
        current_choice = i
        del domain_list_copy[current_domain][d]
        #print("Current choice is ", i)
        #print("constraints are ",constraints[current_variable])
        for j in constraints[current_variable]:
            current_variable_index = constraints[current_variable][j][0]
            other_variable_index = constraints[current_variable][j][1]
            other_variable = j
            if(word_finished[other_variable] == 1):
                if(current_choice[current_variable_index] == words_filled[other_variable][other_variable_index]):
                    match_count = match_count + 1
            else:
                for k in domain_list_copy[word_domain[other_variable]]:
                #print (k)
                    if(current_choice[current_variable_index] == k[other_variable_index]):
                        #print("Match Found")
                        match_count = match_count + 1
                        break
                    
            #print (constraints[current_variable][j])
            #print("Current variable is ", current_variable)
            #print("Current variable constrained index is ", current_variable_index)
            #print("Current variable domain is ", domain_list_copy[word_domain[current_variable]])
            #print("Current constrained variable is ", current_choice[current_variable_index])
            #print("Other Variable is ", other_variable)
            #print("Other variable constrained index is ", other_variable_index)
            #print("Other variable domain is ", domain_list_copy[word_domain[other_variable]])
            
            
        #print("Match count is : ",match_count)
        if(match_count == len(constraints[current_variable])):
            #print(current_choice, " might be a perfect match for variable ", current_variable)
            word_finished[current_variable] = 1
            words_filled[current_variable] = current_choice
            if(solve_cross(domain_list_copy, current_word + 1)):
                return True
            else:
                domain_list_copy = copy.deepcopy(domain_list_func_copy)
                d = d + 1
                word_finished[current_variable] = 0
                del words_filled[current_variable]
        else:
            domain_list_copy = copy.deepcopy(domain_list_func_copy)
            d = d + 1
            
            
    return False

current_word = 0
t0 = time.time()
solve_cross(domain_list, current_word)
t1 = time.time()

#print("words filled are ", words_filled)

for i in main_matrix:
    for j in i:
        if j == -1:
            j = '#'
        elif j == 0:
            j = '-'
        else:
            dire = directions[j]
            count = word_count[j]
            row = word_indexes[j][0]
            column = word_indexes[j][1]
            w = words_filled[j]
            #print("j is ", j, "w is ", w)
            if dire == 'a':
                for k in range(count):
                    main_matrix_copy[row][column] = w[k]
                    column = column + 1
            elif dire == 'd':
                for k in range(count):
                    main_matrix_copy[row][column] = w[k]
                    row = row + 1
                    
print("\n      -------------")
print("\n")
print("      ", end=" ")
for i in main_matrix_copy:
    for j in i:
        if j == -1:
            j = '#'
        elif j == 0:
            j = '-'
        print(j, end=" ")
    print("\n")
    print("      ", end=" ")
print("------------\n")

print("\n Total time taken is ", t1-t0, "sec \n\n")