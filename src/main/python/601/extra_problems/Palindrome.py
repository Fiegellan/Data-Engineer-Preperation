def isPalindrome(a):
    if len(a) < 2: return True
    elif len(a)>2:
        if a[0]==a[-1]:
            return isPalindrome(a[1:-1])
        else:
            return False

print isPalindrome('amanaplanacanalpanama')
print isPalindrome('a man a plan a canal panama')
print isPalindrome('able was I ere I saw elba')