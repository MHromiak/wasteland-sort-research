# wasteland-sort-research

This repository holds all the files used to test the complexity and performance of the Wasteland sorting algorithm. To run, navigate to stats 
and call "python sort_compare.py". Output plots will be generated in stats/plots and written output to stats/sorting_results.txt. To change data being tests, modify
the "info" variable in sort_compare.py. The tuples represent the number of values and the range of those values to be generated. Additionally, you will have to modify
"plot_times" in visualize.py and line 43 in sort_compare.py to account for your new data.

A public-use version of Wasteland sort is available on PyPI: https://pypi.org/project/wasteland-sort/
