import os
import re
os.chdir('./videos/学而思奥数一年级')

for root, dirs, files in os.walk("."):
    for filename in files:
        # if filename.startswith('Bastien Piano Basics Level 1 Performance '):
            # newname = filename[41:]
        newname = re.sub('学而思 小学奥数 一年级 第', '', filename)
        os.rename(filename, newname)
        print('Renamed {} to {}'.format(filename, newname))
