from emoji import emojize

def main():
    string = input("Input: ")
    result = emojize(string,language='alias')
    print(f"Output: {result}")

main()
