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

#numbers = [1,1,1,2,3]

#numbers.append(100) #if we wanna add new element to our list

#numbers.insert(2, 100) #if we wanna replace element in a list we need for first parameter add index of element that we wanna reaplce and second parameter is new element that we place instead old one

#numbers.extend([1,2,3]) #if we wanna add a couple of elements in our list then use this method

#numbers.sort() #placing elements by their digital size

#numbers.reverse() #swaps elements

#numbers.pop() #deletes element by their index

#numbers.remove(1) #removes that element what you wanna to, by their value

#numbers.clear() #deleting all elements from the list

#numbers.count(1) this method count how many elements in your list that u wanna to know

#len(numbers) #this method showing lenght of your list

#EmptyList = [input("Enter Your data: "),input("Enter Your data: "),input("Enter Your data: ")]

#print(EmptyList)

#n = int(input('Enter your list lenght: '))

#user_list = []

#i = 0
#while i < n:
   #string = 'Enter element: ' + str(i + 1), ": "
  # user_list.append(input(string))
 #  i += 1

#print(user_list)

#string = 'henersy'.upper() # this method make letters in upperCase

#string = "HENERSY".isupper()/isLower #Checking is that string in upperCase

#string = "heNersy".capitalize() # this method capitalize first letter of a word and mekes other letters to lowerCase

#string = "Henersy".find("r") #This method finds leter which you wanna to and shows its index

#string = "Henersy,domination,cowboysFromHell"# This Method splits words with symbol which we want to use as a marker where we wanna to split

#music = string.split(',')

#for i  in range(len(music)):

 # music[i] = music[i].capitalize()

#result = ', '.join(music) #joining splitted words with each other with sighn that we use join method for

#string = "Henersy"

#print(result)

                            #indexes and cuts

#index - element designation by its order
#cuts - this is the mechanics of indexes with which we can highlight a certain segment of what we want to output
#example:
#sport = "Basketball"
#print(sport[0:5:3]) #[1 - from what index we wanna start: 1 - with what index we wanna end: 1 - how many elements we wanna skip from start ]

#lis = [2,3, 'hey', 6.7]

#print(lis[0:3:2])


                          #cortages(tuples)

#tuple - like list but without posibility of change it

#tup = (1,2,3,4,5)

#tup[0] = 3 #we cant do this

#print(tup)

#array = [1,2,3,4]

#new_tuple = tuple(array) #we can change list to tuple but cant change tuple to list

#hey = 1,2,3 #also we cant make tuple without any brackets


                          #dictionary

#syntax - randomWord = {key to some data : some data }

#country = {'code': 'UA', 'name': 'Ukraine', 'population': 40}

#print(country['name'])


                          #dictionary function

#country = dict(name = 'Ukraine', code = 'UA', population = 40) # dict function makes new dictionary

#print(country['name'])

#for key, value in country.items() :

 #  print(key, ' - ', value)

#print(country.get('code')) #get function gets value from the key

#print(country.clear()) #clear function clears dictionary

#print(country.pop('code'))

#print(country.popitem())

#country.keys() key function output is key

#country.values() value frunction output is value

#country.items() item function output is tuple that included key and value

#HOW TO UPDATE THE VALUE?

#country['name'] = 'Potuzhnostan'

#user_list = {
	#'user_1': {
	#	"first_name": "John",
	#	"last_name": "Wick",
	#	"age": 35,
	#	"living": ("Zhytomyr", "Peremoga street", 45),
 #  },
#	 "user_2": {}
#}

#print(user_list["user_1"]['living'][0])

                         #set and frozen set

#/// set

#set - its like list but elements located in random order and they cant be the same

#set_l = {5,6,7,2,4,3,5,5,6,7}

#we can add some elements,delete some element and add new lists in set with: add,remove,update

#print(set_l)

#set_list = [1,2,3,4,2,2,11]

#set_list2 = set(set_list) #with set frunction we can make set

#print(set_list2)

#/// frozenset #this is like set but we cant update,add or delete something like in tuples

#list = [1,2,3,3,3,2,2,1,4,5,6,6,6]

#rozen = frozenset(list)

#print(frozen)


                       #Functions

#def test_func(el):
#	print(el, end='')
#	print("!")

#test_func('YO')

#def algorithm(a, b):
#	res = a + b
#	return res

#result = algorithm(5,4)

#print(result)

#def minimal(l):
    #min_number = l[0]
    #for el in l:
   #     if el < min_number:
  #          min_number = el

 #   print(min_number)


#numbers = [3,1,4,5,6,4,8]

#minimal(numbers)

#func = lambda x, y: x + y #anonimous function

#func(4,5)

                              #Work with files




#data = input('Enter data: ')

# file = open('data/text.txt', 'r') #opne function creates new file with 1 argument is locations of gile and second is how we want ot work with file. w - we want add something in file and with restarting we clear file, a - we adding information without clearing file, r - read file


#file.write(data)

#
#
# print(file.read()) #read function is for reading file in argumnets it accept how many symbolt we need to output

#for line in file:
#	print(line)

#file.close()



                       #exeption handler (try,exept)

#exeption handler - like if else but with exepot function u can avoid fatal errors

#try:
#	x = int(input("Enter number: "))
#except ZeroDivisionError:
 #   print('division zero!')
#except ValueError:
 #     print("enter number please!")
#finally:
#      print('Finally!')