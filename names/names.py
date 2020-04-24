# The nested
# The obvious choice is to implement a binary search
# The BST class and the compare method is required.
# To save time I will import the one that is already written.
# Wouold be nice to implement from scratch, but this is a timed Sprint Challenge!
from binary_search_tree import BinarySearchTree
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print ("Nested Loops")
# print (f"runtime: {end_time - start_time} seconds")

# Create an instance of the BST
# Grrrr! Must give it the root value!
bst = BinarySearchTree(names_1[0])  

# Add the names in the name_1 file
for n1 in names_1:
    bst.insert(n1)

# Now check each name in the name_2 file fir dups
# If the name is a duplicate add it to the duplicate list
for n2 in names_2:
    if bst.contains(n2):
        duplicates.append(n2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
