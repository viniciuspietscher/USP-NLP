# a
print("a")
file = open("file.txt", 'w')
for i in range(1,11):
    file.write(str(i)+" ")
file.close()

# b
print("b")
file2 = open("file.txt", 'r')
print(file2.read())
file2.close()
