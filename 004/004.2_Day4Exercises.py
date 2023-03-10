'''
Day 4 Exercises
'''
a = input("Type a number: ")
# print(a + 10) # This throws an error due to adding a string and an integer

b = int(a)
print(b + 10)

print(b * 10)
print(a * 10)

print('hi' * 10)

print(float(a))

print(type(10.1))
print(type(10))
print(str(10.12))

mylist = ['a', 'b', 'c']
z = mylist[1]
print(type(z))

print(z == b)
print(mylist[1] == b)
print(type(z == b))

print(mylist.index('b'))

mylist.__setitem__(1, 'd')
print(mylist)

mylist[1] = 'e'
print(mylist)

print(mylist.__getitem__(2))
print(mylist[2])


'''
Bonus
'''
filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']
x = 0

for filename in filenames:
    filenames[x] = filename.replace('.', '-', 1)
    print(filename)
    print(filenames[x])
    filename = 'New Name.txt'
    x = x + 1

print(filenames)

files = ('1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt')
print(files)

print(type(filenames))
print(type(files))

print(dir(tuple))


'''
Coding Exercise 1
'''
amount = input("Enter a Dollar Amount (exclude the dollar sign '$'): ")
euro_conv = float(amount) * .95
print(euro_conv)


'''
Coding Exercise 2
'''
ranking = ['John', 'Sen', 'Lisa']

selection = input("Enter a Rank from 1 to 3: ")

print(ranking[int(selection)-1])


'''
Coding Exercise 3
'''
ranking = ['John', 'Sen', 'Lisa']

print("Contestants:", ranking)
selection = input("Enter a name to display their rank: ")

print(ranking.index(selection)+1)


'''
Bug Fixing Exercise 1
'''
elements = ['a', 'b', 'c']
# print(elements(1))
print(elements[1])


'''
Bug Fixing Exercise 2
'''
elements = ['a', 'b', 'c']
new = 'x'
# new = elements[1]
elements[1] = new
print(elements)
