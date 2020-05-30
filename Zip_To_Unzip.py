import os
import zipfile

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.zip'):
        newFileName = os.path.splitext(filename)[0]
        handle = zipfile.ZipFile(filename)
        handle.extractall(os.getcwd() + '//' + newFileName)
        print(os.path.join(os.getcwd(), filename))
        continue
    else:
        continue