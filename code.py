import os

path, dirs, files = next(os.walk("/home/ur_directory"))     #directory containing source files.
file_count = len(files)
f2=open('/home/ur_directory/result/result.txt','a') #file where you want to copy (destination file)
for times in range (file_count):
  fpath= "/home/ur_directory/Aws_records/{}".format(files[times])  #saving path of file in variable
  #print(fpath)
  f=open(fpath,"r")
  count=0
  for x in f.readlines():
     count+=1
     if (count==1):
     f2.write("\n======\n")
     f2. write(files[times])
     f2.write(x)
f2.write("\n")
f.close
f2.close
