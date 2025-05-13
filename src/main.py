import numpy as np
import matplotlib.pyplot as plt
from pendulum_model import InvertedPendulum
from constants import GRAVITY, MASS, LENGTH, TIME_STEP

def main():
    initial_angle_rad = 0.1
    initial_angular_velocity_rad_s = 0.0 

    pendulum = InvertedPendulum(
        mass=MASS,
        length=LENGTH,
        gravity=GRAVITY,
        time_step=TIME_STEP,
        initial_angle=initial_angle_rad,
        initial_angular_velocity=initial_angular_velocity_rad_s
    )

    time_duration_s = 10
    num_steps = int(time_duration_s / TIME_STEP)
    time_array = np.linspace(0, time_duration_s, num_steps)
    
    angles_rad = np.zeros(num_steps)
    angular_velocities_rad_s = np.zeros(num_steps)

    for i in range(num_steps):
        angles_rad[i] = pendulum.angle 
        angular_velocities_rad_s[i] = pendulum.angular_velocity
        
        pendulum.update_state()


    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(time_array, angles_rad, label='Ángulo (rad)')
    plt.title('Simulación del Péndulo Invertido')
    plt.ylabel('Ángulo (rad)')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(time_array, angular_velocities_rad_s, label='Velocidad Angular (rad/s)', color='orange')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad Angular (rad/s)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()