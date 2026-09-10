def isPalindrome(x):
    sx = str(x)
    return True if str(x) == sx[::-1] else False
    
ispalindrome = isPalindrome(121)
print(ispalindrome)