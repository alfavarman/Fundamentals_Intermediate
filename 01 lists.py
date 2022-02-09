
numbers = [1, -1, 20, 34, 2990, 34903, 20, -2332]
s_numbers = sorted(numbers)
fruits = ["rambutan", "orange", "apple", "mango", "banana"] * 2
all_lists = numbers + s_numbers + fruits
#:: step index, - index
selected = numbers [0:1] + fruits [::2] + all_lists[:-2]

#to copy list:
a = list(numbers)
b = numbers.copy()
c = numbers[:]
d = numbers
a.append(0)
b.append(0)
c.append(0)
#d.append(0)

print(numbers)
print(a)
print(b)
print(c)
print(d)
print("""


""")

print("s_numbers")
print(s_numbers)
print("fruits")
print(fruits)
print("all")
print(all_lists)
print("\nselected")
print(selected)