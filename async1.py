'''
Asynchronous programming is a technique that enables your program to start a potentially long-running task, and then rather than having to wait until that task has finished, to be able to continue to be responsive to other events while the task runs. Once the task is completed, your program is presented with the result.
'''

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
