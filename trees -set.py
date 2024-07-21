#Creating a set of trees
trees = {'oak', 'pine', 'birch', 'maple'}

# Adding an element to the set
trees.add('cedar')

# Removing an element from the set
trees.remove('pine')

# Checking if an element exists in the set
has_oak = 'oak' in trees
print(f"Has oak: {has_oak}")

# Iterating through the set
for tree in trees:
    print(tree)
    
# Original set
print(trees)
