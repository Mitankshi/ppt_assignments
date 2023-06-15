def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Move slow and fast pointers until they meet
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset slow to the first element
    slow = nums[0]

    # Move slow and fast pointers until they meet again
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 4, 2, 2]
findDuplicate(nums=nums)
