# -*- coding: utf-8 -*-
#
from rubber import play_rubber
from PyQt4 import QtCore, QtGui
import sys

class window_rubber(QtGui.QWidget):
    def __init__(self, parent = None):
        # make window
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle(u'Модель груза на резинке')
        self.setFixedSize(300,250)
        # make components
        btnStart = QtGui.QPushButton(u'Старт')
        self.lab_speed = QtGui.QLabel(u'Скорость воспроизведения')
        self.ed_speed = QtGui.QLineEdit()
        self.ed_speed.setText('10')
        self.ed_speed.setValidator(QtGui.QIntValidator(0, 10, self))
        self.lab_toughness = QtGui.QLabel(u'Вязкость')#vjazkost вязкость
        self.ed_toughness = QtGui.QLineEdit()
        self.ed_toughness.setText('4')
        self.ed_toughness.setValidator(QtGui.QIntValidator(0, 10, self))
        self.lab_stiffness = QtGui.QLabel(u'Жесткость')#gestkost жесткость
        self.ed_stiffness = QtGui.QLineEdit()
        self.ed_stiffness.setText('5')
        self.ed_stiffness.setValidator(QtGui.QIntValidator(0, 50, self))
        self.lab_number_el = QtGui.QLabel(u'Количество звеньев')
        self.ed_number_el = QtGui.QLineEdit()
        self.ed_number_el.setText('20')
        self.ed_number_el.setValidator(QtGui.QIntValidator(0, 20, self))
        self.lab_weight = QtGui.QLabel(u'Вес')
        self.ed_weight = QtGui.QLineEdit()
        self.ed_weight.setText('2')
        self.ed_weight.setValidator(QtGui.QIntValidator(0, 10, self))
        
        self.speed_p = QtGui.QLabel('0-10')
        self.toughness_p = QtGui.QLabel('0-10')
        self.stiffness_p = QtGui.QLabel('0-50')
        self.num_p = QtGui.QLabel('0-20')
        self.weight_p = QtGui.QLabel('0-10')
        
        
        big_box_v = QtGui.QVBoxLayout()
        big_box_h = QtGui.QHBoxLayout()
        little_box_v1 = QtGui.QVBoxLayout()
        little_box_v2 = QtGui.QVBoxLayout()
        little_box_v3 = QtGui.QVBoxLayout()
        
        little_box_v1.addWidget(self.lab_speed)
        little_box_v1.addWidget(self.lab_toughness)
        little_box_v1.addWidget(self.lab_stiffness)
        little_box_v1.addWidget(self.lab_number_el)
        little_box_v1.addWidget(self.lab_weight)
        
        little_box_v2.addWidget(self.ed_speed)
        little_box_v2.addWidget(self.ed_toughness)
        little_box_v2.addWidget(self.ed_stiffness)
        little_box_v2.addWidget(self.ed_number_el)
        little_box_v2.addWidget(self.ed_weight)
        
        little_box_v3.addWidget(self.speed_p)
        little_box_v3.addWidget(self.toughness_p)
        little_box_v3.addWidget(self.stiffness_p)
        little_box_v3.addWidget(self.num_p)
        little_box_v3.addWidget(self.weight_p)
        
        big_box_h.addLayout(little_box_v1)
        big_box_h.addLayout(little_box_v2)
        
        big_box_v.addLayout(big_box_h)
        big_box_v.addWidget(btnStart)
        self.setLayout(big_box_v)
        
        QtCore.QObject.connect(btnStart, QtCore.SIGNAL("clicked()"), self.start_play)
        
    def start_play(self):
        play_rubber(int(self.ed_speed.text()),
                    int(self.ed_toughness.text()),
                    int(self.ed_stiffness.text()),
                    int(self.ed_number_el.text()),
                    int(self.ed_weight.text()))
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = window_rubber()
    window.show()
    sys.exit(app.exec_())