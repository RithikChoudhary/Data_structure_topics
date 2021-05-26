class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lis = []
        var = None
        for i in range(len(candies)):
            for j in range(len(candies)):
                var = True if (candies[i]+extraCandies)  >= candies[j] else False
                if var == False:
                    break
            lis.append(var)
        return lis
    
