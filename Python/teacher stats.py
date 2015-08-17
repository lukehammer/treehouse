# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

def most_classes(dic):
  max_count = 0 
  for key in dic:
    classes = dic[key]
    count_of_classes = len(classes)
    if count_of_classes >= max_count:
      teacher_name = key
      max_count = count_of_classes
  return teacher_name

def num_teachers(dic):
  return len(dic) 

def stats(dic):
  to_return = []
  for key in dic:
    teacher_name = key
    classes = dic[key]
    number_of_classes = len(classes)
    to_return.append([teacher_name, number_of_classes])
  return to_return
    
def courses(dic):
    course_list = []
    for classes in dic.values:
        for course in classes:
            course_list.append(course)
    return course_list
