def HelloWorld(n):
    if n == 0:
        return
    
    HelloWorld(n-1)
    print('HelloWorld')

a = int(input())
HelloWorld(a)