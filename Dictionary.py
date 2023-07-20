student = {
      'name':'Romarick',
      'roll_no':32,
      'Percentage':92,
      'Best_subject':'Computer Science',
      'Destination':'BUEA'
}
print(student)
print("Student name: ", student["name"])
print(student.get('name'))
print(type(student))
for key in student:
    print(key, "=", student[key])
#updating value in a dictionary
student['Percentage'] = 86.3
print("Dictionary after update: \n",student)
#adding items in a dictionary
student['branch'] = 'Computer Science'
print(student)
#delete using pop function
student.pop('roll_no')
print(student)
#printing values pair of a dictionary
print(student.items())
#returning all the values of a dictionary
print(student.values())

