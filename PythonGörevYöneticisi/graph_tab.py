import psutil
import GPUtil
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer

class GraphTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        self.cpu_graph = self.create_graph("🧠 CPU Kullanımı", 'y')
        self.ram_graph = self.create_graph("💾 RAM Kullanımı", 'c')
        self.disk_graph = self.create_graph("📀 Disk Kullanımı", 'm')
        self.gpu_graph = self.create_graph("🎮 GPU Kullanımı", 'g')

        layout.addWidget(self.cpu_graph["widget"])
        layout.addWidget(self.ram_graph["widget"])
        layout.addWidget(self.disk_graph["widget"])
        layout.addWidget(self.gpu_graph["widget"])

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all)
        self.timer.start(1000)

    def create_graph(self, title, color):
        graph = pg.PlotWidget(title=title)
        graph.setBackground('#121212')
        graph.setYRange(0, 100)
        curve = graph.plot(pen=pg.mkPen(color, width=3))
        graph.getAxis('left').setTextPen('#bbb')
        graph.getAxis('bottom').setTextPen('#bbb')
        graph.showGrid(x=True, y=True, alpha=0.3)
        return {"widget": graph, "data": [], "curve": curve}

    def update_all(self):
        cpu = psutil.cpu_percent()
        self.update_graph(self.cpu_graph, cpu)

        ram = psutil.virtual_memory().percent
        self.update_graph(self.ram_graph, ram)

        try:
            disk = psutil.disk_usage('C:\\').percent
        except Exception:
            disk = 0
        self.update_graph(self.disk_graph, disk)

        try:
            gpus = GPUtil.getGPUs()
            gpu = gpus[0].load * 100 if gpus else 0
        except Exception:
            gpu = 0
        self.update_graph(self.gpu_graph, gpu)

    def update_graph(self, graph_obj, value):
        graph_obj["data"].append(value)
        if len(graph_obj["data"]) > 60:
            graph_obj["data"].pop(0)
        graph_obj["curve"].setData(graph_obj["data"])
