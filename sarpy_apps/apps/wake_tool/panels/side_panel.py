from tkinter_gui_builder.panel_templates.widget_panel.widget_panel import AbstractWidgetPanel
from sarpy_gui_apps.apps.wake_tool.panels.button_panel import ButtonPanel
from sarpy_gui_apps.apps.wake_tool.panels.info_panel import InfoPanel
from tkinter_gui_builder.panel_templates.file_selector.file_selector import FileSelector


class SidePanel(AbstractWidgetPanel):
    buttons = ButtonPanel
    file_selector = FileSelector
    info_panel = InfoPanel

    def __init__(self, parent):
        AbstractWidgetPanel.__init__(self, parent)
        widget_list = ["file_selector", "buttons", "info_panel"]
        self.init_w_basic_widget_list(widget_list, 2, [1, 2])
        self.set_label_text("wake tool controls")
