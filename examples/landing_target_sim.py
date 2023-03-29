#!/usr/bin/env python3

# Publishes relative target position updates for the drone to land on

import logging
import asyncio
from mavsdk import System
from mavsdk.precision_target import PositionLocal, ObservationFrame
import numpy as np

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

detection_range_m = 15.0

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    logging.info("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            logging.info(f"-- Connected to drone!")
            break

    async for pos_vel_ned in drone.telemetry.position_velocity_ned():
        # print(f"position body: {pos_vel_ned}")
        
        # TODO:
        # 1. in order to feed into landing_target_estimator on PX4 I would have to publish messages that end up being IR Lock Reports :x
        # 2. Only when publishing as IR Lock Report messages, I need to get the vehicle's NED position. If I publish NED positions, I can just publish constant values.

        # position_local = PositionLocal(pos_vel_ned.position.north_m + 3.5, pos_vel_ned.position.east_m + 2.5, 0.0)
        # help(pos_vel_ned.position)
        # exit(1)
        # Check detection range
        vec_pos_drone_ned = np.array([pos_vel_ned.position.north_m, pos_vel_ned.position.east_m, pos_vel_ned.position.down_m])
        vec_pos_marker_ned = np.array([3.5, 2.5, 0])

        distance_marker_drone = np.linalg.norm(vec_pos_drone_ned - vec_pos_marker_ned)
        if distance_marker_drone < detection_range_m:
            position_local = PositionLocal(vec_pos_marker_ned[0], vec_pos_marker_ned[1], vec_pos_marker_ned[2])
            logging.info(position_local)
            await drone.precision_target.publish_position_relative(position_local, ObservationFrame.LOCAL_NED)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())