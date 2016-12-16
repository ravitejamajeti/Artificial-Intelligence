import copy
import numpy as np
from collections import defaultdict
from random import randint
from evaluate import *

board_p = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
base_nodes_p = [5,5,5,5,5,5,5]

columns_p = [0,1,2,3,4,5,6]

#board_p = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]
#
#base_nodes_p = [2,2,2]
#
#columns_p = [0,1,2]

#columns_p = [0,1]

#board_p = [[0,0],
#           [0,0]]

#base_nodes_p = [1,1]

board = np.array(board_p)

columns = np.array(columns_p)

base_nodes = np.array(base_nodes_p)

parent_list = {}

child_list = {}

child_list = defaultdict(list)

node_desc = {}

level = {}

level = defaultdict(list)

score_detail = {}

def cal_minimax(node_num):
    #node_num = 1
    score_temp = []
    brd = np.array(node_desc[node_num])
    if(np.count_nonzero(brd) == depth - 2):
        for i in child_list[node_num]:
            score_temp.append(score_detail[i])
            
        min_score = min(score_temp)
        score_detail[node_num] = min_score
        score_temp = []
        return
    else:
        for i in child_list[node_num]:
            cal_minimax(i)
        
        for i in child_list[node_num]:
            score_temp.append(score_detail[i])
        
        if(np.count_nonzero(brd)%2 == 0):
            score = min(score_temp)
        else:
            score = max(score_temp)
        
        score_detail[node_num] = score
        score_temp = []
    return

def connect(board, base_nodes, played_by, depth, pnode):
    
    global node_num
    
    parent_node = pnode
    col = 0
    if(np.count_nonzero(board) < depth):
        for i in np.nditer(base_nodes, op_flags=['readwrite']):
            if i >= 0:
                
                
#                print("Parent Node num is ", parent_node)
#                print("Parent board is ")
#
#                for c in columns:
#                    print(c, end=" ")
#
#                print("\n")
#                print("--------------")
#
#                #print("played by ", played_by)
#
#                for b in board:
#                    for bb in b:
#                        print(bb, end=" ")
#                    print("\n")
        
                if played_by == "min":
#                    print("Played by ",played_by)
#                    print("col is ",col)
#                    print("i is ",i)
                    board[i, col] = 2
                elif played_by == "max":
#                    print("Played by ",played_by)
#                    print("col is ",col)
#                    print("i is ",i)
                    board[i, col] = 1
                i[...] = i - 1
                
                node_num = node_num + 1
                
                level[np.count_nonzero(board)].append(node_num)
                
                node_desc[node_num] = np.array(board)
                
                parent_list[node_num] = parent_node
                
                child_list[parent_node].append(node_num)
                
                #print("Child list is ", child_list)
                
                #if node_num == 35:
#                print("Node num is ", node_num)
#                print("Child board is ")
#
#                for j in columns:
#                    print(j, end=" ")
#
#                print("\n")
#                print("--------------")
#
#                for j in board:
#                    for k in j:
#                        print(k, end=" ")
#                    print("\n")

                board1 = np.array(board)
                base_nodes1 = np.array(base_nodes)
        
#                if(np.count_nonzero(board) == depth):
#                    evaluate_board(board)

                if played_by == "min":
                    next_player = "max"
                elif played_by == "max":
                    next_player = "min"

                if(np.count_nonzero(board) < depth):
                    connect(board1, base_nodes1, next_player, depth, node_num)

                i[...] = i + 1
                board[i, col] = 0
            col = col + 1
    return

depth = input("Enter depth : ")
depth = int(depth)

orig_depth = depth
lev = 0
node_num = 1
node_desc[node_num] = np.array(board)

fplayer = input("Do you want to play first (y/n) : ")

if(fplayer == 'y'):
    for j in columns:
        print(j, end=" ")

    print("\n")
    print("--------------")

    for j in board:
        for k in j:
            print(k, end=" ")
        print("\n")
        
    col_num = input("Enter column number : ")
    col_num = int(col_num)
    
    board[base_nodes[col_num],[col_num]] = 2
    base_nodes[col_num] = base_nodes[col_num] - 1
    
    node_desc[node_num] = np.array(board)
    level[np.count_nonzero(board)].append(node_num)
    lev = lev + 1
    depth = depth + 1
    
    print("Board played by min is : ")

    for j in columns:
        print(j, end=" ")

    print("\n")
    print("--------------")

    for j in board:
        for k in j:
            print(k, end=" ")
        print("\n")
    print("Base nodes are ", base_nodes)
    
played_by = "max"
connect(board, base_nodes, played_by, depth, 1)

for i in level[depth - 1]:
    a = node_desc[i]
    #print("a is ",a)
    score = evaluate_board(a)
    score_detail[i] = score
    
print("current depth is ", depth)

cal_minimax(1)

score_temp = []
for i in child_list[1]:
    score_temp.append(score_detail[i])
    
max_score_1 = max(score_temp)

c_list = child_list[1]
print("max_score_1 is ",max_score_1)
print("minmax board is ",node_desc[c_list[score_temp.index(max_score_1)]])

board_temp = node_desc[c_list[score_temp.index(max_score_1)]]

for i in range(len(board)):
    for j in range(len(board[i])):
        if(board[i][j] != board_temp[i][j]):
            print("diff is ", j)
            max_node = j
            
#max_node = randint(0,6)
#max_node = 1

#print("rand generated is ", max_node)
#board[base_nodes[max_node],[max_node]] = 1
board = board_temp
base_nodes[max_node] = base_nodes[max_node] - 1
depth = depth + 1
lev = lev + 1

print("Board played by max is : ")

for j in columns:
    print(j, end=" ")

print("\n")
print("--------------")

for j in board:
    for k in j:
        print(k, end=" ")
    print("\n")
print("Base nodes are ", base_nodes)


#print("Node_num after function is ", node_num)
#print("Child list is ", child_list)
#print("Parent list is ", parent_list)
#print("Node_desc is ", node_desc)
#print("Level list is ",level)
#for i in level:
#    print (i)
#
#print("Level to be calculated is : ", lev)

#cont = input("Do you want to continue (y/n) : ")
cont = 'y'
def gen_extra_states(lev, board):
    return_list = []
    delete_list = []
    selected_node = 0
    #print("Levels to be calculated are : ", level[lev])
#    print("Board is ",board)
    
    next_list = []
    
    for i in level[lev]:
        #print(np.array_equal(node_desc[i],board))
        if i in node_desc:
            if np.array_equal(node_desc[i],board):
                selected_node = i
            else:
                selected_list = [i]

                for j in range(orig_depth - 2):
                    for k in selected_list:
                        for l in child_list[k]:
                            delete_list.append(l)
                            next_list.append(l)
                    selected_list = copy.deepcopy(next_list)
                    next_list = []
                
    #print("Nodes to be deleted are ", delete_list)
    
    for i in delete_list:
        if i in child_list:
            del child_list[i]
        if i in parent_list:
            del parent_list[i]
        del node_desc[i]
        
    #print("Selected node is ", selected_node)
    
    #print("Orig depth is ", orig_depth)
    
    selected_list = [selected_node]
    next_list = []
    
    for i in range(orig_depth - 2):
        for j in selected_list:
            for k in child_list[j]:
                next_list.append(k)
            
        selected_list = copy.deepcopy(next_list)
        next_list = []
    return selected_list,selected_node
    
def get_basenodes(brd):
    base_nodes = [5,5,5,5,5,5,5]
    for i in brd:
        for j in range(len(i)):
            if i[j] > 0:
                base_nodes[j] = base_nodes[j] - 1
    
    return base_nodes

def check_quad(one_array):
    
    count = 0
    # vertical quads for one
    ver_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and one_array[i][0] + 3 == one_array[l][0] and one_array[i][1] == one_array[j][1] and one_array[i][1] == one_array[k][1] and one_array[i][1] == one_array[l][1]:
                        count = count + 1
                        
    
    
    #Horizantal quads for one
    hor_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] == one_array[j][0] and one_array[i][0] == one_array[k][0] and one_array[i][0] == one_array[l][0] and (one_array[i][1] + 1) == one_array[j][1] and (one_array[i][1] + 2) == one_array[k][1] and (one_array[i][1] + 3) == one_array[l][1]:
                        count = count + 1
    
    
    # ahead diagonal quads for one
    ahead_dia_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and one_array[i][0] + 3 == one_array[l][0] and (one_array[i][1] + 1) == one_array[j][1] and (one_array[i][1] + 2) == one_array[k][1] and (one_array[i][1] + 3) == one_array[l][1]:
                        count = count + 1
    
    
    # behind diagonal quads for one
    beh_dia_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and one_array[i][0] + 3 == one_array[l][0] and (one_array[i][1] - 1) == one_array[j][1] and (one_array[i][1] - 2) == one_array[k][1] and (one_array[i][1] - 3) == one_array[l][1]:
                        count = count + 1
    
    return count

while cont == 'y':
    col_num = input("Enter column number : ")
    col_num = int(col_num)

    board[base_nodes[col_num],[col_num]] = 2
    base_nodes[col_num] = base_nodes[col_num] - 1
    lev = lev + 1
    depth = depth + 1
    
    print("Board played by min is : ")

    for j in columns:
        print(j, end=" ")

    print("\n")
    print("--------------")

    for j in board:
        for k in j:
            print(k, end=" ")
        print("\n")
    print("Base nodes are ", base_nodes)
    
    two_array = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                two_array.append([i,j])
                
    win_count = check_quad(two_array)
    
    if win_count > 0:
        print("You Win")
        break

    if np.count_nonzero(board) == 42:
        break
    
    #print("Level to be calculated is : ", lev)
    selected_list,selected_node = gen_extra_states(lev, board)
    #print("Selected list is : ",selected_list)
    
    #print("Present depth is ", depth)
    for i in selected_list:
        played_by = "max"
        connect(node_desc[i], np.array(get_basenodes(node_desc[i])), played_by, depth, i)
        
    #print("Node_num after function is ", node_num)
    #print("Child list is ", child_list)
#    print("Parent list is ", parent_list)
    #print("Level list is ",level.keys())
#    print("Node_desc is ", node_desc)
    
    #print("Terminal nodes are ", level[depth])
    for i in level[depth - 1]:
        a = node_desc[i]
        #print("a is ",a)
        score = evaluate_board(a)
        score_detail[i] = score
        
    cal_minimax(selected_node)

    score_temp = []
    for i in child_list[selected_node]:
        score_temp.append(score_detail[i])

    print("Scores are ",score_temp)
    max_score_1 = max(score_temp)

    c_list = child_list[selected_node]
    #print("max_score_1 is ",max_score_1)
    #print("minmax board is ",node_desc[c_list[score_temp.index(max_score_1)]])
    
    board_temp = node_desc[c_list[score_temp.index(max_score_1)]]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] != board_temp[i][j]):
                print("diff is ", j)
                max_node = j

    #max_node = randint(0,6)
    board = board_temp
    
#    while base_nodes[max_node] == -1:
#        max_node = randint(0,6)
        
    #print("Final rand generated is ", max_node)
    #board[base_nodes[max_node],[max_node]] = 1
    base_nodes[max_node] = base_nodes[max_node] - 1
    depth = depth + 1
    lev = lev + 1
    
    print("Board played by max is : ")

    for j in columns:
        print(j, end=" ")

    print("\n")
    print("--------------")

    for j in board:
        for k in j:
            print(k, end=" ")
        print("\n")
        
    one_array = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                one_array.append([i,j])
                
    win_count = check_quad(one_array)
    
    if win_count > 0:
        print("AI Wins")
        break
        
    if np.count_nonzero(board) == 42:
        break


                
                
    
                
    