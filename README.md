# Think Python Exercises

## Overview
In order to improve my abilities with Python, and programming in general, I have been reading through [Think Python](https://greenteapress.com/wp/think-python-2e/), 2nd Edition. This book has been great for both introducing me to Python syntax and refreshing me on some fundamental computer science concepts and terminology. The programming exercises are pretty fun and my solutions can be found in the subsequent chapter directories of this repository.

## File Naming
When I started this I wasn't sure how to name the files & sparse modules created for the examples. I began by naming the files with a convention ex[ercise].x.y.z.py where x, y, and z represent chapter, section and exercise numbers respectively. However, I later ran into some trouble trying to import these functions later when I wanted to use them (for example, exercise 11.10.1) due to the multiple periods. As the entire purpose of working through these examples is to learn I updated my convention part way through to use underscores (ex[ample]_x_y_z.py). However, when reviewing some of the previous examples I noticed myself waffling between either. You'll have to forgive me for this bad form which I am well aware of. One day perhaps I'll fix this.

## Symlinks
Certain chapters introduce files, such as words.txt, that are required in exercises in later chapters. I ran into some problems with these files. The first was that it seemed to matter where I was running the python file from. I expected locations to be relative to the file the script was in, so that for example a file in the ch11 directory could reference '../ch9/words.txt'. However, this wasn't how things worked in practice. I found that the links were relative to the PWD of where the python process was running from and so the above would only work if I was running `$ python myscript.py` from `ch11`. I then went and tried to hack around this by using symlinks, thinking that would reduce the footprint of my repository, but apparently git ignores symlinks and just follows the link to the data. Whoops. A valuable learning exercise but also a source of future gardening. All files should be moved so that they are all in the ./text (or some other similarly named) directory of this repository and all script references should be updated. I should also standardize running these examples from the root directory of this repository. 