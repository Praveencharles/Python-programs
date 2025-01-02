import numpy as np
from collections import counter
from scipy import stats
a=[11,21,34,22,27,11,23,21]
mean=sum(a)/len(a)
print(mean)
mean=np.mean(a)
print(mean)
def median(nums):
    nums.sort()
    if len(nums)%2==0:
        return int(nums[len(nums)//2-1]+nums[len(nums)//2])/2
    else:
        return nums[len(nums)//2]
print(median(a))
data=dict(counter(a))
mode=[k for k, v in data, items()if v==max(list(data.values()))]
print(mode)
print(stats.mode(a)[0][0])
def q(nums):
    nums=sorted(nums)
    q1=median(nums[:len(nums)//2])
    q2=median(nums)
    if len(nums)%2==0:
        q3=median(nums[len(nums)//2:])
    else:
        q3=median(nums[len(nums)//2+1:])
    return q1,q2,q3
print(q(a))
n=len(a)
std=(sum(map(lambda x:(x-sum(a)/n)**2,a))/n)**0.5
print(std)
print(np.std(a))
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        