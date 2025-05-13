# Inverted Pendulum Simulation

This project implements a simulation of an inverted pendulum, a classic problem in dynamics and control theory. The inverted pendulum is a simple yet powerful model used to study stability, control systems, and robotics.

## Project Structure

The project is organized as follows:

```
python-inverted-pendulum
├── src
│   ├── pendulum_model.py      # Contains the InvertedPendulum class and its dynamics
│   ├── constants.py           # Defines constants for the simulation
│   └── main.py                # Entry point for running the simulation
├── tests
│   └── test_pendulum_model.py  # Unit tests for the InvertedPendulum class
├── requirements.txt           # Lists the required dependencies
└── README.md                  # Project documentation
```

## Overview

The `InvertedPendulum` class in `pendulum_model.py` simulates the dynamics of the inverted pendulum. It includes methods to calculate the forces acting on the pendulum and to update its state based on these calculations.

## Constants

The constants used in the simulation are defined in `constants.py`. These include:

- `GRAVITY`: The acceleration due to gravity (default: 9.81 m/s²)
- `MASS`: The mass of the pendulum (default: 1.0 kg)
- `LENGTH`: The length of the pendulum (default: 1.0 m)
- `TIME_STEP`: The time step for the simulation (default: 0.01 s)

You can easily modify these constants to adjust the simulation parameters.

## Running the Simulation

To run the simulation, execute the `main.py` file. This will initialize the pendulum model, run the simulation, and visualize the results. You can also modify the constants directly in `constants.py` or through user input in `main.py`.

## Testing

Unit tests for the `InvertedPendulum` class are located in `tests/test_pendulum_model.py`. These tests ensure that the methods for calculating dynamics and updating the state function correctly.

## Requirements

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Conclusion

This project serves as an educational tool for understanding the dynamics of an inverted pendulum. It provides a foundation for further exploration into control systems and robotics.