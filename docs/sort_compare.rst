------------
sort_compare
------------

A data minipulation file which times each sorting algorithm on ten sorts of randomly generated data and
 graphs the resulting times for ease of comparison. Note that radix sort is kept from the graphs as the time disparity 
 caused the other bars to be invisibly small. The full raw data is shown in stats/sorting_results.txt. Graphs are stored in stats/plots


 .. py:function:: compare()

    Compares all sorts in oter_sorts with wasteland_sort

    :returns: None. Puts plots in stats/plots and running time averages in ./sorting_results.txt


.. py:function:: heap(data: List[list]) -> List[float]

    Runs timing trials for Heapsort over 'data'.

    :param data: List of data to be sorted

    :returns: List of average sorting times for each set of data


.. py:function:: merge(data: List[list]) -> List[float]

    Runs timing trials for Mergesort over 'data'.

    :param data: List of data to be sorted

    :returns: List of average sorting times for each set of data


.. py:function:: quicksort(data: List[list]) -> List[float]

    Runs timing trials for Quicksort over 'data'.

    :param data: List of data to be sorted

    :returns: List of average sorting times for each set of data


.. py:function:: radix(data: List[list]) -> List[float]

    Runs timing trials for Radix sort over 'data'.

    :param data: List of data to be sorted

    :returns: List of average sorting times for each set of data


.. py:function:: timsort(data: List[list]) -> List[float]

    Runs timing trials for Timsort over 'data'.

    :param data: List of data to be sorted

    :returns: List of average sorting times for each set of data


.. py:function:: wasteland(data: List[list]) -> List[float]

    Runs timing trials for Wasteland sort over 'data'.

    :param data: List of data to be sorted

    :returns: List of average sorting times for each set of data


.. py:function:: data_from_stats(data: List[list]) -> List[list]

    Takes a list of all samples generated in compare() and separates them into data sets

    :param data: List of data to be sorted

    :returns: List of lists of integers. Each list of lists represents a set of data (e.g. small, medium, large)