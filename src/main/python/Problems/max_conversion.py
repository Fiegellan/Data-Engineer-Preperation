# If a number is odd, the next transform is 3*n+1
# If a number is even, the next transform is n/2
# The number is finally transformed into 1.
# The step is how many transforms needed for a number turned into 1.
# Given an integer n, output the max steps of transform number in [1, n] into 1.

counter = 0
def max_conversion_number(n):
    global counter
    if n%2 != 0 and n!=1:
        n=3*n+1
        # print 'odd', n
        counter +=1
        max_conversion_number(n)
    elif n%2 == 0:
        n=n/2
        # print 'even',n
        counter += 1
        max_conversion_number(n)
    else:
        print 'one' ,counter
        return counter

print max_conversion_number(3)
