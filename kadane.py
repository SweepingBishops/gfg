def maxSubArraySum(arr,N):
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
