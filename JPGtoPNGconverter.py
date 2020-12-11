import sys
import os
from PIL import Image

from pathlib import Path
import glob
from os import walk

#grab first and second argument

#check if /new folder exists and if not create it
#TODO frab first and second argument
#TODO check if new/ exists
#TODO loop through pokedex
#TODO convert images to png
#TODO save to new folder

def folder_check(fname1, fname2):
    first_dir = Path(f'./{fname1}')
    first_dir2 = str(first_dir)
    # new_dir = Path('~/Projects_Code/Udemy_Complete_Python_Developer/new')
    new_dir = Path(f'./{fname2}')

    ready = None

    fdata = []
    dirdata = []

    for (root, dirs, files) in os.walk('./Pokedex'):
        fdata.extend(files)#get the files from pokedex
        for name in files:
            dirdata.append(os.path.join(root, name))


    if not os.path.isdir(new_dir):#checking for new/ directory
        print('The New home must be created!')
        os.mkdir(new_dir)
        print('Done!')
        ready = True
    else:
        print(f'The new directory already exists!: {new_dir}')
        ready = True

        if os.path.isdir(first_dir):
            print('The Pokedex is ready')
            ready = True
        else:
            print(f"I cant find the Pokedex: {first_dir2}")
            ready = False

    print('Ready: ', ready)
    if ready is True:
        print('last method!')
        for infile in dirdata:
            print('Infile: ', infile)

            filenam, extension = os.path.splitext(infile)
            outfile = filenam + ".png"
            #separate files again
            extension2 = os.path.basename(outfile)
            final_outfile = os.path.join('./', new_dir, extension2)
            print('Final Outfile', final_outfile)

            if infile != final_outfile:
                try:
                    with Image.open(infile) as im:
                        im.save(final_outfile)
                        print(outfile)
                except OSError:
                    print('Cannot convert: ', infile)



if __name__ == '__main__':

    folder_check('Pokedex/', 'new/')
