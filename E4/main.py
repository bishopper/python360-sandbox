# x = [1,2,3]
# print(x[-1])

# x = [1,2,3,10]
# print(len(x))


# x = [1,2,3]
# x[1] = "ali"
# print(x)

# x = [1,2,3]
# x.append([1,2])
# print(x)

# x = [1,2,3]
# x.extend([1,2])
# print(x)

# x = [1,2,3]
# x.insert(0,4)
# print(x)

# x = ["ali",2,3]
# x.remove("ali")
# print(x)

# x = ["ali",2,3]
# x.pop()
# print(x)

# x = ["ali",2,3]
# x.clear()
# print(x)

# x = ["ali",2,3]
# print(x)
# del x
# print(x)

# x = [3,1,2]
# x.sort()
# print(x)

# x = [3,1,2]
# x.sort(reverse=True)
# print(x)

# x = [3,1,2]
# x.reverse()
# print(x)


# x = [1,2,3]
# y = x.copy()
# y.append(4)
# print(x)
# print(y)

# y = [1,2,[3,4]]
# print(y[2][0])

# x = [1,2,3,[4,5,7,[[10,True,20,[100,200,[1,2]]],8,9,11],True,""]]
# print(x[3][3][0][3][2][0])


# x = ()
# print(x)
# print(type(x))

# x = (5,1)
# print(x)
# print(type(x))
# print(x[1])

# x = (1,2,3)
# x.clear()
# print(x)

# person = (26,"ali")
# age , name = person
# print(age)
# print(name)


# person = (1,2,3,4,5,6,7)
# x, *y , z = person
# print(x)
# print(y)
# print(z)


# person = (1,2,3,3,2,1)
# print(person.count(1))

# person = (1,2,3)
# print(person.index(2))

# x = (1,2,3,4,5)
# x = list(x)
# x.pop()
# x = tuple(x)
# print(x)


# x = {"ali","reza","mohammad"}
# print(x[0])

# x = {}
# x = {1}
# print(x)


# x = {1,2,3,4,5,4,5,4,5}
# print(x)

# x = [1,2,3]
# x = set(x)
# print(x)


# x = {1,2,3}
# x.add(4)
# print(x)


# x = {1,2,3}
# x.update({4,5,6})
# print(x)


# x = {1,2,3}
# x.remove(4)
# print(x)

# x = {1,2,3}
# x.discard(3)
# print(x)


# x = {"ali","reza","mohammad"}
# x.pop()
# print(x)
# x.clear()
# print(x)
# del x


# x = {3,1,2}
# print(x.re)

# x = {1,2,3,4}
# y = {3,4,5,6}
# print(x | y)
# print(x.union(y))
# print(x & y)
# print(x.intersection(y))
# print(y -x)

person = {
    "age" : 26,
    "isAlive"  : True
}

# print(person["name"])
# print(person.get("name","na moshakhas"))
person["name"] = "mohammad"
# print(person)

# del person
# print(person)

# age = person.pop("age","ali")
# print(age)
# print(person)


print(person.keys())
print(person.values())
print(person.items())

