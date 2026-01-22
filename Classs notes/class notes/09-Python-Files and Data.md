# Files and Data

18 November 2025

## Files
For this section, we'll learn how to open and read text files.
when we open files, we need to consider the location
or **path** to the file.
The **path** to the file is the direction we take to get to the file.
Included in a path, is the **file's name** and the folder that it lives in.

### Opening Files
To open a file, we use he `open()` function The `open()` function
returns a **file object**. A **file object** represents a **file stream**
which is like a pipe that connects our python file to the external file.

```python
# information.txt is a file that we want to open
file =open("information.txt")
```

### Reading their contents
When reading the contents of a file, you recievve the first line of data,
then the second, ..., all the way to the end.
Use the `.readline()` method to read one lne of information.
If you call it again, it will give you the next line of information.
```python
# omitted code above
first_line = file.readline()		#string
first_line = file.readline()
```

If you wat to read all lines of the fie, **iterate over the file**
```python
 # omitted code above
for line in file:
	# do something with the line
	print(line)		# line is a string
```
### Managing File Streams
When we open up a file stream, we should always close it after
we've finished reading/writing any info. This helps to lower the risk 
of corrupting any data in the file. To close a file stream, we use the
`.close()` metthod.
```python
# omitted code above 
file.close()		# closesthee stream safely
```

An alternate way to open/ close files is to use the `with` keyword. `with`
helps us create these things described as closures.
```python
# the file is information.txt
with open("information.txt") as file:
	line = file.readline()
	for line in file:
		print(line)

file.readline()		# this would break
```

## Lists

Lists are a type of data in storing more than one 
piece of information that is related. with lists, order matters. To
create a list, we use `[]`.
```python
# create an empty list
some_list = []
```

### Convert a string to a list
There are times when we want to get information from a string.
One use case when this is important is the example of a 
`.csv` or comma-seperated values file.

```csv
Name,Age,Favourite Superhero		
Coco,67,HK
...
Batman,38,Batman
```

```python
# As a string, the second line would be
info = "Coco,67,Batman"
#Split the string whenever there is a ,
info_list = info.split(",")		#["Coco", "6.7", "HK"]
```

### Accessing Specific Items in a List

To access a specific elemet inside the list, we use `[]`
bracket notation. We give the **index** of the item, which
is like the address of the item. **Indices** are always integerrs.

```python
# omitted code above
# 		   0	  1      2
# info_list -> ["Coco", "67", "HK"]
# Access Coco's age -- index = 1
print(f"Coco's age is {info_list[1]}.")
# Access Coco's fave superhero -- index = -1
print(f"Coco's fave superhero is {info_list[-1]}.")

```

