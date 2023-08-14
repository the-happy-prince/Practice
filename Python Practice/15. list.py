marks = [3, 5, 6]
print(marks)

# List can be changed but tupples can't
marks.append(7)
marks.append("Eight")
print(marks)

print(marks[-2])
print(marks[1:])
print(marks[1:2:1]) # starts from index 1, ends before index 2 and jump 1 index

lst = [i*i for i in range(10)]
print(lst)

l = [10, 73, 23, 26, 87, 92, 12]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

n = [10, 73, 23, 26, 87, 92, 12]
print(n)
n.insert(2, 45)
print(n)

n.extend(l)
print(n)