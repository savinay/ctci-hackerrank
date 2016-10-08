def is_matched(expression):
    stack = []
    hash_brackets = {"(":")", "{":"}", "[":"]"}
    for x in expression:
        if x == "{" or x == "[" or x == "(":
            stack.append(x)
        if x == "}" or x == "]" or x == ")":
            if len(stack) > 0:
                if hash_brackets[stack[-1]] == x:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
    

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"