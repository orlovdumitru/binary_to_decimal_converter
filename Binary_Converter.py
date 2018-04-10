# convert from binary to decimal
# calling method decimal() and send 0's and 1's as an argument

def binary(b):
  
  for i in b:
    if i not  in '10':
      return "Your input strint must contain only 0's and 1's"
  
  decimal = 0
  
  if b == '0':
    return (0)
  if b == '1':
    return (1)

  m = 2**(len(b)-1)
  for x in b:
    if x == '1':
      decimal +=  m
      m //= 2
    elif x == '0':
      m //= 2
  return (decimal)

print(binary('10011'))
