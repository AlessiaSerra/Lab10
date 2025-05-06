import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}
        self.dao = DAO


    def buildGraph(self, anno):
        nodes = self.dao.getNodes(anno)
        self._graph.add_nodes_from(nodes)
        for node in nodes:
            self._idMap[node.id] = node

        edges = self.dao.getEdges(anno)
        for edge in edges:
            self._graph.add_edge(self._idMap[edge[0]], self._idMap[edge[1]])




