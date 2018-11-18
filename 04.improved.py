edges = []
for i in range(3):
    edges.append(input('Zadaj ' + str(i+1) + '. stranu trojuholnika:\n'))

edges.sort()
if edges[0] + edges[1] > edges[2] and edges[0] + edges[2] > edges[1] and edges[1] + edges[2] > edges[0]:
    print('Trojuholnik sa da nakreslit')
else:
    print('Trojuholnik sa neda nakreslit')