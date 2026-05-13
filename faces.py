def main():
    message = input()
    message = convert(message)
    print(message)

def convert(string):
    return string.replace(':)', '🙂').replace(':(', '🙁')

main()