class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}           
        left = 0
        count = 0       
        len = 0         
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            count = max(count, freq[s[right]])
            while (right - left + 1) - count > k:
                freq[s[left]] -= 1
                left += 1
            len = max(len, right - left + 1)
        return len
if __name__ == "__main__":
    s = input("Enter the string :")
    k = int(input("Enter k value:"))
    solution = Solution()
    result = solution.characterReplacement(s, k)
    print(result)
