import unittest
from src.pendulum_model import InvertedPendulum
from src.constants import GRAVITY, MASS, LENGTH, TIME_STEP

class TestInvertedPendulum(unittest.TestCase):

    def setUp(self):
        self.pendulum = InvertedPendulum(
            mass=MASS,
            length=LENGTH,
            gravity=GRAVITY,
            time_step=TIME_STEP,
            initial_angle=0.1, 
            initial_angular_velocity=0.0
        )

    def test_calculate_angular_acceleration(self):
        self.pendulum.angle = 0.0
        self.pendulum.angular_velocity = 0.0
        accel_at_zero = self.pendulum.calculate_angular_acceleration()
        self.assertAlmostEqual(accel_at_zero, 0.0)

        self.pendulum.angle = 0.01
        accel_small_positive = self.pendulum.calculate_angular_acceleration()
        self.assertGreater(accel_small_positive, 0.0)

        self.pendulum.angle = np.pi / 6
        expected_accel = (GRAVITY / LENGTH) * np.sin(np.pi / 6)
        actual_accel = self.pendulum.calculate_angular_acceleration()
        self.assertAlmostEqual(actual_accel, expected_accel)

    def test_update_state(self):
        initial_state = (self.pendulum.angle, self.pendulum.angular_velocity)
        self.pendulum.update_state()
        updated_state = (self.pendulum.angle, self.pendulum.angular_velocity)
        
        self.assertNotEqual(initial_state, updated_state)

    def test_constants(self):
        self.assertEqual(GRAVITY, 9.81)
        self.assertEqual(MASS, 1.0)
        self.assertEqual(LENGTH, 1.0)
        self.assertEqual(TIME_STEP, 0.01)

if __name__ == '__main__':
    unittest.main()