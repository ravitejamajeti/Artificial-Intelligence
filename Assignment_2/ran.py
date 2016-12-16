from random import randint
import random

main_gen = []

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
        main_gen.append(rand)
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

np = 100
n = 8
steps = 10

runs = 1
mut_prob = 0.1
fit_min = n*n

for run in range(0, runs):
    
    main_gen = []
    fit = []
    next_gen_child = []
    next_gen_fit = []
    
    generate_population(np, n)
    
    for i in range(0, np):
        fit_main = fitness(main_gen[i], n)
        if(fit_main == 0):
            print("Zero fitness found for parent chromosome - ", i, " Chromosome details are - ", main_gen[i])
        fit.append(fit_main)
    
    for step in range(0, steps):
        
        main_gen = [main_gen for (fit,main_gen) in sorted(zip(fit,main_gen))]
    
        fit.sort()
        
        #print("main_gen is ", main_gen)
        
        pop = 0
        
        while(pop < np):

            child = crossover(main_gen[pop], main_gen[pop + 1], n)
            
            #print("Parent 1 is ", main_gen[pop], " Parent 2 is ", main_gen[pop + 1], "Child is : ", child, "pop is ", pop, "step is ", step)
            
            mp = random.random()
            
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

            fit_child = fitness(child, n)
            
            if(fit_child == 0):
                print("Zero fitness found for child chromosome - ", child, " Step number is - ", step, " Run number is - ", run)
            if(fit_min > fit_child):
                fit_min = fit_child
            
            next_gen_child.append(child)
            next_gen_fit.append(fit_child)
            
            pop = pop + 2
            
        for i in range(0, int(np/2)):
            next_gen_child.append(main_gen[i])
            next_gen_fit.append(fit[i])
        
        main_gen = next_gen_child
        fit = next_gen_fit
        next_gen_child = []
        next_gen_fit = []
        
print("Total Minimum fitness found is : ",fit_min)