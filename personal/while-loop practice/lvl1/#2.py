# Print the following patterns using loop :
# a.
# *
# **
# ***
# ****
# b.
#    *  
#  *** 
# *****
#  *** 
#    *  
# c.
# 1010101
#  10101 
#   101  
#    1 

# a.
# x = 0
# while True:
#     if x == 5:
#         break

#     print(x*'*')
#     x += 1

# b.
# x = 1
# flag = 1
# while True:
#     if x == 5:
#         flag = -1
#     if x == -1:
#         break
#     print(x*'x')
#     x+=(flag*2)

# c.
# x = '1010101'
# while True:
#     print(x)
#     x = list(x)
#     del x[-1]
#     del x[-1]
#     x = ''.join(x)
#     if len(x) == 1:
#         print(x)
#         break