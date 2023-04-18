def test(nums, k):
    s = 0
    for i in range(len(nums))[:k]:
        if len(str(abs(nums[i])))>2:
            s = s + nums[i]
    return s

nums = [4, 5, 17, 9, 14, 108, -9, 12 ,76]
print("Original list:",nums)
K = 4
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K))
nums = [4, 5, 17, 9, 14, 108, -9, 12 ,76]
print("\nOriginal list:",nums)
K = 6
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K))
nums = [114, 215, -117, 119, 14, 108, -9, 12 ,76]
print("\nOriginal list:",nums)
K = 5
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K)) 
print("\nOriginal list:",nums)
K = 1
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K))  
