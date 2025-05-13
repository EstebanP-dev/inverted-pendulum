import unittest
from src.pendulum_model import InvertedPendulum
from src.constants import GRAVITY, MASS, LENGTH, TIME_STEP

class TestInvertedPendulum(unittest.TestCase):

    def setUp(self):
        self.pendulum = InvertedPendulum(initial_angle=0.1, initial_angular_velocity=0.0)

    def test_calculate_dynamics(self):
        # Test the dynamics calculation at a specific state
        angle, angular_velocity = self.pendulum.calculate_dynamics()
        self.assertIsNotNone(angle)
        self.assertIsNotNone(angular_velocity)

    def test_update_state(self):
        # Test the state update after one time step
        initial_state = (self.pendulum.angle, self.pendulum.angular_velocity)
        self.pendulum.update_state()
        updated_state = (self.pendulum.angle, self.pendulum.angular_velocity)
        
        self.assertNotEqual(initial_state, updated_state)

    def test_constants(self):
        # Test if constants are correctly imported
        self.assertEqual(GRAVITY, 9.81)
        self.assertEqual(MASS, 1.0)
        self.assertEqual(LENGTH, 1.0)
        self.assertEqual(TIME_STEP, 0.01)

if __name__ == '__main__':
    unittest.main()