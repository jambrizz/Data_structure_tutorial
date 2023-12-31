# Sets

## Introduction to Sets
A set is a collection of elements that is unique. This has an advantage over arrays when it comes to only
adding unique elements to a collection. This is useful when efficiency and organization is important as
well as when you want to add, remove or query an element in the set.

## How Sets work
Sets store items unordered, unchangeable and do not allow duplicate items to be inserted. Unordered means that the items do not have a defined order and cannot be referred by an index or key. Unchangeable means that once the set has been created you cannot change the items in the set. However you can remove or add items to the set.
## Real world applications
Sets are useful to store unique values to avoid duplicate data being added to a set. By default, sets
stores data in a sorted manner which is more efficient than an array. Sets are dynamic so you do not
need to worry about overflowing the set. The Big O for searching through a set is O(logN). The
implementation of a set can be accomplished using a variety of data structures including TreeSets.

### Common operations with sets

|Operation |What it does|
|:--------:|:----------:|
|add()|Adds an element to a set|
|remove()|Removes an element from the set|
|member()|Determines if an element exists in a set|
|size()|Returns the length of the set|

Set data structures are commonly used is software development in a variety of ways from algorithms, data analysis as well as in databases where their speciality of only allowing unique elements to be added to a set. They are commonly used in two ways the **Rosteer Form** and as a **Set-Builder form**. 

Other basic methods for sets are as follows:

- Union: This method is used to unite two sets using a union() function. 
- Intersection: This is used to identify common elements used by two sets where they intersect and this is accomplished by using a intersection() function or using an operator.
- Difference: This is utilized to identify the differences between two sets usina a difference() function or an operator.

### Roster Form 
Elements are inside of **"{}"** and all the elements are seperated by commas.

```python
Cars = {"volvo", "ford", "toyota", "chevrolet", "dodge"}

primeNumbers = {1, 3, 5, 7, 11, 13}
```

### Set-Builder Form
In a Set-Builder Form, elements of a set can also be a statement expressing some kind of relation with the elements.

```python
A = {y: y > 0, y: y < 8, y: y + 3 * 5}
```

## Example problems

[Set examples](/python_data_structure_tutorial/examples/example_sets.py)

## Practice problems