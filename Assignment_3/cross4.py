import copy
from collections import OrderedDict
from collections import defaultdict
import sys
import time

main_matrix = [[-1, -1, 1 ,2, 3, -1, -1, -1, 4, 5, 6, -1, -1], [-1, 7, 0, 0, 0, 8, -1 , 9 , 0, 0, 0, 10, -1], [-1, 11, 0, 0, 0, 0, -1, 12, 0, 0, 0, 0, -1], [13, 0, 0, -1, 14, 0, 15, 0, 0, -1, 16, 0 ,17], [18, 0, 0, 19, -1, 20, 0, 0, -1, 21, 0, 0, 0], [22, 0, 0, 0, -1, 23, 0, 0 , -1, 24, 0, 0, 0], [-1, 25, 0, 0, 26, -1, -1, -1, 27, 0, 0, 0, -1], [-1, -1, 28, 0, 0, 29, -1, 30, 0, 0, 0, -1, -1], [-1, -1, -1, 31, 0, 0, 32, 0, 0, 0, -1, -1, -1], [-1, -1, -1, -1, 33, 0, 0, 0, 0, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1]]


main_matrix_copy = copy.deepcopy(main_matrix)

directions = {1: 'd', 2: 'd', 3: 'd', 4: 'd', 5: 'd', 6: 'd', 7: 'd', 8: 'd', 9:'d', 10:'d', 11:'a', 12:'a', 13:'d', 14:'a', 15:'d', 16:'d', 17:'d', 18:'a', 19:'d', 20:'a', 21:'d', 22:'a', 23:'a', 24:'a', 25:'a', 26:'d', 27:'d', 28:'a', 29:'d', 30:'d', 31:'a', 32:'d', 33:'a'}

word_count = {1: 8, 2: 3, 3: 4, 4: 4, 5: 3, 6: 8, 7: 6, 8: 5, 9: 5, 10: 6, 11: 5, 12: 5, 13: 3, 14: 5, 15: 3, 16: 3, 17: 3, 18: 4, 19: 5, 20: 3, 21: 5, 22: 4, 23: 3, 24: 4, 25: 4, 26: 4, 27: 4, 28: 4, 29: 4, 30: 4, 31: 7, 32: 4, 33: 5}

word_finished = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 15, 32: 0, 33: 0, 100: 0, 400: 0 , 700: 0, 900: 0, 130: 0, 210: 0, 270: 0, 300: 0}

words_filled = {}

word_constr = {1: 2, 2: 4, 3: 4, 4: 3, 5: 3, 6: 1, 7: 3, 8: 4}

word_constr_num = [1,6,31,7,10,8,700,900,9,11,12,14,19,21,33,3,210,270,300,4,18,22,24,25,26,27,28,29,30,32,2,5,13,15,16,17,20,23,100,400,130]
#word_constr_val = [4,4,4,3,3,3,2,1]

word_indexes = {1:[0,2], 2:[0,3], 3:[0,4], 4:[0,8], 5:[0,9], 6:[0,10], 7:[1,1], 8:[1,5], 9:[1,7], 10:[1,11], 11:[2,1], 12:[2,7], 13:[3,0], 14:[3,4], 15:[3,6], 16:[3,10], 17:[3,12], 18:[4,0], 19:[4,3], 20:[4,5], 21:[4,9], 22:[5,0], 23:[5,5], 24:[5,9], 25:[6,1], 26:[6,4], 27:[6,8], 28:[7,2], 29:[7,5], 30:[7,7], 31:[8,3], 32:[8,6], 33:[9,4]}

domain_set = {3:['2a', '5a', '13a', '15a', '16a', '17a', '20a', '23a', '100a', '400a', '130a'], 4:['3a', '4a', '18a', '22a', '24a', '25a', '26a', '27a', '28a', '29a', '30a', '32a', '210a', '270a', '300a'], 5:['8a', '9a', '11a', '12a', '14a', '19a', '21a', '33a', '700a', '900a'], 6:['7a', '10a'], 7:['31a'], 8:['1a', '6a']}

word_domain = {1:'1a', 2:'2a', 3:'3a', 4:'4a', 5:'5a', 6:'6a', 7:'7a', 8:'8a', 9:'9a', 10:'10a', 11:'11a', 12:'12a', 13:'13a', 14:'14a', 15:'15a', 16:'16a', 17:'17a', 18:'18a', 19:'19a', 20:'20a', 21:'21a', 22:'22a', 23:'23a', 24:'24a', 25:'25a', 26:'26a', 27:'27a', 28:'28a', 29:'29a', 30:'30a', 31:'31a', 32:'32a', 33:'33a', 100:'100a', 400:'400a', 700:'700a', 900:'900a', 130:'130a', 210:'210a', 270:'270a', 300:'300a'}

word_domain_inv = {'130a': 130, '20a': 20, '900a': 900, '210a': 210, '5a': 5, '15a': 15, '27a': 27, '28a': 28, '24a': 24, '11a': 11, '8a': 8, '14a': 14, '17a': 17, '30a': 30, '23a': 23, '10a': 10, '13a': 13, '7a': 7, '19a': 19, '400a': 400, '33a': 33, '2a': 2, '16a': 16, '18a': 18, '29a': 29, '22a': 22, '300a': 300, '6a': 6, '100a': 100, '32a': 32, '4a': 4, '26a': 26, '31a': 31, '9a': 9, '700a': 700, '12a': 12, '270a': 270, '25a': 25, '3a': 3, '1a': 1, '21a': 21}

d29 = input("Enter letter for 29 -- ")
d32 = input("Enter letter for 32 -- ")
d30 = input("Enter letter for 30 -- ")


if d29.isalpha() and d32.isalpha() and d30.isalpha():
    print("Input Validated Successfully for alphabets")
else:
    print("Validation Failed - Input should contain only alphabets")   
    sys.exit()
    
if len(d29) > 1 or len(d32) > 1 or len(d30) > 1:
    print("Validation Failed -- Only one character should be given") 
    sys.exit()
else:
    print("Input Validated Successfully for length")
    
with open("words.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip('\n'))
        

domain_list = {}

domain_list = defaultdict(list)
count = 0
for i in array:
    if len(i) > 2 and len(i) < 9:
        if(len(i) == 3):
            domain_list['2a'].append(i)
            domain_list['5a'].append(i)
            domain_list['13a'].append(i)
            domain_list['15a'].append(i)
            domain_list['16a'].append(i)
            domain_list['17a'].append(i)
            domain_list['20a'].append(i)
            domain_list['23a'].append(i)
            domain_list['100a'].append(i)
            domain_list['400a'].append(i)
            domain_list['130a'].append(i)
        elif(len(i) == 4):
            domain_list['3a'].append(i)
            domain_list['4a'].append(i)
            domain_list['18a'].append(i)
            domain_list['22a'].append(i)
            domain_list['24a'].append(i)
            domain_list['25a'].append(i)
            domain_list['26a'].append(i)
            domain_list['27a'].append(i)
            domain_list['28a'].append(i)
            if(i[3] == d29):
                domain_list['29a'].append(i)
            if(i[3] == d30):
                domain_list['30a'].append(i)
            if(i[2] == d32):
                domain_list['32a'].append(i)
            domain_list['210a'].append(i)
            domain_list['270a'].append(i)
            domain_list['300a'].append(i)
        elif(len(i) == 5):
            domain_list['8a'].append(i)
            domain_list['9a'].append(i)
            domain_list['11a'].append(i)
            domain_list['12a'].append(i)
            domain_list['14a'].append(i)
            domain_list['19a'].append(i)
            domain_list['21a'].append(i)
            domain_list['33a'].append(i)
            domain_list['700a'].append(i)
            domain_list['900a'].append(i)
        elif(len(i) == 6):
            domain_list['7a'].append(i)
            domain_list['10a'].append(i)
        elif(len(i) == 7):
            domain_list['31a'].append(i)
        elif(len(i) == 8):
            domain_list['1a'].append(i)
            domain_list['6a'].append(i)
        count = count + 1

#print("domain of 29 is ", domain_list['29a'])
#print("domain of 30 is ", domain_list['30a'])
#print("domain of 32 is ", domain_list['32a'])
constraints = {1:{700:[1,1], 11:[2,1], 130:[3,2], 18:[4,2], 22:[5,2], 25:[6,1], 28:[7,0], 100:[0,0]}, 2:{700:[1,2], 11:[2,2], 100:[0,1]}, 3:{700:[1,3], 11:[2,3], 100:[0,2], 14:[3,0]}, 4:{900:[1,1], 12:[2,1], 14:[3,4], 400:[0,0]}, 5:{900:[1,2], 12:[2,2], 400:[0,1]}, 6:{900:[1,3], 12:[2,3], 16:[3,0], 210:[4,1], 24:[5,1], 270:[6,2], 300:[7,3], 400:[0,2]}, 7:{11:[1,0], 130:[2,1], 18:[3,1], 22:[4,1], 25:[5,0], 700:[0,0]}, 8:{700:[0,4], 11:[1,4], 14:[2,1], 20:[3,0], 23:[4,0]}, 9:{12:[1,0], 14:[2,3], 20:[3,2], 23:[4,2], 900:[0,0]}, 10:{900:[0,4], 12:[1,4], 16:[2,1], 210:[3,2], 24:[4,2], 270:[5,3]}, 11:{7:[0,1], 1:[1,2], 2:[2,2], 3:[3,2], 8:[4,1]}, 12:{9:[0,1], 4:[1,2], 5:[2,2], 6:[3,2], 10:[4,1]}, 13:{18:[1,0], 22:[2,0], 130:[0,0]}, 14:{3:[0,3], 8:[1,2], 15:[2,0], 9:[3,2], 4:[4,3]}, 15:{14:[0,2], 20:[1,1], 23:[2,1]}, 16:{6:[0,3], 10:[1,2], 17:[2,0]}, 17:{16:[0,2], 210:[1,3], 24:[2,3]}, 18:{13:[0,1], 7:[1,3], 1:[2,4], 19:[3,0]}, 19:{18:[0,3], 22:[1,3], 25:[2,2], 28:[3,1], 31:[4,0]}, 20:{8:[0,3], 15:[1,1], 9:[2,3]}, 21:{24:[1,0], 270:[2,1], 300:[3,2], 31:[4,6], 210:[0,0]}, 22:{13:[0,2], 7:[1,4], 1:[2,5], 19:[3,1]}, 23:{8:[0,4], 15:[1,2], 9:[2,4]}, 24:{21:[0,1], 6:[1,5], 10:[2,4], 17:[3,2]}, 25:{7:[0,5], 1:[1,6], 19:[2,2], 26:[3,0]}, 26:{25:[0,3], 28:[1,2], 31:[2,1], 33:[3,0]}, 27:{300:[1,1], 31:[2,5], 33:[3,4], 270:[0,0]}, 28:{1:[0,7], 19:[1,3], 26:[2,1], 29:[3,0]}, 29:{28:[0,3], 31:[1,2], 33:[2,1]}, 30:{31:[1,4], 33:[2,3], 300:[0,0]}, 31:{19:[0,4], 26:[1,2], 29:[2,1], 32:[3,0], 30:[4,1], 27:[5,2], 21:[6,4]}, 32:{31:[0,3], 33:[1,2]}, 33:{26:[0,3], 29:[1,2], 32:[2,1], 30:[3,2], 27:[4,3]}, 100:{1:[0,0], 2:[1,0], 3:[2,0]}, 400:{4:[0,0], 5:[1,0], 6:[2,0]}, 700:{7:[0,0], 1:[1,1], 2:[2,1], 3:[3,1], 8:[4,0]}, 900:{9:[0,0], 4:[1,1], 5:[2,1], 6:[3,1], 10:[4,0]}, 130:{13:[0,0], 7:[1,2], 1:[2,3]}, 210:{21:[0,0], 6:[1,4], 10:[2,3], 17:[3,1]}, 270:{27:[0,0], 21:[1,2], 6:[2,6], 10:[3,5]}, 300:{30:[0,0], 27:[1,1], 21:[2,3], 6:[3,7]}}

domain_list_main = copy.deepcopy(domain_list)

used_words = []

words_fwd_chk = {}

def fwd_chk(domain_list):
    
    domain_list_afterchk = defaultdict(list)
    
    domain_list_afterchk = copy.deepcopy(domain_list)
    
    global words_fwd_chk
    count = 0
    flag = 0
    
    #print("words_fwd_chk is ", words_fwd_chk)
    
    for i in words_fwd_chk:
        flag = 0
        #print("Checking for variable ", i)
        current_domain = word_domain[i]
        domain_list_afterchk[current_domain] = []
        #print("domain is ", domain_list[current_domain])
        for j in domain_list[current_domain]:
            if j in used_words:
                continue
            count = 0
            #print("j is ", j)
            for k in range(len(j)):
                #print("words_fwd_chk[i] is ", words_fwd_chk[i])
                if k in words_fwd_chk[i]:
                    #print("words_fwd_chk[i][k] is ", words_fwd_chk[i][k], " j[k] is ", j[k])
                    if words_fwd_chk[i][k] == j[k]:
                        count = count + 1
                        #print("count is ", count)
            if(count == len(words_fwd_chk[i])):
                flag = 1
                domain_list_afterchk[current_domain].append(j)
                #print("Fwd Check is fine for variable ", i)
        if flag == 0:
            #print("Fwd Check is not ****** fine for variable ", i)
            return False, domain_list_afterchk
    
        #print("domain in fwd check is ",domain_list_afterchk[current_domain])
    return True, domain_list_afterchk

def solve_cross(domain_list, domain_count, cnt):
    
    #print("words_filled Words are ", words_filled)
    
    global words_fwd_chk
    
    flag = 0
    
    words_fwd_chk_bkp = {}
    
    for i in word_finished:
        if(word_finished[i] == 0):
            flag = 1
            
    if(flag == 0):
        return True
    
    d = 0
    match_count = 0
    
    for i in domain_list:
        domain_count[i] = len(domain_list[i])
        #print("i is ",i, " count is ", domain_count[i])
        
    domain_count = OrderedDict(sorted(domain_count.items(), key=lambda t: t[1]))
    
    #print("domain count is ", domain_count)
    
    current_variable = word_domain_inv[list(domain_count.keys())[0]]
    
    if cnt == 1:
        current_variable = 1
    #current_variable = word_constr_num[current_word]
    current_domain = word_domain[current_variable]
    
    #print("Current variable is ", current_variable)
    #print("domain list is ", domain_list[current_domain])
    
    for i in domain_list[current_domain]:
        match_count = 0
        current_choice = i
        
        if i in used_words:
            continue
            
        used_words.append(current_choice)
        
        #if(current_variable == 700 or current_variable == 900):
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
                for k in domain_list[word_domain[other_variable]]:
                    if k in used_words:
                        continue
                    if(current_choice[current_variable_index] == k[other_variable_index]):
                        #print("Match Found")
                        match_count = match_count + 1
                        break
                    
            #print (constraints[current_variable][j])
            #print("Current variable is ", current_variable)
            #print("Current variable constrained index is ", current_variable_index)
            #print("Current variable domain is ", domain_list[word_domain[current_variable]])
            #print("Current constrained variable is ", current_choice[current_variable_index])
            #print("Other Variable is ", other_variable)
            #print("Other variable constrained index is ", other_variable_index)
            #print("Other variable domain is ", domain_list[word_domain[other_variable]])
            
            
        #print("Match count is : ",match_count)
        if(match_count == len(constraints[current_variable])):
            #print(current_choice, " might be a perfect match for variable ", current_variable)
            word_finished[current_variable] = 1
            words_filled[current_variable] = current_choice
            
            words_fwd_chk_bkp = copy.deepcopy(words_fwd_chk)
            
            if current_variable in words_fwd_chk:
                del words_fwd_chk[current_variable]
            
            for j in constraints[current_variable]:
                if(j not in words_filled):
                    if(j in words_fwd_chk):
                        temp = words_fwd_chk[j]
                        temp[constraints[current_variable][j][1]] = current_choice[constraints[current_variable][j][0]]
                        words_fwd_chk[j] = temp
                    else:
                        temp = {}
                        temp[constraints[current_variable][j][1]] = current_choice[constraints[current_variable][j][0]]
                        words_fwd_chk[j] = temp
            
            status, domain_list_afterchk = fwd_chk(domain_list)
            
            if status:
                domain_list_afterchk_backup = copy.deepcopy(domain_list_afterchk)
                del domain_list_afterchk[current_domain]
                domain_count_value = domain_count[current_domain]
                del domain_count[current_domain]
                #print("domain while deleting is count is ", domain_count)
                if(solve_cross(domain_list_afterchk, domain_count, cnt + 1)):
                    return True
                else:
                    domain_list_afterchk = copy.deepcopy(domain_list_afterchk_backup)
                    domain_count[current_domain] = domain_count_value
                    #print("Backtracking")
                    used_words.remove(current_choice)
                    d = d + 1
                    word_finished[current_variable] = 0
                    del words_filled[current_variable]
                    words_fwd_chk = copy.deepcopy(words_fwd_chk_bkp)
            else:
                #print("fwd check failed")
                used_words.remove(current_choice)
                d = d + 1
                word_finished[current_variable] = 0
                del words_filled[current_variable]
                words_fwd_chk = copy.deepcopy(words_fwd_chk_bkp)
        else:
            used_words.remove(current_choice)
            d = d + 1
            
            
    return False

cnt = 0
current_word = 0
domain_count = {}
for i in domain_list:
    domain_count[i] = len(domain_list[i])
    #print("count is ", domain_count[i])
t0 = time.time()
if solve_cross(domain_list, domain_count, cnt + 1):
    print("\n ########## Puzzle Cracked ########## \n")
else:
    print("There is no solution for given input -- Try another combination -- Recommended - d,e,e : n,t,h : n,e,h : e,e,h")
    sys.exit()
t1 = time.time()

words_filled = OrderedDict(sorted(words_filled.items(), key=lambda t: t[0]))
#print("words_filled Words are ", words_filled)

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
                    
print("      --------------------------")
print("\n")
print("      ", end=" ")
for i in main_matrix_copy:
    for j in i:
        if j == -1:
            j = ' '
        elif j == 0:
            j = '-'
        print(j, end=" ")
    print("\n")
    print("      ", end=" ")
print("--------------------------")

print("\n Total time taken is ", t1-t0, "sec \n\n")