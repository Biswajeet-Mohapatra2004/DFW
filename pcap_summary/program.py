from scapy.all import rdpcap
packets=rdpcap("./ipp.pcap")
uniqueClients=[]
uniqueServers=[]
uniqueComn=[]
clientPorts=[]
serverPorts=[]
protocol_names=[]
for packet in packets:
    layer_name=[]
    while packet:
        layer_name.append(packet.name)
        packet=packet.payload
        protocol_names.append(layer_name[-1])

for packet in packets:
    if packet.haslayer('IP'):
       
        if packet['IP'].src not in uniqueClients:
            uniqueClients.append(packet['IP'].src)
            clientPorts.append(packet['IP'].sport)
        if packet['IP'].dst not in uniqueServers:
            serverPorts.append(packet['IP'].dport)
            uniqueServers.append(packet['IP'].dst)  
        if f"{packet['IP'].src}->{packet['IP'].dst}" not in uniqueComn:
            uniqueComn.append(f"{packet['IP'].src}->{packet['IP'].dst}")      



print("UniqueClients:\n")
print(uniqueClients,f"length:{len(uniqueClients)}","\n")
print("UniqueServers:\n")
print(uniqueServers,f"length:{len(uniqueClients)}","\n") 
print("Unique client server communication: \n")
print(uniqueComn,"\n") 
print("Unique client port:\n")
print(clientPorts,"\n") 
print("Unique Server ports: \n")
print(serverPorts,"\n")
print("Protocols found:\n")
print(list(set(protocol_names)))



