from subprocess import Popen,PIPE

# env : windows 7
def load_vhd(file):
    p1 = Popen("diskpart",stdin=PIPE)
    p1.stdin.write('''select vdisk file="%s"\r\n'''%file)
    p1.stdin.write('''attach vdisk \r\n''')

load_vhd(r"D:\workspace\srcRead.vhd")    

