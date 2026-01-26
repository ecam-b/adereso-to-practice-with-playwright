import time
from playwright.sync_api import Locator
from pages.inbox.modals.create_column import CreateColumnModal


class ColumnComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator 
        self.page = root_locator.page # Referencia a la página completa
        self.title = self.root.locator(".column-title span[uib-tooltip]")
        self.burger_menu = self.root.locator('div[uib-tooltip="Más opciones"]')
        self.floating_menu = self.page.locator(".dropdown-column-options").filter(visible=True)
        self.opt_edit = self.floating_menu.locator('div[ng-click="editColumn()"]')
        self.opt_export = self.floating_menu.locator("div[ng-click='exportColumn()']")
        self.opt_delete = self.floating_menu.locator("div[ad-confirm-click='deleteColumn()']")

    def open_options(self):
        """Abre el menú y asegura que sea visible antes de retornar."""
        self.burger_menu.click()
        self.floating_menu.wait_for(state="visible", timeout=3000)

    def select_edit_option(self, max_retries=5, timeout=2000):
        """
        Intenta abrir el modal de edición. 
        Si el click falla porque la app no estaba lista, reintenta el flujo completo.
        """
        modal = CreateColumnModal(self.page)

        for i in range(max_retries):
            try:
                self.open_options()
                self.opt_edit.click()
                # Esperamos una señal de éxito (que el modal aparezca)
                modal.container.wait_for(state="visible", timeout=2000)
                return modal # Éxito: retornamos el objeto del modal
            
            except Exception as e:
                print(f"[DEBUG] Intento {i+1} fallido para abrir modal: {str(e)}")
                self.page.keyboard.press("Escape") 
                time.sleep(1) # Pequeña pausa para que la app se asiente
        
        # Último intento fuera del try para que lance el error real si falla definitivamente
        self.open_options()
        self.opt_edit.click()
        modal.wait_until_visible()
        return modal
    
    def select_delete_option(self):
        self.open_options()
        self.opt_delete.click()

        from pages.inbox.modals.delete_confirmation_modal import DeleteConfirmationModal
        return DeleteConfirmationModal(self.page)