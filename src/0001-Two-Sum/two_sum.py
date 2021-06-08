
#Difference: if use enumerate() or not

##Solution 1

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        nums_len = len(nums)
        for i in range(nums_len):
            dif = target - nums[i]
            if dif in nums_hash: 
                return [nums_hash[dif], i]
            nums_hash[nums[i]] = i
        return []
        
        
if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 3
    print(Solution().twoSum(nums, target))
    
    
    
       
    
# Solution 2  
    
class Solution:
    def twoSums(self,nums,target):
        nums_hash = {}
        for i ,v in enumerate(nums):
            dif = target - v
            if dif in nums_hash:
                return [nums_hash[dif],i]
            nums_hash[v]=i
        return []


if __name__ == '__main__':
nums = [1, 2, 3]
target = 3
print(Solution().twoSum(nums, target))
