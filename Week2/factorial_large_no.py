class Solution:
    def factorial(self, n):
        fact=1
        for i in range(1,n+1):
          fact*=i
        factl = list(str(fact))
        return factl
n = int(input("Enter the number:"))
obj=Solution()
result=obj.factorial(n)
print(result)