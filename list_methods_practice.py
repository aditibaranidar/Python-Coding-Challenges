"""
def insert_function(i,e):
  starting_list.insert(i,e)
  i = input("What would you like integer e to be?")
  e = input("What position(i) to be?")
  
def print_function(starting_list):
  print(starting_list)
  
def remove_function(e):
  starting_list.remove(e)

def append_function(e):
  starting_list.append(e)
  
def sort_function(starting_list):
  starting_list.sort()
  
def pop_function():
  starting_list.pop()
  
def reverse_function():
  starting_list.reverse()

starting_list = []  
continue_input = input("Would you like to keep changing your list?")
while continue_input == "Yes":
  print("1. insert i and e: insert integer e at position i\n2.print: prints the list\n3.remove e:deletes the first occurence of e\n4.append e:insert integer e at the end of the list\n5.sort:sort the list\n6.pop:pops the last element from the list\n7.reverse: reverse the list\n")
  input1 = input("What operation do you want to do? Pick a number from 1-7 using the options above.")
  #i = input("What would you like integer e to be?")
  #e = input("What position(i) to be?")
  
  if input1 == 1:
    print("hi")
    e = input("What would you like integer e to be?")
    i = input("What do you want the position(i) to be?")
    starting_list.insert(i,e)
    
  if input1 == 2:
    print(starting_list)
    
  if input1 == 3:
    e_input= input("What was your integer?")
    starting_list.remove(e_input)
    
  if input1 == 4:
    starting_list.append(e)
    
  
  if input1 == 5:
    starting_list.sort()
  
  if input1 == 6:
    starting_list.pop()
    
  if input1 == 7:
    starting_list.reverse()
"""
list1 = []
input2 = input("Would you like to change your list?")


if input2 == "yes":
  while input2 == "yes":
    print("1.insert i and e: insert integer e at position i\n2.print: prints the list\n3.remove e:deletes the first occurence of e\n4.append e:insert integer e at the end of the list\n5.sort:sort the list\n6.pop:pops the last element from the list\n7.reverse: reverse the list\n8.stop playing\n")
    input1 = int(input("Which operation would you like to do?"))
      
    if input1 == 1:
      i = input("What position do you want to place your number in?")
      e = input("What number do you want to place?")
      list1.insert(int(i),e)
      
    if input1 == 2:
      print(list1)
      
    if input1 == 3:
      list1.remove(e)
      
    if input1 == 4:
      e_input = input("What integer would you like to place?")
      list1.append(e_input)
      
    if input1 == 5:
      list1.sort()
      
    if input1 == 6:
      list1.pop()
      
    if input1 == 7:
      list1.reverse()
      
    if input1 == 8:
      print("thanks for playing!")
      break
      
      
else:
  print("Thanks for playing!")
  
  

  