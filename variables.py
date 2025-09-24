


#x = 1 #int
#y = 2.5 #float
#name = 'john' #str
#is_cool = True #bool


name = 'mahou'
age = 26
# Multiple Assignment
#x, y, name, is_cool = (1, 2.5 , 'john', True)

#print(x, is_cool)
# print('my name is {name} and I am {age}'.format(name=name,age=age))
# print(f'my name is {name}, and I am {age}')

# s = 'hello world'

# print(s.capitalize())




# Create list
# numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# numbers2 = list((1, 2, 3, 4, 5))

# print(fruits[1])
# print(len(fruits))


#Add to list
fruits.append('Mangos')
print(fruits)


#remove from list
fruits.remove('Oranges')
print(fruits)

# insert into position
fruits.insert(2,'Strawberries')
print(fruits)

#remove with pop
fruits.pop(2)
print(fruits)


#reverse list
fruits.reverse()
print(fruits)

#sorl list
fruits.sort()
print(fruits)

fruits[0] = 'mahou'
print(fruits)




fruits[1] = 'ayoub'
print(fruits)
