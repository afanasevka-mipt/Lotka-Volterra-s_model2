import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scp

class LVM2(object):
    def __init__(self, alpha, beta, gamma, delta, x0, y0):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.x0 = x0
        self.y0 = y0

    def model(self, x, t):
       x1, y1 = x
       dx1 = self.alpha * x1 - self.beta * x1 * y1
       dy1 = self.gamma * x1 *y1 - self.delta * y1
       return [dx1, dy1]
    
    def solution(self):
        X0 = np.array([self.x0, self.y0])
        t = np.linspace(0, 40, 1000)
        self.res = scp.odeint(self.model, X0, t)
        return self.res
    
    def draw(self):
        x, y = self.res.T
        plt.plot(x, 'g', label = "Victims")
        plt.plot(y, 'r', label = "Predators")
        plt.grid()
        plt.xlabel('Time')
        plt.ylabel('Population')
        plt.title("Lotka-Volterra's model")
        plt.legend()
        plt.show()



