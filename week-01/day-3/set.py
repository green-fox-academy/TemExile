# set introduction
a = {2,3,5,6,9}
a.remove(2)
a.remove(5)
for i in range(len(a)):
    b = list(a)
    print(b[i])
if 482 in a:
    a.remove(482)
else:
    a.remove(42)
    pass

# what's in my bag
oliver = {"laptop", "notebook", "pen", "sunglasses", "hand sanitizer"}
ethan = {"sunglasses", "notebook", "phone"}
mia = {"laptop", "sunglasses", "hand sanitizer"}
print(oliver and ethan)
print(oliver - mia)
print(oliver and ethan and mia)

# unique with set
namelist = ["Ava", "Oliver", "Ethan", "Amelia", "Oliver", "Mia", "Lucas", "Ava", "Ethan", "Enzo"]
nameset = set()
nameset.update(namelist)
print(nameset)
