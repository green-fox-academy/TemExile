# Print all
numbers = [4,5,6,7]
print(numbers)

# Third
q = [4,5,6,7]
print(q[2])

# Compare_length
p1 = [1,2,3]
p2 = [4,5]
if len(p2) > len(p1):
    print("\'p2\' has more elements than \'p1\'")

# Sum elements
r = [54,23,66,12]
print(sum(r[1:3]))

# Change elements
s = [1,2,3,8,5,6]
s[3] = 4
print(s[3])

# Increment element
t = [1,2,3,4,5]
t[2] += 1
print(t[2])

# Matrix
m = []
for i in range(4):
    a = [0, 0, 0, 0]
    a[i] = 1
    m.append(a)
print(m)

# double items
numList = [3,4,5,6,7]
for i in range(len(numList)):
    numList[i] = numList[i]*2
print(numList)

# colors
colors = [["lime", "forest green", "olive", "pale green", "spring green"],
          ["orange red", "red", "tomato"],
          ["orchid", "violet", "pink", "hot pink"]]

# append a
animals = ["koal", "pand", "zebr"]
animals.append("a")

# swap_elements
abc = ["first", "second", "third"]
temp = abc[0], abc[2]
abc[2], abc[0] = temp
print(abc)

# sum all elements
ai = [3,4,5,6,7]
print(sum(ai))

# reverse list
aj = [3,4,5,6,7]
print(aj[::-1])