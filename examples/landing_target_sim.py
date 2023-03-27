#!/usr/bin/env python3

# Publishes relative target position updates for the drone to land on


import asyncio
from mavsdk import System
from mavsdk.precision_target import PositionLocal

async def run():
    drone = System()
    await drone.connect(system_address="udp://localhost:14551")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    async for pos_vel_ned in drone.telemetry.position_velocity_ned():
        # print(f"position body: {pos_vel_ned}")
        
        # TODO:
        # 1. in order to feed into landing_target_estimator on PX4 I would have to publish messages that end up being IR Lock Reports :x
        # 2. Only when publishing as IR Lock Report messages, I need to get the vehicle's NED position. If I publish NED positions, I can just publish constant values.

        # position_local = PositionLocal(pos_vel_ned.position.north_m + 3.5, pos_vel_ned.position.east_m + 2.5, 0.0)
        position_local = PositionLocal(3.5, 2.5, 0)
        print(position_local)
        await drone.precision_target.publish_position_relative(position_local)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())