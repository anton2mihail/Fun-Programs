def main(stringsssss):
    stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
    for i in stringsssss:
        if i in pchar:
            stack.append(i)
        elif len(stack) == 0 or pchar[stack[len(stack)-1]] != i:
            return False
    return len(stack) == 0




print(main("{}"))
