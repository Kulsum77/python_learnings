"""
This program implements that the given number is largest of all
"""
numbers=[12,87,35,63,91,79]
i = 0
largest = numbers[0]
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1

print("The largest number is:", largest)