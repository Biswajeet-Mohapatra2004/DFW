import argparse as ap
parser=ap.ArgumentParser(description="sample argument")
parser.add_argument("input",type=str,help="input file required!!")
args=parser.parse_args()
malicious_mac=[]
with open(args.input,'r') as file:
    for line in file:
        if "Hp" not in line and "Dell" not in line:
            elems=line.strip().split(" ")
            malicious_mac.append(elems[1])
print("The malicious devices are as follows with device MAC address")            
print(malicious_mac)            
