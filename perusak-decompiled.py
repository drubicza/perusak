import os
import time

os.system('clear')
logo = "\x1b[1;38m\n ____                           _ \n|  _ \\ ___ _ __ _   _ ___  __ _| | __ \n| |_) / _ \\ '__| | | / __|/ _` | |/ / \n|  __/  __/ |  | |_| \\__ \\ (_| |   < \n|_|   \\___|_|   \\__,_|___/\\__,_|_|\\_\\ By JustAHacker \n"
print logo + '\n\x1b[1;33m\ntools ini digunakan untuk merusak hp korban'
time.sleep(2)
print '\x1b[1;31mSubscribe Channel Pembuat Script ini \n \x1b[1;36mJustA Hacker'
print 'github = https://github.com/justahackers/perusak'
print 'youtube = JustA Hacker'
time.sleep(5)
print 'Whatsapp = 6289682009902'
time.sleep(1)
nohp = raw_input('\x1b[1;33mNomor Hp Korban : ')
time.sleep(3)
os.system('clear')
if nohp.isalpha():
    print 'tolong masukkan nomor telepon'
    os.sys.exit()
    os.system('python2 perusak.py')
a = 1

def loop(a):
    for i in range(1000000):
        print '\x1b[1;32m' + str(a) + ' \x1b[1;33mVirus Berbahaya Telah Dikirim ke ' + '\x1b[1;34m' + nohp
        time.sleep(0.2)
        print '\x1b[1;31mMerusak hp korban....'
        time.sleep(0.1)
        print '\x1b[1;34mSubscribe JustA Hacker'
        time.sleep(0.2)
        a += 1

if __name__ == '__main__':
    loop(a)
# okay decompiling 1.pyc
