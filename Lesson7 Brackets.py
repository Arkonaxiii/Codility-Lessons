def solution(S):
   
   pairs = {'}': '{', ']': '[', ')': '('}
   stack = []
   lefts = ['{','[','(']
   
   for letter in S:
       if letter in lefts:
           stack.append(letter)
       else:
            if len(stack) == 0:
                return 0
            if pairs[letter] != stack.pop():
                return 0
   if len(stack) == 0:
        return 1
   else:
        return 0
