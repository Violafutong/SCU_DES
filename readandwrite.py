import os
import ctf
#明文路径\密钥路径\初始向量路径
def read():
    paths = ["des_plain.txt","des_key.txt","des_iv.txt"]
    context = []
    temp  = []
    for path in paths:
        with open(path) as f:
            context.append (f.read())
    for string in context:      
        string = str(bin(int(string,16)))[2:]
        if not len(string)%4 == 0:
            for _ in range(4-len(string)%4):
                string = '0'+string
        temp.append(string)
    return temp
def write():
    path = "des_ Cipher.txt"
    with open(path,'w') as f:
       for i in ctf.words:           
        f.write(i)

def read_data(filename):
    with open(filename,'b') as f:
        string = f.reand()
    return string
    
if __name__ == "__main__":
    read()

