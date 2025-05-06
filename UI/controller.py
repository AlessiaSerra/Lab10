import flet as ft
import networkx as nx

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._graph = None

    def fillDDstato(self):
        pass

    def handleRaggiungibili(self, e):
        pass

    def handleCalcola(self, e):
        anno = int(self._view._txtAnno.value)
        if anno<1816 or anno >2016:
            self._view.create_alert("Inerisci una data nell'intervallo 1816-2016 !")
            return
        self._graph = self._model.buildGraph(anno)

        for state in self._graph.nodes():
            self.view._txt_result.append(ft.Text(f"{state} -- {state.degree()}"))

