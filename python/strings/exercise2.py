def is_palindrome(s):
    cleaned = ''.join(s.split()).lower()   # remove spaces and lowercase
    return cleaned == cleaned[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))                        # False
