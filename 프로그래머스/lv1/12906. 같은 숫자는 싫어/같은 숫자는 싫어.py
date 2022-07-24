def solution(s):
  sol=[]

  for i in range(len(s)-1):
      if s[i]!=s[i+1]:
          sol.append(s[i])

  sol.append(s[-1])

  return sol