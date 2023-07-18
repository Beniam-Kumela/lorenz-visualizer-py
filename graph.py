import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

def lorenz_ode(beta, sigma, rho, dt):
    dx = (sigma * (y - x)) * dt
    dy = (x * (rho - z) - y) * dt
    dz = ((x * y) - (beta * z)) * dt
    
    xnew = x + dx
    ynew = y + dy
    znew = z + dz
    
    return xnew, ynew, znew

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_title("Lorenz System for beta=8/3, rho=28, sigma=10.")

x_val = []
y_val = []
z_val = []

x = 0.01
y = 0.01
z = 0.01

n_iter = 10000

for i in range(n_iter):
    x, y, z = lorenz_ode(beta=8/3, sigma=10, rho=28, dt=0.01)
    
    x_val.append(x)
    y_val.append(y)
    z_val.append(z)
   
ax.plot(x_val, y_val, z_val, color = 'b')

plt.show()    

plt.savefig('Lorenz_System_Graph.png')