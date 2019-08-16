# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:45:27 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

prob_list = []
error_list = []

def false_val_prob(a,b,N):
    ran_arr = np.random.randint(a,b,N)
    false_list = []
    n = 0
    for i in range(len(ran_arr)):
        if ran_arr[i] == False:
            n += 1
            print("A zero has been hit, at iteration {:}".format(i))
            false_list.append(i)
    print(48*"-")
    print("{:} zeros have been hit".format(n))
    print(48*"-")
    
    p = n/N
    pt = 1/(b-a)
    error = abs(p-pt)
    print("The experimental probability of a zero being hit is {:.5f}".format(p))
    print(48*"-")
    print("The theoretical probability of a zero being hit is {:.5f}".format(pt))
    print(48*"-")
    print("The error is {:.5f}".format(error))
    print(48*"-")
    x = [i for i in range(len(false_list))]
    prob_list.append(p)
    error_list.append(error)
    t = [k for k in range(len(prob_list))]
    plt.subplot(1,2,1)
    plt.plot(x,false_list,'ko',alpha=0.5, label="Zero Hits")
    plt.title("Iterations Where Zeros Were Hit")
    plt.xlabel("x-points"); plt.ylabel("Iteration points")
    plt.subplot(1,2,2)
    plt.plot(t,prob_list,'md', label="Probability Values")
    plt.plot(t,error_list,'cd', label="Error Values")
    plt.title("Probability and Error at Each Iteration")
    plt.xlabel("Iteration"); plt.ylabel("Probability")
#    print(prob_list)
    mean_p = sum(prob_list)/len(prob_list)
    var_p = 0
    for i in range(len(prob_list)):
        var_p += (prob_list[i]-mean_p)**2
    var_p = var_p/len(prob_list)
    stan_p = np.sqrt(var_p)
    print("The emperical variance of the probability is {:.8f}".format(var_p))
    print(48*"-")
    print("The emperical standard deviation of the probability is {:.8f}".format(stan_p))
    
def greater_than_false_prob(a,b,N):
    ran_arr = np.random.randint(a,b,N)
    greater_list = []
    n = 0
    for i in range(len(ran_arr)):
        if ran_arr[i] > False:
            greater_list.append(ran_arr[i])
            n += 1
            print("A value greater than zero: {:} has been hit at iteration {:}".format(ran_arr[i],i))
    print(48*"-")
    print("{:} values have been hit".format(n))
    
    p = n/N
    pt = 10/(b-a)
    error = abs(p-pt)
    print(48*"-")
    print("The experimental probability of a value greater than zero to be hit is {:.5f}".format(p))
    print(48*"-")
    print("The theoretical probability of a value greater than zero to be hit is {:.5f}".format(pt))
    x = [i for i in range(len(greater_list))]
    prob_list.append(p)
    error_list.append(error)
    t = [k for k in range(len(prob_list))]
    plt.subplot(1,2,1)
    plt.plot(x,greater_list,'k+',alpha=0.5)
    plt.title("Iterations Where a Value Greater Than Zero Has Been Hit")
    plt.xlabel("Iterations"); plt.ylabel("Values")
    plt.subplot(1,2,2)
    plt.plot(t,prob_list,'md')
    plt.plot(t,error_list,'cd')
    plt.title("Probability and Error of Each Iteration")
    plt.xlabel("Iterations"); plt.ylabel("Probability")
    
    mean_p = sum(prob_list)/len(prob_list)
    var_p = 0
    for i in range(len(prob_list)):
        var_p += (prob_list[i] - mean_p)**2
    var_p = var_p/len(prob_list)
    stan_p = np.sqrt(var_p)
    print(48*"-")
    print("The emperical variance of the probability is {:.8f}".format(var_p))
    print(48*"-")
    print("The emperical standard deviation of the probability is {:.8f}".format(stan_p))
    

N_input = input("N = ")
N = int(N_input)


def iterations(N):
    for i in range(N):
#        false_val_prob(-10,10,250)
        greater_than_false_prob(-10,10,250)



iterations(N)