#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  x=[]
  for i in range(len(str)):
    x.append(str[:i+1])
  x="".join(x)
  return x
  
  """
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
  """
