# Project 2

## Preliminary Steps
1. Install MuJoCo and poetry

- [Install Mujoco](https://mujoco.readthedocs.io/en/stable/programming/index.html#getting-started)
- [Install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

2. Clone repo 

```
git clone https://github.com/purdue-mars/VIP-GEAI
cd 02-block-pick-and-place
```

3. Install dependencies 

```
poetry install
```

4. Intialize virtual environment

```
poetry shell
```

## Part 1: Open-loop Box Pick and Place

Goal: get the robot to pick up the brick in the right bin and place it in the left bin within the **target green zone** via following a precomputed trajectory open-loop

To run the starter script:
``` 
python3 part_1/main.py 
```
> NOTE: Initially, the robot will just go to the **target green zone**

Update the `part_1/main.py` file with the following steps:
1. STEP 1.1: Generate Task-relevant Poses
2. STEP 1.2: Create Joint-position trajectory following the task-relevant poses

### Helpful tips

- On the left sidebar of the MuJoCorenderer, click: 
  - `Rendering > Frame > Site|Body|Geom` to toggle rendering of the coordinate frames
  - `Rendering > Label > Site|Body|Geom` to toggle rendering of the labels
- Helpful utils are provided for you to in the robohive library:
  - [quat2mat](https://github.com/vikashplus/robohive/blob/ef6f2c3deb93555d779bb3f9af0b3c21414c6bc0/robohive/utils/quat_math.py#L152): convert quaternion to rotation matrix
  - [mat2quat](https://github.com/vikashplus/robohive/blob/ef6f2c3deb93555d779bb3f9af0b3c21414c6bc0/robohive/utils/quat_math.py#L110): convert rotation matrix to quaternion
  - [generate_joint_space_min_jerk](https://github.com/vikashplus/robohive/blob/ef6f2c3deb93555d779bb3f9af0b3c21414c6bc0/robohive/utils/min_jerk.py#L5): generate joint space trajectory given start and end joint angles

## Part 2: Box Pick and Place with Collision Avoidance

Coming soon

## Part 3: Closed-loop Box Pick and Place using Vision and Learning

Coming soon
