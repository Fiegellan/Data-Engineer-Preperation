# https://www.youtube.com/watch?v=--gtVtFN354

# if given a list of integer arrays, and a number k, output sets of numbers that sum to k

# (1,3,2,5,46,6,74) k = 5

# solution (1,4),(2,5)

def find_pairs(a,k):
    solution = {}
    for i in a:
        if i < k:
            if k-i in a:
                # print i, k-i
                solution[i]=k-i

    return solution


array = (1,3,2,5,46,6,74)
k = 5

print find_pairs(array,k)