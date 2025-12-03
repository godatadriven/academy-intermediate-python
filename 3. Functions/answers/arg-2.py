
import math

def mult_numbers(*nums):
    return math.prod(nums)

# without math

def mult_numbers_no_import(*nums):
    answer = 1
    for n in nums:
        answer *= n
    return answer

mult_numbers(5,6,2,10), mult_numbers_no_import(5,6,2,10)