"""Think Python, 2nd Edition

In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

1. Write a program that searches a directory and all of its
subdirectories, recursively, and returns a list of complete paths for
all files with a given suffix (like .mp3). Hint: os.path provides
several useful functions for manipulating file and path names.  

2. To recognize duplicates, you can use md5sum to compute a “checksum” for
each files. If two files have the same checksum, they probably have
the same contents.  

3. To double-check, you can use the Unix command diff. """

import os
import hashlib

start_path = 'mp3s'
path_dir = {}
for path, dirs, files in os.walk(start_path):
    for filename in files:
        path_list = path_dir.get(filename, [])
        path_list.append(os.path.join(path, filename))
        path_dir[filename] = path_list

print(f'path_dir: {path_dir}')
duplicates = {k:v for k,v in path_dir.items() if len(v) > 1}
print(f'duplicates: {duplicates}')

hashes = {}
for k, v in duplicates.items():
    hash_list = []
    for filename in v:
        md5_hash = hashlib.md5()
        with open(filename, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
            hash_list.append(md5_hash.hexdigest())
    hashes[k] = hash_list
    
print(f'hashes: {hashes}')

"""
path_dir: {'one.mp3': ['mp3s/one.mp3'], 'two.mp3': ['mp3s/two.mp3'], 'track1.mp3': ['mp3s/artist_album/track1.mp3', 'mp3s/album/track1.mp3']}
duplicates: {'track1.mp3': ['mp3s/artist_album/track1.mp3', 'mp3s/album/track1.mp3']}
hashes: {'track1.mp3': ['cdef8749a1d71ef84425e729f011d4f4', 'cdef8749a1d71ef84425e729f011d4f4']}
"""
    
