class Solution:
    def isValid(self, s: str) -> bool:

        o = []
        d = {")" : "(", "}" : "{", "]" : "[" }

        for i in s:
            
            if (i in d.values()):
                o.append(i)
            elif (len(o) == 0):
                return False
            else:
                if (o[-1] == d[i]):
                    o.pop()
                else:
                    return False

        return len(o) == 0
