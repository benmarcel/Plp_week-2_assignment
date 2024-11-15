# create an empty list 
my_list = [];

# append the following elements to my my_list 10,20,30,40
my_list.append(10);
my_list.append(20);
my_list.append(30);
my_list.append(40);

# insert 15 at the second position in the list 
my_list.insert(1, 15)

# extend my_list with another list 
another_list = [2,4,6,8,12]

my_list.extend(another_list)

# remove the last item from my_list
del my_list[-1]

# sort my_list in ascending order
my_list.sort()

# find and print the index of 30 in my_list
index = my_list.index(30)
print(index)