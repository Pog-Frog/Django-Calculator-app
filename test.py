eq = "45+96+|78|+|78|+78"
while True:
    if "|" in eq:
        print(eq.index("|"))
        t = eq.index("|") + 1
        tmp = eq[t:]
        print(tmp)
    else:
        break