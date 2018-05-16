'''produce list of chars without printing them explicitly'''
def print_chars():
        print([chr(a) for a in range(ord('a'), ord('z')+1)])

if __name__ == '__main__':
        print_chars()
