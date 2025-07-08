"""
This program implements that when the user gave a number it will add till the number and print the sum value   
"""

num = int(input("Enter the number : "))
add = 0
i = 1
while i<=num:
    add+=i
    i+=1
    
print("The total number added is :",add)  