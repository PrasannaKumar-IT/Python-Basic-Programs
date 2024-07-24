def is_palindrome(s):
    return s==s[::-1]
str1=input("Enter the string:")
ans=is_palindrome(str1)
if ans:
    print("The Given String is a Palindrome")
else:
    print("The Given String is Not a Palindrome")