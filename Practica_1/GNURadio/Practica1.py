#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: PaulaJavier
# GNU Radio version: v3.10.11.0-89-ga17f69e7

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import Practica1_epy_block_0 as epy_block_0  # embedded python block
import sip
import threading



class Practica1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Practica1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self.media = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.media.set_update_time(0.10)
        self.media.set_title('Meda')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.media.set_min(i, -1)
            self.media.set_max(i, 1)
            self.media.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.media.set_label(i, "Data {0}".format(i))
            else:
                self.media.set_label(i, labels[i])
            self.media.set_unit(i, units[i])
            self.media.set_factor(i, factor[i])

        self.media.enable_autoscale(False)
        self._media_win = sip.wrapinstance(self.media.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._media_win)
        self.epy_block_0 = epy_block_0.blk()
        self.blocks_vector_source_x_0 = blocks.vector_source_f((1, 2, -1), True, 1, [])
        self.RMS = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.RMS.set_update_time(0.10)
        self.RMS.set_title('Valor RMS')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.RMS.set_min(i, -1)
            self.RMS.set_max(i, 1)
            self.RMS.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.RMS.set_label(i, "Data {0}".format(i))
            else:
                self.RMS.set_label(i, labels[i])
            self.RMS.set_unit(i, units[i])
            self.RMS.set_factor(i, factor[i])

        self.RMS.enable_autoscale(False)
        self._RMS_win = sip.wrapinstance(self.RMS.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._RMS_win)
        self.PotenciaPromedio = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.PotenciaPromedio.set_update_time(0.10)
        self.PotenciaPromedio.set_title('Potencia Promedio')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.PotenciaPromedio.set_min(i, -1)
            self.PotenciaPromedio.set_max(i, 1)
            self.PotenciaPromedio.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.PotenciaPromedio.set_label(i, "Data {0}".format(i))
            else:
                self.PotenciaPromedio.set_label(i, labels[i])
            self.PotenciaPromedio.set_unit(i, units[i])
            self.PotenciaPromedio.set_factor(i, factor[i])

        self.PotenciaPromedio.enable_autoscale(False)
        self._PotenciaPromedio_win = sip.wrapinstance(self.PotenciaPromedio.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._PotenciaPromedio_win)
        self.MediaCuadratica = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.MediaCuadratica.set_update_time(0.10)
        self.MediaCuadratica.set_title('Media cuadratica')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.MediaCuadratica.set_min(i, -1)
            self.MediaCuadratica.set_max(i, 1)
            self.MediaCuadratica.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.MediaCuadratica.set_label(i, "Data {0}".format(i))
            else:
                self.MediaCuadratica.set_label(i, labels[i])
            self.MediaCuadratica.set_unit(i, units[i])
            self.MediaCuadratica.set_factor(i, factor[i])

        self.MediaCuadratica.enable_autoscale(False)
        self._MediaCuadratica_win = sip.wrapinstance(self.MediaCuadratica.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._MediaCuadratica_win)
        self.DesviacionEstandar = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.DesviacionEstandar.set_update_time(0.10)
        self.DesviacionEstandar.set_title('Desviacion Estandar')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.DesviacionEstandar.set_min(i, -1)
            self.DesviacionEstandar.set_max(i, 1)
            self.DesviacionEstandar.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.DesviacionEstandar.set_label(i, "Data {0}".format(i))
            else:
                self.DesviacionEstandar.set_label(i, labels[i])
            self.DesviacionEstandar.set_unit(i, units[i])
            self.DesviacionEstandar.set_factor(i, factor[i])

        self.DesviacionEstandar.enable_autoscale(False)
        self._DesviacionEstandar_win = sip.wrapinstance(self.DesviacionEstandar.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._DesviacionEstandar_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_source_x_0, 0), (self.epy_block_0, 0))
        self.connect((self.epy_block_0, 4), (self.DesviacionEstandar, 0))
        self.connect((self.epy_block_0, 1), (self.MediaCuadratica, 0))
        self.connect((self.epy_block_0, 3), (self.PotenciaPromedio, 0))
        self.connect((self.epy_block_0, 2), (self.RMS, 0))
        self.connect((self.epy_block_0, 0), (self.media, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Practica1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=Practica1, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
