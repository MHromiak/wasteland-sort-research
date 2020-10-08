import os, sys, shutil, copy, time
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from other_sorts import heapsort as h, merge as m, quicksort as q, timsort as t, radix as r

from wasteland_sort import wasteland_sort as ws
from stats import stats, visualize
from typing import List
from pprint import pprint


def compare():
    #Modify info to change the data distribution and sample size
    info = [(100, 1000), (1000, 10000), (4000, 40000), (2, 20000), (100000, 20000)]
    data_i = [stats.generate_data(info) for x in range(10)]
    
    #Sorts info into each size/distribution category
    i_vals = data_from_stats(data_i)
    
    #Reset plot directory
    folder = myPath + "/plots"
    try:
        shutil.rmtree(folder)
    except:
        pass
    os.mkdir(folder)
    
    floats = []
    ints = []
    print("starting sort")
    
    #Time all sorts except Radix
    ints.append(heap(copy.copy(i_vals)))
    ints.append(merge(copy.copy(i_vals)))
    ints.append(quicksort(copy.copy(i_vals)))
    ints.append(timsort(copy.copy(i_vals)))
    ints.append(wasteland(copy.copy(i_vals)))

    #Plot above averages
    visualize.plot_times(ints)

    #Insert titles and time Radix sort
    ints.insert(0, ("Small", "Medium", "Large", "Close", "Far", "Sort name"))
    ints.append(radix(copy.copy(i_vals)))

    #Write results to file
    results = open("sorting_results.txt", "w")
    for item in ints:
        results.write(str(item) + "\n")
    results.close()


def heap(data: List[list]) -> List[float]:
    times = []
    for dset in data:
        set_times = []
        for d in dset:
            start = time.time()
            h.heap_sort(d)
            end = time.time()
            set_times.append(end - start)
        times.append(sum(set_times) / len(set_times))
    print("heapsort sorting complete")
    return (times, "heap")


def merge(data: List[list]) -> List[float]:
    times = []
    for dset in data:
        set_times = []
        for d in dset:
            start = time.time()
            m.merge_sort(d)
            end = time.time()
            set_times.append(end - start)
        times.append(sum(set_times) / len(set_times))
    print("mergesort sorting complete")
    return (times, "merge")


def quicksort(data: List[list]) -> List[float]:
    times = []
    for dset in data:
        set_times = []
        for d in dset:
            start = time.time()
            q.quick_sort(d)
            end = time.time()
            set_times.append(end - start)
        times.append(sum(set_times) / len(set_times))
    print("quicksort sorting complete")
    return (times, "quicksort")


def radix(data: List[list]) -> List[float]:
    times = []
    for dset in data:
        set_times = []
        for d in dset:
            start = time.time()
            r.radixSort(d)
            end = time.time()
            set_times.append(end - start)
        times.append(sum(set_times) / len(set_times))
    print("radix sorting complete")
    return (times, "radix")


def timsort(data: List[list]) -> List[float]:
    times = []
    for dset in data:
        set_times = []
        for d in dset:
            start = time.time()
            try:
                list.sort(d)
            except:
                print("Couldn't sort:" + str(len(d)))
                continue
            end = time.time()
            set_times.append(end - start)
        try:
            times.append(sum(set_times) / len(set_times))
        except:
            times.append(None)
    print("timsort sorting complete")
    return (times, "timsort")


def wasteland(data: List[list]) -> List[float]:
    times = []
    for dset in data:
        set_times = []
        for d in dset:
            start = time.time()
            ws.wasteland_sort(d, False)
            end = time.time()
            set_times.append(end - start)
        times.append(sum(set_times) / len(set_times))
    print("wasteland sorting complete")
    return (times, "wasteland")


def data_from_stats(data: List[list]) -> List[list]:
    keepr = 0
    extracted = [[], [], [], [], []]

    #Orders all samples into small, medium, large, near, far. If you want more categories, change this as well
    for sample in data:
        for d in sample:
            extracted[keepr].append(d)
            keepr += 1
            keepr %= 5
    return extracted


#Call to run the analysis
compare()