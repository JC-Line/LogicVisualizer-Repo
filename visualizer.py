from pyvis.network import Network
logic = Network(height="750px", width="100%",)
logic.add_node(1, label="Demo570")

logic.barnes_hut()

logic.show("visualizerTest.html")