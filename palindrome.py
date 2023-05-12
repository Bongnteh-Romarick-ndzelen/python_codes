str = input("Enter a string to check if its palindrome: ")
if (str == str[::-1]):  #reversing a string and checking if thesame
      print(str, "is a palindrome string")
else:
      print(str, "is not a palindrome string ")