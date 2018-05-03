import sys


if __name__ == "__main__":
    sys.stdout.write('hello1' + '\n')
    print('hello')
    print('please input:')
    hi = sys.stdin.readline()[:-1]
    print(len(hi))


