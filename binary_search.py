import time
import matplotlib.pyplot as plt
import numpy as np

#looping one
def find_element(elements:list, element:int):
    for i in elements:
        if element == i:
            return True
    return False

#recursive one
def find_element2(elements:list, element:int):
    if len(elements) == 0:
        return False
    if elements[0]== element:
        return True
    else:
        return find_element2(elements[1:], element)

#only works for continuous lists
def find_element3(elements:list, element:int):
    if element >= elements[0] and element <= elements[-1]:
        return True
    else:
        return False

#cuts the list in half until there is only one element
def find_element4(elements:list, element:int):
    while len(elements) > 0:
        if len(elements) == 1:
            return elements[0] == element
        half = int(len(elements) / 2)
        if elements[half] == element:
            return True
        elif elements[half] > element:
            elements = elements[:half]
        elif elements[half] < element:
            elements = elements[half:]
    return False\

def binary_search(elements:list, element:int):
    if len(elements) == 0:
        return False
    if len(elements) == 1:
        return elements[0] == element
    half = int(len(elements) / 2)

    if element == elements[half]:
        return True
    elif element < elements[half]:
        return binary_search( elements[:half], element)
    elif element > elements[half]:
        return binary_search(elements[half:], element)


times = []
#testing platform
elements = list(range(0, 1000000, 1))

errors = 0
for max_element in range(0, 1000000, 1000):
    tic = time.time()
    print(max_element)
    product = binary_search(list(range(0, max_element, 1)), max_element)
    toc = time.time()
    elapsed = toc - tic
    times.append(elapsed)
    print(elapsed)
    print(product)
    print(max_element)

#numpy trackers
plt.plot(times)
plt.xlabel("element")
plt.ylabel("time")
plt.show()
print(errors)

