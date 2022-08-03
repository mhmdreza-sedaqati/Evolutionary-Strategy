from numpy import random



def One_Plus_One_ES(z):
    tmp = One_Plus_One_Mutation(z)
    t = tmp
    z = Check_Fitness(z , t)
    return z



def One_Plus_One_Mutation(z):
    x = random.normal(loc = 0 , scale = 1 , size = 1)
    t = z + x[0]
    return t



def Fitness_function(z):
    result = (z * z) + (2 * z)
    return result



def Check_Fitness(x , y):
    fitness_x = Fitness_function(x)
    fitness_y = Fitness_function(y)
    if fitness_x > fitness_y:
        return y
    else:
        return x



def One_plus_mute(z , sigma):
    x = random.normal(loc = 0 , scale = sigma , size = 1)
    t = z + x[0]
    return t



def Parent_Selection(population):
    C = 2
    a_random_number = len(population) - 1
    Parents_list = []
    
    while C != 0:
        y = random.uniform(0 , a_random_number , size = (1))
        x = round(y[0])
        Parents_list.append(population[x])
        del(population[x])
        print(x)
        C = C - 1
        a_random_number = a_random_number - 1
                
    return Parents_list



def Child_generation(Parents_list):
    Children_list = []
    for j in Parents_list:
        ls = One_Plus_One_Mutation(j)
        Children_list.append(ls)
    return Children_list


Met = "3"
count = 5
n = 100



#Part 1
if Met == "1":
    while count > 1:
        z = One_Plus_One_ES(z)
        print(z)
        count = count - 1
        
        

#Part 2
if Met == "2": 
    k = 0.9
    h = 5
    sigma = 1
    moving_well = 0
    s = 0
    
    while count > 1:
        print("Sigma : " , sigma)
        x = One_plus_mute(z , sigma)
        y = Check_Fitness(z , x)
        if y == x:
            moving_well = moving_well + 1

        z = y
        print(z)
        
        count = count - 1
        h = h - 1
        s = s + 1
        if h == 0:
            average = moving_well / s
            if average > 0.2:
                sigma = sigma / k
            if moving_well < 0.2:
                sigma = sigma * k
            h = 5
            moving_well = 0
            
            
            
#Part 3
if Met == "3":

    mod = "1"
    population = [7 , -13 , 65 , 14 , -23 , 19 , 4 , -9 , 30 , 45]
    
    while count > 1:

        Parents_list = Parent_Selection(population)
        Children_list = Child_generation(Parents_list)
        count = count - 1
        
        print("population : " , population)
        print("Parents : " , Parents_list)
        print("Children : " , Children_list)

        if mod == "2":
            for j in Children_list:
                population.append(j)

        else:
            fitted_list = []
            parents_children_list = []
            
            for k in Children_list:
                parents_children_list.append(k)
                
            for l in Parents_list:
                parents_children_list.append(l)
                
            print("parents and children : " , parents_children_list)
            
            for p in parents_children_list:
                fitted_list.append(Fitness_function(p))
            print("fit list : " , fitted_list)
            
            minimum = min(fitted_list)

            print("Minimum : " , minimum)
            
            X_fitted_list = []
            X_parents_children_list = []
            for tst in range(len(fitted_list)):
                if fitted_list[tst] == minimum:
                    print(fitted_list[tst])
                    print(parents_children_list[tst])
                    
                    abc = parents_children_list[tst]
                    population.append(abc)
                    minimum_0 = tst
                
                else:
                    print(fitted_list[tst])
                    X_parents_children_list.append(parents_children_list[tst])
                    X_fitted_list.append(fitted_list[tst])
                    
            print(X_parents_children_list)        
            print(X_fitted_list)
            minimum_1 = min(X_fitted_list)
            
            for V in range(len(X_fitted_list)):
                if X_fitted_list[V] == minimum_1:
                    xyz = X_parents_children_list[V]
                    population.append(xyz)
                    break

        print("New Population : " , population)

