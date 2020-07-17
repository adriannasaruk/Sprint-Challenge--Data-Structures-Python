import time
import os
import sys

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #case1 value is less than self value
        if value < self.value:
            #If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                #repeat the process for left subtree
                self.left.insert(value)

        #case2 value is greater than self value
        elif value >= self.value:
            #if there is no right child inser value there
            if self.right is None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #case 1 if self.value equals target
        if self.value == target:
            return True
        #case2 if target is less than self.value
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        #case3 otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

start_time = time.time()

f = open(os.path.join(sys.path[0],'names_1.txt'), 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(os.path.join(sys.path[0],'names_2.txt'), 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

root = names_1.pop(5000)

tree = BSTNode(root)

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    tree.insert(name_1)

for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
