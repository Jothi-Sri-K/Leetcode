class Solution:
    def findComplement(self, num: int) -> int:
        num_bin=list(str((bin(num)[2:])))
        for i in range(0,len(num_bin)):
            if num_bin[i]=='0':
                num_bin[i]='1'
            else:
                num_bin[i]='0'
        num_bin=''.join(num_bin)
        return int(num_bin,2)
        
        



        
        