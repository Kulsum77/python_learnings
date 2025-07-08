"""
This program implements that the list is removed from the element
"""
mylist=["black","white","pink","violet","yellow","red","blue","brown"]
result = []
for i in range(len(mylist)):
    if i != 0 and i != 4 and i != 5:
        result.append(mylist[i])
