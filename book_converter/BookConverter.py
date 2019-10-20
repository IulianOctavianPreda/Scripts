from os import listdir, rename
from os.path import isfile, join
import subprocess
import os

#!!! you need to have installed in your system the software named "Calibre" as it uses one of it's libraries


# Here you specify the extension you want THE OUTPUT file to have, it can be mobi, pdf, epub.
# as well as AZW3 DOCX EPUB FB2 HTML HTML LIT LRF MOBI OEB PDB PDF PML RB RTF SNB TCR TXT TXTZ

# So INPUT : AZW4 CHM Comic DJVU DOCX EPUB FB2 HTLZ HTML LIT LRF MOBI ODT PDB PDF PML RB RTF Recipe SNB TCR TXT
# To
# OUTPUT : AZW3 DOCX EPUB FB2 HTML HTML LIT LRF MOBI OEB PDB PDF PML RB RTF SNB TCR TXT TXTZ

def get_final_filename(f):
    f = f.split(".")
    filename = ".".join(f[0:-1])
    processed_file_name = filename+".mobi"
    return processed_file_name


# return file extension. pdf or epub or mobi
def get_file_extension(f):
    return f.split(".")[-1]


def checkIfFolderExists(path):
    if not os.path.exists(path):
        os.makedirs(path)


# list of extensions that needs to be ignored.
ignored_extensions = [""]

# here all the downloaded files are kept
mypath = "./ToConvert/"
checkIfFolderExists(mypath)

# path where converted files are stored
mypath_converted = "./Converted/"
checkIfFolderExists(mypath_converted)


# path where processed files will be moved to, clearing the downloaded folder
mypath_processed = "./AlreadyConverted/"
checkIfFolderExists(mypath_processed)


raw_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
converted_files = [f for f in listdir(
    mypath_converted) if isfile(join(mypath_converted, f))]

for f in raw_files:
    final_file_name = get_final_filename(f)
    print(final_file_name)
    extension = get_file_extension(f)
    if final_file_name not in converted_files and extension not in ignored_extensions:
        print("Converting : "+f)
        try:
            print(mypath+f)
            subprocess.call(["C:\\Program Files (x86)\\Calibre2\\ebook-convert.exe",
                             mypath + f, mypath_converted + final_file_name])
            s = rename(mypath+f, mypath_processed+f)
            print(s)
        except Exception as e:
            print(e)
    else:
        print("Already exists : "+final_file_name)
