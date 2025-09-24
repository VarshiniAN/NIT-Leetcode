class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
if __name__=="__main__":
    nums=list(map(int,input().split()))
    target=int(input("Target:"))
    res=Solution()
    ans=res.search(nums,target)
    print(ans)
