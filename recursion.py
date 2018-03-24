def loopN(n):
    ct = 0
    while ct<n:
        print("Hello World")
        ct = ct +1

loopN(4)

print('- ' * 20)
    
def loopRecursiveN3(n):
    if n==0:
        print("Finished")
    else:
        print("Hello")
        print("World")
        loopRecursiveN3(n-1)

loopRecursiveN3(4)
