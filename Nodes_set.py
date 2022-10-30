Nodes = []

Max_lenght_Nodes_Set = 99

Node = (input('Please input the nodes, inputing a 0 terminates this step. ').strip())
while (Node != '0') and (len(Nodes) < Max_lenght_Nodes_Set):
    if Node in Nodes:
        print('This node is already in the set.')
    else:
        Nodes.append(Node)
    Node = (input().strip())

print(Nodes)