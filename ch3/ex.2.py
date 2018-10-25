def do_twice(f,v):
    f(v)
    f(v)

def print_spam():
    print('spam')

# do_twice(print_spam)
def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')

def do_four(f, v):
    do_twice(f,v)
    do_twice(f,v)
