import psutil
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QListWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer

class ProcessTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("🔍 İşlem ara (örneğin chrome)")
        self.search_bar.textChanged.connect(self.update_list)
        self.search_bar.setStyleSheet("""
            padding: 10px;
            font-size: 14pt;
            border: 2px solid #444;
            border-radius: 12px;
            background-color: #222;
            color: #eee;
            selection-background-color: #6a9ef8;
        """)

        self.process_list = QListWidget()
        self.process_list.setStyleSheet("""
            font-size: 13pt;
            border: 2px solid #444;
            border-radius: 12px;
            background-color: #121212;
            color: #ddd;
        """)

        self.kill_button = QPushButton("❌ Seçilen İşlemi Sonlandır")
        self.kill_button.clicked.connect(self.kill_process)
        self.kill_button.setStyleSheet("""
            QPushButton {
                background-color: #ff4c4c;
                color: white;
                font-weight: 700;
                border-radius: 15px;
                padding: 14px;
                box-shadow: 0px 4px 8px rgba(0,0,0,0.4);
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #e03b3b;
            }
        """)

        layout.addWidget(self.search_bar)
        layout.addWidget(self.process_list)
        layout.addWidget(self.kill_button)

        self.setLayout(layout)

        self.update_list()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_list)
        self.timer.start(5000)

    def update_list(self):
        keyword = self.search_bar.text().lower()
        self.process_list.clear()
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                name = proc.info['name']
                pid = proc.info['pid']
                if keyword in name.lower():
                    self.process_list.addItem(f"{pid} - {name}")
            except Exception:
                pass

    def kill_process(self):
        selected = self.process_list.currentItem()
        if selected:
            pid = int(selected.text().split(" - ")[0])
            try:
                psutil.Process(pid).terminate()
                QMessageBox.information(self, "İşlem", f"PID {pid} sonlandırıldı.")
                self.update_list()
            except Exception as e:
                QMessageBox.warning(self, "Hata", str(e))
        else:
            QMessageBox.warning(self, "Seçim", "Lütfen bir işlem seç.")
