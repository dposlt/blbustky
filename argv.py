from sys import argv

if len(argv) == 2:
    print(f'Hello, {argv[1]}')
    print(argv)
else:
    print('Hello world')
