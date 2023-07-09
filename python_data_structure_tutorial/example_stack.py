"""
    This is an example of a stack data structure. 
    We will create a stack which will be used as a backpack and we will push items into the backpack and pop items from the backpack. 
    We will also check the top of the stack, check if the stack is empty and check the size of the stack.
"""
#Create a stack using a list.
def stack():
    stack = []
    return stack

#Create function to push items into the stack.
def push_item(stack, item):
    stack.append(item)
    print(item)

#Create function to pop items from the stack.
def pop_item(stack):
    item = stack.pop()
    print(item)

#Create functions to check the top of the stack.   
def top_of_stack(stack):
    return stack[-1]

#Create function to check if the stack is empty.   
def isEmpty(stack):
    if stack == []:
        return True
    else:
        return False

#Create function to check the size of the stack.    
def size(stack):
    return len(stack)


    
    

#Now we will create a stack and call it backpack.
backpack = stack()

print("******checking if the stack is empty******")
print(isEmpty(backpack))
print("****************************************")

print()
print("******pushing items into the stack******")
push_item(backpack, 'book')
print(backpack)
push_item(backpack, 'laptop')
print(backpack)
push_item(backpack, 'pen')
print(backpack)
print("****************************************")

print()
print("******popping items from the stack******")
pop_item(backpack)
print(backpack)
print("****************************************")

print()
print ("******checking the top of the stack******")
print(top_of_stack(backpack))
print("****************************************")

print()
print("******checking if the stack is empty******")
print(isEmpty(backpack))
print("****************************************")

print()
print("******checking the size of the stack******")
print(size(backpack))
print("****************************************")


