#Write a Python Program to Put Positive and Negative Numbers in Separate List using For Loop?
list1 = [107, 260, 47, 100, 148]
 

new_list = set(list1)
 

new_list.remove(max(new_list))
 


print(max(new_list))
