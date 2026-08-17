class Solution:
    def isPalindrome(self, x: int) -> bool:
        rvr = 0

        if x<0:
            return False
        elif x%10 == 0 and x!=0:
            return False
        
        while x>rvr:
            last_num = x%10
            rvr = rvr*10 + last_num
            x = x//10
        return x == rvr or x == rvr//10

        
