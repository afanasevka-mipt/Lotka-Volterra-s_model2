import numpy as np
import matplotlib.pyplot as plt

class LVM(object):
    def __init__(self, alpha, beta, gamma, delta, x0, y0):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.x0 = x0
        self.y0 = y0

    def fun_vec(self, r, t): #Определение функции-вектора правых частей системы
        x = r[0]
        y = r[1]
        fx = self.alpha*x - self.beta*x*y
        fy = self.gamma*x*y - self.delta*y
        self.fz = np.array([fx, fy], float)
        return self.fz
    
    def solution(self): # Решение уравнения
        a = 0
        b = 40
        N = 1000
        h = (b-a)/N
        self.time = np.linspace(a, b, N+1)
        self.xpoints = []
        self.ypoints = []
        r = np.array([self.x0, self.y0], float)
        
        for t in self.time: #Основной цикл вычисления по методу Рунге-Кутты
            self.xpoints.append(r[0])
            self.ypoints.append(r[1])
            k1 = h*self.fun_vec(r, t)
            k2 = h*self.fun_vec(r+0.5*k1, t+0.5*k1)
            k3 = h*self.fun_vec(r+0.5*k2, t+0.5*k2)
            k4 = h*self.fun_vec(r+k3, t+h)
            r += (k1+2.*k2+2.*k3+k4)/6.
        
        return self.time, self.xpoints, self.ypoints
    
    def draw(self): #График
        plt.plot(self.time, self.xpoints, 'g', label='Prey')
        plt.plot(self.time, self.ypoints, 'r', label='Predator')
        plt.xlabel('Time')
        plt.ylabel('Population number')
        plt.title("Lotka-Volterra's model")
        plt.grid(True)
        plt.legend()
        plt.show()