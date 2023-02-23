def palindrome(word):
    return word == word[::-1]


check_word = input("write a word to check: ")
print(palindrome(check_word))