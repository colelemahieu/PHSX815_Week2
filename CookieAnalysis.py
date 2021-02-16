# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from math import floor

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    #Calculate quartiles for the times array
    if len(times)%2==0:
        med_times = (float(times[(len(times)/2)-1]) + float(times[len(times)/2]))/2
    else:
        med_times = times[int(floor(len(times)/2))]

    #Calculate quartiles for the times_avg array
    if len(times_avg)%2==0:
        med_avg = (float(times_avg[(len(times_avg)/2)-1]) + float(times_avg[len(times_avg)/2]))/2
    else:
        med_avg = times_avg[int(floor(len(times_avg)/2))]

    if (len(times)%4==2 or len(times)%4==3):
        quart1 = times[int(floor(len(times)/4))]
        quart3 = times[len(times)-int(floor(len(times)/4))-1]
    else:
        quart1 = float(times[int(floor(len(times)/4))-1] + times[int(floor(len(times)/4))])/2
        quart3 = float(times[len(times)-(int(floor(len(times)/4))-1)-1] + times[len(times)-int(floor(len(times)/4))-1])/2 

    if (len(times_avg)%4==2 or len(times_avg)%4==3):
        quart1_avg = times_avg[int(floor(len(times_avg)/4))]
        quart3_avg = times_avg[len(times_avg)-int(floor(len(times_avg)/4))-1]
    else:
        quart1_avg = float(times_avg[int(floor(len(times_avg)/4))-1] + times_avg[int(floor(len(times_avg)/4))])/2
        quart3_avg = float(times_avg[len(times_avg)-(int(floor(len(times_avg)/4))-1)-1] + times_avg[len(times_avg)-int(floor(len(times_avg)/4))-1])/2


    #Plotting details
    plt.figure()
    plt.hist(times, bins=100, density=True, alpha=0.75)

    #Plot Quartiles
    plt.axvline(med_times, color="k", linestyle="solid", linewidth=1.25)
    plt.axvline(quart1, color="k", linestyle="solid", linewidth=1.25)
    plt.axvline(quart3, color="k", linestyle="solid", linewidth=1.25)
    
    plt.xlabel("Eating Rate of 4 Cookies per Day")
    plt.ylabel('"Probability"')
    plt.title("Times (Divided into Quartiles)",fontweight="bold")
    
    plt.figure()
    plt.hist(times_avg, bins=100, density=True, alpha=0.75)

    #Plot and Label Quartiles
    plt.axvline(med_avg, color="k", linestyle="solid", linewidth=1.25)
    plt.text(med_avg-0.008, 20.5, "Median", rotation=90, fontweight="bold")
    plt.axvline(quart1_avg, color="k", linestyle="solid", linewidth=1.25)
    plt.text(quart1_avg-0.008, 20.5, "First Quartile", rotation=90, fontweight="bold")
    plt.axvline(quart3_avg, color="k", linestyle="solid", linewidth=1.25)
    plt.text(quart3_avg-0.008, 20.5, "Third Quartile", rotation=90, fontweight="bold")
    
    plt.xlabel("Average Time Between Missing Cookies (Days)")
    plt.ylabel('"Probability"')
    plt.title("Average Times", fontweight="bold")
    
    plt.show()
