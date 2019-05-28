def print_reverse_string(in_string):
    for i in range(1, len(in_string)+1):
        print(in_string[-i])

def make_way_for_ducklings():
    prefixes=['J','K','L','M','N','Ou','P','Qu']
    suffix = 'ack'
    for letter in prefixes:
        print(letter + suffix)

print_reverse_string('reverse me')
make_way_for_ducklings()
