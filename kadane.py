def maxSubArraySum(arr,N):
'''
Given an array of N integers, find the contiguous subarray
(containing at least one number)which has the maximum sum and return
its sum.

Time: O(n)
Space: O(1)
'''
    max_sum = arr[0]
    current_sum = 0
    for num in arr:
        if current_sum < 0:
            current_sum = num
        else:
            current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
