from typing import List

'''
This is the first approach with brute force, by just comparing the
num[i] with num[i+1] is it == target??
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        n = len(nums) # mengambil panjang dari list nums
        for i in range(n): # iterasi nums[0]
            for j in range(i+1, n): # iterasi nums[i+1]
                # tujuannya agar bandingin nums[i] + nums[i+1] == target?
                if nums[i] + nums[j] == target:
                    return [i,j]
                
solution = Solution()
print(solution.twoSum([1,2,3], 5))
'''

'''This is the most efficient approach'''
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        hash = {} # make a new map
        '''
        hash will look like : 
        hash = {
            1: 0,
            2: 1,
            3: 2
        }
        '''
        # use enumerate to iterate and get both index and element
        for i, num in enumerate(nums): 
    
            '''
            count the numbers needed
            imagine that a + b = target
            we make it as b = target - a
            ex : target is 5 with [1,2,3]
            b = 5 - a
            '''

            b = target - num
            
            #check if the key is in hash
            if b in hash:
                return[hash[b],i]
            hash[num] = i

solution = Solution()
print(solution.twoSum([1,2,3],5))

