import math
from matplotlib import pyplot as plt
x = [i for i in range(10000)]
y = [
    0.1 * math.exp(-(i * math.log(0.1 / 0.001) / 10000)) for i in range(10000)
]
with open("x.txt", 'w') as fp:
    fp.write("[")
    for i in x:
        fp.write("'{:0>4d}',".format(i))
    fp.write("]\n")
    fp.write("[")
    for i in y:
        fp.write(str(i))
        fp.write(",")
    fp.write("]\n")

# print(y)
# plt.figure()
# plt.style.use('ggplot')
# plt.plot(x, y)
# plt.xlabel("Steps")
# plt.ylabel("Learning rate")
# plt.title("Exponential decay learning rate")
# plt.show()