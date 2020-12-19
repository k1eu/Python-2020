from igraph import Graph, plot

"""
Zadanie: przedstawić graficznie drzewo zadane przez listę dzieci, 

gg = [[1, 2], [], [3, 4], [], []]
"""

gg = [[1, 2], [], [3, 4], [], []]
n = len(gg)

g = Graph(directed=False)

g.add_vertices(n)

# Add ids and labels to vertices
for i in range(n):
    g.vs[i]["id"] = i
    g.vs[i]["label"] = 'node' + str(i)

# Add edges
edges = []
for i in range(n):
    for c in gg[i]:
        edges.append((i, c))


g.add_edges(edges)

visual_style = {}
out_name = 'tree.png'  # Set bbox and margin
visual_style['bbox'] = (500, 500)
visual_style['margin'] = 27  # Set vertex colours
visual_style['vertex_color'] = 'white'  # Set vertex size
visual_style['vertex_size'] = 50  # Set vertex lable size
visual_style['vertex_label_size'] = 15  # Don't curve the edges
visual_style['edge_curved'] = True  # Set the layout
my_layout = g.layout_lgl()
visual_style['layout'] = my_layout  # Plot the graph
plot(g, out_name, **visual_style)