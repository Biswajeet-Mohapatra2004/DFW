import subprocess as sp
import argparse as ap
parser=ap.ArgumentParser(description="sample argument")
parser.add_argument("inputFile1",type=str,help="input file required!!")
parser.add_argument("inputFile2",type=str,help="input file required!!")
parser.add_argument("tool",type=str,help="tool required")
args=parser.parse_args()
def check(fileName):
    result=sp.run([args.tool,fileName],stdout=sp.PIPE,stderr=sp.PIPE)
    return result

hash1=check(args.inputFile1)
hash2=check(args.inputFile2)

if hash1==hash2:
    print("Both are same: ")
else:
    print("Both file different")    

