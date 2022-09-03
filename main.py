from genericpath import isdir
import os
from shutil import rmtree

HOME = os.path.expanduser('~')
DOWNLOADS = HOME + "/Downloads/"

if os.path.exists(DOWNLOADS):
    [rmtree(DOWNLOADS+f) for f in os.listdir(DOWNLOADS) if isdir(os.path.join(DOWNLOADS, f))]
    [os.remove(DOWNLOADS+f) for f in os.listdir(DOWNLOADS) if os.path.isfile(os.path.join(DOWNLOADS, f))]
    print("Files has been deleted")
else:
    print("There are not files")