"""
Let's learn about list comprehensions! You are given three integers x, y, and z
representing the dimensions of a cuboid along with an integer n. Print a list of all
possible coordinates given by (i, j, k) on a 3D grid where the sum of i +j+k is not
equal to n. Please use list comprehensions rather than multiple loops, as a learning exercise.
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[u, v, w] for u in range(0,x+1) for v in range(0,y+1) for w in range(0,z+1) if (u+v+w != n)])

"""
above is equivalent to the below code (just for explanation)
>>> results = []
>>> for x in [1, 2, 3]:
...     for y in [4, 5, 6]:
...         results.append([x, y])
... 
>>> print(results)
[[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
"""