__author__ = 'luke'

# You can check for dictionary membership using the
# "key in dict" syntax from lists.

def members(dic, list_of_keys):
  count = 0
  for i in dic:
    if i in list_of_keys:
      count +=1


  return count



### Example
my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
print (members(my_dict, my_list))
