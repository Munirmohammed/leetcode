class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        MOD = 10**9+7

        
        max_mod = (pow(2, p, MOD)-1)%MOD   

        return (max_mod*pow( (max_mod-1)%MOD ,(pow(2, p-1, MOD-1)-1) % (MOD-1), MOD)) % MOD
        
        
