class Solution:
    def grayCode(self, n: int) -> List[int]:
        def generate(n):
            if(n == 0):
                return ['0']
            if(n == 1):
                return ['0', '1']
            else:
                x = generate(n-1)
                return ['0'+i for i in x]+ ['1'+i for i in x[::-1]]
        return [int(x, 2) for x in generate(n)]
