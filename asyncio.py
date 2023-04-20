import asyncio
import time

counter = 0

async def foo1():
  global counter
  while True:
    counter += 1
    counter -= 1
    print(counter)
    await asyncio.sleep(0)

async def foo2():
  global counter
  while True:
    counter += 1
    counter -= 1
    print(counter)
    await asyncio.sleep(0)

# asyncio.gather(foo1(),foo2())
# asyncio.get_event_loop().run_forever()