# d
file = open("file.txt", 'a')
for i in range(21,31):
    file.write(str(i)+ " ")
file.close()

# e
print("e")
file2 = open("file.txt", 'r')
print(file2.read().replace(" ", "\n"))
file2.close()
