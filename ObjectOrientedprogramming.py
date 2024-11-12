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




#Assignment
#1.create a class with the following
#class  Cohort:these are the things you need from them
# Name
# description
# start-date
# end-date
#add a constructor for cohort class
#solutions
class corhort:
   students_name='Fayima Rahuman'
   description='Corhort4 student witu'
   start_date='20/august/2024'
   end_date='20/December/2024'
Corhot4=corhort()   
print(Corhot4.students_name) 
print(Corhot4.description) 
print(Corhot4.start_date)
print(Corhot4.end_date)
   

#2.create a function or method to the class that prints  the cohort name and the total number of students
class corhort:
    def __init__(corhot_details,name,total_number_of_students):
        corhot_details.name=name
        corhot_details.total_number_of_students=total_number_of_students
    def myfunc(cohort_details):
            print(f"Corhort name is    {cohort_details.name}   and the total number of students is    {cohort_details.total_number_of_students}")
Corhort4=corhort('Cohort4',59)   
Corhort4.myfunc()
        
#3.create a new object of the cohort class
class corhot:
    def __init__(student_details,name,age,):
        student_details.name=name
        student_details.age=age
    def __str__(student_details):
            return (f"The student name is{student_details.name} and the student age is {student_details.age}")
students=corhot('Fayima Rahuman','22')
print(students)           
    



#read about the constructors and instances
