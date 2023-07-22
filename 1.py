import numpy as np
import matplotlib.pyplot as plt

#課題１：データの生成

data_length = 100 #データの個数
# 初期値
x_0 = 1
x =[x_0]
np.random.seed(100)
for t in range(data_length-1):
    n = np.random.normal(loc=0,scale=1)
    x_next = x[-1] + n
    x.append(x_next)

nois = np.random.normal(loc=0,scale=1,size=100)
y = x + nois
# 図示
# plt.plot(range(data_length),x,label="x")
# plt.plot(range(data_length),y,label="y")
# plt.xlabel("T")
# plt.legend()
# plt.show()

# 課題2　
lamda = 1
EPOCHS = 100
a = 0.1
x_pre = np.zeros(100)
for epoch in range(EPOCHS):
    for t in range(0,98):
        # 偏微分結果（x=100おかしい)
        x_pre[t] = x[t] + a*(2*x[t]-x[t+1]-y[t])
    x_pre[99] = x[99] + a*(x[99]-y[99])
plt.plot(range(data_length),x,label="x")
plt.plot(range(data_length),x_pre,label="x_pre")
# plt.plot(range(data_length),y,label="y")
plt.xlabel("T")
plt.legend()
plt.show()