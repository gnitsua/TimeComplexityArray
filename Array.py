import math
from typing import List
import matplotlib.pyplot as plt
import numpy as np


class Array(List[int]):
    index_accessed = []

    def __getitem__(self, item):
        self.index_accessed.append(item)
        return super().__getitem__(item)

    def show(self):
        fig, ax = plt.subplots()
        num_bins = len(self)
        counts, bins, patches = ax.hist(self.index_accessed, num_bins)
        num_accessed = len(self.index_accessed)
        n = len(self)
        ax.plot(range(0,n),np.full((n,),n),linestyle="--")
        ax.plot(range(0,n),np.full((n,),n*np.log(n)),linestyle="--")
        ax.plot(range(0,n),np.full((n,),n**2),linestyle="--")
        ax.plot(range(0,n),np.full((n,),np.average(counts)))
        ax.legend(("O(n)","O(nlog(n)","O(n^2)","Actual"))
        ax.set_title("Time Complexity")
        plt.show()