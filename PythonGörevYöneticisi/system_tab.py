import psutil
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer

class SystemTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(20)

        self.cpu_label = QLabel("CPU: ")
        self.ram_label = QLabel("RAM: ")
        self.disk_label = QLabel("Disk: ")
        self.gpu_label = QLabel("GPU: ")

        label_style = "color: #ddd; font-size: 14pt; font-weight: 700;"
        for lbl in (self.cpu_label, self.ram_label, self.disk_label, self.gpu_label):
            lbl.setStyleSheet(label_style)

        layout.addWidget(self.cpu_label)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.disk_label)
        layout.addWidget(self.gpu_label)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        try:
            disk = psutil.disk_usage('C:\\').percent  # Windows için
        except Exception:
            disk = 0

        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            gpu = int(gpus[0].load * 100) if gpus else 0
        except Exception:
            gpu = 0

        self.cpu_label.setText(f"🧠 CPU Kullanımı: %{cpu}")
        self.ram_label.setText(f"💾 RAM Kullanımı: %{ram}")
        self.disk_label.setText(f"📀 Disk Kullanımı: %{disk}")
        self.gpu_label.setText(f"🎮 GPU Kullanımı: %{gpu}")
