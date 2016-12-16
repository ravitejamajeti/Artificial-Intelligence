def convert_to_tuple(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            arr[x][y] = tuple(arr[x][y])
    arr = tuple(tuple(x) for x in arr)
    return arr

def remove_dup(arr, arr_up):
    arr_final = []
    flag = 0
    for i in arr:
        flag = 0
        for j in arr_up:
            if set(i) < set(j):
                flag = 1
        if flag == 0:
            arr_final.append(list(i))
    return arr_final

def calculate_pairs(one_array, a):
    
    #horizantal pairs for one
    hor_pairs = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            if one_array[i][0] == one_array[j][0] and (one_array[i][1] + 1) == one_array[j][1]:
                #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1])
                hor_pairs.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]]])
    hor_pairs = convert_to_tuple(hor_pairs)
    
    
    #vertical pairs for one
    ver_pairs = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1])
            if (one_array[i][0] + 1) == (one_array[j][0]) and (one_array[i][1] ) == one_array[j][1]:
                #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1])
                ver_pairs.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]]])
    ver_pairs = convert_to_tuple(ver_pairs)
    
    
    # behind diagonal pairs for one
    beh_diag_pairs = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1])
            if (one_array[i][0] + 1) == (one_array[j][0]) and (one_array[i][1] - 1 ) == one_array[j][1]:
                #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1])
                beh_diag_pairs.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]]])
    beh_diag_pairs = convert_to_tuple(beh_diag_pairs)
    
    
    # ahead diagonal pairs for one
    ahead_diag_pairs = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1])
            if (one_array[i][0] + 1) == (one_array[j][0]) and (one_array[i][1] + 1 ) == one_array[j][1]:
                #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1])
                ahead_diag_pairs.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]]])
    ahead_diag_pairs = convert_to_tuple(ahead_diag_pairs)
    
    
    # vertical triples for one
    ver_triples = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and (one_array[i][1]) == one_array[j][1] and (one_array[i][1]) == one_array[k][1]:
                    #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1])
                    ver_triples.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]]])
    ver_triples = convert_to_tuple(ver_triples)
    
    
    #Horizantal triples for one
    hor_triples = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                if one_array[i][0] == one_array[j][0] and one_array[i][0] == one_array[k][0] and (one_array[i][1] + 1) == one_array[j][1] and (one_array[i][1] + 2) == one_array[k][1]:
                    #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1])
                    hor_triples.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]]])
    hor_triples = convert_to_tuple(hor_triples)

    
    # behind diagonal triples for one
    beh_diag_triples = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and (one_array[i][1] - 1) == one_array[j][1] and (one_array[i][1] - 2) == one_array[k][1]:
                    #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1])
                    beh_diag_triples.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]]])
    beh_diag_triples = convert_to_tuple(beh_diag_triples)
    
    
    # ahead diagonal triples for one
    ahead_diag_triples = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and (one_array[i][1] + 1) == one_array[j][1] and (one_array[i][1] + 2) == one_array[k][1]:
                    #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1])
                    ahead_diag_triples.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]]])
    ahead_diag_triples = convert_to_tuple(ahead_diag_triples)
    
    
    # vertical quads for one
    ver_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and one_array[i][0] + 3 == one_array[l][0] and one_array[i][1] == one_array[j][1] and one_array[i][1] == one_array[k][1] and one_array[i][1] == one_array[l][1]:
                        #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1],"--",one_array[l][0],one_array[l][1])
                        ver_quads.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]],[one_array[l][0],one_array[l][1]]])
    ver_quads = convert_to_tuple(ver_quads)  
    
    
    #Horizantal quads for one
    hor_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] == one_array[j][0] and one_array[i][0] == one_array[k][0] and one_array[i][0] == one_array[l][0] and (one_array[i][1] + 1) == one_array[j][1] and (one_array[i][1] + 2) == one_array[k][1] and (one_array[i][1] + 3) == one_array[l][1]:
                        #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1],"--",one_array[l][0],one_array[l][1])
                        hor_quads.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]],[one_array[l][0],one_array[l][1]]])
    hor_quads = convert_to_tuple(hor_quads)  
    
    
    # ahead diagonal quads for one
    ahead_dia_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and one_array[i][0] + 3 == one_array[l][0] and (one_array[i][1] + 1) == one_array[j][1] and (one_array[i][1] + 2) == one_array[k][1] and (one_array[i][1] + 3) == one_array[l][1]:
                        #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1],"--",one_array[l][0],one_array[l][1])
                        ahead_dia_quads.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]],[one_array[l][0],one_array[l][1]]])
    ahead_dia_quads = convert_to_tuple(ahead_dia_quads)  
    
    
    # behind diagonal quads for one
    beh_dia_quads = []
    for i in range(len(one_array)):
        for j in range(i+1, len(one_array)):
            for k in range(j+1, len(one_array)):
                for l in range(k+1, len(one_array)):
                    if one_array[i][0] + 1 == one_array[j][0] and one_array[i][0] + 2 == one_array[k][0] and one_array[i][0] + 3 == one_array[l][0] and (one_array[i][1] - 1) == one_array[j][1] and (one_array[i][1] - 2) == one_array[k][1] and (one_array[i][1] - 3) == one_array[l][1]:
                        #print(one_array[i][0],one_array[i][1],"--",one_array[j][0],one_array[j][1],"--",one_array[k][0],one_array[k][1],"--",one_array[l][0],one_array[l][1])
                        beh_dia_quads.append([[one_array[i][0],one_array[i][1]],[one_array[j][0],one_array[j][1]],[one_array[k][0],one_array[k][1]],[one_array[l][0],one_array[l][1]]])
    beh_dia_quads = convert_to_tuple(beh_dia_quads)  

    
    ahead_diag_pairs = remove_dup(ahead_diag_pairs, ahead_diag_triples)
    beh_diag_pairs = remove_dup(beh_diag_pairs, beh_diag_triples)
    ver_pairs = remove_dup(ver_pairs, ver_triples)
    hor_pairs = remove_dup(hor_pairs, hor_triples)
    ahead_diag_triples = remove_dup(ahead_diag_triples, ahead_dia_quads)
    beh_diag_triples = remove_dup(beh_diag_triples, beh_dia_quads)
    hor_triples = remove_dup(hor_triples, hor_quads)
    ver_triples = remove_dup(ver_triples, ver_quads)
    
    count = 0
    
    for i in hor_pairs:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1])
        if(i[0][1] - 1 >= 0):
            if(a[i[0][0]][i[0][1] - 1] == 0):
                flag_filled = 0
        if(i[1][1] + 1 <= 6):
            if(a[i[1][0]][i[1][1] + 1] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 1
        
    
    for i in ver_pairs:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1])
        if(i[0][0] - 1 >= 0):
            if(a[i[0][0] - 1][i[0][1]] == 0):
                flag_filled = 0
        if(i[1][0] + 1 <= 5):
            if(a[i[1][0] + 1][i[1][1]] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 1
        
    
    for i in beh_diag_pairs:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1])
        if(i[0][0] - 1 >= 0 and i[0][1] + 1 <= 6):
            if(a[i[0][0] - 1][i[0][1] + 1] == 0):
                flag_filled = 0
        if(i[1][0] + 1 <= 5 and i[1][1] - 1 >= 0):
            if(a[i[1][0] + 1][i[1][1] - 1] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 1
        
        
    for i in ahead_diag_pairs:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1])
        if(i[0][0] - 1 >= 0 and i[0][1] - 1 >= 0):
            if(a[i[0][0] - 1][i[0][1] - 1] == 0):
                flag_filled = 0
        if(i[1][0] + 1 <= 5 and i[1][1] + 1 <= 6):
            if(a[i[1][0] + 1][i[1][1] - 1] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 1
        
        
    for i in ver_triples:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1])
        if(i[0][0] - 1 >= 0):
            if(a[i[0][0] - 1][i[0][1]] == 0):
                flag_filled = 0
        if(i[2][0] + 1 <= 5):
            if(a[i[2][0] + 1][i[2][1]] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 50
        
    
    for i in hor_triples:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1])
        if(i[0][1] - 1 >= 0):
            if(a[i[0][0]][i[0][1] - 1] == 0):
                flag_filled = 0
        if(i[2][1] + 1 <= 6):
            if(a[i[2][0]][i[2][1] + 1] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 50
        
    for i in beh_diag_triples:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1])
        if(i[0][0] - 1 >= 0 and i[0][1] + 1 <= 6):
            if(a[i[0][0] - 1][i[0][1] + 1] == 0):
                flag_filled = 0
        if(i[2][0] + 1 <= 5 and i[2][1] - 1 >= 0):
            if(a[i[2][0] + 1][i[2][1] - 1] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 50
        
    
    for i in ahead_diag_triples:
        flag_filled = 1
        #print(i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1])
        if(i[0][0] - 1 >= 0 and i[0][1] - 1 >= 0):
            if(a[i[0][0] - 1][i[0][1] - 1] == 0):
                flag_filled = 0
        if(i[2][0] + 1 <= 5 and i[2][1] + 1 <= 6):
            if(a[i[2][0] + 1][i[2][1] - 1] == 0):
                flag_filled = 0
        if(flag_filled == 0):
            #print("Empty")
            count = count + 50
        
        
    count = count + 100 * len(ver_quads) + 100 * len(hor_quads) + 100 * len(ahead_dia_quads) + 100 * len(beh_dia_quads)
    return count


def evaluate_board(arr):
    one_array = []
    two_array = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                one_array.append([i,j])
            elif arr[i][j] == 2:
                two_array.append([i,j])
                
    max_wins = calculate_pairs(one_array, arr)
    min_wins = calculate_pairs(two_array, arr)
    
    return (max_wins - min_wins)
    
    #print("max wins are ", max_wins)
    #print("min wins are ", min_wins)

#def dummy():
#    a = [[0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 1, 0, 1, 0],
#         [0, 0, 1, 1, 2, 1],
#         [0, 2, 1, 2, 1, 1],
#         [1, 1, 2, 2, 2, 1]]
#
#    evaluate_board(a)
#    
#dummy()