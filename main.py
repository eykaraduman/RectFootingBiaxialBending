from fbs_runtime.application_context import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize

import os
import sys
from configparser import ConfigParser

from AppUi import Ui_AppFrame
from RectFootingPressDistribution import RectFootingPressDistribution

class RectFootingApp(QtWidgets.QFrame, Ui_AppFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        Ui_AppFrame.__init__(self)
        self.setFixedSize(QSize(495, 495))
        self.setupUi(self)
        image_profile = QtGui.QImage("images/biaxialbend.png")  # QImage object
        image_profile = image_profile.scaled(350,200,
                                             aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                             transformMode=QtCore.Qt.SmoothTransformation)

        self.figure.setPixmap(QtGui.QPixmap.fromImage(image_profile))

        self.figure.show()

        self.te_n.setValue(400.00)
        self.te_mx.setValue(120.00)
        self.te_my.setValue(150.00)
        self.te_lx.setValue(2.5)
        self.te_ly.setValue(1.5)
        self.te_x.setValue(1.25)
        self.te_y.setValue(0.75)

        self.btnHesapla.clicked.connect(self.btnHesapla_clicked)
        self.btnDosyadanHesapla.clicked.connect(self.btnDosyadanHesapla_clicked)
        self.btn_ger_xy_hesapla.clicked.connect(self.btn_ger_xy_hesapla_clicked)
        self.btnYardim.clicked.connect(self.btnYardim_clicked)

    def cikti_olustur(self, rf:RectFootingPressDistribution):
        self.te_result.clear()
        self.te_result.append('Eksantiriste Bölge = {0}'.format(rf.eccentricity_region.name))
        self.te_result.append('N={0:0.2f} tm, Mx={1:0.2f} tm, My={2:0.2f} tm'.format(rf.p, rf.mx, rf.my))
        self.te_result.append('Lx={0:0.2f} m, Ly={1:0.2f} m'.format(rf.lx, rf.ly))
        self.te_result.append('ex={0:0.4f}, ey={1:0.4f}'.format(rf.ex, rf.ey))
        self.te_result.append('Xn={0:0.4f} m, Yn={1:0.4f} m, Xq={2:0.4f} m, Yp={3:0.4f} m'.format(rf.xn, rf.yn, rf.xq, rf.yp))
        self.te_result.append('σo={0:0.4f} t/m², σp={1:0.4f} t/m², σr={2:0.4f} t/m², σq={3:0.4f} t/m²'.format(rf.po, rf.pp, rf.pr, rf.pq))
        self.te_result.append('σ1={0:0.4f} t/m², σ2={1:0.4f} t/m², σ3={2:0.4f} t/m², σ4={3:0.4f} t/m²'.format(rf.p1, rf.p2, rf.p3, rf.p4))


    def btnHesapla_clicked(self):
        rf = RectFootingPressDistribution("", self.te_n.value(), self.te_mx.value(), self.te_my.value(), self.te_lx.value(), self.te_ly.value())
        self.cikti_olustur(rf)


    def btnDosyadanHesapla_clicked(self):
        try:
            # select config file
            ini_file_path= \
            QtWidgets.QFileDialog.getOpenFileName(self.parent(), 'Dosya aç', '', "Hesap bilgi dosyası (*.ini)",
                                                  options=QtWidgets.QFileDialog.Options())[0]
            if ini_file_path == '':
                return

            # create output file path
            dir = os.path.dirname(ini_file_path)
            output_file_name = os.path.splitext(os.path.basename(ini_file_path))[0]
            output_file_path = r'{0}/{1}.{2}'.format(dir, output_file_name, 'txt')
            f = open(output_file_path, "w+")

            # parse .ini file and create output .txt file
            parser = ConfigParser()
            parser.read(ini_file_path, encoding="utf-8-sig")
            lx = float(parser.get('Boyutlar', 'Lx'))
            ly = float(parser.get('Boyutlar', 'Ly'))
            yukler = list(parser.items('Yukler'))
            kesitler = list(parser.items('Kesitler'))

            f.write('{:-<112}\n'.format('-'))
            f.write(
                '|{:<25}|{:^8}|{:^8}|{:^14}|{:^14}|{:^14}|{:^10}|{:^10}|\n'.format('Hal Ad', 'Lx (m)', 'Ly (m)', 'N(t)', 'Mx(tm)', 'My(tm)', 'ex', 'ey'))
            f.write('{:-<112}\n'.format('-'))
            for i in yukler:
                val = i[1].split(',')
                hal = val[0]; n = float(val[1]); mx = float(val[2]); my = float(val[3])
                rf = RectFootingPressDistribution(hal, n, mx, my, lx, ly)
                f.write('|{:<25}|{:^8.2f}|{:^8.2f}|{:^14.4f}|{:^14.4f}|{:^14.4f}|{:^10.4f}|{:^10.4f}|\n'.format(rf.name, rf.lx, rf.ly, rf.p, rf.mx, rf.my, rf.ex, rf.ey))
            f.write('{:-<112}\n\n'.format('-'))
            f.write('{:-<163}\n'.format('-'))
            f.write('|{:<25}|{:^15}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|\n'.format('Hal Ad', 'Basınç Bölge', 'Xn (m)', 'Yn (m)', 'Xq(m)','Yp(m)', 's1(t/m²)', 's2(t/m²)', 's3(t/m²)', 's4(t/m²)'))
            f.write('{:-<163}\n'.format('-'))
            for i in yukler:
                val = i[1].split(',')
                hal = val[0]; n = float(val[1]); mx = float(val[2]); my = float(val[3])
                rf = RectFootingPressDistribution(hal, n, mx, my, lx, ly)
                f.write('|{:<25}|{:^15}|{:^14.2f}|{:^14.2f}|{:^14.4f}|{:^14.4f}|{:^14.4f}|{:^14.4f}|{:^14.4f}|{:^14.4f}|\n'.format(rf.name, rf.eccentricity_region.name, rf.xn, rf.yn, rf.xq, rf.yp, rf.p1, rf.p2, rf.p3, rf.p4))
            f.write('{:-<163}\n'.format('-'))

            for j in kesitler:
                ad = j[0]; kesit = j[1].split(',')
                x = float(kesit[0]); y = float(kesit[1])
                f.write('\nKesit-{}\n'.format(ad))
                f.write('{:-<42}\n'.format('-'))
                f.write('|{:<25}|{:^14}|\n'.format('Hal Ad','Gerilme (t/m²)'))
                f.write('{:-<42}\n'.format('-'))
                for i in yukler:
                    val = i[1].split(',')
                    hal = val[0]; n = float(val[1]); mx = float(val[2]); my = float(val[3])
                    rf = RectFootingPressDistribution(hal, n, mx, my, lx, ly)
                    f.write('|{:<25}|{:^14.2f}|\n'.format(hal, rf.pressure_at_point(x, y)))
                f.write('{:-<42}\n'.format('-'))
            f.close()
            os.startfile(output_file_path)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.parent(), 'Hata', e.message, QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
        finally:
            pass

    def btn_ger_xy_hesapla_clicked(self):
        rf = RectFootingPressDistribution("", self.te_n.value(), self.te_mx.value(), self.te_my.value(),
                                          self.te_lx.value(), self.te_ly.value())
        self.cikti_olustur(rf)
        ger = rf.pressure_at_point( self.te_x.value(), self.te_y.value())
        self.te_xy_ger.setValue(0.00) if ger < 0.0 else self.te_xy_ger.setValue(ger)

    def btnYardim_clicked(self):
        os.startfile('help.pdf')
        pass

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        window = RectFootingApp()
        # window = QMainWindow()
        version = self.build_settings['version']
        # window.setWindowTitle("MyApp v" + version)
        # window.resize(250, 150)
        window.show()
        return self.app.exec_()                 # 3. End run() with this line

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)