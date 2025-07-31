import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QTabWidget
from PyQt5.QtGui import QFont

from system_tab import SystemTab
from process_tab import ProcessTab
from graph_tab import GraphTab

class TaskManagerApp(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔥 Görev Yöneticisi v3 - Modern")
        self.resize(720, 520)

        self.addTab(SystemTab(), "🧠 Sistem")
        self.addTab(ProcessTab(), "🧾 İşlemler")
        self.addTab(GraphTab(), "📈 Grafik")

        self.setStyleSheet("""
    QTabWidget::pane {
        border: none;
        background-color: #121212;
        margin-top: 10px;
        padding: 10px;
        border-radius: 15px;
    }
    QTabBar::tab {
        background: #222;
        color: #bbb;
        padding: 12px 30px;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
        margin: 0 5px;
        font-weight: 600;
        font-size: 15pt;
        min-width: 120px;
        max-width: 160px;
        text-align: center;
        transition: all 0.3s ease;
        border-bottom: 4px solid transparent;
    }
    QTabBar::tab:selected {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #7aa9ff, stop:1 #4a6efb);
        color: white;
        font-weight: 700;
        border-bottom: 4px solid #3f51b5;
    }
    QTabBar::tab:hover {
        background: #4f7de8;
        color: white;
        border-bottom: 4px solid #2a3d9a;
    }
""")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    window = TaskManagerApp()
    window.show()
    sys.exit(app.exec_())
