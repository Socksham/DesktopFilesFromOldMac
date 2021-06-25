x = 0
final = 2
fibonacci = [1, 2]

while fibonacci[-1] < 4000000:
    fibonacci_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(fibonacci_number)
    x += 1
    if(fibonacci_number % 2 == 0):
        final += fibonacci_number
    
print(final)
