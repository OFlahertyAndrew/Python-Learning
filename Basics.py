#Text Type:	        str
#Numeric Types:	    int, float, complex
#Sequence Types:    list, tuple, range
#Mapping Type:      dict
#Set Types:	        set, frozenset
#Boolean Type:	    bool
#Binary Types:	    bytes, bytearray, memoryview
#None Type:	        NoneType

#Use these types to typecast. Ex: str(58) -> "58"

#Function definition
def function():
    print("Function was called!")

#Function call
function()

#Initialize multiple variables to the same value
abc = abcd = abcde = "Hi!"

#Use type(variable) to get the type for a variable
print("ABC's Type: " + str(type(abc)))

#List initialization | Collection of oredered data | Mutable
list_example = ["apple", "banana", "cherry"]
list_example2 = ["hello",1,4,8,"good"]
list_example.append("strawberry") #The append() adds a single item to the end of the list, without modifying the original list
list_example.pop(2) #The pop() method removes the item at the given index from the list and returns it.
list_example.pop() #The pop() method removes the last item from the list and returns it.
print(list_example)

#Tuple initialization | Ordered collection of data | Immutable
tuple_example = ("apple", "banana", "cherry")
tuple_example2 = ("good",1,2,3,"morning")
#Tuples do not have append(), add(), update(), or pop() methods due to them being immutable
print(tuple_example)

#Dict initialization | Unordered collection of data that stores data in key-value pairs | Mutable, keys do not allow duplicates
dict_example = {"name" : "John", "age" : 36}
dict_example2 = dict1={"key1":1,"key2":"value2",3:"value3"}
print(dict_example)
print(dict_example["name"]) #Prints John

#Set initialization | Unordered collection | Mutable, has no duplicate elements
set_example = {"apple", "banana", "cherry"}
set_example2 = {1,2,3,4,5}
set_example.add("strawberry") #The set add() method adds a given element to a set at a random position
set_example.pop() #The pop() method removes a random item from the set
print(set_example)

#Frozen Set initialization | Unordered collection | Immutable, has no duplicate elements
#Essentially, just a set that cannot be changed once initialized
frozenset_example = frozenset({"apple", "banana", "cherry"})
#Frozen Sets do not have append(), add(), update(), or pop() methods due to them being immutable
print(frozenset_example)

#For loop with range. Starts at 0 and goes to 2
for i in range(3):
    print(i)
    #Output:
    #0
    #1
    #2

int_example = 1 #Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length
float_example = 10.003 #Float, or "floating point number" is a number, positive or negative, containing one or more decimals
#Float can also be scientific numbers with an "e" to indicate the power of 10
complex_example = 1j #Complex numbers are written with a "j" as the imaginary part
complex_example2 = 3 + 5j

#Random numbers
from hashlib import sha3_224
from operator import truediv
import random
random_example = random.randrange(1,10) #Generates a random number between 1-9
print(random_example)

#Use 3 quotes to assign a multi-line string, you may also use 3 single quotes
multiline_string = """Hello
There
How
Are
You"""
print(multiline_string)

#Strings are arrays, and therefore can be treated as such
string_example = "Hello, world!"
print(string_example[3])

#Strings can be looped through
for x in "Hello there, old friend.":
    print(x)

#Print string length
print(len(string_example))

#To check if a certain phrase or character is present in a string, we can use the keyword in
print("world" in string_example) #Returns true, since the string IS in the string_example
print("hi!" not in string_example) #Returns true, since the string IS NOT in the string_example
if "hi!" not in string_example:
    print("hi! IS NOT in the string_example variable")

#Get the substring (characters) from position 2 to position 5 (not-included)
print(string_example[2:5]) #Output: llo
#Get the characters from the start to position 5 (not included)
print(string_example[:5]) #Output: Hello
#Get the characters from position 2, and all the way to the end
print(string_example[2:]) #Output: llo, world!

#Use negative indexes to start the slice from the end of the string
#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
print(string_example[-5:-2])
print(string_example[-8:-1:-2])

my_string = "0123456789"
print(my_string[-2: -6: -2])
#Prints 86 -> -2 is inclusive (8 inclusive), -6 is exclusive (4 is exclusive), and the step is -2 (every other element going left)

s1 = True
s2 = False

s1 = s1 | s2 #OR operator
s1 |= s2 #Rewritten version
print(s1) #True

s1 = s1 & s2 #AND operator
s1 &= s2 #Rewritten version
print(s1) #False

s1 = s1 ^ s2 #XOR operator, true if ONLY one of these is true. "Exclusive OR"
s1 ^= s2 #Rewritten version
print(s1) #False

