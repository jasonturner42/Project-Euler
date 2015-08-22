#Fibonacci number generator

sequence = [1,2]   #create list with first two Fibonacci terms

def fib(limit):  #define a function to generate the sequence, with argument as the maximum in sequence
    first = 1
    second = 2
    while first + second < limit:
        next = first + second
        sequence.append(next)
        first = second
        second = next

fib(int(raw_input('Please enter the upper limit of your requested sequence: ')))

even_count = 0   #initialize variable to hold sum of even Fib numbers under given maximum

for x in range(len(sequence)):    #loop to sum the even Fib numbers
    if sequence[x] % 2 == 0:
        even_count = even_count + sequence[x]

print sequence
print "Sum of the even numbers is:"
print even_count









