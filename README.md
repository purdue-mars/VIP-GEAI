# VIP-GEAI
Course Info for [VIP-GEAI](https://engineering.purdue.edu/VIP/teams/ge-ai)

### [`01-intro-to-robotics`](https://github.com/raghavauppuluri13/VIP-GEAI/blob/master/01-intro_to_robotics.ipynb)

This initial project aims to provide a "Hello World" into robot manipulation. 

You will implement basic versions of standard robot kinematics algorithms and control for a 2D robot arm:
- Computing forward kinematics, inverse kinematics, jacobian
- PD control

Also, you will get exposure to using APIs for [gymnasium](https://gymnasium.farama.org/) a standard framework used for representing reinforcement learning environments 
(specifically the MuJoCo [`reacher`](https://gymnasium.farama.org/environments/mujoco/reacher/) environment).

### [`02-pick-n-place`](https://github.com/purdue-mars/VIP-GEAI/tree/master/02-block-pick-and-place) 
This project aims to introduce the building blocks of robot manipulation, starting from one of the simplest tasks, but easily made complex: pick and place! We use [RoboHive](https://github.com/vikashplus/robohive/tree/main)'s MuJoCo panda and scene environments.

#### Part 1: Open-loop Box Pick and Place

![arm](https://github.com/purdue-mars/VIP-GEAI/assets/41026849/86a71edf-deba-46dc-b1db-776b7b55c050)
> Final student demo from Fall 2023

Get the robot to pick up the brick in the right bin and place it in the left bin within the target green zone via following a joint-space trajectory in open-loop

#### Part 2: Oops! Knocked something over! Adding obstacles avoidance...

A gentle introduction to motion planning algorithms to create collision-free trajectories to complete the pick and place task.

#### Part 3: Adding some learning to the mix...

Often, a robotic system may not have perfect perception of the object pose in the real world, how can the arm still perform robust pick and place using only raw images as input?

Get an introduction to learning techniques commonly found in robotics:
- reinforcement learning
- behavior cloning
