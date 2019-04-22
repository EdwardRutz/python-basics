# Introducing Lists 

>Lists are a data type that allows multiple ordered values to be stored in a single container.

## Overview

- Common use cases of lists
- Manipulate lists through appending, extending, concatenating and removing
- Iterate values
- Multidimensionality


---------------------------------------------


## 1. Meet Lists

- A List Literal is surrounded by brackets, "[ ]"
- Create a new list with an open/closed bracket, ` []`
- Find how many items in a list, `len[list]`
  - ` number_of_items = ___(["apple", "banana", "cherry"]) `

```python
languages = ["C#", "Ruby", "Swift"]
len(languages)	# 3

banner = list("Congratulations")
```

- Lists can store any data type

- Lists are mutable. They can be changed.
- List methods do not return a new list, they modify the existing list.
- Strings are immutable, they cannot be changed. 
- String methods return a brand new string entirely, because you can't change them. 
- Add to a list, `.append()'
- Extend a list by adding a different list to it, `.extend()`


```python
temperatures = []
temperatures.append(98.6)
temperatures.append(99.4)	
print(temperatures)		#[98.6, 99.4]

er_temps = [102.2, 101.1, 99.9]
temperatures.extend(er_temps)	#Extend the list with er_temps

primary_care_doctors = ["Dr. Scholls", "Dr. Pepper"]
er_doctors = ["Doug", "Susan"]
all_doctors = primary_care_doctors + er_doctors 	#concatenate two lists
print(all_doctors)
```

- Add Paul to the beatles list
- Show the two lists together

```
beatles = ["John"]
others = ["George", "Ringo"]
beatles.append("Paul")
beatles.extend(others)
```
### Indexing in Python

- `python -i wishlist.py`, opens python REPL
- Zero (0) is the first item on a list
- The last item in a list is negative one, -1
- Insert at beginning list, `.insert(0, "Leaning Python")`
- Lists are mutable, but strings in list are immutable
- You can access a specific character on a String by using an index, but you cannot change it.


```python
books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested gift: {}".format(books[0]))
books.insert(0,"Learning Python")

lyrics = "Books, check 'em out!"
lyrics[0]		#'B'
```

### Deleting Items from a List

- List indecies act as labels
- Del deletes the label and not the object
- Garbage collection removes items without a label
- Garbage collection or collection is a form of automatic memory management
- Collection reclaims memory from objects which are no longer being used.
- [Unicode in Python](https://docs.python.org/3.6/howto/unicode.html)
- [Wikipedia: Garbage Collection](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science))


```python
my_lunch = "\N{TACO
print(my_lunch)
carne_asada = my_lunch
del my_lunch
```

- Remove the last item on a list, `books.pop()`
- Remove specific items, `books.pop(0)

```python
classics = [
    "The Mona Lisa",
    "Starry Night",
    "The Scream",
    "Guernica",
    "The Persistence of Memory",
]

painting = classics.pop()
print(painting)

```

```python
elements = [
    "Hydrogen",
    "Helium",
    "Lithium",
    "Symposium",
    "Beryllium",
    "Boron",
    "Carbon",
]

incorrect = elements.___(__)	# pop(3)
print("{} is not an element".format(incorrect))
```

```python
options = [
    "rock",
    "paper",
    "scissors",
    "flamethrower",
]

del options[3]
print("There are {} options".format(len(options)))	# 3
```

```python
classics = [
    "The Mona Lisa",
    "Starry Night",
    "The Scream",
    "Guernica",
    "The Persistence of Memory",
]

painting = classics.pop()
print(painting)				#The Persistence of Memory
```


---------------------------------------------


## 2. Using Lists



### Interation


### Mutability



### Split and Join



### Multidimensional Lists








---------------------------------------------


## 3. Build a Shopping List Application

- A console app
- [Github: shopping-list](https://github.com/EdwardRutz/shopping-list)

### User Stories

- As a user, Contually be prompted to add an item to list if needed
- User, Provide help to user
- As a user, I should be able to add an item to the list
- User, keep track of the length of the list
- User, be able to look at the list anytime and verify order
- User, state when done, print out entire list

## App



---------------------------------------------

## Python List Methods

-  Add to a list, `.append()'


## Python REPL Easter Egg

- Easter egg, in the Python REPL type, `import this `

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!



## Sources

- https://teamtreehouse.com/library/introducing-lists
- https://www.w3schools.com/python/python_lists.asp
- [Unicode in Python](https://docs.python.org/3.6/howto/unicode.html)
- [Wikipedia: Garbage Collection](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science))

