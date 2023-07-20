import os
destination = "E:\\my\\Desktop\\python programs\\text.txt"

source = "E:\\my\\desktop\\text.txt"

try:
      if os.path.exists(destination):
            print("There is already a file there!")
      else:
            os.replace(source,destination)
            print()
except FileNotFoundError:
      print(source+" was not found")