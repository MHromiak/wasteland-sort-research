---------
visualize
---------

.. py:function:: plot_times(timed: List[tuple]):

    Plot passed in data as bar graphs. Each list in 'times' should follow the format [([data_1], data_1_name), ([data_2], data_2_name), ...]

    :param times: List of tuples to be unpacked

    :returns: None

.. py:function:: generate_bar_plot(data: list, title: str)

    Generates a bar plot of 'data' with title 'title'

    :params data: Data to be plotted
    :params title: Desired plot title

    :returns: None, but saves the plots in stats/plots
