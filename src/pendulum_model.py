import numpy as np

class InvertedPendulum:
    def __init__(self, mass, length, gravity, time_step, initial_angle=0.0, initial_angular_velocity=0.0):
        self.mass = mass
        self.length = length
        self.gravity = gravity
        self.time_step = time_step
        self.angle = initial_angle
        self.angular_velocity = initial_angular_velocity
        self.moment_of_inertia = self.mass * self.length**2

    def calculate_angular_acceleration(self):
        angular_acceleration = (self.gravity / self.length) * np.sin(self.angle)
        return angular_acceleration

    def update_state(self):
        angular_acceleration = self.calculate_angular_acceleration()
        self.angular_velocity += angular_acceleration * self.time_step
        self.angle += self.angular_velocity * self.time_step
        self.angle = (self.angle + np.pi) % (2 * np.pi) - np.pi

    def get_state(self):
        return self.angle, self.angular_velocity