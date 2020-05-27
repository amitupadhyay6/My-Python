# 1-> Let's take string as user input

str = input() # Let's give "Hello World"

print(str)


# In[ ]:


str


# In[ ]:


type(str)


# # 2-> Let's take integer as user input

# In[ ]:


num = input() # Let's give 9


# In[ ]:


type(num)


# As you can see by default Python take user input as String , henc we need to explicitly define the object type.

# In[ ]:


num = int(input()) # let's give 9


# In[ ]:


num, type(num)


# # 3-> Let's take Float as user input  (Same way as Integer)

# In[ ]:


fl = float(input()) # let's take 4.5


# In[ ]:


fl, type(fl)


# In[ ]:


f = float(input()) # Let's give int, it will be converted to float, Vice verse is not possible check after this.


# In[ ]:


f, type(f)


# In[ ]:


m = int(input()) # if you define it as integer and pass the value as float, interpreter will flash the error


# # 4-> Other way to get the int and float values

# In[ ]:


x = input() # let's give 3


# In[ ]:


x, type(x)


# In[ ]:


x = int(x)


# In[ ]:


x, type(x)


# In Same way we can do for float as well

# In[ ]:


#Note - You can not convert int/float to string.


# In[ ]:


y = str(x)


# # 5-> Let's take multiple string values in single row

# In[ ]:


x,y,z = input().split()


# In[ ]:


x,y,z, type(x), type(y), type(z)


# Split("value") is a string function which split the string on value provided, by default it take " " or Space

# In[ ]:


str = "Amit#Upadhyay"
str


# In[ ]:


str = str.split("#")


# In[ ]:


str, type(str), str[0], type(str[0]) # 3rd item is 1st value in the list and 4th item is type of that value


# Split Function split the string and gives you the list of the strings

# In[ ]:


str = "2 3 4 5 6"
str, str.split()


# # 6-> Let's take multiple int/float in single row

# In[ ]:


n, m = int(input().split()) # let's take 3 4


# As we saw it earlier that output of the split is list, so you can't have list as input, it expect string or float

# # Map() Function in Python

# The map(function, iterables) function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.

# Let's use int() function and iterable as list (The output of split will be list)

# Function : Int()

# Iterable : input().split() # It will return list, which is iterble

# In[ ]:


x, y, z = map(int, input().split()) # let's take 3,4, 5


# In[ ]:


x,y, z, type(y)


# In the same we can do for float

# # 7-> Let's take input in the list

# In[ ]:


# Let's make list of string


# In[ ]:


mylist = input().split() # let's take "I am Amit Upadhyay"


# In[ ]:


mylist


# In[ ]:


type(mylist)


# In[ ]:


# Let's make list of int/float, 


# In[ ]:


numlist = map(int, input().split()) # let's take 2 3 4 5 6 7


# In[ ]:


numlist, type(numlist)


# map object is returned by map() function, you can see in above output that type is map

# No big deal, let's convert this into list in a same way as we converted the string into int using int()

# In[ ]:


numlist = list(numlist)


# In[ ]:


numlist, type(numlist)


# In[ ]:


#let's check the type of it's member


# In[ ]:


type(numlist[3])


# We can combine the map and conversion in single line, by calling the map() function in list() function

# In[ ]:


numlist = list(map(float, input().split())) # let's take 2.2 3 4 5 66


# In[ ]:


numlist, type(numlist), type(numlist[3])


# In[ ]:


# Slicing - You can slice the list or string using [Starting_From:Till_here], Till_here index will not be included


# In[ ]:


n = [2,3,4,5,6]


# In[ ]:


n[:] # It will print all 0 to last


# In[ ]:


n[2:] # from second index to last


# In[ ]:


n[:3] # from 0 index to index 3


# In[ ]:


n[2:4] # from 2 index to index 4


# In[ ]:


n[-1:] # from index -1 (means from end) to till end of index, which is only one value


# In[ ]:


# If we are taking input in the list, if there is condtion that we need to take 5 value for the list, 
# and user gives more that can be restricted by slicing


# In[ ]:


# we need 3 value for the list
n = 3


# In[ ]:


mylist = list(map(int, input().split()[:n])) # let's give 2 3 4 5 6 7


# In[ ]:


mylist, len(mylist), type(mylist), type(mylist[2])


# In[ ]:


# You can see the output, we have interger list with 3 members.

