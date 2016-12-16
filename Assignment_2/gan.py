from random import randint
import random

main_gen = {}

def generate_population(np, n):
    p = 0;
    while(p < np): 
        i = 0
        rand = []
        flag = 0
        while(i < n):
            ran = randint(0,n-1)

            for j in range(0,i):
                if(ran == rand[j]):
                    flag = 1

            if(flag == 1):
                flag = 0
                continue
                
            else:
                rand.append(ran)
            i = i + 1
        #print (rand)
        main_gen[p] = rand
        p = p + 1;

def fitness(chromosome, n):
    fitness = 0
    for i in range(0, n):
        count = 1
        for j in range(i+1, n):
            present_x = chromosome[i]
            present_y = i
            
            next_x = chromosome[j]
            next_y = j
            
            if(present_x + count == next_x and present_y + count == next_y):
                fitness = fitness + 1
            elif(present_x + present_y == next_x + next_y):
                fitness = fitness + 1
            elif(present_x ==
                 next_x):
                fitness = fitness + 1
            count = count + 1
    return fitness

def cross_pos():
    i = 0
    flag = 0
    rand = []
    while(i < 2):
            ran = randint(0,7)

            for j in range(0,i):
                if(ran == rand[j]):
                    flag = 1

            if(flag == 1):
                flag = 0
                continue
            else:
                rand.append(ran)
            i = i + 1

    rand.sort()
    return rand

def crossover(c1, c2, n):
    c3 = []
    temp = []
    for i in range(0,n):
        c3.append(0)
    
    rand = cross_pos()
    
    while(rand[0] == 0 and rand[1] == 7):
        rand = cross_pos()
            
    #print ("2 random numbers generated are : ", rand)
    
    #c1_temp = copy.copy(c1)
    #c2_temp = copy.copy(c2)
    
    #print("c1 is : ",c1)
    #print("c2 is : ",c2)
    
    slic = c1[rand[0]:rand[1]+1]
    
    for i in range(rand[0], rand[1]+1):
        c3[i] = c1[i]
        
    #print("slice is : ",slic)
    #print("c3 is : ",c3)
    
    for i in range(rand[1] + 1, n):
        temp.append(c2[i])
    
    for i in range(0, rand[1] + 1):
        temp.append(c2[i])
        
    #print ("temp is : ",temp)
    
    for i in range(len(slic)):
        temp.remove(slic[i])
        
    #print("modified temp is ", temp)
    
    for i in range(rand[1] + 1, n):
        c3[i] = temp.pop(0)
        
    for i in range(0, rand[0]):
        c3[i] = temp.pop(0)
    
    #print("Final c3 is : ", c3)
    
    return c3


np = input("Enter population : ")
n = input("Enter number of queens : ")
runs = input("Enter number of runs : ")

np = int(np)
n = int(n)
runs = int(runs)

if(n > 8):
    steps = np * 50
else:
    steps = np

mut_prob = 0.1
fit_min = n*n
opt = 0;

for run in range(0, runs):
    
    generate_population(np, n)

    for i in range(0, np):
        fit = fitness(main_gen[i], n)
        if(fit == 0):
            print("Zero fitness found for parent chromosome - ", i, " Chromosome details are - ", main_gen[i])
            opt = opt + 1
            
    for i in range(0, steps):
        p1 = randint(0,np-1)
        p2 = randint(0,np-1)

        while(p2 == p1):
            p2 = randint(0,np-1)

        p3 = randint(0,np-1)

        while(p3 == p1 or p3 == p2):
            p3 = randint(0,np-1)

        child = crossover(main_gen[p1], main_gen[p2], n)
        
        mp = random.random()
        
        #print("mp is ",mp)
        if(mp < mut_prob):
            mut_pos1 = randint(0,n-1)
            mut_pos2 = randint(0,n-1)
            
            e1 = child[mut_pos1]
            e2 = child[mut_pos2]
            
            e3 = e1
            e1 = e2
            e2 = e3
            
            child[mut_pos1] = e1
            child[mut_pos2] = e2
            #print("Mutated", mp)
        
        main_gen[p3] = child
        
        fit = fitness(child, n)
        
        #print("Fitness of child is : ", fit)

        if(fit == 0):
            print("Zero fitness found for child chromosome - ", child, " Run number is - ", run)
            opt = opt + 1
        if(fit_min > fit):
            fit_min = fit
            
print("Total Minimum fitness found is : ",fit_min)
print("Total number of optimizations are  : ",opt)