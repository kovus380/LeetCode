class Solution:

                
    def generateParenthesis(self, n: int) -> List[str]:
        
        combs = []
        def dfs(s, n, leave, depth):
            leave_tmp = leave[:]
            if depth == 2 * n:
                combs.append(s)
                print(s)
                return 
            if leave_tmp[0] == 0:
                print(1, s)
                s += ")"
                leave_tmp[1] -= 1
                dfs(s, n, leave_tmp, depth + 1)

            else:
                if leave_tmp[0] == leave_tmp[1]:
                    print(2, s)
                    s += "("
                    leave_tmp[0] -= 1
                    dfs(s, n, leave_tmp, depth + 1)
                elif leave_tmp[0] < leave_tmp[1]:
                    print(3, s)
                    s += ")"
                    leave_tmp[1] -= 1
                    dfs(s, n, leave_tmp, depth + 1)
                    
                    print(4, s, leave_tmp)
                    s = s[:-1] + "("
                    leave_tmp[1] += 1
                    leave_tmp[0] -= 1
                    dfs(s, n, leave_tmp, depth + 1)
        
        
        dfs("", n, [n, n], 0)
        return combs