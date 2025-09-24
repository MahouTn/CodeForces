# courses = ['Math', 'Physics', 'DevOps', 'Upgrade']

# print(courses[:2]) #start from 0 to 2 but 2 not included
# print(courses[2:]) #start from 2 to end

# courses.append('Cloud') #add to the end of the list
# courses.insert(0, 'mahou') #add in the begining of the List
# print(courses)
# courses.remove('Cloud')
# print(courses)


# courses.reverse()
# print(courses)




courses2 = ['Math', 'Physics', 'DevOps', 'Upgrade']
for index, item in enumerate(courses2, start=1):
    print(index, item)