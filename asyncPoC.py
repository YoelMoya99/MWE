import asyncio
import random

# One-time function HARDWARE CONFIGURATION MAIN ARQUITECTURE
async def run_once():
    print("Run once executed")

# Normal task 1 -> From Another Object
async def normal_task_1():
    print("Normal task 1 running")

# Normal task 2 -> From Another Object
async def normal_task_2():
    print("Normal task 2 running")

# Async task A -> From another Object
async def async_task_a():
    await asyncio.sleep(1)
    print("Async task A done")

# Async task B -> From Another Object
async def async_task_b():
    await asyncio.sleep(2)
    print("Async task B done")

# Async task C — fire-and-forget -> From Another Object
async def async_task_c():
    print("Async task C started")
    await asyncio.sleep(3)
    print("Async task C finished")

# Infinite loop -> MAIN ARQUITECTURE
async def main_loop():
    while True:
        await normal_task_1()
        await normal_task_2()

        # Conditionally fire-and-forget task C
        if random.random() < 0.5:  # 50% chance
            asyncio.create_task(async_task_c())

        # Wait for A and B to complete
        await asyncio.gather(
            async_task_a(),
            async_task_b()
        )

        await asyncio.sleep(5)

# Entrypoint
async def main():
    await run_once()
    await main_loop()

asyncio.run(main())

