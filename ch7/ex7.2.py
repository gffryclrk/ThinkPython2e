def eval_loop():
    prev = ''
    while True:
        line = input('> ')
        if line == 'done':
            print(prev)
            break
        else:
#           print(line)
            result = eval(line)
            print(result)
            prev = result

eval_loop()
