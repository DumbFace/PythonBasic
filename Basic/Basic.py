# print("HelloWorld")


# Array variety
# a = [1.2,"Test",2]
# print(a)


#Double Comparison
# x = 2 
# if (1 < x < 3):
#     print("true")

# for letter in 'Python': # First Example
#     print ('Current Letter :', letter) 


#While loop

# count = 0
# while (count < 9):
#     print ('The count is:', count)
#     count = count + 1
#     print ("Good bye!")


# Function

# def sum(a, b = 10):
#     return a+b

# sum = sum(1)

# print(sum)
# print("Test function")

# Cut string
# testString = "                    Hello There            u"
# numbericString = "184748374"
# hybridNumbericString = "297daa74dfef"

# print(testString[0:-1])

# Count string
# print ("Count: ",len(testString))

#Replace string 
# print (testString.lower().replace("hello","bye",1))

#Find string
# print (testString.find("e"))

#Trim strnig
# print (testString.strip())
# print (testString)

# IsNumberic String ?
# print( numbericString.isnumeric())
# print( hybridNumbericString.isnumeric())


# Array
# numbers = ['a','b','c','d']
# print (numbers[0:0])

# del numbers[2:3]

# print (numbers)

# Append

# numbers = ['a','b','c','d']
# print (numbers)
# numbers.append('e')
# print(numbers)


# Pop
numbers = ['a','b','c','d']

print(numbers)
pop = numbers.pop()

print(numbers)

print (pop)

# Find index array

# aList = [123,'xyz','zara','abc']
# print(aList)
# aList.clear()
# print(aList)
# print ("Index for xyz : ", aList.index('xyz'))
# print ("Index for zara : ", aList.index('zara'))
# print ("Index for 123 : ", aList.index(123))


#Dictionary 
point = {'x': { 'x1':1,'x2':2 },'y': 2}
print (point)
point['z'] = {'userName': 'Khang','Age' : 18, 'country': { 'a':'uncle Ho','b' : 'Ha Noi' }} 
# print(point)
# point['z'] = "'z1': {'username': khang}"
# print(point['z']['userName'])
# print(point['z']['country']['a'])


# print(point.keys())
# print(point.values())

print(point.keys('x1'))