import argparse as ap
import  os
import subprocess as sp

parser=ap.ArgumentParser(description="sample argument")
parser.add_argument("inputDirectory",type=str,help="Input directory required!!")
parser.add_argument("outputDirectory",type=str,help="output directory required!!")
parser.add_argument("fileType",type=str,help="fileType required!!")

args=parser.parse_args()


file_names=[]
All_Files=os.listdir(args.inputDirectory)
for file in All_Files:
     if os.path.isfile(os.path.join(args.inputDirectory,file)):
          file_names.append(file)
          
          
def Foremost(inputLOC,outputLOC,ImageFile,fileType,docName):
    os.mkdir(f"{outputLOC}/{docName}")
    print("Method called!!")
    result=sp.run(["sudo","foremost","-i",f"{inputLOC}/{ImageFile}","-o",f"{outputLOC}/{docName}","-t",f"{fileType}"],stdout=sp.PIPE,stderr=sp.PIPE)       
    
       
for file in file_names:
     docName=input("Enter a directory named for the image to recover: ")
     Foremost(args.inputDirectory,args.outputDirectory,file,args.fileType,docName)
         

    
print("All the images have been recoverd!!")    
     


