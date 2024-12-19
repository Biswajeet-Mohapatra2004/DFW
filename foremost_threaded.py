import argparse as ap
import  os
import subprocess as sp
import threading
import time

parser=ap.ArgumentParser(description="sample argument")
parser.add_argument("inputDirectory",type=str,help="Input directory required!!")
parser.add_argument("outputDirectory",type=str,help="output directory required!!")
parser.add_argument("fileType",type=str,help="fileType required!!")

args=parser.parse_args()

threadArr=[]
file_names=[]
All_Files=os.listdir(args.inputDirectory)
for file in All_Files:
     if os.path.isfile(os.path.join(args.inputDirectory,file)):
          file_names.append(file)
               
def Foremost(inputLOC,outputLOC,ImageFile,fileType,docName):
    result=sp.run(["sudo","foremost","-i",f"{inputLOC}/{ImageFile}","-o",f"{outputLOC}/{docName}","-t",f"{fileType}"],stdout=sp.PIPE,stderr=sp.PIPE)       
       
for i in range(1,len(file_names)+1):
     thread=threading.Thread(target=Foremost,args=(args.inputDirectory,args.outputDirectory,file,args.fileType,f"recovery{i}"))
     threadArr.append(thread)
#     Foremost(args.inputDirectory,args.outputDirectory,file,args.fileType,f"recovery{i}")
for thread in threadArr:
    thread.start()
    thread.join()
    print("Thread finished, as main thread ends!!")
    
             

    
print("All the images have been recoverd!!")    
     
