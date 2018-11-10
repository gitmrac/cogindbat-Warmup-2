#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    z=[]
    for i in range(0,len(str),2):
        z.append(str[i])
    result="".join(z)
    return result
    
    
    """
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
    
    """
