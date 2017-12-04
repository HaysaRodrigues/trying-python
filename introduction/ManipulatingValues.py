# Concat strings

print('lo' + 've')

# Keep values in a var

spam = 40
print(spam)

# concat the var
foo = 'love'
mix = 'strings'

print(foo + mix)

# changing the value of foo
foo = 'bar'
print(foo)

# ---------------------------------------- #
# https://www.python.org/dev/peps/pep-0008/
# ---------------------------------------- #

# In python you can use the operator * with strings

foo = 'bar'
print(foo * 10)

# in python if you want to concat a string with a integer you have to:

print(str(29) + ' <-- This is a string with an integer.')
print(float(3.99))
print(int(-99))

# sum up two integer
print(int(8) + 87)

# if I want to get some value from user and do some math operation

print('Tell me the number: ')
myInt = input()

myInt = int(myInt)

sec = myInt + 2

print(sec)

# to round up some value
print(round(5.8787878787, 2))



