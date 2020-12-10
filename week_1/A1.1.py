# Task 1: Define a function to print a string diagonally...

name = input("Enter your name: ")
spaces=""

for i in name:
    print(spaces,i)
    spaces+=" "

# Try printing in reverse diagonal...

# def pattern(str, len):
     
#     # i and j are the indexes 
#     # of characters to be 
#     # displayed in the ith 
#     # iteration i = 0 initially 
#     # and go upto length of string
#     # j = length of string initially 
#     # in each iteration of i, we 
#     # increment i and decrement j,
#     # we print character only of
#     # k==i or k==j
#     for i in range(0, len):
     
#         j = len -1 - i
#         for k in range(0, len):
         
#             if (k == i or k == j):
#                 print(str[k], 
#                       end = "")
#             else:
#                 print(end = " ")
         
#         print(" ") 
 
# # Driver code
# str = "Ebad Shahid"
# len = len(str)
# pattern(str, len)