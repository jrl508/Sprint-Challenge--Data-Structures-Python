import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

##########################################################################
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            #go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            #go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target < self.value:
            if not self.left:
               return False
            else:
                return self.left.contains(target)
        
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

name_tree = BinarySearchTree(names_1[0])

duplicates =[]


for name in names_1[1:]:
    name_tree.insert(name)

for name in names_2:
    if name_tree.contains(name):
        duplicates.append(name)

dup_count = len(duplicates)
end_time = time.time()
runtime = end_time - start_time
print("{dup_count} duplicates:\n\n {duplicates} \n\n".format(dup_count=dup_count ,duplicates=duplicates))
print("runtime: {runtime} seconds".format(runtime=runtime))