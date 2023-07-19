# Binary Trees
A binary tree is a data structure where each node has two children and each element in the tree can only have two children.
## Introduction to Binary 
Take a look at the image below from [geeksforgeeks](https://www.geeksforgeeks.org/introduction-to-binary-tree-data-structure-and-algorithm-tutorials/)
<br><br>
<img src = "images/binary_tree.png">
<br><br>
The node at the very top of the binary tree is called the root. If a tree is empty the root will be NULL. Binary trees have the following part: data, a pointer to the left child and a pointer to the right child. In this image the root is represented by the number 1. The children of the root are 2 and 3. In binary trees the end nodes are called leaf nodes and in this example they are the numbers 4, 5 , 6 and 7.

|Common Operations|
|:----------------:|
|Inserting elements|
|Reoving elements|
|Searching for an element|
|Deleting an element|
|Traversing|

|Other Operations|
|:---------------:|
|Finding the height of a binary tree|
|Finding the level of the tree|
|Size of the entire binary tree|

## How Binary Trees work


## Real world applications
Binary trees are used in many applications including but not limited to:
- Compilers/ Expression Trees
- Data compression algorithmns
- Priority Queue
- Hierarchial data
- Editing software like Microsoft Excel or Google's sheets
- Finding elements
- Memory allocation in computers
- Performing encoding or decoding operations
- Organizing and retrieving data from large data sets.

### Advantages of Binary Trees
- Efficient Searching: Binary search algorithms perform in O(log n) time complexity. Since each node has at most two child nodes it can quickly search for an element.
- Ordered traversal: The structure of a binary tree lends itself to be traversed in a specific order.
- Memory efficient: Since each node requires two pointer per node they are memory efficient which makes it a good choice for storing large amounts of data in memory while still allowing efficient search operations.
- Fast insertion and deletion: If the developer needs dynamic data structures for example in the use of databases then the time complexity of O(log n) is ideal for speedy insertions or deletion of elements.
- Easy to implement: Binary trees are not complicated to understand and because of this they are popular data structures and implemented in a variety of ways.  
- Efficient sorting: Developers can implement efficient sorting algorithms to quickly sort data.

### Disadvantages of Binary Trees
- Limited structure: Since each node is limited to no more than two child nodes can limit there usefulness.
- Space inefficiency: Binary trees can be inefficient again due to the limitation of each node having no more than two child nodes and needing two pointers for each node. This can eat into memory.
- Unbalanced trees: If a binary tree is unbalnced by having one subtree larger than the rest can result in ineeficient search operations.

## Example problems
[Binary Tree Examples](/python_data_structure_tutorial/examples/example_binary_tree.py)
## Practice problems