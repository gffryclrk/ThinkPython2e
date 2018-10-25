def print_grid(rows,cols):
    # hborder = print('+','- '*4, '+ ', 
    # rows = 2
    # cols = 2

    # htop = '+ ' + '- '*4
    htop = ('+ ' + '- '*4)*cols + '+'
    gbody = ('/ ' + ' '*8)*cols + '/'
    grid = (htop + '\n' + (gbody + '\n')*4)*rows + htop
    print(grid)
    
   # def print_h_border(col_num):
   #     print(htop*col_num, '+')
   #
   # def print_v_border(col_num):
   #     cell = '/ ' + ' '*8
   #     print(cell*col_num, '/')

   # print_h_border(cols)
   # print_v_border(cols)
   # print_v_border(cols)
   # print_v_border(cols)
   # print_v_border(cols)
   # print_h_border(cols)
   # print_v_border(cols)
   # print_v_border(cols)
   # print_v_border(cols)
   # print_v_border(cols)
   # print_h_border(cols)

print_grid(2,2)
print_grid(4,4)
