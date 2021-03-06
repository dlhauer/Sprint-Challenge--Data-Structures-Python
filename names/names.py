import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n") 
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n") 
f.close()

duplicates = []  

name_tree = BinarySearchTree(names_1[0])
for name_1 in names_1:
    name_tree.insert(name_1)

for name_2 in names_2:
    if name_tree.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
