""" Think Python, 2nd Edition

Chapter 14
Exercise 1  

Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if
necessary). If the pattern string appears anywhere in the file, it
should be replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message, and
exit.  """

import sys

def sed(pattern, replacement, in_path, out_path):
    """Function to write contents of file_in to file_out with pattern
    strings replaced """

    f_in = open(in_path, 'r')
    new_body = f_in.read().replace(pattern, replacement)
    f_in.close()
    
    f_out = open(out_path, 'w')
    f_out.write(new_body)
    f_out.close()
    
if __name__ == '__main__':
    sed(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
