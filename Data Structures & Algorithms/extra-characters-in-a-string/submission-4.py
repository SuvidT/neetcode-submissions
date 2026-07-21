class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        # dp[i] will store the minimum extra characters from index i to the end
        dp = [0] * (n + 1)
        
        # Work backward from the end of the string to the beginning
        for i in range(n - 1, -1, -1):
            # Choice A: Assume the current character is extra (+1 penalty)
            dp[i] = 1 + dp[i + 1]
            
            # Choice B: Look through the dictionary to see if any word fits here
            for word in dictionary:
                w_len = len(word)
                # If the word physically fits and perfectly matches the substring
                if i + w_len <= n and s[i : i + w_len] == word:
                    # If it matches, we take the best score between what we have
                    # and jumping completely past this word (dp[i + w_len])
                    dp[i] = min(dp[i], dp[i + w_len])
                    
        return dp[0]