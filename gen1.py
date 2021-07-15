
def gen(nums):
  for i in nums:
    yield i

nums = gen([1,2,3,4,5,])

print(next(nums))
print(next(nums))
print(next(nums))