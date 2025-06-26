import networkx as nx
import database.DAO as DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}
        self.dao = DAO.DAO()



    def getStati(self):
        return self.dao.getStati()


    def getGradi(self):
        dict = {}
        for node in self._graph.nodes():
            dict[node.state] = self._graph.degree(node)

        return dict



    def buildGraph(self, anno):
        nodes = self.dao.getNodes(anno)
        self._graph.add_nodes_from(nodes)
        for node in nodes:
            self._idMap[node.id] = node

        edges = self.dao.getEdges(anno)
        if anno >= 2006:
            edges2006 = self.dao.getEdges2006()
            edges.extend(edges2006)
        for edge in edges:
            self._graph.add_edge(self._idMap[edge[0]], self._idMap[edge[1]])
        print(self._graph)
        return True

    def getComponentiConnesse(self):
        tree = nx.dfs_tree(self._graph)
        print(self._graph.number_of_edges())



    def getCompConnRicorsione(self, stato):
        path = [stato]
        da_visitare = set()
        da_visitare.add(self._graph.nodes())
        for node in da_visitare:
           if node





