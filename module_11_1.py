import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

'''Создадим программу, генерирующую изображение с тремя графиками
   нормального распределения Гаусса '''

def gauss(sigma, mu):
    return 1/(sigma * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sigma**2))

dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

plt.plot(x, gauss(0.5, 1.0), 'ro-')
plt.plot(x, gauss(1.0, 0.5), 'go-')
plt.plot(x, gauss(1.5, 0.0), 'bo-')


plt.legend(['sigma = 0.5, mu = 1.0',
            'sigma = 1.0, mu = 0.5',
            'sigma = 1.5, mu = 0.0'], loc='upper left')


fig.savefig('gauss.png')

''' Создадим программу, генерирующую изображение с тремя графиками сигмоид'''

def sigmoid(alpha):
    return 1 / ( 1 + np.exp(- alpha * x) )

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )

plt.plot(x, sigmoid(0.5), 'ro-')
plt.plot(x, sigmoid(1.0), 'go-')
plt.plot(x, sigmoid(2.0), 'bo-')

plt.legend(['A = 0.5', 'A = 1.0', 'A = 2.0'], loc = 'upper left')

fig.savefig('sigmoid.png')

''' Строим линейный график'''

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )

a = [1, 2, 3, 4, 5]
b = [25, 29, 14, 16, 22]

plt.plot(a, b)
plt.xlabel('Ось х')
plt.ylabel('Ось у')
plt.title('Линейный график')
fig.savefig('lin.png')

