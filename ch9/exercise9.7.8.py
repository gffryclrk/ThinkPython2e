def six_digit_palendromic():
    def string_digit(d):
        return str(d).rjust(6, '0') 

    pals = []
    i = 1

    while i < 999997:

        if (string_digit(i)[2:] == string_digit(i)[2:][::-1] and 
            string_digit(i+1)[1:] == string_digit(i+1)[1:][::-1] and
            string_digit(i+2)[1:5] == string_digit(i+2)[1:5][::-1] and 
            string_digit(i+3) == string_digit(i+3)[::-1]):
            pals.append(i)

        i+=1

    return pals

print(six_digit_palendromic())
