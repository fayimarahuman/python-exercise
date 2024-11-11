#Dictionaries
#key value pair i.e the name,age,locaton etc
#syntax
#access the item
#change the items
#Add items
#remove Items
#loops
student={
    'name':'Gillian',
    'age':22,
    'location':'Muyenga'
}

fruits={
    1:'apple',
    2:'orange',
    3:'banana'
    
}

#Accessing items involves accessing the values
#for example
print(student['name'])
print(student['age'])
print(student['location'])


#print the keys of the student dictionaries
print(student.keys())
#print the length of the dictionaires
print(len(student.keys()))

#add a key contact to the student dictionary
student['contact']='0753670268'
print(student['contact'])
print(student)
#Update Gillian to Apio Gillian
student['name'] = 'Apio Gillian'
print(student)
#access all the valusof the dictionary
student.values()
print(student.values())
#remove the contact key from the dictionary
student.pop('contact')
print(student)