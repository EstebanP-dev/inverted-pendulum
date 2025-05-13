class InvertedPendulum:
    def __init__(self, mass, length, gravity, time_step):
        self.mass = mass
        self.length = length
        self.gravity = gravity
        self.time_step = time_step
        self.angle = 0.0  # Initial angle (radians)
        self.angular_velocity = 0.0  # Initial angular velocity (radians/s)

    def calculate_dynamics(self):
        # Calculate the forces acting on the pendulum
        force = self.gravity * self.mass * self.length * self.angle
        torque = -force * self.length
        return torque

    def update_state(self):
        # Update the state of the pendulum based on the calculated dynamics
        torque = self.calculate_dynamics()
        angular_acceleration = torque / (self.mass * self.length**2)
        self.angular_velocity += angular_acceleration * self.time_step
        self.angle += self.angular_velocity * self.time_step

    def get_state(self):
        return self.angle, self.angular_velocity