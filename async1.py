import asyncio

async def main():
  print('something')
  task = asyncio.create_task(foo('text'))
  #await task
  print('finished')

async def foo(test):
  print(test)
  await asyncio.sleep(2)

asyncio.run(main())
