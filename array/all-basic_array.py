arr = []

n = int(input("Enter number of array: "))
print(n)

for i in range(n):
  num = int(input(f"Enter Array Values - {i+1}: "))
  arr.append(num)

max_value = arr[0]
min_value = arr[0]

for m in arr:
  if m > max_value:
    max_value = m
  if m < min_value:
    min_value = m

print(f"\nMin value: {min_value} x Max value: {max_value}")

sum = 0
for i in arr:
  sum = sum+i

asc = []
for i in range(n-1, -1, -1):
  value = arr[i]
  asc.append(value)

print(f"\nThe reverse of {arr} is {asc}")

found = False
search = int(input("\nEnter the number you want to found: "))
for i in arr:
  if search == i:
    found = True
    break

if found:
  print(f"\n{search} is in the list")
else:
  print(f"\n{search} is not in the list")

sort = []
for i in range(n):
  for j in range(i+1, n):
    if arr[i] > arr[j]:
      arr[i], arr[j] = arr[j], arr[i]

print(f"\nSorted array - {arr}")

  


print(f"\nsum of {arr} is {sum}")
