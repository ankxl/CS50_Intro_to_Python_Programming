def main():
    string = input('File name: ').strip().lower()
    print(file_extension(string))

def file_extension(string):
    if string.endswith('.gif'):
        return('image/gif')
    elif string.endswith('.jpg') or string.endswith('.jpeg'):
        return('image/jpeg')
    elif string.endswith('.png'):
        return('image/png')
    elif string.endswith('.pdf'):
        return('application/pdf')
    elif string.endswith('.txt'):
        return('text/plain')
    elif string.endswith('.zip'):
        return('application/zip')
    else:
        return('application/octet-stream')

main()