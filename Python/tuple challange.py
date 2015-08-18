__author__ = 'luke'
# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.


def combo(list1,list2):
  to_return = []
  for step in enumerate(list1):
    a = list2[step[0]],step[1]
    to_return.append(a)
  return to_return

print combo(['swallow', 'snake', 'parrot'], 'abc')