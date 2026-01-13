arr = []
n = int(input("Enter length of list: "))

for i in range(n):
   value = int(input(f"Enter value of arr - {i+1}: "))
   arr.append(value)

print(f"\nArray: {arr}")

zero_at_last = []
for i in arr:
  if i!=0:
    zero_at_last.append(i)

zeros = n-len(zero_at_last)
print(zeros)
zero_at_last.extend([0] * zeros)
print(f"All zero at last - {zero_at_last}")


for i in range(n):
  for j in range(i+1, n):
    if arr[i] > arr[j]:
      arr[i], arr[j] = arr[j], arr[i]

print(f"\nSorted Array - {arr}")

highest_value = arr[0]

for i in range(1, n):
  if arr[i] > arr[0]:
    highest_value = arr[i]
 

print(f"\nHighest value of the list is {highest_value}")