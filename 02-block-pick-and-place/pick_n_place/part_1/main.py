# """ =================================================
# Copyright (C) 2018 Vikash Kumar
# Adapted by Raghava Uppuluri for GE-AI Course
# Author  :: Vikash Kumar (vikashplus@gmail.com)
# Source  :: https://github.com/vikashplus/robohive
# License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
# ================================================= """

DESC = """
DESCRIPTION: Simple Box Pick and Place \n
HOW TO RUN:\n
    - Ensure poetry shell is activated \n
    - python3 main.py \n
"""

from robohive.physics.sim_scene import SimScene
from robohive.utils.inverse_kinematics import qpos_from_site_pose
from robohive.utils.min_jerk import *
from robohive.utils.quat_math import euler2quat, quat2mat, mat2quat
from pick_n_place.utils.xml_utils import replace_simhive_path

from pathlib import Path

import click
import numpy as np

BIN_POS = np.array([0.235, 0.5, 0.85])
BIN_DIM = np.array([0.2, 0.3, 0])
BIN_TOP = 0.10
ARM_nJnt = 7


@click.command(help=DESC)
@click.option(
    "-s",
    "--sim_path",
    type=str,
    help="environment to load",
    required=True,
    default="pick_place.xml",
)
@click.option("-h", "--horizon", type=int, help="time (s) to simulate", default=2)
def main(sim_path, horizon):
    # Prep
    sim_path = Path(__file__).parent.parent.absolute() / "env" / sim_path
    sim_xml = replace_simhive_path(str(sim_path))
    print(f"Loading {sim_xml}")
    sim = SimScene.get_sim(model_handle=sim_xml)

    # setup
    target_sid = sim.model.site_name2id("drop_target")
    box_sid = sim.model.body_name2id("box")
    eef_sid = sim.model.site_name2id("end_effector")

    ARM_JNT0 = np.mean(sim.model.jnt_range[:ARM_nJnt], axis=-1)

    while True:
        # Update targets
        if sim.data.time == 0:
            print("Resamping new target")
            # Sample random place targets
            target_pos = (
                BIN_POS
                + np.random.uniform(high=BIN_DIM, low=-1 * BIN_DIM)
                + np.array([0, 0, BIN_TOP])
            )  # add some z offfset
            target_elr = np.random.uniform(high=[3.14, 0, 0], low=[3.14, 0, -3.14])
            target_quat = euler2quat(target_elr)

            # ---------------- 1.1 REPLACE WITH YOUR OWN TARGETS----------------

            # Box pose in Global Frame
            box_pos = sim.data.xpos[box_sid]  # cartesian position
            box_mat = sim.data.xmat[box_sid]  # rotation matrix

            # propagage targets to the sim for viz (ONLY FOR VISUALIZATION)
            sim.model.site_pos[target_sid][:] = target_pos - np.array([0, 0, BIN_TOP])
            sim.model.site_quat[target_sid][:] = target_quat

            # reseed the arm for IK (ONLY FOR VISUALIZATION)
            sim.data.qpos[:ARM_nJnt] = ARM_JNT0
            sim.forward()
            # ---------------- 1.1 REPLACE WITH YOUR OWN TARGETS----------------

            # --------------- 1.2 GENERATE FULL JOINT TRAJECTORY FOR TASK----------------
            # IK
            ik_result = qpos_from_site_pose(
                physics=sim,
                site_name="end_effector",
                target_pos=target_pos,  # change!
                target_quat=target_quat,  # change!
                inplace=False,
                regularization_strength=1.0,
            )

            print(
                "IK:: Status:{}, total steps:{}, err_norm:{}".format(
                    ik_result.success, ik_result.steps, ik_result.err_norm
                )
            )

            # generate min jerk trajectory
            waypoints = generate_joint_space_min_jerk(
                start=ARM_JNT0,
                goal=ik_result.qpos[:ARM_nJnt],
                time_to_go=horizon,
                dt=sim.model.opt.timestep,
            )
            # --------------- 1.2 GENERATE FULL JOINT TRAJECTORY FOR TASK----------------

        # propagate waypoint in sim
        waypoint_ind = int(sim.data.time / sim.model.opt.timestep)
        sim.data.ctrl[:ARM_nJnt] = waypoints[waypoint_ind]["position"]
        sim.advance(render=True)

        # reset time if horizon elapsed
        if sim.data.time > horizon:
            # UPDATE ^ 'horizon' to the horizon for all the trajectories combined
            sim.reset()


if __name__ == "__main__":
    main()
