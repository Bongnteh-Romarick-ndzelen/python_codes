Country_file = open('countries.txt','r')
#checking if you can read countries.txt
print(Country_file.readable())
print(Country_file.readline())
print(Country_file.readline())
print(Country_file.readlines())
print(Country_file.read())
Country_file.close()