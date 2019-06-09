def is_palindrome(string):
    if string.lower() == string.lower()[::-1]:
        return True
    return False

print(is_palindrome("ere e ere"))
print(is_palindrome("lama"))
print(is_palindrome("Ama"))