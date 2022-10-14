from cProfile import label
from pyvis.network import Network
logic = Network(height="750px", width="100%",)

# add nodes

nodeIds = [3,4,5,6,7]

for i in nodeIds:
    nodeLabels = "Act" + str(i)

for i in nodeLabels:
    print(i)

logic.add_nodes(nodeIds,
label=["act3","act4","act5","act6","act7"],
size= [75,75,75,75,75])

logic.add_node(1, label="Demo570", title="Demo Activity", size = 100,shape = "circularImage",image = "https://m.media-amazon.com/images/I/A1YG9F6BL8L.jpg")

logic.add_node(2, label="Drg570", title="Drainage Activity",size = 100,shape = "circularImage", image = "https://www.agronomy.org/files/images/news/td.in_.out_.3-800x600.jpg")

# add edges

sources = [3,4,5,6]
targets = [4,5,6,7]

edge_data = zip(sources,targets)

for i in edge_data:
    logic.add_edge(i[0],i[1])

logic.add_edge(1,2,title = "Demo570 - Drg570 [5]")
logic.add_edge(1,4)
logic.add_edge(2,6)

# Physics to use
logic.barnes_hut()

# Output HTML
logic.show("visualizerTest.html")