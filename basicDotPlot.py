import matplotlib.pyplot as plt

inFile=open("imageBin//5.txt")
for line in inFile:
    line=line.split(" ")
    line[1]=line[1].split("\n")[0]
    plt.scatter(float(line[0]),float(line[1]))
plt.show()