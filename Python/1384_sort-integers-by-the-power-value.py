# link https://leetcode.com/problems/sort-integers-by-the-power-value/submissions/
class Solution(object):
    def getKth(self, lo, hi, k):
        
          
        def Powercalculator(n):
            jumps = 0
            while(n!=1):
                if(n%2==0):
                    n=n//2
                else:
                    n=3*n+1
                jumps+=1
            return jumps
        
        heap = []
        for n in range(lo,hi+1):
            
            jumps = Powercalculator(n)
            heapq.heappush(heap,[jumps,n])
        
        #return the kth larget from the min heap
        return (heapq.nsmallest(k, heap)[k-1][1])
