from PySide2 import QtWidgets, QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, icon, root,parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.root = root
        self.setToolTip(f'Kancolle Voice Clock by Conrad')
        menu = QtWidgets.QMenu(parent)
        open_app = menu.addAction("Open")
        open_app.triggered.connect(lambda: self.root.deiconify())

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: self.root.destroy())

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        if reason == self.DoubleClick:
            self.open_app()

    def open_app(self):
        self.root.deiconify()