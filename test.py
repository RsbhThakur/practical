# Stack =[]
# def Push(Stack,element):
#     Stack.append(element)
#     print(f"{element} successfully Pushed into Stack")
# def Pop(Stack):
#     try:
#         a = Stack.pop()
#         print(f"{a} Popped from Stack")
#     except:
#         print("No elements to Pop!")
# def Display(Stack):
#     for i in range(len(Stack)-1,-1,-1):
#         print(Stack[i],end=" ")
#         print()
# def Menu():
#     print("Welcome to menu driven program to implement stack in python!")
#     while True:
#         a = input("To Perform operations enter 1 for Push, 2 for Pop, 3 for Display, Enter for exit: ")
#         if(a=='1'):
#             a = input("Enter the element to Push into the Stack: ")
#             Push(Stack, a)
#         elif(a=='2'):
#             Pop(Stack)
#         elif(a=='3'):
#             Display(Stack)
#         else:# def Menu():
#     while True:
#         print("Welcome to menu driven program to implement stack in python!")
#         a = input("To Perform operations enter 1 for Push, 2 for Pop, 3 for Display, Enter for exit: ")
#         if(a=='1'):
#             a = input("Enter the element to Push into the Stack: ")
#             Push(Stack, a)
#         elif(a=='2'):
#             Pop(Stack)
#         elif(a=='3'):
#             Display(Stack)
#         else:
#             break
# if __name__ == '__main__':
#     Menu()
#             break
# if __name__ == '__main__':
#     Menu()

# import pickle
# def add():
#     with open('shoes.dat','ab') as f:
#         s_id = input("Enter Shoes ID: ")
#         name = input("Enter the name: ")
#         brand = input("Enter Brand: ")
#         types = input("Enter Type of the shoes: ")
#         price = int(input("Enter The Price: "))
#         dat=[s_id,name,brand,types,price]
#         pickle.dump(dat,f)
#     print("Added Successfully!")
# def display():
#     with open('shoes.dat','rb') as f:
#         while True:
#             try:
#                 print(pickle.load(f))
#             except EOFError:
#                 break
# def search(s_id):
#     dat=[]
#     notFound=True
#     with open('shoes.dat','rb') as f:
#         while True:
#             try:
#                 dat.append(pickle.load(f))
#             except EOFError:
#                 break
#     for i in range(len(dat)):
#         if(dat[i][0]==s_id):
#             print(f"The details of shoes with shoe ID: {s_id} is {dat[i]}")
#             notFound=False
#         elif(i==len(dat)-1 and notFound):
#             print("No Record with that ID!")

# def Menu():
#     print("Welcome to menu driven program to store the shoes data!")
#     while True:
#         a = input("Press 1 for adding record, 2 for displaying, 3 for searching details by shoe id and enter for exit: ")
#         if(a=='1'):
#             add()
#         elif(a=='2'):
#             display()
#         elif(a=='3'):
#             s_id = input("Enter shoe ID to search: ")
#             search(s_id)
#         else:
#             break
# if __name__ == '__main__':
#     Menu()