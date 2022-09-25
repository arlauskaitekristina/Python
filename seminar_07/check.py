import function


def check(data):
    match data[1]:
        case '+':
            return function.sum(data[0], data[2])
        case '-':
            return function.minus(data[0], data[2])
        case '*':
            return function.mult(data[0], data[2])
        case '/':
            return function.dev(data[0], data[2])
        case _:
            print("Wrong equation sign!")
            return "Wrong equation sign!"