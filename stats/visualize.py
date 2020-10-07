import numpy as np
from matplotlib import pyplot as plt
from typing import List



def plot_times(times: List[tuple]):
    small = []
    medium = []
    large = []
    close = []
    far = []
    for time in times: 
        small.append((time[0][0], time[1] + "\n" +str(round(time[0][0], 6))))
        medium.append((time[0][1], time[1] + "\n" +str(round(time[0][1], 6))))
        large.append((time[0][2], time[1] + "\n" +str(round(time[0][2], 6))))
        close.append((time[0][3], time[1] + "\n" +str(round(time[0][3], 6))))
        far.append((time[0][4], time[1] + "\n" +str(round(time[0][4], 6))))
    print("generating plots")
    generate_bar_plot(small, "Small amount of data (n = 1000)")
    generate_bar_plot(medium, "Medium amount of data (n = 10000)")
    generate_bar_plot(large, "Large amount of data (n = 40000)")
    generate_bar_plot(close, "Close together data (n = 20000)")
    generate_bar_plot(far, "Far apart data (n = 20000)")
    print("generated plots")

def generate_bar_plot(data: list, title: str):
    parsed_data = [d[0] for d in data]
    labels = [d[1] for d in data]
     
    
    fig = plt.figure(figsize = (10, 5)) 
    
    # creating the bar plot 
    plt.bar(labels, parsed_data, color ='maroon',  
            width = 0.4) 
    
    plt.xlabel("Algorithm used") 
    plt.ylabel("Average time to sort (n = 10)") 
    plt.title(title)
    plt.savefig("plots/" + title.split(" ")[0])

