class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ans = ""
        temp = path.split('/')
        for i in temp:
            if i == '' or i=='.':
                pass
            elif i =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        for i in stack:
            ans += '/'+i
        return ans if ans else '/'
