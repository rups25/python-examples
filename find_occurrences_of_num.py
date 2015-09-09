"""
sorted_list = [5, 12, 16, 20, 20, 20, 20, 80, 70]
find_occurrences_of_num(sorted_list, 20)
return 4
"""

def find_occurrences_of_num(sorted_list, num_to_find):
  count = 0
  for i in range(0, len(sorted_list)):
    if sorted_list[i] == num:
      count += 1
  return count
  
def find_occurrences_of_num_binary(sorted_list, num_to_find):
  upper_bound_index = len(sorted_list)-1
  lower_bound_index = 0
  
  mid_index = (upper_bound_index - lower_bound_index) / 2 + lower_bound_index
  
  while (upper_bound_index - lower_bound_index)/2 != 0:
  
    if num_to_find < sorted_list[mid_index]:
      upper_bound_index = mid_index  
      mid_index = (upper_bound_index - lower_bound_index) / 2 + lower_bound_index
  
    elif num_to_find > sorted_list[mid_index]:
      lower_bound_index = mid_index  
      mid_index = (upper_bound_index - lower_bound_index) / 2 + lower_bound_index
    
    else:
      break
    
    
    
  
  
  
 
 
 
 
 
 
 
 
 
 
 
 
  mid = len(sorted_list)/2
  
  if num < sorted_list[mid]:
    x = find_occurrences_of_num_binary(sorted_list[:mid], num_to_find)

    
  
  