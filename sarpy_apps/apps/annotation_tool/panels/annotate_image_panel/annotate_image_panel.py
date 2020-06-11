from sarpy_gui_apps.apps.annotation_tool.panels.annotate_image_panel.annotate_dashboard.annotate_dashboard import AnnotateDash
from tkinter_gui_builder.panel_templates.image_canvas_panel.image_canvas_panel import ImageCanvasPanel
from tkinter_gui_builder.panel_templates.widget_panel.widget_panel import AbstractWidgetPanel


class AppVariables:
    def __init__(self):
        self.image_fname = "None"       # type: str
        self.sicd_metadata = None


class AnnotateImagePanel(AbstractWidgetPanel):
    annotate_dashboard = AnnotateDash         # type: AnnotateDash
    image_canvas_panel = ImageCanvasPanel      # type: ImageCanvasPanel

    def __init__(self, parent):
        # set the master frame
        AbstractWidgetPanel.__init__(self, parent)
        self.app_variables = AppVariables()
        widgets_list = ["image_canvas_panel", "annotate_dashboard"]

        self.init_w_vertical_layout(widgets_list)

        self.annotate_dashboard.set_spacing_between_buttons(0)
        self.image_canvas_panel.set_canvas_size(600, 400)
