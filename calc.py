def solve(x):
    j = 0

    if x[0] == '(':
        del x[0]
    if x[-1] == ')':
        del x[-1]
    for i in range(len(x) - 1, 0, -1):
        if x[i] == ')':
            del x[i]
        elif x[i] == '(':
            del x[i]
    x = ' '.join(map(str, x)).split()

    c=1
    k = 0
    while k < len(x) - 1:
        if x[k].isdigit() and x[k+1].isdigit():
            x[k] = int(x[k] + x[k+1])
            del x[k+1]
            c+=1
        k+=1

    lenans = len(x)

    i = 0
    while i < lenans:
        if x[i] == '*':
            if len(x[:i-1]) > 1:
                x = x[:i-1] + [int(x[i-1]) * int(x[i+1])] + x[i+2:]
            if len(x[:i-1]) == 1:
                x = [x[:i-1]] +[int(x[i-1]) * int(x[i+1])] + x[i+2:]
            if x[:i-1] == []:

                x = [float(x[i-1]) * float(x[i+1])] + x[i+2:]
            lenans = len(x)
            i = 0
        elif x[i] == '/':
            if len(x[:i-1]) > 1:
                x = x[:i-1] + [float(x[i-1]) / float(x[i+1])] + x[i+2:]
            if len(x[:i-1]) == 1:
                x = [x[:i-1]] +[float(x[i-1]) / float(x[i+1])] + x[i+2:]
            else:
                x = [float(x[i-1]) / float(x[i+1])] + x[i+2:]
            lenans = len(x)
            i = 0
        if lenans == 1:
            break
        i+=1

    
    lenans = len(x)
    i=0
    while i < lenans:
        
        if x[i] == '+':
            if len(x[:i-1]) > 1:
                x = x[:i-1] + [float(x[i-1]) + float(x[i+1])] + x[i+2:]
            if len(x[:i-1]) == 1:
                x = [x[:i-1]] +[float(x[i-1]) + float(x[i+1])] + x[i+2:]
            else:
                x = [float(x[i-1]) + float(x[i+1])] + x[i+2:]
            i = 0
            lenans = len(x)

        elif x[i] == '-':
            if len(x[:i-1]) > 1:
                x = x[:i-1] + [float(x[i-1]) - float(x[i+1])] + x[i+2:]
            if len(x[:i-1]) == 1:
                x = [x[:i-1]] +[float(x[i-1]) - float(x[i+1])] + x[i+2:]
            else:
                x = [float(x[i-1]) - float(x[i+1])] + x[i+2:]
            i = 0
            lenans = len(x)
        if lenans == 1:
            break
        i+=1
    if type(x) == type([1]):
        x = x[0]


    return x
x = ['('] + list(input()) + [')']
stack = []
stack_i = []
lensolved = 0
i = 0
while i < len(x) - 1:
    if '(' == x[i]:
        stack.append('(')
        stack_i.append(i)
    if ')' == x[i]:
        if x[:stack_i[-1]] and x[i+1:]:
            x = x[:stack_i[-1] - 1] + [solve(x[stack_i[-1] + 1:i])] + x[i+1:]
        elif x[:stack_i[-1]]:
            x = x[:stack_i[-1] - 1] + [solve(x[stack_i[-1] + 1:i])]
        elif x[i+1:]:
            x = [solve(x[stack_i[-1] + 1:i])] + x[i+1:]
        else:
            break
        del stack[-1]
        del stack_i[-1]
        i = 0
    i+=1
x = solve(x)
print(x)
