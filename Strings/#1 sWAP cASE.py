def swap_case(s):
    c =''
    for l in s:
        if l.isupper():
            l=l.lower()
            c =c+l
        elif l.islower():
            l=l.upper()
            c =c+l
        else:
            c=c+l
    return c
