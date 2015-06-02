# convert base 10 to base 3
def calculate_base3(base10_number):
  
  if base10_number == 0:
    return 0
  elif base10_number == 1:
    return 1
  else:
    quotient = base10_number
    result = ''
    
    while quotient > 0:
      remainder = quotient%3
      result += str(remainder)
      quotient = quotient/3
    return result[::-1] 

print calculate_base3(7)