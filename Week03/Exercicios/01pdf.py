qd = open("qbdata.txt", 'r')

ex1 = open("ex1.txt", 'w')
for i in qd.readlines():
    ex1.write(i.split("QB")[0]+"teve o valor "+i.split("%")[1].strip()+"\n")

qd.close()
ex1.close()
