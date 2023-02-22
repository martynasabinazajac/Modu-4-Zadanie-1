check_word=input("write a word to check: ")
def palindrome(word):
  if word[:]==word[::-1]:
    return True
  else:
    return False
print(palindrome(check_word))