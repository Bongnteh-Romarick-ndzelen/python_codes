class Students:
    def __init__(self, name, age, classname, marks1, marks2):
        
        self.name = name
        self.age = age
        self.classname = classname
        self.marks1 = marks1
        self.marks2 = marks2
    def greetings(self):
        print("Hello",self.name,"How are You!","You are now",self.age,"years old.")
        print("You are in",self.classname,"!","Goodluck!")
    def calculate_average(self):
        return (self.marks1 + self.marks2)/2
    
    #creating the instances of the class
    #objects
son = Students('Paul', 25,'form 5A Science', 20, 55)
print(son.calculate_average())
print(son.greetings())
    