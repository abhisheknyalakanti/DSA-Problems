class stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return len(self.stack)==0
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()
   def peek(self):
       if self.isEmpty():
           raise IndexError("peek from an empty stack")
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("stack elements(from top to bottom):")
            for item in reversed(self.stack):
                print(item)
stack=Stack()
while True:
    print("/nstack operations")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.check if stack is empty")
    print("5.get size of stack")
    print("6.display stack")
    print("7.exit")
    choice=input("enter your choice(1-7):")
    if choice=='1':
        item = input("enter item to push onto stack:")
        stack.push(item)
        print("item",item,"pushed onto the stack")
   elif choice=='2':
       try:
           item=stack.pop()
           print("popped item:",item)
      except IndexError:
          print("stack is empty.cannot pop")
    elif choice=='3':
        try:
            item=stack.peek()
           print("top item on the stack:",item)
      except IndexError:
          print("stack is empty")
    elif choice=='4':
        if stack.isEmpty():
            print("stack is empty")
        else:
            print("stack is not empty")
    elif choice=='5':
        print("size of stack:",stack.size())
    elif choice=='6':
        stack.display()
    elif choice=='7':
        print("exiting program")
        break
    else:
        print("invalid choice.please enter  number between 1-7")
              
       
    
    
