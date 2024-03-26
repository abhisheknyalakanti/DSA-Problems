class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA=sum(aliceSizes)
        sumB=sum(bobSizes)
        setB=set(bobSizes)
        target_sum=(sumA+sumB)//2
        for candy in aliceSizes:
            diff=target_sum-(sumA-candy)
            if diff in setB:
                return[candy,diff]
        return []    