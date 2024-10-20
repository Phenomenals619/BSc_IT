from ete3 import Tree

# Define your tree structure correctly
t = Tree('(male,female,(((((ME,Brother,Sister),Father,Mother))GrandFather GrandMother))Parent)Tree;', format=1)

# Print the tree in ASCII format 
#print(t.get_ascii(show_internal=True))
print(t)
