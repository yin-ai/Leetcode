class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def helper(x):
          if x == len(s)-1:
              res.append(''.join(c))
              return
          
          dict_ = set()
          for i in range(x, len(c)):
              if c[i] not in dict_:
                  dict_.add(c[i])
                  c[i], c[x] = c[x], c[i]
                  helper(x+1)
                  c[i], c[x] = c[x], c[i]
        helper(0)
        return res
