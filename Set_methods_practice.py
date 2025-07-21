"""
nathan_classes = ['Taekwondo','Swimming','RSM','Basketball']
kahan_classes = ['Keyboard','Taekwondo', 'Cricket','Art']

print("Question 1: Which classes do nathan and kahan have together?")
print("")
print("Question 2: What are all of the classes that Nathan and Kahan go to?")
print("")
print("Question 3: What classes does Nathan go to that Kahan doesn't?")
print("")
print("Question 4: What classes does Kahan goes to that Nathan doesn't?")
print("")

#Which classes do nathan and kahan have together?
nathan_classes2 = set(nathan_classes)
kahan_classes2 = set(kahan_classes)

union1 = nathan_classes2.union(kahan_classes2) 
intersection1 = 

for i in nathan_classes2:
  if i in kahan_classes2:
    print("1. Nathan and Kahan both go to " + i + " class.")
    
#What are all of the classes that Nathan and Kahan go to?
total_classes= nathan_classes +kahan_classes
total_classes2 = set(total_classes)
print("2. Nathan and Kahan's classes are:")
for item in total_classes2:
  print(item)
  
#What classes does Nathan go to that Kahan doesn't?
print("3. These classes are classes that Nathan goes to but not Kahan:")
for a in nathan_classes2:
  if a not in kahan_classes2:
    print(a)

#What classes does Kahan goes to that Nathan doesn't?
print("4. These classes are classes that Kahan goes to but not Nathan:")
for b in kahan_classes2:
  if b not in nathan_classes2:
    print(b)
"""
set_kahan = {'Keyboard','Taekwondo', 'Cricket','Art'}
set_nathan = {'Taekwondo','Swimming','RSM','Basketball'}

joint_set = set_nathan.union(set_kahan)
print("These are all of the classes that Kahan and Nathan take: "+ str(joint_set))

intersection_set = set_nathan.intersection(set_kahan)
print("Nathan and Kahan have these/this class(es) together:" + str(intersection_set))

difference1 = set_nathan.difference(set_kahan)
print("Nathan goes to these classes but Kahan doesn't:" + str(difference1))

difference2 = set_kahan.difference(set_nathan)
print("Kahan goes to these classes but Nathan doesn't:" + str(difference2))