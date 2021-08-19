class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        st = set()
        ans = 0
        for end in range(len(s)):
            ch = s[end]
            while ch in st:
                st.remove(s[start])
                start+=1
            st = st.union({ch})
            ans = max(ans, end+1-start)
        return ans
