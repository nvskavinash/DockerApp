import os
import socket
import sys

hostname = socket.gethostname()

def count(file_name):
    path = '/home/data'
    path=os.path.join(path, file_name)
    #print(path)
    with open(path, 'rb') as f:
        p=f.read()
        words=p.split()
        #print(words)
        wcount=len(words)
        print("Number of words in %s is %s" % (file_name,wcount))
        return wcount
        

all_files = os.listdir('/home/data')   # imagine you're one directory above test dir
#print(all_files)
txt_files =list(filter(lambda x: x[-4:] == '.txt', all_files))
print(txt_files)# only text files
#print(type(txt_files))
#files = list(txt_files)
#print(files)

dict = {}
for f in txt_files:
    #print(f)
    dict[f] = count(f)
print(dict)
maximum=max(dict, key=dict.get)

orig_stdout = sys.stdout
sys.stdout = open('/home/output/result.txt', 'w')
print("Grand total of all the words present in all files is: "+str(sum(dict.values())))
print("The document with highest number of words is: "+str(maximum)+" with number of words: "+str(dict[maximum]))
print("IP Address:"+socket.gethostbyname(hostname))
print("Submitted by: Venkata Sai Krishna Avinash Nukala, M12888641")
sys.stdout.close()
sys.stdout=orig_stdout


with open('/home/output/result.txt', 'r') as f1:
    print(f1.read())
f1.close()