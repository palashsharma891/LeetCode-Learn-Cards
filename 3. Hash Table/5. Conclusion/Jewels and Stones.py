class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jset = set(jewels)
        total = 0
        for stone in stones:
            if stone in jset:
                total += 1
                
        return total
        
        
#        mapping = {}
 #       for stone in stones:
  #          if stone not in mapping:
   #             mapping[stone] = 1
    #        else:
     #           mapping[stone] += 1
                
#        total = 0
 #       for key in mapping.keys():
  #          if key in jewels:
   #             total += mapping[key]
                
    #    return total
