import sys
import os
from enum import Enum

# Matplotlib
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure

# PyQt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

from .widgets.xsection import CrossSectionWidget
progname = os.path.basename(sys.argv[0])

# Tools = Enum('Tools', 'OrthoXSection CustomXSection')

# def CrossSectionWidgetFromDataSet(dataset):
#         self.expand_trace(args=[dataset], kwargs=data)
    
#         xlabel = self.get_label(data['x'])
#         ylabel = self.get_label(data['y'])
#         zlabel = self.get_label(data['z'])
#         xaxis = data['x'].ndarray[0, :]
#         yaxis = data['y'].ndarray


# class CrossSectionWidget(FigureCanvas, BasePlot):

#     def __init__(self, xaxis, yaxis, z, units, labels, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)

#         self.compute_initial_figure()

#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)

#         FigureCanvas.setSizePolicy(self,
#                                    QtWidgets.QSizePolicy.Expanding,
#                                    QtWidgets.QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)
    

#     def compute_initial_figure(self):
#         pass


class ApplicationWindow(QMainWindow):
    def __init__(self, dataset):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Main Window
        self.setWindowTitle("QCoDeS Qt Ui")

        # Menus
        # File
        self.file_menu = QtWidgets.QMenu('&File', self)
        self.menuBar().addMenu(self.file_menu)
        # Tools
        tool_menu = QtWidgets.QMenu('&Tools', self)
        self.menuBar().addMenu(tool_menu)

        # help
        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        self.help_menu.addAction('&About', self.about)

        # toolbars
        toolbar = self.addToolBar('Tools')

        # Tools
        tools = dict()
        def addTool(id, action, name, shortcut, tip, **kwargs):
            if 'icon' in kwargs.keys():
                tools[id] =  QAction(kwargs['icon'], name, self)
            else:
                tools[id] =  QAction(name, self)
            tools[id].setShortcut(shortcut)
            tools[id].setStatusTip(tip)
            tools[id].triggered.connect(action)
            toolbar.addAction(tools[id])
            tool_menu.addAction(tools[id])
            # if 'menu' in kwargs.keys():
            #     kwargs['menu'].addAction(tools[id])
            # if 'toolbar' in kwargs.keys():
            #     kwargs['toolbar'].addAction(tools[id])

        imagepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/crosshair.png')
        addTool('OrthoXSection', self.test,
                'Orthorgonal cross section', 'Ctrl+o',
                'The orthorgonal cross section tool creates a profile of the data at a given point', icon=QIcon(imagepath))
        print(imagepath)

        #5f8cba


        # Main Widget
        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        cw = CrossSectionWidget(dataset, tools=tools)
        l.addWidget(cw)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)
    def test(self):
        print('test')
    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About", "QCoDeS Qt Ui v0.1" )




# qApp = QtWidgets.QApplication(sys.argv)
# aw = ApplicationWindow()
# aw.setWindowTitle("%s" % progname)
# aw.show()
# sys.exit(qApp.exec_())
