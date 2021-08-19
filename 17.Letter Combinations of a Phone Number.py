class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def getall(lst,digits,l,t):
            nums = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
            if l!=len(digits)-1:
                for i in nums[digits[l]]:
                    getall(lst,digits,l+1,t+i)
            else:
                for i in nums[digits[l]]:
                    lst.append(t+i)
                
        if len(digits)<=0:
            return []
        lst = list()
        getall(lst,digits,0,"")
        print(lst)
        return lst
