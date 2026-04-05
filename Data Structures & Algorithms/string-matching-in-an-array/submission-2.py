class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def rabin_karp(pattern, text):
            n, m = len(text), len(pattern)
            if m > n:
                return False
            
            BASE, MOD = 31, 10**9 + 7
            
            # Precompute powers
            power = 1
            for _ in range(m - 1):
                power = (power * BASE) % MOD
            
            # Compute initial hashes
            p_hash = t_hash = 0
            for i in range(m):
                p_hash = (p_hash * BASE + ord(pattern[i]) - ord('a')) % MOD
                t_hash = (t_hash * BASE + ord(text[i])   - ord('a')) % MOD
            
            for i in range(n - m + 1):
                if t_hash == p_hash and text[i:i+m] == pattern:  # verify on match
                    return True
                if i < n - m:
                    # Roll the hash forward
                    t_hash = (t_hash - (ord(text[i]) - ord('a')) * power) % MOD
                    t_hash = (t_hash * BASE + ord(text[i+m]) - ord('a')) % MOD
                    t_hash = (t_hash + MOD) % MOD  # keep positive
            return False

        return [w for w in words if any(rabin_karp(w, other) for other in words if other != w)]
