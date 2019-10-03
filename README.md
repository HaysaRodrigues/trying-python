# Trying Python :snake:

This repository has the intent of keep all my routine of studies about Python. 

To do this I am following the instructions of the book [Automate Boring Stuff Python Programming](https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994) by Al Sweigart.
The book is awesome! But it worth to remember that this repository it's just about the way I have been arranging my studies based on book's samples.

You can find more about the book:
[Automate Boring Stuff Python Programming web site](http://automatetheboringstuff.com/)

**How this repository is organized**:

1. [applications](https://github.com/HaysaRodrigues/trying-python/tree/master/applications): samples of applications made in python, all done following the book Automate Boring Stuff Python Programming mentioned before.

2. [introduction](https://github.com/HaysaRodrigues/trying-python/tree/master/introduction):
Basic concepts of python, Hello World, Math Operations, manipulating values.


---
 
#### Basics 

* `print "Hello, Python!"`

* Reserved words: `and, exec, not, assert, finally, or, break, for, pass, class, from, print, continue, global, raise, def, if, return, del, import, try, elif, in, while, else, is, with, except, lambda, yield`

* There is no braces to indicate blocks of code, this is defined by line indentation.

* Python accepts single ('), double (") and triple (''' or """) quotes, as long as it starts and ends with the same.

* Comments are made using `#` or `'''`

`#this is a comment`

`''' this is a comment '''`


#### Variables

```
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

```

* python also allows you to assign a single value to several variables simultaneously:

``` a = b = c = 1 ```

* :warning: Python has five standard data types: `Numbers, String, List, Tuple, Dictionary`

##### String

```
str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string

```

#### Lists

* In python a list can be of different data type. The values can be accessed using the slice operator ```[] and [:]

* The plus sign (+) is the list concatenation and the asterisk is the repetition operator (*).

```
#!/usr/bin/python

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists

```

#### Tuples

* A tuple is another sequence data type that is similar to the list. It consists of a number of values separated by commas and however enclosed within parentheses.

* So the main difference between a list and a tuple is that list are enclosed by brackets [] and their elements and size can be changed, while tuples are enclosed in parentheses () and cannot be updated. Also, tuples can be also read-only.

```

#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists

```

#### Dictionary (also known as dict)

* Python's dictionaries are kind of hash table type. It consists of key-value pairs.  

* Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).

```
#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

```

