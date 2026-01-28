class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        count=1
        max=1
        ele=0
        for i in range(len(nums)):
            count=1
            for j in range(1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count>max:
                max=count
                ele=nums[i]
        return ele       