#this little program creates a Fibonacci Sequence and asks you which number in the sequence you need

fibo = [0,1]
def fibor(fibo):
    for each in range(2,1000):
        fibo.append(fibo[each - 2]+fibo[each - 1])

fibor(fibo)

usernumber = int(input("Which Fibonacci Sequence number do you need? "))

print(fibo[usernumber])


