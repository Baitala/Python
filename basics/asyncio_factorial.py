# Test for async/await from official doc
# https://docs.python.org/3.6/library/asyncio-task.html
# All commented lines are for Python 3.7
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        #print(f"Task {name}: Compute factorial({i})...")
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    #print(f"Task {name}: factorial({number}) = {f}")
    print("Task %s: factorial(%s) = %s" % (name, number, f))

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

#asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))
loop.close()
