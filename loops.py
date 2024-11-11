#range()
#sequences for loops
#particular  of sequences
#sequences:lists,strings
name="Birungi"
for item in name:
    print(item)
    marks=[60,70,80]
def total_mark():
    marks=[60,70,80]
    sum=0
    for mark in marks:
        #sum+-mark:
      print(f"the total mark is:{sum}")
total_mark() 
#range is a functions taking in parameters i.e
#range(start,stop,step)
#using a loop print all numbers from 0-6  i.e (0,1,2,3,4,5,6)
# #hint use a range function 
# def range_from_zero_six():
#    for num in range(7):
#     print(num) 
# range_from_zero_six()  
# #example 2 print numbers between 0-10
# for num in range (11):
#   print(num)    
# #print numbers btn 1-20
#   for num in range(1,21):
#       print(num)
#print the following range of even numbers from (2-10) i.e (2,4,6,8,10)
def range_of_even_numbers_from_two_ten():
    for even in range(2,11,2): #2 stands for star
        print(even)
range_of_even_numbers_from_two_ten()

#print the following range of odd numbers(0,3,5,7,9)
def for_odd_numbers_ranging_from_zero_to_nine():
    for odd_numbers in range(0,10,3):
      print(odd_numbers)
for_odd_numbers_ranging_from_zero_to_nine()
#Lists and tupples
#their syntax
#List[]
#tuples()
#difference btn the two
#similarity btn the two
products=['pen','pencils','book']
colors=('red','green','pink')
#add rubber to the products list
products.append('rubber')
print(products)
# insert at the second posittion ruler to the products list
products.insert(2,'rubber')
print(products)
#display the length
products=['pen','pencils','book']
print(len(products))

colors=('red','green','pink')
print(len(colors))
#add purple to the tupple
#colors.append('purple')
#converting a turple to list
colors=('green','red')
new_colors=list(colors)
print(type(new_colors))
new_colors.append('purple')
print(new_colors)
#converting list to tupple
color=tuple(new_colors)
print=type(colors)


fruits=("apple")
print(fruits,type(fruits))


#sets 
#they are imutable
#they are unordered and don't allow duplicates
#syntax,{}
set_of_numbers=(2,7,8)



