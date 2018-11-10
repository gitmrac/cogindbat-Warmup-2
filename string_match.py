#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a,b):
    c=0
    p=min(len(a),len(b))
    for i in range(p):
        if a[i]==b[i]:
            if(i==p-1):
                break
            else:
                if(a[i+1]==b[i+1]):
                    c+=1                
        else:
            continue
    return c
"""
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
