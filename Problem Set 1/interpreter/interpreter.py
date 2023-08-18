def main():
    expression = input("Expression: ")
    print(interpreter(expression))

def interpreter(string):
    x,y,z = string.split()
    x = int(x)
    z = int(z)
    match y:
        case '+':
            return(float(x + z))
        case '-':
            return(float(x - z))
        case '*':
            return(float(x * z))
        case '/':
            return(float(x / z))

main()