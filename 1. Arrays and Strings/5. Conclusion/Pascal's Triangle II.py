class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        nums = [
            [1],
            [1, 1]
        ]
        
        for i in range(2, rowIndex+1):
            nums += [[1]]
            for j in range(1, i):
                temp = nums[i-1][j-1] + nums[i-1][j]
                nums[i] += [temp]
                
            nums[i] += [1]
            
        return nums[rowIndex]
