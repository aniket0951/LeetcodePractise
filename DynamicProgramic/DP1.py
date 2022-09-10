def FibonacciNumber(number):
       prev1=1
       prev2=0
       for i in range(1,number):
           curr= prev1+prev2
           prev2=prev1
           prev1=curr
       return prev1%1000000007
n = 656
print("First fibonacci number is", FibonacciNumber(n))

def minPartition(n):
        coins = [2000,500,200,100,50,20,10,5,2,1]
        ans = []
        i = 0
        while n and i < 10:
            if n >= coins[i]:
                ans.append(coins[i])
                n -= coins[i]
            else:
                i += 1
        return ans     

# n = 43
# n = 1000
n = 8098
print("Minimum number of Coins", minPartition(n))

arr = [0,0,0,1]