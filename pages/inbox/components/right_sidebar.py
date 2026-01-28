from playwright.sync_api import Locator

class RightSideBar:
    def __init__(self, root_locator: Locator):
        self.root = root_locator
        self.page = root_locator.page

        self.btn_datos_perfil = self.root.locator('btn[uib-tooltip="Datos de perfil"]')
        self.btn_datos_ticket = self.root.locator('btn[uib-tooltip="Datos del ticket"]')
        self.btn_pedidos = self.root.locator('btn[uib-tooltip="Pedidos"]')
        self.btn_omnicanalidad = self.root.locator('btn[uib-tooltip="Omnicanalidad"]')
        self.btn_comentarios = self.root.locator('btn[uib-tooltip="Comentarios"]')
        self.btn_integracion = self.root.locator('btn[uib-tooltip="Integración"]')
        self.btn_escalamiento = self.root.locator('btn[uib-tooltip="Escalamiento del ticket"]')
        self.btn_anteriores = self.root.locator('btn[uib-tooltip="Tickets Anteriores"]')
        self.btn_historial = self.root.locator('btn[uib-tooltip="Historial de asignación"]')
