import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import time
from tqdm import tqdm

print("Welcome to the Lorenz System Animator!")
time.sleep(2)

print("We will animate the formation of the Lorenz attractor.")
time.sleep(2)

print("This is a classical example of chaos from a non-linear dynamical system.")
time.sleep(2)

print("Let's get started by specifying what color you want the animated graph to be.")
color = input("Enter first letter of color here (k for black): ")

print("Finally, how many frames do you want the animation to be?")
F = int(input("Enter frames here (600 = 30s; 1200 = 1 min): "))

def lorenz_ode(beta, rho, sigma, x, y, z, dt):
    dx = (sigma * (y - x)) * dt
    dy = (x * (rho - z) - y) * dt
    dz = ((x * y) - (beta * z)) * dt
    
    xnew = x + dx
    ynew = y + dy
    znew = z + dz
    
    return xnew, ynew, znew

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

beta=8/3
rho=28
sigma=10

x=0.01
y=0.01
z=0.01

dt = 0.01

x_val = []
y_val = []
z_val = []

def animate(frame):
    global x, y, z
    
    x, y, z = lorenz_ode(beta, rho, sigma, x, y, z, dt)
    
    x_val.append(x)
    y_val.append(y)
    z_val.append(z)
    
    ax.plot(x_val, y_val, z_val, color = color)
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    
    ax.set_title("Lorenz System for beta=8/3, rho=28, sigma=10. Frame = " + str(frame)+ ".")

anim = FuncAnimation(fig, animate, frames = tqdm(range(F)), interval = 50, repeat = True)
anim.save("Lorenz_Animation.gif", writer = "Pillow")
plt.close()  