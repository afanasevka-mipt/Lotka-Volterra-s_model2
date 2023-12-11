from Classes2 import LVM2

x0 = int(input('Start number of prey:'))
y0 = int(input('Start number of predators:'))
alpha = float(input('Prey population growth rate:'))
beta = float(input('Hunting rate:'))
gamma = float(input('Predators population decrease:'))
delta = float(input('Predators population growth rate:'))

g = LVM2(alpha, beta, gamma, delta, x0, y0)
g.solution()
g.draw()