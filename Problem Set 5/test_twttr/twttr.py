def main():
    word = input('Input: ')
    print(f"Output: {shorten(word)}")


def shorten(word):
    format_str = word
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if len(word) == 0:
        return format_str
    count = 0
    for i in range(len(word)):
        if (word[i] in vowels):
            format_str = format_str[0:i-count] + word[i+1:]
            count = count + 1
    return format_str


if __name__ == "__main__":
    main()
