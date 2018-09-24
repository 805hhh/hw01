for i in range(1,10):
    for j in range(1,i):
        print (end="       ")
    for k in range(i,10):
            print("{}x{}={:<2d}".format(i,k,i*k),end=" ")
    print(" ")
