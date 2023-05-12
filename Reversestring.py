def reverse_string(string):
      if len(string)==1:
            return string
      return string[::-1]
string = input("Enter a string to reverse: ")
reverse_string(string)
print(reverse_string(string))