import numpy as np
import matplotlib.pyplot as plt

#課題１：データの生成

data_length = 100 #データの個数
# 初期値
x_0 = 1
data =[x_0]
for t in range(data_length-1):
    n = np.random.normal(loc=0,scale=1)
    x_next = data[-1] + n
    data.append(x_next)

nois = np.random.normal(loc=0,scale=1,size=100)
y = data + nois
plt.plot(range(data_length),data,label="x")
plt.plot(range(data_length),y,label="y")
plt.xlabel("T")
plt.legend()
plt.show()

# 課題2　