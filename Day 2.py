class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
nums=list(map(int,input().split()))
target=int(input("Target:"))
print(search(nums,target))
