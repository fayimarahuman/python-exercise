#Object Oriented Programming
#OOP deals with classes and objects/instances
# A class has properties/attributes
#objects come from class and most cases it consists properties 0f class
# python OPP is used almost every where and their methods are i.e the things you want the class to do
#syntax
#1 creating a class
#Cohort class
#these are the things you need from them
# Name
# description
# start-date
# end-date



#Assignment
#1.create a class with the following
#class  Cohort:these are the things you need from them
# Name
# description
# start-date
# end-date
#add a constructor for cohort class
#solutions
class Corhort:
    name='Fayima Rahuman'
    description='cohort4student witu'
    start_date='20/August/2024'
    end_date='10/december/2024'
Corhort4=Corhort ()
print(Corhort4.name) 
print(Corhort4.description) 
print(Corhort4.start_date)
print(Corhort4.end_date)
   

#2.create a function or method to the class that prints  the cohort name and the total number of students
class corhort:
    def __init__(students,name,total_number_of_students):
        students.name=name
        students.total_number_of_students=total_number_of_students
    def myfunc(students):
            print(f"Corhort name is  {students.name} and the total number of students is  {students.total_number_of_students}")
Corhort4=corhort('Cohort4',59)   
Corhort4.myfunc()
        
#3.create a new object of the cohort class
students=Corhort()
name='fayima'
age=22
registration_number='2024/DSC/0034/SS'
print(students.name)



#read about the constructors and instances
# class Person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)