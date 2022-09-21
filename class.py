#assignment 1 regarding dict,tuples,list

#example of lists,Slicing& index slicing
list = [1,2,3,4,5,6,7]  
print(list[0])  
print(list[1])  
print(list[2])  
print(list[3])  
# Slicing the elements  
print(list[0:6])  
# By default the index value is 0 so its starts from the 0th element and go for index -1.  
print(list[:])  
print(list[2:5])  
print(list[1:6:2])  

#output:
1
2
3
4
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[3, 4, 5]
[2, 4, 6]

#examples of list (append,remove,pop() & length)
list1 = ["book","pen","bag"]
print(list1)

# to know the type of list
print(type(list1))

# to know the length of list
print(len(list1))
#output :
["book","pen","bag" ]
<class 'list'>
3
#addition of item in the list1
list1.append("scale")
print(list1)
#output:
["book","pen","bag", "scale"]
list1 = ["book","pen","bag"]
print(list1)

#remove of item in the list1
list1.remove("book")
print(list1)

#using the pop method 
list1.pop(0)
print(list1)
#output:['book','pen','bag']
['pen,bag']
['bag']

#example of tuples  
# Creating an empty tuple  
empty_tuple = ()  
print("Empty tuple: ", empty_tuple)  
  
# Creating tuple having integers  
int_tuple = (4, 6, 8, 10, 12, 14)  
print("Tuple with integers: ", int_tuple)  
  
# Creating a tuple having objects of different data types  
mixed_tuple = (4, "Python", 9.3)  
print("Tuple with different data types: ", mixed_tuple)  
  
# Creating a nested tuple  
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))  
print("A nested tuple: ", nested_tuple)  

#output:

Empty tuple:  ()
Tuple with integers:  (4, 6, 8, 10, 12, 14)
Tuple with different data types:  (4, 'Python', 9.3)
A nested tuple:  ('Python', {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
  
#example of sets

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print("\n Days",Days)    
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nAdding other months to the set...");    
months.add("July");    
months.add ("August");    
print("\nPrinting the modified set...");    
print(months)  

#output:
 Days {'Saturday', 'Friday', 'Thursday', 'Tuesday', 'Monday', 'Sunday', 'Wednesday'}

printing the original set ... 
{'May', 'January', 'February', 'June', 'April', 'March'}

Adding other months to the set...

Printing the modified set...
{'May', 'January', 'February', 'June', 'April', 'March', 'July', 'August'}

#example of dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}     
print("printing Employee data .... ")    
print(Employee)    
print("Deleting some of the employee data")     
del Employee["Name"]    
del Employee["Company"]    
print("printing the modified information ")    
print(Employee)    
print("Deleting the dictionary: Employee");    
del Employee    
print("Lets try to print it again\n ")    
print(Employee)

#output:
printing Employee data .... 
{'Name': 'John', 'Age': 29, 'salary': 25000, 'Company': 'GOOGLE'}
Deleting some of the employee data
printing the modified information 
{'Age': 29, 'salary': 25000}
Deleting the dictionary: Employee
Lets try to print it again 
NameError: name 'Employee' is not defined
