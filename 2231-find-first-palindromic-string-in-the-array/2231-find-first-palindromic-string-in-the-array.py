class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindrome=''
        count=0
        i=0
        while(count<1 and i<len(words) ):
            reversed_string=words[i]
            reversed_string=reversed_string[::-1]
            if words[i]==reversed_string:
                count+=1
                palindrome=words[i]
            else:
                i+=1
        return palindrome
        