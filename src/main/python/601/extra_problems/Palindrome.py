def isPalindrome(a):
    if len(a) < 2: return True
    elif len(a)>2:
        if a[0]==a[-1]:
            return isPalindrome(a[1:-1])
        else:
            return False

def reverse_string(z):
    l = len(z) - 1
    for i in range(0, len(z) / 2):
        z[i],z[l-i]=z[l-i],z[i]

    return z

def atoi(a):
    a.strip()
    if a[0]=='-':
        return -int(a[1::])
    else:
        return int(a)

def helper(h,f,a):
    octo = a

    print octo
    if h >= a:
        if 2*h+4*(a)==f:
            return 'number of chickens: ' + str(h) + ' number of cows: ' + str(a)
        else:
            return helper(h-1,f,a+1)
    else:
        return 'no solution'

def animal_qeustion(h,f):
    return helper(h,f,0)

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def binomial_coeffienct(n,k):
    a,b,c = factorial(n), factorial(k), factorial(n-k)
    return a/(b*c)

print binomial_coeffienct(5,2)

# print(animal_qeustion(380,9201))
# print(animal_qeustion(4,8))




# 80*4+300*2
### # testing
# print type(atoi(' -123 '))

# print reverse_string([1,2,5,4,6,7,9])


# print isPalindrome('amanaplanacanalpanama')
# print isPalindrome('a man a plan a canal panama')
# print isPalindrome('able was I ere I saw elba')
