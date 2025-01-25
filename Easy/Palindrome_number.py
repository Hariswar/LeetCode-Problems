#9. Palindrome number - easy

#Roadmap to solve this problem:
# 121 % 10 = 1 : When you do this you will get 1, this is the one in the end. 
# 121 / 100 = 1 : When you do this you will get 1, this is the one in the beginning. 
# 121 % 100 = 21 : When you do this you will get 21. 
# 21 / 10 = 2 : Now u will get 2. 

# This should give you 121 as the same things as the given input. This is how u solve this palindrome question. 

class Solution:
    def isPalindrome(self, x: int) -> bool: 
      divider_value = 1
      if x < 0:
         return False 
      
      while x >= 10 * divider_value:
        divider_value *= 10
        
        while x:
            right = x % 10
            left = x // divider_value
            if left != right: 
                return False 
            x = (x % divider_value) // 10
            divider_value /= 100
        return True
     
        

