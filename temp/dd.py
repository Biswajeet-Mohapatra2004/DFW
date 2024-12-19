import subprocess as sp
import argparse as ap
import os

parser=ap.ArgumentParser(description="sample argument")
parser.add_argument("input",type=str,help="input file required!!")
parser.add_argument("output",type=str,help="input file required!!")
parser.add_argument("tool",type=str,help="tool required")
args=parser.parse_args()

file_names=os.listdir(args.input)
file_list=[]
for files in file_names:
    if os.path.isfile(os.path.join(args.input,files)):
        file_list.append(files)


def createImage(fileName):
    result=sp.run(["sudo",args.tool,f"if={args.input}/{fileName}",f"of={args.output}/{fileName}.dd",],stdout=sp.PIPE,stderr=sp.PIPE)
    return result

for files in file_list:
    createImage(files)
print("All images have been created!!")
