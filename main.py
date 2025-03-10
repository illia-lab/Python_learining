#comment
#print(5 // 3)#ділення з заокругленням числа
#print(5 ** 2)#піднесення до квадрата
#print('Hello World', 5 , 4 ,5 , ".",)
#print("result: ", min(1,43,3,2,56,2), sep="")
#print("result: ", max(1,43,3,2,56,2), sep="")
#print("result: ", round(5/3))
#input('Введіть сві вік: ')


#/////////////

#number = 5 #int

#digit = 4.504939 #float

#word = "huhu: " #sring

#boolean = True #bool

#print(word + str(digit))

#del(number)
#print(word, boolean )
#print(number)

#str_num = '5'

#print(word + str(number + int(str_num)))


#num1 = int(input("Введіть число: "))
#num2 = int(input("Введіть число: "))

#print( "result: ", num1 + num2)
#print( "result: ", num1 * num2)
#print( "result: ", num1 / num2)
#print( "result: ", num1 - num2)

#word2 = 'hi'

#print( word2 * 2)

#if 5 == 5:
#	print("Correct") #else print("incorect")

#user_data = int(input("Enter some data: "))

#if user_data > 5 and user_data != 6:
#	print("Your number is bigger than 5")

#elif user_data < 5: ...elif - else if - optional functions(u can use it when u want add new condition withount editing any code at the start)

#	print("gugugu")

#else: print('huhuhuhuhuhu')
#data = input()

#number = 5 if data == "Five" else 0 ...ternary operator - if data equals "Five" then we will see number 5

#print(number)


                           #Cycles


#for i in range(6): #range atribute that allow you to set range with what your cycle will work
#	print(i)

#word = 'Hello World'
#countdown = 0

#for i in word:
#	if i == 'l':
#		countdown += 1

#print("count:", countdown)

#i = 5

#while i < 15:
	#print(i)
	#i += 2

#isHasCar = True

#while isHasCar:
#	if input("Введіть інформацію: ") == "Stop": isHasCar = False


                    #Cycle Operators


#for i in range(1,11):
#	if i == 5 :
#		break

#	if i % 2 == 0:
#		continue

#	print(i)

#found = None

#for i in "Hello":
#	if i == "l":
#		found = True
#		break

#	else: found = False

#print(found)

                      #lists

#nums = [5, 6, 7, 8, True, "hello", 6.7]

#nums[0] = 50

#print(nums)

#print(nums[1]) #if we wanna print only one element from list

#print(nums[-1]) #if we wanna print last element from list


                     #list methods

numbers = [1,1,1,2,3]

#numbers.append(100) #if we wanna add new element to our list

#numbers.insert(2, 100) #if we wanna replace element in a list we need for first parameter add index of element that we wanna reaplce and second parameter is new element that we place instead old one

#numbers.extend([1,2,3]) #if we wanna add a couple of elements in our list then use this method

numbers.sort() #placing elements by their digital size

#numbers.reverse() #swaps elements

#numbers.pop() #deletes element by their index

#numbers.remove(1) #removes that element what you wanna to, by their value

#numbers.clear() #deleting all elements from the list

#numbers.count(1) this method count how many elements in your list that u wanna to know

#len(numbers) #this method showing lenght of your list

#EmptyList = [input("Enter Your data: "),input("Enter Your data: "),input("Enter Your data: ")]

#print(EmptyList)

n = int(input('Enter your list lenght: '))

user_list = []

i = 0
while i < n:
   string = 'Enter element: ' + str(i + 1), ": "
   user_list.append(input(string))
   i += 1

print(user_list)