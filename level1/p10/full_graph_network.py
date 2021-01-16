from level1.p10.zadanko import NetworkRouteMonitor
from igraph import Graph, plot
from typing import Dict

monitor = NetworkRouteMonitor()
monitor.use_target('1.1.1.1')
#monitor.use_target('91.200.38.109')
#monitor.use_target('google.pl')
print(monitor.net)
for (k,v) in monitor.net.items():
    print(f'{k} --> {v}')




# GRAF

temp = {}
i : int = 1
n = 0
edges = []
for (a,b) in monitor.net.items():
    if len(b) > 1:
        n += len(b) + 1
        try:
            print(temp[str(a)])
        except:
            temp[str(a)] = i
            i += 1
        for h in b:
            try:
                print(temp[str(h)])
            except:
                temp[str(h)] = i
                i += 1
    else:
        try:
            print(temp[str(a)])
        except:
            temp[str(a)] = i
            i += 1

        try:
            print(temp[str(b)])
        except:
            temp[str(b)] = i
            i += 1
        n += 2

for (a,b) in monitor.net.items():
    if len(b) > 1:
        for h in b:
            edges.append((temp[str(a)],temp[str(h)]))
    else:
        edges.append((temp[str(a)],temp[str(b)]))

# edges.append((a, b))
g = Graph(directed=False)

g.add_vertices(n)

# Add ids and labels to vertices
for i in range(n):
    g.vs[i]["id"] = i
    g.vs[i]["label"] = i


g.add_edges(edges)

visual_style = {}
out_name = 'netgraph.png'  # Set bbox and margin
visual_style['bbox'] = (2000, 2000)
visual_style['margin'] = 27  # Set vertex colours
visual_style['vertex_color'] = 'white'  # Set vertex size
visual_style['vertex_size'] = 25  # Set vertex lable size
visual_style['vertex_label_size'] = 15  # Don't curve the edges
visual_style['edge_curved'] = False  # Set the layout
my_layout = g.layout_lgl()
visual_style['layout'] = my_layout  # Plot the graph
plot(g, out_name, **visual_style)