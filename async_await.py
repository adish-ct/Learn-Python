import asyncio

async def task():
    print("Task started")
    await asyncio.sleep(2)
    # we can use await here for taking any data from database.
    print("Task finished")


if __name__ == "__main__":
    asyncio.run(task())