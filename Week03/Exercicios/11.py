dic = {}
dic['one'] = 1
dic['two'] = 2
dic['three'] = 3
dic['four'] = 4
dic['five'] = 5

# a
print(dic.keys())

# b
print(dic.values())

# c
print(dic)

# d
print(dic['two'])

# e
print(dic)

# f
for key,value in dic.items():
    print(key, "tem como valor", value)
