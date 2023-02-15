def solve(s):
    if type(s) == type('s'): s = list(s)
    if (len(s) == 1):
        try:
            return [int(s[0])]
        except ValueError:
            print("input is invalid")
            quit()
    
    sc_c = 0
    leng = len(s)
    i = 0

    while i < leng:

        if s[i] == ' ' and i < leng - 1:
            s = s[:i] + s[i + 1:]
        try:
            if (s[i].isdigit()):
                d = int(s[i])
                j = i + 1
                if i < len(s) - 1:
                    while (s[j].isdigit() and j < len(s)):
                        d = d * 10 + int(s[j])
                        j += 1
                        if j == len(s):
                            break
                if i > 0:
                    if s[i-1] == '.':
                        s = s[:i-2] + [float(s[i-2]) + d / 10] + s[i + 1::]
                
                    else:
                        s = s[:i] + [d] + s[j:]
                else:
                    s = s[:i] + [d] + s[j:]
                oldl = leng
                leng = len(s)
                i -= (oldl - leng)
                if i < 0: i = 0
        except:
            pass

        i += 1
    return solve_rec(s)
    


def solve_rec(s):
    if len(s) == 1: return s

    leng = len(s)
    i = 0
    sc_w = 0
    while i < leng:
        sc_w = 0
        if len(s) == 1:
            break


        if s[i] == '+' and s[i-1] != ')' and s[i+1] != '(':
            s = s[:i-1] + [s[i-1] + s[i+1]] + s[i+2:]
            leng = len(s)
            i = 0
        if s[i] == '-' and s[i-1] != ')' and s[i+1] != '(':
            s = s[:i-1] + [s[i-1] - s[i+1]] + s[i+2:]
            leng = len(s)
            i = 0
        if s[i] == '*' and s[i-1] != ')' and s[i+1] != '(':
            s = s[:i-1] + [s[i-1] * s[i+1]] + s[i+2:]
            leng = len(s)
            i = 0
        if s[i] == '/' and s[i+1] == '/' and s[i-1] != ')' and s[i+2] != '(':
            s = s[:i-1] + [s[i-1] // s[i+2]] + s[i+3:]
            leng = len(s)
            i = 0
        elif s[i] == '/' and s[i-1] != ')' and s[i+1] != '(':
            s = s[:i-1] + [s[i-1] / s[i+1]] + s[i+2:]
            leng = len(s)
            i = 0




        elif s[i] == '(':
            sc_w += 1
            j = i + 1
            while (s[j] != ')' or sc_w != 1):
                if s[j] == ')': sc_w -= 1
                if s[j] == '(': sc_w += 1
                j += 1


            s = s[:i] + solve_rec(s[i + 1:j]) + s[j+1:]
            leng = len(s)
            i = 0

        i += 1


    return s



print(*solve(input()))
            
