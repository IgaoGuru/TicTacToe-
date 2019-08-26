import time
import matplotlib.pyplot as plt
import numpy as np

elements = list(range(123))

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
    stop = False

    if len(elements) == 0:
        return False
    if element > elements[-1] or element < elements[0]:
        return False

    while stop == False:
        half = int(len(elements) / 2)
        if elements[half] == element:
            return True
        elif elements[half] >= (element - 1) and elements[half] <= (element + 1):
            return True
        elif len(elements) == 1:
            stop = True
            return False
        elif elements[half] > element:
            elements = elements[:half]
        elif elements[half] < element:
            elements = elements[half:]


times = []
#testing platform
errors = 0
for i in elements:
    tic = time.time()
    product = find_element4(elements,i)
    toc = time.time()
    elapsed = toc - tic
    times.append(elapsed)
    print(elapsed)
    print(product)
    print(i)
    if product == False:
        errors += 1

#numpy trackers
plt.plot(times)
plt.xlabel("element")
plt.ylabel("time")
plt.show()
print(errors)

