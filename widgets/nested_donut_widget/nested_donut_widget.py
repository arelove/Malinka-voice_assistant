__author__ = 'Ar3love'

from functools import partial
from random import randrange
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout
from PySide6 import QtCharts
from PySide6.QtGui import QPainter, QColor
import csv


class NestedDonut(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.create_nested_graph()

    def create_nested_graph(self):
        # Title Bar Axes and Legend
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chart_view.chart()

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.setTitle("График Продаж")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart.setTheme(QtCharts.QChart.ChartThemeDark)

        # set bar size policy
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.chart_view.sizePolicy().hasHeightForWidth())
        self.chart_view.setSizePolicy(sizePolicy)
        self.chart_view.setMinimumSize(QSize(0, 300))

        self.layout.addWidget(self.chart_view)

        self.setup_donuts()

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_rotation)
        self.update_timer.start(1000)

    def setup_donuts(self):
        self.donuts = []
        with open('unique_csv/stats.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Добавление данных в список
                # Предполагается, что каждая строка содержит два значения
                self.donuts.append((int(row[0]), int(row[1])))

        # Создание серии данных для графика
        self.max_size = 0.9
        self.min_size = 0.1

        s = 0
        for i, (value1, value2) in enumerate(self.donuts):
            donut = QtCharts.QPieSeries()
            first_blood = donut.append(f'Кол-во использований ассистента', value1)
            monster_kill = donut.append(f'Кол-во включений программы', value2)
            first_blood.setColor(QColor(120, 81, 169))
            monster_kill.setColor(QColor(83,55,122))
            for slice in donut.slices():
                slice.setLabelVisible(True)
                slice.setLabelColor(QColor(Qt.white))
                slice.setLabelPosition(QtCharts.QPieSlice.LabelInsideHorizontal)
                slice.hovered.connect(lambda exploded, slc=slice: self.exploded_slice(exploded, slc))

            size = (self.max_size - self.min_size) / len(self.donuts)
            donut.setHoleSize(self.min_size + s * size)
            donut.setPieSize(self.min_size + (s + 1) * size)
            self.chart.addSeries(donut)
            s += 1

    def update_rotation(self):
        for donut in self.chart.series():
            phase_shift = randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phase_shift)
            donut.setPieEndAngle(donut.pieEndAngle() + phase_shift)

    def exploded_slice(self, exploded, slc):
        if exploded:
            self.update_timer.stop()

            slice_startangle = slc.startAngle()
            slice_endangle = slc.startAngle() + slc.angleSpan()

            donut = slc.series()
            idx = self.chart.series().index(donut)
            for i in range(idx + 1, len(self.chart.series())):
                self.chart.series()[i].setPieStartAngle(slice_endangle)
                self.chart.series()[i].setPieEndAngle(360 + slice_startangle)
        else:
            for donut in self.chart.series():
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)
            self.update_timer.start()
            slc.setExploded(exploded)
