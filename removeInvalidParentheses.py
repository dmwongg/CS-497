def is_valid(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

def remove_invalid_parentheses(s):
    def dfs(s, index, left_count, right_count, left_rem, right_rem, expr):
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                valid_str = ''.join(expr)
                if is_valid(valid_str):
                    result.add(valid_str)
            return

        if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
            dfs(s, index + 1, left_count, right_count, left_rem - (s[index] == '('), right_rem - (s[index] == ')'), expr)

        expr.append(s[index])

        if s[index] != '(' and s[index] != ')':
            dfs(s, index + 1, left_count, right_count, left_rem, right_rem, expr)
        elif s[index] == '(':
            dfs(s, index + 1, left_count + 1, right_count, left_rem, right_rem, expr)
        elif s[index] == ')' and left_count > right_count:
            dfs(s, index + 1, left_count, right_count + 1, left_rem, right_rem, expr)

        expr.pop()

    left, right = 0, 0
    for char in s:
        if char == '(':
            left += 1
        elif char == ')':
            if left == 0:
                right += 1
            else:
                left -= 1

    result = set()
    dfs(s, 0, 0, 0, left, right, [])
    return list(result)


print(remove_invalid_parentheses("()())()"))  
print(remove_invalid_parentheses("(a)())()")) 
print(remove_invalid_parentheses(")("))  
