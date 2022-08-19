# My solution

def valid_parenthesis(string):
    valid_char = ['(', ')', '{', '}', '[', ']']
    char_ls = []
    for each_char in string:
        char_ls.append(each_char)
    # print(char_ls)
    if char_ls[0] == '(' and char_ls[-1] == ')':
        return True
    elif char_ls[0] == '{' and char_ls[-1] == '}':
        return True
    elif char_ls[0] == '[' and char_ls[-1] == ']':
        return True
    else:
        return 'Invalid Parenthesis'

# test_case1 = valid_parenthesis("()")
# test_case2 = valid_parenthesis("(){}[]") # Won't work for this test case
# print(test_case1)
# print(test_case2)


# Actual solution
def valid_parenthesis_solution(string):
    stack = [] #stack data structure
    close_to_open = {")" : "(", "]" : "[", "}" : "{"} #hashmap to map all possible cases
    for char in string: 
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]: #checks if the stack is not empty and if the char at last index equals the char
                print(stack[-1])
                print(close_to_open[char])
                stack.pop() #if true then remove(pop) that char
            else:
                return False
        else:
            stack.append(char) #adds the char to list and keeps going
    return True if not stack else False #if stack is empty then only return true

test_case1 = valid_parenthesis_solution("([])")
# test_case2 = valid_parenthesis_solution("(){}[}") # Won't work
print(test_case1)
# print(test_case2)