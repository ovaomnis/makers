print('Your number is:', numb := int(input("Enter ur number: ")),'\n' + ('FizzBuzz' if numb % 3 == 0 and numb % 5 == 0 else 'Fizz' if numb % 3 == 0 else 'Buzz' if numb % 5 == 0 else numb))