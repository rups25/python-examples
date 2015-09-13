def binary_search(list_of_nums, num_to_find):
  lower_bound_index = 0
  upper_bound_index = len(list_of_nums)
  mid_index = (upper_bound_index - lower_bound_index)/2 + lower_bound_index
    
  while (upper_bound_index - lower_bound_index)/2 != 0:
    if num_to_find < list_of_nums[mid_index]:
      upper_bound_index = mid_index
      # print "upper_bound_index = %s" %upper_bound_index
      mid_index = (upper_bound_index - lower_bound_index) / 2 + lower_bound_index
      # print 'mid_index = %s' %lower_bound_index
      
    elif num_to_find > list_of_nums[mid_index]:
      lower_bound_index = mid_index
      # print "lower_bound_index = %s" %lower_bound_index
      mid_index = (upper_bound_index - lower_bound_index) / 2 + lower_bound_index
      # print "mid_index = %s" %mid_index
      
    else:
      break
  
  if list_of_nums[mid_index] != num_to_find:
    return 0
  else:
    return mid_index

  
  
def find_num_occurrences(list_of_nums, num):
  mid_index = binary_search(list_of_nums, num)
  
  if mid_index > 0 :
  
    print mid_index
    left_index = mid_index-1
    right_index = mid_index+1
    count = 1

  else:
    return 0
  
  while list_of_nums[left_index] == num:
    count += 1
    left_index -= 1
    
  while list_of_nums[right_index] == num:
    count += 1
    right_index += 1

  return count
    
  
# print binary_search([2, 6, 8, 10, 15, 65, 99, 100, 110], 110)

print find_num_occurrences([1, 5, 7 , 8, 9, 20, 20, 20, 80, 90], 2)


    