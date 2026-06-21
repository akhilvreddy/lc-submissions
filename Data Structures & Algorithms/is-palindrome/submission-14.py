class Solution:
    """
    plan:
    - use two pointer approach
    left pointer - start at index 0
    right pointer - start at index len(string)-1

    while left < right: is the core loop

    1) if the char is not part of alphabet, skip
    2) normalize char to lowercase everytime

    if it is true the whole loop, default to return True. else break in middle of loop to false
    """

    def isPalindrome(self, s: str) -> bool:
        leftPtr, rightPtr = 0, len(s)-1

        while (leftPtr < rightPtr):
            while ((leftPtr < rightPtr) and (not s[leftPtr].isalnum())):
                leftPtr +=1

            while ((leftPtr < rightPtr) and (not s[rightPtr].isalnum())):
                rightPtr -=1
        
            if s[leftPtr].lower() != s[rightPtr].lower():
                return False
            
            leftPtr, rightPtr = leftPtr + 1, rightPtr - 1

        return True