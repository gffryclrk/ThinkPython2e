# Think Python Exercises

These exercises are proving valuable in learning the Python ecosystem and best practices. 

## Overview
In order to improve my abilities with Python, and programming in general, I have been reading through [Think Python](https://greenteapress.com/wp/think-python-2e/), 2nd Edition. This book has been great for both introducing me to Python syntax and refreshing me on some fundamental computer science concepts and terminology. The programming exercises are pretty fun and my solutions can be found in the subsequent chapter directories of this repository.

## Evolution
When I began the exercises for this book I was writing the solutions as scripts and running them from the command line. For example, `$ python 3.5.py` in bash. In this manner I would manually check that the program behaved as I expected. Later I improved my workflow and organization of code in order to re-use sections of code as modules (as in `ex13_1_2.py`). I learned that by doing this I needed to be using the `if __name__ == '__main__'` construct. During this time I would continue to run the scripts from the command line in order to assess their correctness.

As the exercises and solutions grew in complexity I began writing unit tests to validate the correctness of functions. The tests are contained in the `test` directory and begin with chapter 12 `ch12_10_2_anagram_test`. For many of the solutions past this point I had stopped running the implementations and was instead running only the tests to assert the correctness of the solutions. Thus the `if __name__ == '__main__'` construct is absent from many of these exercises and instead the solutions are called from their respective unit tests. 

## File Naming
When I started this I wasn't sure how to name the files & sparse modules created for the examples. I began by naming the files with a convention ex[ercise].x.y.z.py where x, y, and z represent chapter, section and exercise numbers respectively. However, I later ran into some trouble trying to import these functions. For example, there are issues importing `exercise 11.10.1` due to the use of periods. As I worked through the exercises and began learning more I updated the way in which I named files and changed the use of periods in filenames to underscores. The file naming convention thus becomes `ex[ample]_x_y_z.py`. However, when reviewing some of the previous examples I noticed myself waffling between either. You'll have to forgive me for this bad form.

## Symlinks
Certain chapters introduce files, such as words.txt, that are required in exercises in later chapters. I ran into some problems with these files. The first was that it seemed to matter where I was running the python file from. I expected locations to be relative to the file the script was in, so that for example a file in the ch11 directory could reference '../ch9/words.txt'. However, this wasn't how things worked in practice. I found that the links were relative to the PWD of where the python process was running from and so the above would only work if I was running `$ python myscript.py` from `ch11`. I then went and tried to hack around this by using symlinks, thinking that would reduce the footprint of my repository, which perhaps it did at the cost of being messy. This should probably all be fixed. I also leveraged symlinks a bit to use the python module system in an easy way, such as with ch13/ch11_histogram.py which is just a symlink to ch11/exercise11.2.histogram.py. I could have added ch11 to the syspath which I had done with previous exercises but would still have had to rename the file to replace the dots with underscores. This would alter the consistency and so I opted for the part time hack approach.

