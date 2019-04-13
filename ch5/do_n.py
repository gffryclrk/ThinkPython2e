def do_n(f, n, *args):
    if n <= 0:
        return

    f(*args)
    do_n(f, n-1, *args)



def print_n(s, n):
	if n <= 0:
		return
	print(s)
	print_n(s, n-1)

do_n(print_n, 3, 'Hello', 3)
