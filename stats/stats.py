import random
import csv
import numpy as np
from matplotlib import pyplot as plt
from typing import List


# Normal
# Multimodal
# Skew
def generate_data(info: List[tuple]):
    data = []
    for tup in info:
        data.append(random.choices(range(0, tup[0]), k=tup[1]))
    return data
    

        