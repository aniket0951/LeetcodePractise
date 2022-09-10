from collections import defaultdict
import itertools			
def possibility(m, length, s):

    # counts the occurrence of
    # number which is odd
    countodd = 0
    for i in range(0, length):

        # if occurrence is odd
        if m[int(s[i])] & 1:
            countodd += 1

        # if number exceeds 1
        if countodd > 1:
            return False
    
    return True

# Function to print the largest palindromic
# number by permuting digits of a number
def largestPalindrome(n):
        n = int(n)
        if n == 1:
            return 9
        
        # minimal number with n digits (for ex. for n = 4, min_num = 1000)
        min_num = 10 ** (n - 1)
        
        # maximal number with n digits (for ex. 9999)
        max_num = 10 ** n - 1       
        
        max_pal = 0
        
        # step is equal to 2, because we have to get a number, the 1st digit of which is 9, so we have to   
        # iterate only over odd numbers
        for i in range(max_num, min_num - 1, -2): 
            
            # since we are looking for the maximum palindrome number, it makes no sense to iterate over the 
            # product less than the max_pal obtained from the last iteration
            if i * i < max_pal:
                break
                
            for j in range(max_num, i - 1, -2):
                product = i * j
                
                # since a palindrome with an even number of digits must be mod 11 == 0 and we have no reason to 
                # check the product which less or equal than max_pal
                if product % 11 != 0 and product >= max_pal:
                    continue
                    
                # check if product is a palindrome then update the max_pal
                if str(product) == str(product)[::-1]:
                    max_pal = product

        return max_pal % 1337

     

# num = "444947137"  
num = "00009"  
# nums = [2,4,-2]
# k = 5
# n = len(nums)
print("FirstQuestin", largestPalindrome(num))	
