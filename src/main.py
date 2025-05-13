# main.py

import numpy as np
import matplotlib.pyplot as plt
from pendulum_model import InvertedPendulum
from constants import GRAVITY, MASS, LENGTH, TIME_STEP

def main():
    # Initialize the inverted pendulum model
    pendulum = InvertedPendulum(mass=MASS, length=LENGTH, gravity=GRAVITY)

    # Simulation parameters
    time_duration = 10  # seconds
    num_steps = int(time_duration / TIME_STEP)
    time = np.linspace(0, time_duration, num_steps)
    
    # Arrays to store the results
    angles = np.zeros(num_steps)
    angular_velocities = np.zeros(num_steps)

    # Initial conditions
    pendulum.set_initial_conditions(theta=0.1, omega=0)  # small angle and zero velocity

    # Run the simulation
    for i in range(num_steps):
        pendulum.update_state(TIME_STEP)
        angles[i] = pendulum.theta
        angular_velocities[i] = pendulum.omega

    # Visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(time, angles, label='Angle (rad)')
    plt.title('Inverted Pendulum Simulation')
    plt.ylabel('Angle (rad)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(time, angular_velocities, label='Angular Velocity (rad/s)', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()