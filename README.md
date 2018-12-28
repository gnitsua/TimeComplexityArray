# TimeComplexityArray
Time complexity tracking for python lists

This project is useful for people exploring time complexity for algorithms in Python. 
Starting out it only works with python lists, but I plan to extending it to numpy arrays and dictionaries eventually.

It works by tracking `__getitem__` calls. After you run your algorithm, call `.show()`. 
This plots the number of times that each element of the array was accessed, as well as lines showing several different time complexities.

## Examples

Comparing time complexity of sorting algorithms is a common application of this sort of analysis.
For instance if we wanted to compare the efficency of selection sort and quick sort, you could use the following code:
```
    test = Array(np.random.rand(9))
    selectionSort(test)
    test.show()

    test = Array(np.random.rand(9))
    quickSort(test)
    test.show()
```
