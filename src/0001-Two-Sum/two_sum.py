
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
        nums_hash = {} #创建一个空字典
        for i ,v in enumerate(nums): #以角标为键，对应数字为值
            dif = target - v
            
            if dif in nums_hash:
                return [nums_hash[dif],i] #如果哈希表中存在满足题设的数，则输出这两个数的角标
            
            nums_hash[v]=i #否则存入哈希表
            
        return []


if __name__ == '__main__':
nums = [1, 2, 3]
target = 3
print(Solution().twoSum(nums, target))
