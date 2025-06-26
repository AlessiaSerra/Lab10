import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDstato(self):
        stati = self._model.getStati()
        for stato in stati:
            self._view._ddStato.options.append(ft.dropdown.Option(stato))

    def handleRaggiungibili(self, e):
        pass

    def handleCalcola(self, e):
        anno = int(self._view._txtAnno.value)
        if anno<1816 or anno >2016:
            self._view.create_alert("Inerisci una data nell'intervallo 1816-2016 !")
            return
        created = self._model.buildGraph(anno)

        if created:
            self._view._btnStatiRaggiungibili.disabled = False
            self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato."))
            n_comp = self._model.getComponentiConnesse()
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {n_comp} componeti connesse.\n Di seguito il dettaglio sui nodi.\n"))
            grado_vertici = self._model.getGradi()
            print(grado_vertici)
            for key in grado_vertici.keys():
                self._view._txt_result.controls.append(
                    ft.Text(f" {key} --- {grado_vertici[key]} vicini."))
                self._view.update_page()

