# Stacks
## What are stacks?
The simplest explanation of what a stack is think of it as a line for an amusemant park ride. When some one decides to stand in the line there is a designated spot where they are "added". Normally in this situation is the back of the line and the person at the front of the line is the first person to get on the ride or "removed". This is easy to comprehend because we deal with lines often in our lives for example standing in line at the checkout at your local grocery store and stacks are just like that except When you add a value to the stack it is placed at the **"top"** of the stack and when you **remove** a value it is removed from the top.

The text book definition of a stack is as follows: "A stack is a **linear data structure** in which insertions and deletions are **allowed only at the end**. This is called the **top of the stack**. 

A popular way to remember this concept is the acronym **LIFO** which stand for **"Last In, First Out"** because of this you have to consider if a stack is the right data structure for what you need to accomplish, so a stack may not be the best solution.

## How stacks work
Take a look at the diagram below from [GeeksforGeeks](https://www.geeksforgeeks.org/introduction-to-stack-data-structure-and-algorithm-tutorials/#).
<br><br>
<img src="images/stack.drawio2.png">
<br><br>

In this diagram you can see that value **"C"** was added by using the common stack operation of **push()** to the top of the stack and when a value was removed **pop()**it was the last value added of **"C"**. Now  lets review a different scenenario, lets say we want to **pop()** value **"B"** from the stack that just had the value of **"C"** added then we would need to **pop()** the value C first then B since we can only remove the last value added to the stack. 

A good analogy for how a stack works is, say you have a can of pringles (chips that are packaged in a can instead of a bag) and you want to eat a single chip then by design you are forced to eat the top chip in the can and if you wanted to eat the 4th to the last chip you would need to eat the top chip, 2nd to last and 3rd to last before you can eat the 4th to last chip.

That is how a stack works in a nut shell; however, there are other common operations that you can use in a stack for example:

| Operation | What it does |
| :-------: | :----------- |
| push()    | Inserts a value to the top of the stack.|
| pop() | Removes a value from the top of the stack.|
| top() | Returns the value at the top of the stack.|
|isEmpty() | Returns true if stack is empty of false if not.|
|size() | returns the size of the stack |

## Real world applications
Since the main reason to use a stack is to easy access and remove the most recently added element in a stack, there are some useful situations that it can be used.

1. Back and forward buttons on a web browser:

It is very handy when building websites to be able to go back or foward in between pages. This can be accomplished by creating a stack for **Back** which can be used to track any links in a previously visited page and a stack for **Forward** to track any links to a page we are navigating away from.

1. Undo or Redo functionality:

In a text editor like Microsoft Word it is very useful to have the functionality to undo or redo something the user has changed in a document. This can be accomplished similarly be creating a stack to **Undo** something that was just added to the stack and a **Redo** stack to put back what was just undone from the document.

1. Memory management for computer programming:

A stack can be used to manage the memory allocation or to track which memory blocks are being used.

1. Delimeter checking:

Using a stack data structure can be used to keep track of specified delimeters while a string is being parsed.

1. Recursion in programming:

Recursion is a technique that is used by developers to have a function to call itself.

## Example Problems
Click on the link below to see examples on how to use a stack
[Stack](/python_data_structure_tutorial/examples/example_stack.py)
## Practice problems