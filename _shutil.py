import shutil
import os

source = ""
destination = ""

if os.path.exists(source):
    shutil.copytree(source, destination)

shutil.rmtree(source)
