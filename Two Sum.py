class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        zone=[]
        count=0
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                ans=(nums[i]+nums[j+1])==target
                if ans==True and i!=(j+1):
                    zone.append(i)
                    zone.append(j+1)
                    count+=1
                    break
            if count==1:
                break
                    
        return zone