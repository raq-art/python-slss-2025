# Numbers and Operations

5 November 2025

## Data Types So Far

| Data type			| Name		| example 		|
|  ---				| ---		|---
| String			| `str`		| `"Mr. Coco"`|
| Boolean			| `bool`	|`True` `False` |
| **Integer**		| `int`		| `1` `2` `-100`|
| **Float** 		| `float` 	| `1.0` `-2.3`|
| Dctionary 		| `dict`	| `{"key": "val",}` |

## Operators that work on Numbers

### Addition and Subtraction

```python
sum =  1 + 1			# 2
diff = 10 - 8			# 2
another_sum = 1 + 1.0	# 2.0
```

### Mulitiplication and Division

```python
product = 8 * 8			#64
answer = 10 / 2			#5.0
```

### Order of Operations

```python
# BEDMAS - Brckets, Exponents, Div/Mult, Add/Sub

answer = (2 + 3) * 4 + 2 / 3
```

### Cool Other Operations

```python
# Exponents
ans = 3 ** 2 		#9
# Floor Division
ans = 10 // 3		# 3
# Modulo
ans = 2 % 2		# r0
ans = 3 % 2		# r1
ans = 4 % 2		# r0
ans = 5 % 2 		# r1

# Incremet, Decrement, Mult-rement, Divide-rement
#Update the value of a variable
egg_count = 1
egg_count += 1		# raises the value of the egg count by that number
egg_count -= 1		# decreases the value 
egg_count *= 5		# multiplies the value 
egg_count /= 2		# halves the value

```

##  Loops Again
Recall:

```python
# Repeat something 10 times
for _ in range(10):
	print("This will be printed 10 times")
```

Iterate over a *sequence*.
```python
grocery_list = [
	"cucumbers", 
	"eggs", 
	"hot wheels", 
	"tea"
]

# Print out a pretty version of the list
for item in grocery_list:
	#Create a bulleted list and print it out
	bulleted_item = "* " + item
	seperator = "-------"
	print(bulleted_item)
	print(seperator)
```
Output:
```
* cucumbers
-------
* eggs
-------
* hotwheels
-------
* tea
-------
```



