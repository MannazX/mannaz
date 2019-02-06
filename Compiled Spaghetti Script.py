# -*- coding: utf-8 -*-
"""
Welcome to the "Spaghetti Script series".
These scripts serve as conglomorates of everything that Magnus
has learned about coding over the last 3 months of going to university.
The purpose of these scripts is to be creative and self-educating, 
since coding in python 3.6 is a fundamental part of his education.
This script will include various attempts to simulate and model with this
amazing tool and shall be extended as new knowledge is gained. 
So brace yourself, it's going to be a deep rabbithole!
"""
#First import the desired modules for the script
import numpy as np
import matplotlib.pyplot as plt
import math as m

def Chaos1():
    #A foundation is needed to start a script, this will be in the form of
    #data, pick any file to load down data from, and make your own set!
    spa_file = open('spa_data1.txt', 'r')
    spa_file
    
    x_list = []
    y_list = []
    
    for line in spa_file:
        spl = line.split()
        x_list.append(spl[0])
        y_list.append(spl[1])    
    x_list = np.asarray(x_list)
    y_list = np.asarray(y_list)
    for lists in x_list,y_list:
        print(lists)
#    spa_shuffle = np.random.shuffle(y_list)
    rndm_chaos = []
    for ran in range(len(y_list)):
        rnd_int = np.random.randint(1,98,ran)
        rndm_chaos.append(rnd_int)
    #print(rndm_chaos)
    rndm_chaos = np.concatenate(rndm_chaos)
    rndm_chaos_len = []
    for rlen in range(len(rndm_chaos)):
        rndm_chaos_len.append(rlen)
    
    spa_file.close()
    
    plt.subplot(2,2,1)
    plt.plot(rndm_chaos_len,rndm_chaos,'r+')
    plt.plot(rndm_chaos_len,rndm_chaos)
    plt.xlabel('Random value number'); plt.ylabel('Random value')
    plt.subplot(2,2,2)
    plt.hist(rndm_chaos)
    plt.xlabel('Random distribution intervals'); plt.ylabel('Frequency of distribution')
    plt.subplot(2,2,3)
    plt.plot(x_list,y_list, 'r+')
    plt.plot(x_list,y_list)
    plt.axis([0,20,0,20])
    plt.subplot(2,2,4)
    plt.hist(y_list)
    #As you can see, this is an aweful mess of randomly generated values
    #Plotting these reveals how chaotic the results can become
    #This can be done through numpy arrays aswell, lets dig further into that in
    #The next spaghetti script
    #Docstring will come below
    
"""
spa_file is a list containing the data imported from a text file containing
the data that is used to generate the random chaos.
x_list is a list that will contain the random value numbers for the plots,
that is converted to a numpy array.
y_list is a list that will contain the random values for the plots, also
converted to a numpy array.
"""
def Chaos2():
    #Lets try doing a similar script but this time lets use numpy as our
    #tool for generating a random chaos of a python script
    spa_file2 = np.loadtxt('spa_data2.txt', delimiter = ',', dtype = int)
    spa_arr1 = spa_file2[:,0]
    spa_arr2 = spa_file2[:,1]
    for i in range(len(spa_arr1)):
        arr_ran = np.random.random(i)
        arr_zeros = np.zeros(i, dtype=float)
        arr_zeros += arr_ran
    #print(arr_zeros)
    for j in range(len(spa_arr1)):
        arr_ran_int = np.random.randint(0,10,j)
        arr_zeros2 = np.zeros(j, dtype=int)
    #print(arr_ran_int)
    for i in range(len(arr_ran)):
        if arr_ran_int[i] > arr_ran[i]:
            arr_zeros2 += arr_ran_int
        else:
            break
    #print(arr_zeros2)
    minarg = np.argmin(arr_ran_int)
    maxarg = np.argmax(arr_ran_int)
    for i in range(len(arr_ran_int)):
        if minarg < arr_ran_int[i] < maxarg:
            arr_zeros2 -= minarg
            arr_zeros2 += maxarg
        else:
            break
    
    plt.subplot(2,2,1)
    plt.plot(spa_arr1,spa_arr2)
    plt.plot(spa_arr1,spa_arr2,'r+')
    plt.xlabel('Data length value'); plt.ylabel('Data frequency values')
    plt.title('Plot of the data values')
    plt.subplot(2,2,2)
    plt.hist(spa_arr2)
    plt.title('Histogram of the data frequency values')
    plt.subplot(2,2,3)
    #plt.plot(arr_zeros,arr_zeros2)
    plt.plot(arr_zeros,arr_zeros2,'o')
    plt.xlabel('x-value data'); plt.ylabel('y-value data')
    plt.title('Scatter plot of data values in zeros lists')
    plt.subplot(2,2,4)
    plt.hist(arr_zeros2)
    plt.title('Histogram of the y-value data')

"""
spa_arr1 and 2 are arrays of the first and second data columns respektively
arr_ran = array with randomly generated float values
arr_zeros = array with zero values of float type, that is incremented with the
arr_ran array
arr_ran_int = array with randomly generated integers in the length of spa_arr1
arr_zeros2 = second array with zeros, but of integer type, that is incremented
with the arr_ran_int array.
minarg = The minimum index value of arr_ran_int
maxarg = The maximum index value of arr_ran_int
The first plot shows the values of spa_arr1 and spa_arr2 plotted together
The second plot shows a histogram of the spa_arr2 values
The third plot shows the plotted values of arr_zeros and arr_zeros2 values.
The fourth plot shows a histogram of the arr_zeros2 values
The third and the fourth plot will vary when plotted multiple times, unless if
a numpy seed function is added.
"""

def Chaos3():
    #In this layer we will look at how to soft-code plots of functions and
    #certain equations, when this is done we will look at how their derivatives look.
    def Diff_eq1(t):
        v0 = 2
        w = 20
        return -v0*np.exp(-w*t)
    t = np.linspace(1,2,100)
    y = Diff_eq1(t)
    
    def Diff_eq2(t):
        v0 = 2
        w = 20
        return v0*np.exp(-w*t)+v0
    g = Diff_eq2(t)
    
    def Sine_func(t):
        A = 2
        w = 10
        i = np.pi/2
        return A*np.sin(w*t+i) + A
    h = Sine_func(t)
    
    def Cosine_func(t):
        A = 2
        w = 10
        i = np.pi/2
        return A*np.cos(w*t+i) + A
    k = Cosine_func(t)
    
    def Derivative1(t):
        v0 = 2
        w = 20
        return w*v0*np.exp(-w*t)
    dy = Derivative1(t)
    
    def Derivative2(t):
        v0 = 2
        w = 20
        return -w*v0*np.exp(-w*t)
    dg = Derivative2(t)
    
    def Derivative3(t):
        A = 2
        w = 10
        i = np.pi/2
        return -w*A*np.cos(w*t+i)
    dh = Derivative3(t)
    
    def Derivative4(t):
        A = 2
        w = 10
        i = np.pi/2
        return w*A*np.cos(w*t+i)
    dk = Derivative4(t)
    
    plt.subplot(2,4,1)
    plt.plot(t,y)
    plt.title("Differential equation 1")
    plt.subplot(2,4,2)
    plt.plot(t,g)
    plt.title("Differential equation 2")
    plt.subplot(2,4,5)
    plt.plot(t,dy,'r')
    plt.title("Derivative of above")
    plt.subplot(2,4,6)
    plt.plot(t,dg,'r')
    plt.title("Derivative of above")
    plt.subplot(2,4,3)
    plt.plot(t,h,'g')
    plt.title("Sine wave")
    plt.subplot(2,4,7)
    plt.plot(t,dh,'m')
    plt.title("Derivative of above")
    plt.subplot(2,4,4)
    plt.plot(t,k,'g')
    plt.title("Cosine wave")
    plt.subplot(2,4,8)
    plt.plot(t,dk,'m')
    plt.title("Derivative of above")
    
"""
Diff_eq1 is a function that plots an exponential solution of a differentialequation
Diff_eq2 is a function that plot a similar exponential solution to the above
mentioned equation.

"""

def Chaos4():
    #This is a variation of Euler's method for discretising diff eq's.
    def slope(a,b,c,x):
        dy = a*x+(b+c)
        return dy

    def Solved_Eq(a,b,c,n,h,r):
        y_list = []
        x_list = []
        p_list = []
        y = 0
        x = 0
        for x in range(n):
            y_list.append(y)
            x_list.append(x)
            y += h*slope(a,b,c,x)
            p = c*m.exp(a*x-b)
            p_list.append(p)
            x += h
        plt.subplot(1,2,1)
        plt.plot(x_list,y_list,'r',linestyle = 'dashed')
        plt.title("Equation un-descretised")
        plt.xlabel("x-values"); plt.ylabel("y-values")
        if r == 1:
            plt.subplot(1,2,2)
            plt.plot(x_list,p_list,'m',linestyle = 'dashed')
            plt.title("Equation descretised")
            plt.xlabel("x-values"); plt.ylabel("p-values")
            
    Solved_Eq(2,5,5,50,1,1)        
    Solved_Eq(2,5,5,50,2,1)
    Solved_Eq(2,5,5,50,5,1)         
    
def Chaos5():
    def A(x):
        return(0 if x <= 0 else 1)
    
    def B(x):
        return(1 if x <= 0 else 0)
    
    A = np.vectorize(A)
    x = np.linspace(-20,20,50)
    y = 0.5*np.sin(0.08*x)+0.5
    Av = A(x)
    B = np.vectorize(B)
    Bv = B(x)
    g = 0.5*np.cos(0.08*x-4.8)+0.5
    
    plt.subplot(1,2,1)
    Heave1, = plt.plot(x,Av,'k',linestyle="dashed", label="Heaveside function")
    Sine, = plt.plot(x,y,'mo', label="Sine wave")
    plt.xlabel("x-values"); plt.ylabel("y-values")
    plt.legend(handles = [Heave1, Sine], loc="upper left")
    plt.subplot(1,2,2)
    Heave2, = plt.plot(x,Bv,'r',linestyle="dashed", label="Heaveside function")
    Cosine, = plt.plot(x,g,'go', label="Cosine wave")
    plt.xlabel("x-values"); plt.ylabel("y-values")
    plt.legend(handles = [Heave2, Cosine], loc="upper right")

def Chaos6():
    x_arr = np.arange(2,20,2)
    y_arr = np.arange(2,36,4)
    x_slice = x_arr[1:-2]
    y_slice = y_arr[1:-2]
    
    x_table = np.arange(8).reshape((4,2))
    y_table = 4*np.ones((4,2))
    pr_table = x_table*y_table
    val_arr = np.concatenate(pr_table)
    cu_sum_arr = np.cumsum(val_arr)
    
    n_table = np.arange(16).reshape((4,4))
    p_table = 2*np.ones((4,4))
    sum_table = n_table + p_table
    pro_table = n_table * p_table
    dotp_tables = sum_table @ pro_table
    val_sum = np.concatenate(sum_table)
    val_pro = np.concatenate(pro_table)
    val_dp = np.concatenate(dotp_tables)
    cu_sum_dp = np.cumsum(val_dp)
    
    for length in range(len(val_sum)):
        len_arr = np.linspace(0,length+1,length+1)
    #print(len_arr)
    
    for i in pr_table:
        print(i)
    
    for i in sum_table, pro_table, dotp_tables:
        print(i)
    
    plt.subplot(2,2,1)
    plt.plot(val_arr,cu_sum_arr, 'mo')
    plt.title("Values plotted against their cumulative sum values")
    plt.xlabel("Values"); plt.ylabel("Cumulative sum values")
    plt.subplot(2,2,2)
    plt.plot(x_slice,y_slice, 'rd')
    plt.title("Plot of x and y slices")
    plt.xlabel("x-slices"); plt.ylabel("y-slices")
    plt.subplot(2,2,3)
    Sum, = plt.plot(len_arr,val_sum,linestyle='dashed',label="Sum")
    Product, = plt.plot(len_arr,val_pro,'ro',label="Product")
    Dotproduct, = plt.plot(len_arr,val_dp,'md',label="Dot-product")
    plt.title("Values of sum, product, and dotproduct of the tables")
    plt.xlabel("Values"); plt.ylabel("Length values")
    plt.legend(handles = [Sum,Product,Dotproduct], loc = "upper left")
    plt.subplot(2,2,4)
    plt.plot(val_dp,cu_sum_dp,'kx')
    plt.title("Values of the dot-product plotted against their cumulative sum values")
    plt.xlabel("Values"); plt.ylabel("Cumulative sum values")

def Chaos7():
    data_file = np.loadtxt('spa_data2.txt', delimiter = ',', dtype = int)
    xdata = data_file[:,0]
    ydata = data_file[:,1]
    def median(f):
        med_sum = 0
        n = len(ydata)
        for i in ydata:
            med_sum += f(i)
        return (1/n)*med_sum
    print("The median value for the y-data is {:.1f}".format(median(lambda x:x)))
    med = median(lambda x:x)
    def variance(f):
        var_sum = 0
        n = len(ydata)
        for i in ydata:
            var_sum += f((i-med)**2)
        return (1/n)*var_sum
    print("The variance of the y-data is {:.1f}".format(variance(lambda x:x)))
    var = variance(lambda x:x)
    standard_deviation = np.sqrt(var)
    print("The standard deviation of the y-data is {:.1f}".format(standard_deviation))
    
    plt.subplot(1,2,1)
    plt.plot(xdata,ydata,"g")
    plt.title("x-data plotted against y-data")
    plt.xlabel("x-data"); plt.ylabel("y-data")
    plt.subplot(1,2,2)
    plt.hist(ydata)
    plt.title("Histogram of ydata values")
    plt.xlabel("Value intervals of y-data"); plt.ylabel("Frequency of the values in the intervals")

def Chaos8():
    def mean(f,a,b,n):
        np.random.seed(24)
        mean_sum = 0
        rand_arr = np.random.randint(a,b,n)
        for i in rand_arr:
            mean_sum += f(i)
        return (1/n)*mean_sum
    print("The mean value of the random numbers is {:.1f}".format(mean(lambda x:x,1,10,20)))
    mean = mean(lambda x:x,1,10,20)
    
    def variance(f,a,b,n):
        np.random.seed(24)
        var_sum = 0
        rand_arr = np.random.randint(a,b,n)
        for i in rand_arr:
            var_sum += f((i-mean)**2)
        return (1/n)*var_sum
    print("The variance of the random numbers is {:.1f}".format(variance(lambda x:x,1,10,20)))
    var = variance(lambda x:x,1,10,20)
    standard_deviation = np.sqrt(var)
    print("The standard deviation of the random numbers is {:.1f}".format(standard_deviation))
    
    def plot(a,b,n):
        np.random.seed(24)
        rand_arr = np.random.randint(a,b,n)
        len_list = []
        for i in range(1,n+1):
            len_list.append(i)
        len_arr = np.asarray(len_list)
        plt.subplot(1,2,1)
        plt.plot(len_arr,rand_arr,'gx')
        plt.subplot(1,2,2)
        plt.hist(rand_arr,color="k")
    plot(1,10,20)    

def Pick():
    print("Pick the layer of chaos that you are willing to examine:")
    layer = str(input("Dive to layer:"))
    if layer == "1":
        Chaos1()
    elif layer == "2":
        Chaos2()
    elif layer == "3":
        Chaos3()
    elif layer == "4":
        Chaos4()
    elif layer == "5":
        Chaos5()
    elif layer == "6":
        Chaos6()
    elif layer == "7":
        Chaos7()
    elif layer == "8":
        Chaos8()
    else:
        print("Are you being serious right now!", layer, "is not a layer of the rabbit hole, try again with a bloody number, if you dare! --Magnus")
Pick()