# Left to Right  Pyramid
for i in range(1,6):
    for j in range(i):
        print('*',end=" ")
    print()
    
for i in range(4,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()

print('--------------------------')

# Bottom up  Pyramid
for i in range(6,0,-1):
    for j in range(6-i):
        print(" ", end=" ")
        
    for j in range(2*i-1):
        print("*", end=" ")        

    print()


print('--------------------------')

# Top down Pyramid
for i in range(0,6):
    for j in range(6,i+1,-1):
        print(" " , end = " ")
        
    for j in range(2*i+1):
        print("*" , end = " ")
        
    print()    