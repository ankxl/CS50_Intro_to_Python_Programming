def main():
    string = input()
    print(playback(string))

def playback(string):
    return(string.replace(' ','...'))

main()