# Provide a set of positive integers (an array of integers).
# Each integer represent number of nights user request on Airbnb.com.
# If you are a host, you need to design and implement an algorithm to find out the maximum number a nights you can accommodate.
# The constrain is that you have to reserve at least one day between each request, so that you have time to clean the room.


# 1) Input: [1, 2, 3] ===&gt; output: 4, because you will pick 1 and 3
# 2) input: [5, 1, 2, 6] ===&gt; output: 11, because you will pick 5 and 6
# 3) input: [5, 1, 2, 6, 20, 2] ===&gt; output: 27, because you will pick 5, 2, 20
# 4) input: [5, 1, 2, 6, 20, 2] ===&gt; output: 27, because you will pick 5, 2, 20

night_stay = [5, 1, 2, 6, 20, 2]

index = night_stay.index(max(night_stay))

print night_stay[index]

nights = []

while index > -1:
    print index
    print night_stay[index]
    nights.append(night_stay[index])
    index = index-2

print nights