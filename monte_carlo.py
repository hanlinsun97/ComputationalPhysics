import numpy as np
import matplotlib.pyplot as plt
import random
#   A Monte-Carlo simulation of Ising model on a 2-dimension lattice.

def initializer(initial_condition, lattice_size):
    #   High temperature state / Low temperature state
    if initial_condition is "HighTemperature":
        lattice = np.random.randint(0, 2, size=[lattice_size, lattice_size])
        for i in range(lattice_size):
            for j in range(lattice_size):
                if lattice[i][j] == 0:
                    lattice[i][j] = -1
    elif intial_condition is "LowTemperature":
        lattice = np.ones([lattice_size, lattice_size])
    return lattice

def energy_function(coordinate, lattice):
    x_lower = coordinate[0] - 1
    x_upper = coordinate[0] + 1
    y_lower = coordinate[1] - 1
    y_upper = coordinate[1] + 1

    #   Periodic Boundary Condition

    if x_lower not in range(lattice_size):  
        x_lower += lattice_size
    if x_upper not in range(lattice_size):
        x_upper -= lattice_size
    if y_lower not in range(lattice_size):
        y_lower += lattice_size
    if y_upper not in range(lattice_size):
        y_upper -= lattice_size

    neighbor = [lattice[x_lower, y_lower], lattice[x_lower, y_upper],lattice[x_upper, y_lower],lattice[x_upper, y_upper]]
    energy_before = 0
    energy_after = 0

    for element in neighbor:
        energy_before += element * lattice[coordinate[0], coordinate[1]]
        energy_after += element * (-lattice[coordinate[0], coordinate[1]])
  
    energy_before = -energy_before
    energy_after = -energy_after
    diff = energy_after - energy_before

    return  energy_before, energy_after, diff

def coordinate_generator(lattice_size):
    x = np.random.randint(0, lattice_size)
    y = np.random.randint(0, lattice_size)
    coordinate = (x, y)
    return coordinate

def decision_maker(coordinate, lattice, diff, T):
    #   Flip the spin or not ?
    if diff < 0:
        lattice[coordinate[0], coordinate[1]] = - lattice[coordinate[0], coordinate[1]]
    else:
        p = np.exp(-diff / T)
        q = np.random.rand()    #   Random number generator
        if p > q:
            lattice[coordinate[0], coordinate[1]] = - lattice[coordinate[0], coordinate[1]]
        else:
            pass
    return lattice
def Avg_magnettorque(lattice, lattice_size):
    mag = 0
    for i in range(lattice_size):
        for j in range(lattice_size):
            mag += lattice[i][j]
    mag = mag / (lattice_size * lattice_size)
    return mag

if __name__ == "__main__":
    
    # T = 10
    lattice_size = 5
    initial_condition = "HighTemperature"
    experiment_time = 100000
    Temp = []
    Mag = []
    for T in np.arange(0.1, 1, 0.1):
        print(T)
        lattice = initializer(initial_condition, lattice_size)
        for time in range(experiment_time):
            coordinate = coordinate_generator(lattice_size)
            _, _, diff = energy_function(coordinate, lattice)
            lattice = decision_maker(coordinate, lattice, diff, T)
            mag = Avg_magnettorque(lattice, lattice_size)
            # if time % 100 == 0:
            #     print(mag)
        mag = abs(mag)
        Temp.append(T)
        Mag.append(mag)
    plt.figure(0)
    plt.plot(Temp, Mag)
    plt.xlabel("Temperature")
    plt.ylabel("Average Magnetic Torque")
    plt.legend()
    plt.show()

 
