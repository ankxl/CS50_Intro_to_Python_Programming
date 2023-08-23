def main():
    string = input('Input: ')
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    formatted_string = string
    count = 0
    for i in range(len(string)):
        if (string[i] in vowels):
            formatted_string = formatted_string[:i-count]+string[i+1:]
            count = count + 1
    print(f"Output: {formatted_string}")

main()