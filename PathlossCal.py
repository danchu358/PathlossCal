import os
import sys
import pandas as pd
import numpy as np
import glob
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication

site0 = 0
site1 = 0
site2 = 0
site3 = 0
site4 = 0
site5 = 0
site6 = 0
site7 = 0
site8 = 0
site9 = 0
site10 = 0
site11 = 0
site12 = 0
site13 = 0
site14 = 0
site15 = 0

#------------------------------------------------------------------------- ui 파일 load
Ui_Form = uic.loadUiType("ui_open2.ui")[0]

#------------------------------------------------------------------------- 현재 폴더 위치 및 pathloss 파일 위치 불러오기
folder_address = os.path.dirname(os.path.realpath(__file__))
# filepath_pass = glob.glob('**/Path_loss_ATE0.csv', recursive=True)

#------------------------------------------------------------------------- class 선언
class GroupBoxWindow(QtWidgets.QMainWindow, QPushButton, Ui_Form):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pathloss")
        self.setGeometry(600, 300, 600, 400)
        self.setWindowIcon(QIcon("Pathloss_icon_small.png"))

        groupBox = QGroupBox("Pathloss", self)
        groupBox.move(10, 10)
        groupBox.resize(150, 80)

        btn_open = QPushButton("Open file", self)
        btn_open.move(30, 35)
        btn_open.toggle()
        btn_open.clicked.connect(self.fileopen)

        btn_open2 = QPushButton("Cal", self)
        btn_open2.move(200, 350)
        btn_open2.resize(200, 30)
        btn_open2.toggle()
        btn_open2.clicked.connect(self.losscal)

        self.pathLabel = QLabel(self)
        self.pathLabel.setGeometry(100, 80, 400, 50)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(100, 130, 400, 200)

#------------------------------------------------------------------------- fileopen button click 이후 동작
    def fileopen(self):

        global filename
        global site0, site1, site2, site3, site4, site5, site6, site7, site8, site9, site10, site11, site12, site13, site14, site15

        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/21052/Desktop', 'All File(*);; html File(*.html *.htm)')

        if filename[0]:

            site, ok = QInputDialog.getText(self, 'Input Site', 'Enter:')

            global log_core0
            global log_core1

            if ok:
                self.textEdit.append(str('site') + str(site))  

            # ========================================================== OI_log.txt 파일 불러오기
            df = pd.read_csv(filename[0], names = ['Test_Results'] ,sep="\t",encoding='utf-8')

            # ========================================================== result 열을 만들기 29번째 문자 추출
            df['result'] = df.Test_Results.str.split(' ').str[29]

            # ========================================================== list로 만들기
            df_list = df['result'].values.tolist()

            # ========================================================== list에서 NAN 제거
            cleanedList = [x for x in df_list if str(x) != 'nan']

            # ========================================================== list에서 공백 제거
            remove_set = {''}
            val_List = [i for i in cleanedList if i not in remove_set]

            # ========================================================== list에서 각 요소에서 출력 값 분리
            for i in range(0, 32):
                globals()["TxList{}".format(i + 1)] = val_List[i].split(',')

            del TxList1[1:3]
            del TxList2[1:3]
            del TxList3[1:3]
            del TxList4[1:3]
            del TxList5[1:3]
            del TxList6[1:3]
            del TxList7[1:3]
            del TxList8[1:3]
            del TxList9[1:3]
            del TxList10[1:3]
            del TxList11[1:3]
            del TxList12[1:3]
            del TxList13[1:3]
            del TxList14[1:3]
            del TxList15[1:3]
            del TxList16[1:3]
            del TxList17[1:3]
            del TxList18[1:3]
            del TxList19[1:3]
            del TxList20[1:3]
            del TxList21[1:3]
            del TxList22[1:3]
            del TxList23[1:3]
            del TxList24[1:3]
            del TxList25[1:3]
            del TxList26[1:3]
            del TxList27[1:3]
            del TxList28[1:3]
            del TxList29[1:3]
            del TxList30[1:3]
            del TxList31[1:3]
            del TxList32[1:3]

            # ========================================================== core0, core1 만들기
            log_core0 = list()
            log_core1 = list()

            log_core0 = (TxList1 + TxList3 + TxList5 + TxList7 + TxList9 + TxList11 + TxList13 + TxList15 + TxList17 + TxList19 + TxList21 +
            TxList23 + TxList25 + TxList27 + TxList29 +TxList31 + TxList31)
            log_core1 = (TxList2 + TxList4 + TxList6 + TxList8 + TxList10 + TxList12 + TxList14 + TxList16 + TxList18 + TxList20 + TxList22 + TxList24
            + TxList26 + TxList28 + TxList30 + TxList32 + TxList32)

            # ========================================================== list 문자열 float로 만들기
            log_core0 = list(map(float, log_core0))
            log_core1 = list(map(float, log_core1))

            log_core0 = np.round(log_core0, 2)
            log_core1 = np.round(log_core1, 2)

            # ========================================================== list 파일 DataFrame으로 만들기
            Core_0 = pd.DataFrame(log_core0)
            Core_1 = pd.DataFrame(log_core1)

            log_OI =pd.concat([Core_0, Core_1], axis = 1)
            # log_OI_list = log_OI.values.tolist()
            print(log_OI)


        else:
            QMessageBox.about(self, '파일을 선택하지 않았습니다.')

        if site == '0':
            site0 += 1   
        if site == '1':
            site1 += 1
        if site == '2':
            site2 += 1
        if site == '3':
            site3 += 1
        if site == '4':
            site4 += 1
        if site == '5':
            site5 += 1
        if site == '6':
            site6 += 1
        if site == '7':
            site7 += 1
        if site == '8':
            site8 += 1
        if site == '9':
            site9 += 1
        if site == '10':
            site10 += 1
        if site == '11':
            site11 += 1
        if site == '12':
            site12 += 1
        if site == '13':
            site13 += 1
        if site == '14':
            site14 += 1
        if site == '15':
            site15 += 1  
        
    def losscal(self):
        # ==========================================================
        # oi_log = pd.read_csv('C:/Users/21052/Desktop/chip_loss.csv', names = ['results'], sep="\t", encoding='utf-8')
        # dut0_pathloss = pd.read_csv('C:/Users/21052/Desktop/Path_loss_ATE0.csv', names = ['results'], sep="\t", encoding='utf-8')
        # dut0_pathloss_copy = pd.read_csv('C:/Users/21052/Desktop/Path_loss_ATE0.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')

        oi_log = pd.read_csv('chip_loss.csv', names = ['results'], sep="\t", encoding='utf-8')

        if site0 == 1:
            dut0_pathloss = pd.read_csv('Dut0\Path_loss_ATE0.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut0_pathloss_copy = pd.read_csv('Dut0\Path_loss_ATE0.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut0_pathloss_copy.to_csv('Dut0\Path_loss_ATE0_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site1 == 1:
            dut1_pathloss = pd.read_csv('Dut1\Path_loss_ATE1.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut1_pathloss_copy = pd.read_csv('Dut1\Path_loss_ATE1.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut1_pathloss_copy.to_csv('Dut1\Path_loss_ATE1_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site2 == 1:
            dut2_pathloss = pd.read_csv('Dut2\Path_loss_ATE2.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut2_pathloss_copy = pd.read_csv('Dut2\Path_loss_ATE2.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut2_pathloss_copy.to_csv('Dut2\Path_loss_ATE2_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site3 == 1:
            dut3_pathloss = pd.read_csv('Dut3\Path_loss_ATE3.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut3_pathloss_copy = pd.read_csv('Dut3\Path_loss_ATE3.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut3_pathloss_copy.to_csv('Dut3\Path_loss_ATE3_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site4 == 1:
            dut4_pathloss = pd.read_csv('Dut4\Path_loss_ATE4.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut4_pathloss_copy = pd.read_csv('Dut4\Path_loss_ATE4.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut4_pathloss_copy.to_csv('Dut4\Path_loss_ATE4_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site5 == 1:
            dut5_pathloss = pd.read_csv('Dut5\Path_loss_ATE5.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut5_pathloss_copy = pd.read_csv('Dut5\Path_loss_ATE5.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut5_pathloss_copy.to_csv('Dut5\Path_loss_ATE5_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site6 == 1:
            dut6_pathloss = pd.read_csv('Dut6\Path_loss_ATE6.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut6_pathloss_copy = pd.read_csv('Dut6\Path_loss_ATE6.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut6_pathloss_copy.to_csv('Dut6\Path_loss_ATE6_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site7 == 1:
            dut7_pathloss = pd.read_csv('Dut7\Path_loss_ATE7.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut7_pathloss_copy = pd.read_csv('Dut7\Path_loss_ATE7.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut7_pathloss_copy.to_csv('Dut7\Path_loss_ATE7_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site8 == 1:
            dut8_pathloss = pd.read_csv('Dut8\Path_loss_ATE8.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut8_pathloss_copy = pd.read_csv('Dut8\Path_loss_ATE8.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut8_pathloss_copy.to_csv('Dut8\Path_loss_ATE8_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site9 == 1:
            dut9_pathloss = pd.read_csv('Dut9\Path_loss_ATE9.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut9_pathloss_copy = pd.read_csv('Dut9\Path_loss_ATE9.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut9_pathloss_copy.to_csv('Dut9\Path_loss_ATE9_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site10 == 1:
            dut10_pathloss = pd.read_csv('Dut10\Path_loss_ATE10.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut10_pathloss_copy = pd.read_csv('Dut10\Path_loss_ATE10.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut10_pathloss_copy.to_csv('Dut10\Path_loss_ATE10_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site11 == 1:
            dut11_pathloss = pd.read_csv('Dut11\Path_loss_ATE11.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut11_pathloss_copy = pd.read_csv('Dut11\Path_loss_ATE11.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut11_pathloss_copy.to_csv('Dut11\Path_loss_ATE11_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site12 == 1:
            dut12_pathloss = pd.read_csv('Dut12\Path_loss_ATE12.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut12_pathloss_copy = pd.read_csv('Dut12\Path_loss_ATE12.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut12_pathloss_copy.to_csv('Dut12\Path_loss_ATE12_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site13 == 1:
            dut13_pathloss = pd.read_csv('Dut13\Path_loss_ATE13.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut13_pathloss_copy = pd.read_csv('Dut13\Path_loss_ATE13.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut13_pathloss_copy.to_csv('Dut13\Path_loss_ATE13_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site14 == 1:
            dut14_pathloss = pd.read_csv('Dut14\Path_loss_ATE14.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut14_pathloss_copy = pd.read_csv('Dut14\Path_loss_ATE14.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut14_pathloss_copy.to_csv('Dut14\Path_loss_ATE14_copy.csv', index=False, header=False)
        else:
            print('Nothing')

        if site15 == 1:
            dut15_pathloss = pd.read_csv('Dut15\Path_loss_ATE15.csv', names = ['results'], sep="\t", encoding='utf-8')
            dut15_pathloss_copy = pd.read_csv('Dut15\Path_loss_ATE15.csv', names = ['ch','core0','core1'], sep=",", encoding='utf-8')
        # ========================================================== Pathloss.csv 복사본 저장
            dut15_pathloss_copy.to_csv('Dut15\Path_loss_ATE15_copy.csv', index=False, header=False)
        else:
            print('Nothing')       

        # ========================================================== chip_loss data parser
        oi_sp = oi_log.results.str.split(',')
        print(oi_sp)

        # ========================================================== chip_loss data parser_site0_core0
        for i in range(1, 17):
            globals()["site0_core0_{}".format(i)] = oi_sp[i+1][1]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site0_core0_list = list()

        for i in range(1, 17):
            site0_core0_list.append(eval('site0_core0_'+str(i)))

        site0_core0_list.append(site0_core0_list[-1])

        site0_core0_list = list(map(float, site0_core0_list))
        # site0_core0_df = pd.DataFrame(site0_core0_list)

        # ========================================================== chip_loss data parser_site0_core1
        for i in range(1, 17):
            globals()["site0_core1_{}".format(i)] = oi_sp[i+1][2]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site0_core1_list = list()

        for i in range(1, 17):
            site0_core1_list.append(eval('site0_core1_'+str(i)))

        site0_core1_list.append(site0_core1_list[-1])

        site0_core1_list = list(map(float, site0_core1_list))
        # site0_core1_df = pd.DataFrame(site0_core1_list)

        # ========================================================== chip_loss data parser_site1_core0
        for i in range(1, 17):
            globals()["site1_core0_{}".format(i)] = oi_sp[i+1][3]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site1_core0_list = list()

        for i in range(1, 17):
            site1_core0_list.append(eval('site1_core0_'+str(i)))

        site1_core0_list.append(site1_core0_list[-1])

        site1_core0_list = list(map(float, site1_core0_list))
        # site1_core0_df = pd.DataFrame(site1_core0_list)

        # ========================================================== chip_loss data parser_site1_core1
        for i in range(1, 17):
            globals()["site1_core1_{}".format(i)] = oi_sp[i+1][4]

        # ========================================================== chip_loss data parser_list로 만들기
        site1_core1_list = list()

        for i in range(1, 17):
            site1_core1_list.append(eval('site1_core1_'+str(i)))

        site1_core1_list.append(site1_core1_list[-1])

        site1_core1_list = list(map(float, site1_core1_list))
        # site1_core1_df = pd.DataFrame(site1_core1_list)

        # ========================================================== chip_loss data parser_site2_core0
        for i in range(1, 17):
            globals()["site2_core0_{}".format(i)] = oi_sp[i+1][5]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site2_core0_list = list()

        for i in range(1, 17):
            site2_core0_list.append(eval('site2_core0_'+str(i)))

        site2_core0_list.append(site2_core0_list[-1])

        site2_core0_list = list(map(float, site2_core0_list))
        # site2_core0_df = pd.DataFrame(site2_core0_list)

        # ========================================================== chip_loss data parser_site2_core1
        for i in range(1, 17):
            globals()["site2_core1_{}".format(i)] = oi_sp[i+1][6]

        # ========================================================== chip_loss data parser_list로 만들기
        site2_core1_list = list()

        for i in range(1, 17):
            site2_core1_list.append(eval('site2_core1_'+str(i)))

        site2_core1_list.append(site2_core1_list[-1])

        site2_core1_list = list(map(float, site2_core1_list))
        # site2_core1_df = pd.DataFrame(site2_core1_list)

        # ========================================================== chip_loss data parser_site3_core0
        for i in range(1, 17):
            globals()["site3_core0_{}".format(i)] = oi_sp[i+1][7]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site3_core0_list = list()

        for i in range(1, 17):
            site3_core0_list.append(eval('site3_core0_'+str(i)))

        site3_core0_list.append(site3_core0_list[-1])

        site3_core0_list = list(map(float, site3_core0_list))
        # site3_core0_df = pd.DataFrame(site3_core0_list)

        # ========================================================== chip_loss data parser_site3_core1
        for i in range(1, 17):
            globals()["site3_core1_{}".format(i)] = oi_sp[i+1][8]

        # ========================================================== chip_loss data parser_list로 만들기
        site3_core1_list = list()

        for i in range(1, 17):
            site3_core1_list.append(eval('site3_core1_'+str(i)))

        site3_core1_list.append(site3_core1_list[-1])

        site3_core1_list = list(map(float, site3_core1_list))
        # site3_core1_df = pd.DataFrame(site3_core1_list)

        # ========================================================== chip_loss data parser_site4_core0
        for i in range(1, 17):
            globals()["site4_core0_{}".format(i)] = oi_sp[i+1][9]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site4_core0_list = list()

        for i in range(1, 17):
            site4_core0_list.append(eval('site4_core0_'+str(i)))

        site4_core0_list.append(site4_core0_list[-1])

        site4_core0_list = list(map(float, site4_core0_list))
        # site4_core0_df = pd.DataFrame(site4_core0_list)

        # ========================================================== chip_loss data parser_site4_core1
        for i in range(1, 17):
            globals()["site4_core1_{}".format(i)] = oi_sp[i+1][10]

        # ========================================================== chip_loss data parser_list로 만들기
        site4_core1_list = list()

        for i in range(1, 17):
            site4_core1_list.append(eval('site4_core1_'+str(i)))

        site4_core1_list.append(site4_core1_list[-1])

        site4_core1_list = list(map(float, site4_core1_list))
        # site4_core1_df = pd.DataFrame(site4_core1_list)

        # ========================================================== chip_loss data parser_site5_core0
        for i in range(1, 17):
            globals()["site5_core0_{}".format(i)] = oi_sp[i+1][11]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site5_core0_list = list()

        for i in range(1, 17):
            site5_core0_list.append(eval('site5_core0_'+str(i)))

        site5_core0_list.append(site5_core0_list[-1])

        site5_core0_list = list(map(float, site5_core0_list))
        # site5_core0_df = pd.DataFrame(site5_core0_list)

        # ========================================================== chip_loss data parser_site5_core1
        for i in range(1, 17):
            globals()["site5_core1_{}".format(i)] = oi_sp[i+1][12]

        # ========================================================== chip_loss data parser_list로 만들기
        site5_core1_list = list()

        for i in range(1, 17):
            site5_core1_list.append(eval('site5_core1_'+str(i)))

        site5_core1_list.append(site5_core1_list[-1])

        site5_core1_list = list(map(float, site5_core1_list))
        # site5_core1_df = pd.DataFrame(site5_core1_list)

        # ========================================================== chip_loss data parser_site6_core0
        for i in range(1, 17):
            globals()["site6_core0_{}".format(i)] = oi_sp[i+1][13]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site6_core0_list = list()

        for i in range(1, 17):
            site6_core0_list.append(eval('site6_core0_'+str(i)))

        site6_core0_list.append(site6_core0_list[-1])

        site6_core0_list = list(map(float, site6_core0_list))
        # site6_core0_df = pd.DataFrame(site6_core0_list)

        # ========================================================== chip_loss data parser_site6_core1
        for i in range(1, 17):
            globals()["site6_core1_{}".format(i)] = oi_sp[i+1][14]

        # ========================================================== chip_loss data parser_list로 만들기
        site6_core1_list = list()

        for i in range(1, 17):
            site6_core1_list.append(eval('site6_core1_'+str(i)))

        site6_core1_list.append(site6_core1_list[-1])

        site6_core1_list = list(map(float, site6_core1_list))
        # site6_core1_df = pd.DataFrame(site6_core1_list)

        # ========================================================== chip_loss data parser_site7_core0
        for i in range(1, 17):
            globals()["site7_core0_{}".format(i)] = oi_sp[i+1][15]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site7_core0_list = list()

        for i in range(1, 17):
            site7_core0_list.append(eval('site7_core0_'+str(i)))

        site7_core0_list.append(site7_core0_list[-1])

        site7_core0_list = list(map(float, site7_core0_list))
        # site7_core0_df = pd.DataFrame(site7_core0_list)

        # ========================================================== chip_loss data parser_site7_core1
        for i in range(1, 17):
            globals()["site7_core1_{}".format(i)] = oi_sp[i+1][16]

        # ========================================================== chip_loss data parser_list로 만들기
        site7_core1_list = list()

        for i in range(1, 17):
            site7_core1_list.append(eval('site7_core1_'+str(i)))

        site7_core1_list.append(site7_core1_list[-1])

        site7_core1_list = list(map(float, site7_core1_list))
        # site7_core1_df = pd.DataFrame(site7_core1_list)

        # ========================================================== chip_loss data parser_site8_core0
        for i in range(1, 17):
            globals()["site8_core0_{}".format(i)] = oi_sp[i+1][17]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site8_core0_list = list()

        for i in range(1, 17):
            site8_core0_list.append(eval('site8_core0_'+str(i)))

        site8_core0_list.append(site8_core0_list[-1])

        site8_core0_list = list(map(float, site8_core0_list))
        # site8_core0_df = pd.DataFrame(site8_core0_list)

        # ========================================================== chip_loss data parser_site8_core1
        for i in range(1, 17):
            globals()["site8_core1_{}".format(i)] = oi_sp[i+1][18]

        # ========================================================== chip_loss data parser_list로 만들기
        site8_core1_list = list()

        for i in range(1, 17):

            site8_core1_list.append(eval('site8_core1_'+str(i)))

        site8_core1_list.append(site8_core1_list[-1])

        site8_core1_list = list(map(float, site8_core1_list))
        # site8_core1_df = pd.DataFrame(site8_core1_list)

        # ========================================================== chip_loss data parser_site9_core0
        for i in range(1, 17):
            globals()["site9_core0_{}".format(i)] = oi_sp[i+1][19]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site9_core0_list = list()

        for i in range(1, 17):
            site9_core0_list.append(eval('site9_core0_'+str(i)))

        site9_core0_list.append(site9_core0_list[-1])

        site9_core0_list = list(map(float, site9_core0_list))
        # site9_core0_df = pd.DataFrame(site9_core0_list)

        # ========================================================== chip_loss data parser_site9_core1
        for i in range(1, 17):
            globals()["site9_core1_{}".format(i)] = oi_sp[i+1][20]

        # ========================================================== chip_loss data parser_list로 만들기
        site9_core1_list = list()

        for i in range(1, 17):
            site9_core1_list.append(eval('site9_core1_'+str(i)))

        site9_core1_list.append(site9_core1_list[-1])

        site9_core1_list = list(map(float, site9_core1_list))
        # site9_core1_df = pd.DataFrame(site9_core1_list)

        # ========================================================== chip_loss data parser_site10_core0
        for i in range(1, 17):
            globals()["site10_core0_{}".format(i)] = oi_sp[i+1][21]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site10_core0_list = list()

        for i in range(1, 17):
            site10_core0_list.append(eval('site10_core0_'+str(i)))

        site10_core0_list.append(site10_core0_list[-1])

        site10_core0_list = list(map(float, site10_core0_list))
        # site10_core0_df = pd.DataFrame(site10_core0_list)

        # ========================================================== chip_loss data parser_site10_core1
        for i in range(1, 17):
            globals()["site10_core1_{}".format(i)] = oi_sp[i+1][22]

        # ========================================================== chip_loss data parser_list로 만들기
        site10_core1_list = list()

        for i in range(1, 17):
            site10_core1_list.append(eval('site10_core1_'+str(i)))

        site10_core1_list.append(site10_core1_list[-1])

        site10_core1_list = list(map(float, site10_core1_list))
        # site10_core1_df = pd.DataFrame(site10_core1_list)

        # ========================================================== chip_loss data parser_site11_core0
        for i in range(1, 17):
            globals()["site11_core0_{}".format(i)] = oi_sp[i+1][23]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site11_core0_list = list()

        for i in range(1, 17):
            site11_core0_list.append(eval('site11_core0_'+str(i)))

        site11_core0_list.append(site11_core0_list[-1])

        site11_core0_list = list(map(float, site11_core0_list))
        # site11_core0_df = pd.DataFrame(site11_core0_list)

        # ========================================================== chip_loss data parser_site11_core1
        for i in range(1, 17):
            globals()["site11_core1_{}".format(i)] = oi_sp[i+1][24]

        # ========================================================== chip_loss data parser_list로 만들기
        site11_core1_list = list()

        for i in range(1, 17):
            site11_core1_list.append(eval('site11_core1_'+str(i)))

        site11_core1_list.append(site11_core1_list[-1])

        site11_core1_list = list(map(float, site11_core1_list))
        # site11_core1_df = pd.DataFrame(site11_core1_list)

        # ========================================================== chip_loss data parser_site12_core0
        for i in range(1, 17):
            globals()["site12_core0_{}".format(i)] = oi_sp[i+1][25]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site12_core0_list = list()

        for i in range(1, 17):
            site12_core0_list.append(eval('site12_core0_'+str(i)))

        site12_core0_list.append(site12_core0_list[-1])

        site12_core0_list = list(map(float, site12_core0_list))
        # site12_core0_df = pd.DataFrame(site12_core0_list)

        # ========================================================== chip_loss data parser_site12_core1
        for i in range(1, 17):
            globals()["site12_core1_{}".format(i)] = oi_sp[i+1][26]

        # ========================================================== chip_loss data parser_list로 만들기
        site12_core1_list = list()

        for i in range(1, 17):
            site12_core1_list.append(eval('site12_core1_'+str(i)))

        site12_core1_list.append(site12_core1_list[-1])

        site12_core1_list = list(map(float, site12_core1_list))
        # site12_core1_df = pd.DataFrame(site12_core1_list)

        # ========================================================== chip_loss data parser_site13_core0
        for i in range(1, 17):
            globals()["site13_core0_{}".format(i)] = oi_sp[i+1][27]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site13_core0_list = list()

        for i in range(1, 17):
            site13_core0_list.append(eval('site13_core0_'+str(i)))

        site13_core0_list.append(site13_core0_list[-1])

        site13_core0_list = list(map(float, site13_core0_list))
        # site13_core0_df = pd.DataFrame(site13_core0_list)

        # ========================================================== chip_loss data parser_site13_core1
        for i in range(1, 17):
            globals()["site13_core1_{}".format(i)] = oi_sp[i+1][28]

        # ========================================================== chip_loss data parser_list로 만들기
        site13_core1_list = list()

        for i in range(1, 17):

            site13_core1_list.append(eval('site13_core1_'+str(i)))

        site13_core1_list.append(site13_core1_list[-1])

        site13_core1_list = list(map(float, site13_core1_list))
        # site13_core1_df = pd.DataFrame(site13_core1_list)

        # ========================================================== chip_loss data parser_site14_core0
        for i in range(1, 17):
            globals()["site14_core0_{}".format(i)] = oi_sp[i+1][29]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site14_core0_list = list()

        for i in range(1, 17):
            site14_core0_list.append(eval('site14_core0_'+str(i)))

        site14_core0_list.append(site14_core0_list[-1])

        site14_core0_list = list(map(float, site14_core0_list))
        # site14_core0_df = pd.DataFrame(site14_core0_list)

        # ========================================================== chip_loss data parser_site14_core1
        for i in range(1, 17):
            globals()["site14_core1_{}".format(i)] = oi_sp[i+1][30]

        # ========================================================== chip_loss data parser_list로 만들기
        site14_core1_list = list()

        for i in range(1, 17):
            site14_core1_list.append(eval('site14_core1_'+str(i)))

        site14_core1_list.append(site14_core1_list[-1])

        site14_core1_list = list(map(float, site14_core1_list))
        # site14_core1_df = pd.DataFrame(site14_core1_list)

        # ========================================================== chip_loss data parser_site15_core0
        for i in range(1, 17):
            globals()["site15_core0_{}".format(i)] = oi_sp[i+1][31]

        # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
        site15_core0_list = list()

        for i in range(1, 17):
            site15_core0_list.append(eval('site15_core0_'+str(i)))

        site15_core0_list.append(site15_core0_list[-1])

        site15_core0_list = list(map(float, site15_core0_list))
        # site15_core0_df = pd.DataFrame(site15_core0_list)

        # ========================================================== chip_loss data parser_site15_core1
        for i in range(1, 17):
            globals()["site15_core1_{}".format(i)] = oi_sp[i+1][32]

        # ========================================================== chip_loss data parser_list로 만들기
        site15_core1_list = list()

        for i in range(1, 17):
            site15_core1_list.append(eval('site15_core1_'+str(i)))

        site15_core1_list.append(site15_core1_list[-1])

        site15_core1_list = list(map(float, site15_core1_list))
        # site15_core1_df = pd.DataFrame(site15_core1_list)

        # ========================================================== chip_loss data parser core0, core1 합치기
        # site0_df =pd.concat([site0_core0_df, site0_core1_df], axis = 1)
        # site1_df =pd.concat([site1_core0_df, site1_core1_df], axis = 1)
        # site2_df =pd.concat([site2_core0_df, site2_core1_df], axis = 1)
        # site3_df =pd.concat([site3_core0_df, site3_core1_df], axis = 1)
        # site4_df =pd.concat([site4_core0_df, site4_core1_df], axis = 1)
        # site5_df =pd.concat([site5_core0_df, site5_core1_df], axis = 1)
        # site6_df =pd.concat([site6_core0_df, site6_core1_df], axis = 1)
        # site7_df =pd.concat([site7_core0_df, site7_core1_df], axis = 1)
        # site8_df =pd.concat([site8_core0_df, site8_core1_df], axis = 1)
        # site9_df =pd.concat([site9_core0_df, site9_core1_df], axis = 1)
        # site10_df =pd.concat([site10_core0_df, site10_core1_df], axis = 1)
        # site11_df =pd.concat([site11_core0_df, site11_core1_df], axis = 1)
        # site12_df =pd.concat([site12_core0_df, site12_core1_df], axis = 1)
        # site13_df =pd.concat([site13_core0_df, site13_core1_df], axis = 1)
        # site14_df =pd.concat([site14_core0_df, site14_core1_df], axis = 1)
        # site15_df =pd.concat([site15_core0_df, site15_core1_df], axis = 1)

          # ========================================================== DUT_pathloss data parser_dut0_core0
        if site0 == 1:

            dut0_pathloss = dut0_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut0_core0_{}".format(i+1)] = dut0_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut0_core0_list = list()

            for i in range(1, 17):
                dut0_core0_list.append(eval('dut0_core0_'+str(i)))

            dut0_core0_list.append(dut0_core0_list[-1])

            dut0_core0_list = list(map(float, dut0_core0_list))
            # dut0_core0_df = pd.DataFrame(dut0_core0_list)

            # ========================================================== DUT_pathloss data parser_dut0_core1
            for i in range(0, 16):
                globals()["dut0_core1_{}".format(i+1)] = dut0_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut0_core1_list = list()

            for i in range(1, 17):
                dut0_core1_list.append(eval('dut0_core1_'+str(i)))

            dut0_core1_list.append(dut0_core1_list[-1])

            dut0_core1_list = list(map(float, dut0_core1_list))
            # dut0_core1_df = pd.DataFrame(dut0_core1_list)
            # dut0_df =pd.concat([dut0_core0_df, dut0_core1_df], axis = 1)

        # ========================================================== DUT_pathloss data parser_dut1_core0
        if site1 == 1:

            dut1_pathloss = dut1_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut1_core0_{}".format(i+1)] = dut1_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut1_core0_list = list()

            for i in range(1, 17):
                dut1_core0_list.append(eval('dut1_core0_'+str(i)))

            dut1_core0_list.append(dut1_core0_list[-1])

            dut1_core0_list = list(map(float, dut1_core0_list))
            # dut1_core0_df = pd.DataFrame(dut0_core0_list)

            # ========================================================== DUT_pathloss data parser_dut1_core1
            for i in range(0, 16):
                globals()["dut1_core1_{}".format(i+1)] = dut1_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut1_core1_list = list()

            for i in range(1, 17):
                dut1_core1_list.append(eval('dut1_core1_'+str(i)))

            dut1_core1_list.append(dut1_core1_list[-1])

            dut1_core1_list = list(map(float, dut1_core1_list))

        # ========================================================== DUT_pathloss data parser_dut2_core0
        if site2 == 1:

            dut2_pathloss = dut2_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut2_core0_{}".format(i+1)] = dut2_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut2_core0_list = list()

            for i in range(1, 17):
                dut2_core0_list.append(eval('dut2_core0_'+str(i)))

            dut2_core0_list.append(dut2_core0_list[-1])

            dut2_core0_list = list(map(float, dut2_core0_list))
            # dut2_core0_df = pd.DataFrame(dut2_core0_list)

            # ========================================================== DUT_pathloss data parser_dut2_core1
            for i in range(0, 16):
                globals()["dut2_core1_{}".format(i+1)] = dut2_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut2_core1_list = list()

            for i in range(1, 17):
                dut2_core1_list.append(eval('dut2_core1_'+str(i)))

            dut2_core1_list.append(dut2_core1_list[-1])

            dut2_core1_list = list(map(float, dut2_core1_list))

        # ========================================================== DUT_pathloss data parser_dut3_core0
        if site3 == 1:

            dut3_pathloss = dut3_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut3_core0_{}".format(i+1)] = dut3_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut3_core0_list = list()

            for i in range(1, 17):
                dut3_core0_list.append(eval('dut3_core0_'+str(i)))

            dut3_core0_list.append(dut3_core0_list[-1])

            dut3_core0_list = list(map(float, dut3_core0_list))
            # dut3_core0_df = pd.DataFrame(dut3_core0_list)

            # ========================================================== DUT_pathloss data parser_dut3_core1
            for i in range(0, 16):
                globals()["dut3_core1_{}".format(i+1)] = dut3_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut3_core1_list = list()

            for i in range(1, 17):
                dut3_core1_list.append(eval('dut3_core1_'+str(i)))

            dut3_core1_list.append(dut3_core1_list[-1])

            dut3_core1_list = list(map(float, dut3_core1_list))

        # ========================================================== DUT_pathloss data parser_dut4_core0
        if site4 == 1:

            dut4_pathloss = dut4_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut4_core0_{}".format(i+1)] = dut4_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut4_core0_list = list()

            for i in range(1, 17):
                dut4_core0_list.append(eval('dut4_core0_'+str(i)))

            dut4_core0_list.append(dut4_core0_list[-1])

            dut4_core0_list = list(map(float, dut4_core0_list))
            # dut4_core0_df = pd.DataFrame(dut4_core0_list)

            # ========================================================== DUT_pathloss data parser_dut4_core1
            for i in range(0, 16):
                globals()["dut4_core1_{}".format(i+1)] = dut4_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut4_core1_list = list()

            for i in range(1, 17):
                dut4_core1_list.append(eval('dut4_core1_'+str(i)))

            dut4_core1_list.append(dut4_core1_list[-1])

            dut4_core1_list = list(map(float, dut4_core1_list))

        # ========================================================== DUT_pathloss data parser_dut5_core0
        if site5 == 1:

            dut5_pathloss = dut5_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut5_core0_{}".format(i+1)] = dut5_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut5_core0_list = list()

            for i in range(1, 17):
                dut5_core0_list.append(eval('dut5_core0_'+str(i)))

            dut5_core0_list.append(dut5_core0_list[-1])

            dut5_core0_list = list(map(float, dut5_core0_list))
            # dut5_core0_df = pd.DataFrame(dut5_core0_list)

            # ========================================================== DUT_pathloss data parser_dut5_core1
            for i in range(0, 16):
                globals()["dut5_core1_{}".format(i+1)] = dut5_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut5_core1_list = list()

            for i in range(1, 17):
                dut5_core1_list.append(eval('dut5_core1_'+str(i)))

            dut5_core1_list.append(dut5_core1_list[-1])

            dut5_core1_list = list(map(float, dut5_core1_list))

        # ========================================================== DUT_pathloss data parser_dut6_core0
        if site6 == 1:

            dut6_pathloss = dut6_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut6_core0_{}".format(i+1)] = dut6_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut6_core0_list = list()

            for i in range(1, 17):
                dut6_core0_list.append(eval('dut6_core0_'+str(i)))

            dut6_core0_list.append(dut6_core0_list[-1])

            dut6_core0_list = list(map(float, dut6_core0_list))
            # dut6_core0_df = pd.DataFrame(dut6_core0_list)

            # ========================================================== DUT_pathloss data parser_dut6_core1
            for i in range(0, 16):
                globals()["dut6_core1_{}".format(i+1)] = dut6_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut6_core1_list = list()

            for i in range(1, 17):
                dut6_core1_list.append(eval('dut6_core1_'+str(i)))

            dut6_core1_list.append(dut6_core1_list[-1])

            dut6_core1_list = list(map(float, dut6_core1_list))

        # ========================================================== DUT_pathloss data parser_dut7_core0
        if site7 == 1:

            dut7_pathloss = dut7_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut7_core0_{}".format(i+1)] = dut7_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut7_core0_list = list()

            for i in range(1, 17):
                dut7_core0_list.append(eval('dut7_core0_'+str(i)))

            dut7_core0_list.append(dut7_core0_list[-1])

            dut7_core0_list = list(map(float, dut7_core0_list))
            # dut7_core0_df = pd.DataFrame(dut7_core0_list)

            # ========================================================== DUT_pathloss data parser_dut7_core1
            for i in range(0, 16):
                globals()["dut7_core1_{}".format(i+1)] = dut7_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut7_core1_list = list()

            for i in range(1, 17):
                dut7_core1_list.append(eval('dut7_core1_'+str(i)))

            dut7_core1_list.append(dut7_core1_list[-1])

            dut7_core1_list = list(map(float, dut7_core1_list))

        # ========================================================== DUT_pathloss data parser_dut8_core0
        if site8 == 1:

            dut8_pathloss = dut8_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut8_core0_{}".format(i+1)] = dut8_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut8_core0_list = list()

            for i in range(1, 17):
                dut8_core0_list.append(eval('dut8_core0_'+str(i)))

            dut8_core0_list.append(dut8_core0_list[-1])

            dut8_core0_list = list(map(float, dut8_core0_list))
            # dut8_core0_df = pd.DataFrame(dut8_core0_list)

            # ========================================================== DUT_pathloss data parser_dut8_core1
            for i in range(0, 16):
                globals()["dut8_core1_{}".format(i+1)] = dut8_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut8_core1_list = list()

            for i in range(1, 17):
                dut8_core1_list.append(eval('dut8_core1_'+str(i)))

            dut8_core1_list.append(dut8_core1_list[-1])

            dut8_core1_list = list(map(float, dut8_core1_list))

        # ========================================================== DUT_pathloss data parser_dut9_core0
        if site9 == 1:

            dut9_pathloss = dut9_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut9_core0_{}".format(i+1)] = dut9_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut9_core0_list = list()

            for i in range(1, 17):
                dut9_core0_list.append(eval('dut9_core0_'+str(i)))

            dut9_core0_list.append(dut9_core0_list[-1])

            dut9_core0_list = list(map(float, dut9_core0_list))
            # dut9_core0_df = pd.DataFrame(dut9_core0_list)

            # ========================================================== DUT_pathloss data parser_dut9_core1
            for i in range(0, 16):
                globals()["dut9_core1_{}".format(i+1)] = dut9_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut9_core1_list = list()

            for i in range(1, 17):
                dut9_core1_list.append(eval('dut9_core1_'+str(i)))

            dut9_core1_list.append(dut9_core1_list[-1])

            dut9_core1_list = list(map(float, dut9_core1_list))

        # ========================================================== DUT_pathloss data parser_dut10_core0
        if site10 == 1:

            dut10_pathloss = dut10_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut10_core0_{}".format(i+1)] = dut10_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut10_core0_list = list()

            for i in range(1, 17):
                dut10_core0_list.append(eval('dut10_core0_'+str(i)))

            dut10_core0_list.append(dut10_core0_list[-1])

            dut10_core0_list = list(map(float, dut10_core0_list))
            # dut10_core0_df = pd.DataFrame(dut10_core0_list)

            # ========================================================== DUT_pathloss data parser_dut10_core1
            for i in range(0, 16):
                globals()["dut10_core1_{}".format(i+1)] = dut10_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut10_core1_list = list()

            for i in range(1, 17):
                dut10_core1_list.append(eval('dut10_core1_'+str(i)))

            dut10_core1_list.append(dut10_core1_list[-1])

            dut10_core1_list = list(map(float, dut10_core1_list))

        # ========================================================== DUT_pathloss data parser_dut11_core0
        if site11 == 1:

            dut11_pathloss = dut11_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut11_core0_{}".format(i+1)] = dut11_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut11_core0_list = list()

            for i in range(1, 17):
                dut11_core0_list.append(eval('dut11_core0_'+str(i)))

            dut11_core0_list.append(dut11_core0_list[-1])

            dut11_core0_list = list(map(float, dut11_core0_list))
            # dut11_core0_df = pd.DataFrame(dut11_core0_list)

            # ========================================================== DUT_pathloss data parser_dut11_core1
            for i in range(0, 16):
                globals()["dut11_core1_{}".format(i+1)] = dut11_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut11_core1_list = list()

            for i in range(1, 17):
                dut11_core1_list.append(eval('dut11_core1_'+str(i)))

            dut11_core1_list.append(dut11_core1_list[-1])

            dut11_core1_list = list(map(float, dut11_core1_list))

        # ========================================================== DUT_pathloss data parser_dut12_core0
        if site12 == 1:

            dut12_pathloss = dut12_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut12_core0_{}".format(i+1)] = dut12_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut12_core0_list = list()

            for i in range(1, 17):
                dut12_core0_list.append(eval('dut12_core0_'+str(i)))

            dut12_core0_list.append(dut12_core0_list[-1])

            dut12_core0_list = list(map(float, dut12_core0_list))
            # dut12_core0_df = pd.DataFrame(dut12_core0_list)

            # ========================================================== DUT_pathloss data parser_dut12_core1
            for i in range(0, 16):
                globals()["dut12_core1_{}".format(i+1)] = dut12_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut12_core1_list = list()

            for i in range(1, 17):
                dut12_core1_list.append(eval('dut12_core1_'+str(i)))

            dut12_core1_list.append(dut12_core1_list[-1])

            dut12_core1_list = list(map(float, dut12_core1_list))

        # ========================================================== DUT_pathloss data parser_dut13_core0
        if site13 == 1:

            dut13_pathloss = dut13_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut13_core0_{}".format(i+1)] = dut13_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut13_core0_list = list()

            for i in range(1, 17):
                dut13_core0_list.append(eval('dut13_core0_'+str(i)))

            dut13_core0_list.append(dut13_core0_list[-1])

            dut13_core0_list = list(map(float, dut13_core0_list))
            # dut13_core0_df = pd.DataFrame(dut13_core0_list)

            # ========================================================== DUT_pathloss data parser_dut13_core1
            for i in range(0, 16):
                globals()["dut13_core1_{}".format(i+1)] = dut13_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut13_core1_list = list()

            for i in range(1, 17):
                dut13_core1_list.append(eval('dut13_core1_'+str(i)))

            dut13_core1_list.append(dut13_core1_list[-1])

            dut13_core1_list = list(map(float, dut13_core1_list))

        # ========================================================== DUT_pathloss data parser_dut14_core0
        if site14 == 1:

            dut14_pathloss = dut14_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut14_core0_{}".format(i+1)] = dut14_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut14_core0_list = list()

            for i in range(1, 17):
                dut14_core0_list.append(eval('dut14_core0_'+str(i)))

            dut14_core0_list.append(dut14_core0_list[-1])

            dut14_core0_list = list(map(float, dut14_core0_list))
            # dut14_core0_df = pd.DataFrame(dut14_core0_list)

            # ========================================================== DUT_pathloss data parser_dut14_core1
            for i in range(0, 16):
                globals()["dut14_core1_{}".format(i+1)] = dut14_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut14_core1_list = list()

            for i in range(1, 17):
                dut14_core1_list.append(eval('dut14_core1_'+str(i)))

            dut14_core1_list.append(dut14_core1_list[-1])

            dut14_core1_list = list(map(float, dut14_core1_list))

        # ========================================================== DUT_pathloss data parser_dut15_core0
        if site15 == 1:

            dut15_pathloss = dut15_pathloss.results.str.split(',')

            for i in range(0, 16):
                globals()["dut15_core0_{}".format(i+1)] = dut15_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut15_core0_list = list()

            for i in range(1, 17):
                dut15_core0_list.append(eval('dut15_core0_'+str(i)))

            dut15_core0_list.append(dut15_core0_list[-1])

            dut15_core0_list = list(map(float, dut15_core0_list))
            # dut15_core0_df = pd.DataFrame(dut15_core0_list)

            # ========================================================== DUT_pathloss data parser_dut15_core1
            for i in range(0, 16):
                globals()["dut15_core1_{}".format(i+1)] = dut15_pathloss[i][1]

            # ========================================================== chip_loss data parser_list와 dataframe으로 만들기
            dut15_core1_list = list()

            for i in range(1, 17):
                dut15_core1_list.append(eval('dut15_core1_'+str(i)))

            dut15_core1_list.append(dut15_core1_list[-1])

            dut15_core1_list = list(map(float, dut15_core1_list))

        # ========================================================== 뺄셈, delta 만들기
        delta_site0_core0_list = [-log_core0[i] + site0_core0_list[i] for i in range(len(log_core0))]
        delta_site0_core0_list = np.round(delta_site0_core0_list, 2)

        delta_site0_core1_list = [-log_core1[i] + site0_core1_list[i] for i in range(len(log_core1))]
        delta_site0_core1_list = np.round(delta_site0_core1_list, 2)


        delta_site1_core0_list = [-log_core0[i] + site1_core0_list[i] for i in range(len(log_core0))]
        delta_site1_core0_list = np.round(delta_site1_core0_list, 2)

        delta_site1_core1_list = [-log_core1[i] + site1_core1_list[i] for i in range(len(log_core1))]
        delta_site1_core1_list = np.round(delta_site1_core1_list, 2)


        delta_site2_core0_list = [-log_core0[i] + site2_core0_list[i] for i in range(len(log_core0))]
        delta_site2_core0_list = np.round(delta_site2_core0_list, 2)

        delta_site2_core1_list = [-log_core1[i] + site2_core1_list[i] for i in range(len(log_core1))]
        delta_site2_core1_list = np.round(delta_site2_core1_list, 2)


        delta_site3_core0_list = [-log_core0[i] + site3_core0_list[i] for i in range(len(log_core0))]
        delta_site3_core0_list = np.round(delta_site3_core0_list, 2)

        delta_site3_core1_list = [-log_core1[i] + site3_core1_list[i] for i in range(len(log_core1))]
        delta_site3_core1_list = np.round(delta_site3_core1_list, 2)


        delta_site4_core0_list = [-log_core0[i] + site4_core0_list[i] for i in range(len(log_core0))]
        delta_site4_core0_list = np.round(delta_site4_core0_list, 2)

        delta_site4_core1_list = [-log_core1[i] + site4_core1_list[i] for i in range(len(log_core1))]
        delta_site4_core1_list = np.round(delta_site4_core1_list, 2)


        delta_site5_core0_list = [-log_core0[i] + site5_core0_list[i] for i in range(len(log_core0))]
        delta_site5_core0_list = np.round(delta_site5_core0_list, 2)

        delta_site5_core1_list = [-log_core1[i] + site5_core1_list[i] for i in range(len(log_core1))]
        delta_site5_core1_list = np.round(delta_site5_core1_list, 2)


        delta_site6_core0_list = [-log_core0[i] + site6_core0_list[i] for i in range(len(log_core0))]
        delta_site6_core0_list = np.round(delta_site6_core0_list, 2)

        delta_site6_core1_list = [-log_core1[i] + site6_core1_list[i] for i in range(len(log_core1))]
        delta_site6_core1_list = np.round(delta_site6_core1_list, 2)


        delta_site7_core0_list = [-log_core0[i] + site7_core0_list[i] for i in range(len(log_core0))]
        delta_site7_core0_list = np.round(delta_site7_core0_list, 2)

        delta_site7_core1_list = [-log_core1[i] + site7_core1_list[i] for i in range(len(log_core1))]
        delta_site7_core1_list = np.round(delta_site7_core1_list, 2)


        delta_site8_core0_list = [-log_core0[i] + site8_core0_list[i] for i in range(len(log_core0))]
        delta_site8_core0_list = np.round(delta_site8_core0_list, 2)

        delta_site8_core1_list = [-log_core1[i] + site8_core1_list[i] for i in range(len(log_core1))]
        delta_site8_core1_list = np.round(delta_site8_core1_list, 2)


        delta_site9_core0_list = [-log_core0[i] + site9_core0_list[i] for i in range(len(log_core0))]
        delta_site9_core0_list = np.round(delta_site9_core0_list, 2)

        delta_site9_core1_list = [-log_core1[i] + site9_core1_list[i] for i in range(len(log_core1))]
        delta_site9_core1_list = np.round(delta_site9_core1_list, 2)


        delta_site10_core0_list = [-log_core0[i] + site10_core0_list[i] for i in range(len(log_core0))]
        delta_site10_core0_list = np.round(delta_site10_core0_list, 2)

        delta_site10_core1_list = [-log_core1[i] + site10_core1_list[i] for i in range(len(log_core1))]
        delta_site10_core1_list = np.round(delta_site10_core1_list, 2)


        delta_site11_core0_list = [-log_core0[i] + site11_core0_list[i] for i in range(len(log_core0))]
        delta_site11_core0_list = np.round(delta_site11_core0_list, 2)

        delta_site11_core1_list = [-log_core1[i] + site11_core1_list[i] for i in range(len(log_core1))]
        delta_site11_core1_list = np.round(delta_site11_core1_list, 2)


        delta_site12_core0_list = [-log_core0[i] + site12_core0_list[i] for i in range(len(log_core0))]
        delta_site12_core0_list = np.round(delta_site12_core0_list, 2)

        delta_site12_core1_list = [-log_core1[i] + site12_core1_list[i] for i in range(len(log_core1))]
        delta_site12_core1_list = np.round(delta_site12_core1_list, 2)


        delta_site13_core0_list = [-log_core0[i] + site13_core0_list[i] for i in range(len(log_core0))]
        delta_site13_core0_list = np.round(delta_site13_core0_list, 2)

        delta_site13_core1_list = [-log_core1[i] + site13_core1_list[i] for i in range(len(log_core1))]
        delta_site13_core1_list = np.round(delta_site13_core1_list, 2)


        delta_site14_core0_list = [-log_core0[i] + site14_core0_list[i] for i in range(len(log_core0))]
        delta_site14_core0_list = np.round(delta_site14_core0_list, 2)

        delta_site14_core1_list = [-log_core1[i] + site14_core1_list[i] for i in range(len(log_core1))]
        delta_site14_core1_list = np.round(delta_site14_core1_list, 2)


        delta_site15_core0_list = [-log_core0[i] + site15_core0_list[i] for i in range(len(log_core0))]
        delta_site15_core0_list = np.round(delta_site15_core0_list, 2)

        delta_site15_core1_list = [-log_core1[i] + site15_core1_list[i] for i in range(len(log_core1))]
        delta_site15_core1_list = np.round(delta_site15_core1_list, 2)

        # ========================================================== DUT results + delta 해서 after 만들기
        if site0 == 1:

            after_site0_core0_list = [dut0_core0_list[i] + delta_site0_core0_list[i] for i in range(len(dut0_core0_list))]
            after_site0_core0_list = np.round(after_site0_core0_list, 2)

            after_site0_core1_list = [dut0_core1_list[i] + delta_site0_core1_list[i] for i in range(len(dut0_core1_list))]
            after_site0_core1_list = np.round(after_site0_core1_list, 2)

        else:
            print('Nothing')

        if site1 == 1:

            after_site1_core0_list = [dut1_core0_list[i] + delta_site1_core0_list[i] for i in range(len(dut1_core0_list))]
            after_site1_core0_list = np.round(after_site1_core0_list, 2)

            after_site1_core1_list = [dut1_core1_list[i] + delta_site1_core1_list[i] for i in range(len(dut1_core1_list))]
            after_site1_core1_list = np.round(after_site1_core1_list, 2)

        else:
            print('Nothing')

        if site2 == 1:

            after_site2_core0_list = [dut2_core0_list[i] + delta_site2_core0_list[i] for i in range(len(dut2_core0_list))]
            after_site2_core0_list = np.round(after_site2_core0_list, 2)

            after_site2_core1_list = [dut2_core1_list[i] + delta_site2_core1_list[i] for i in range(len(dut2_core1_list))]
            after_site2_core1_list = np.round(after_site2_core1_list, 2)

        else:
            print('Nothing')

        if site3 == 1:

            after_site3_core0_list = [dut3_core0_list[i] + delta_site3_core0_list[i] for i in range(len(dut3_core0_list))]
            after_site3_core0_list = np.round(after_site3_core0_list, 2)

            after_site3_core1_list = [dut3_core1_list[i] + delta_site3_core1_list[i] for i in range(len(dut3_core1_list))]
            after_site3_core1_list = np.round(after_site3_core1_list, 2)

        else:
            print('Nothing')

        if site4 == 1:

            after_site4_core0_list = [dut4_core0_list[i] + delta_site4_core0_list[i] for i in range(len(dut4_core0_list))]
            after_site4_core0_list = np.round(after_site4_core0_list, 2)

            after_site4_core1_list = [dut4_core1_list[i] + delta_site4_core1_list[i] for i in range(len(dut4_core1_list))]
            after_site4_core1_list = np.round(after_site4_core1_list, 2)

        else:
            print('Nothing')

        if site5 == 1:

            after_site5_core0_list = [dut5_core0_list[i] + delta_site5_core0_list[i] for i in range(len(dut5_core0_list))]
            after_site5_core0_list = np.round(after_site5_core0_list, 2)

            after_site5_core1_list = [dut5_core1_list[i] + delta_site5_core1_list[i] for i in range(len(dut5_core1_list))]
            after_site5_core1_list = np.round(after_site5_core1_list, 2)

        else:
            print('Nothing')

        if site6 == 1:

            after_site6_core0_list = [dut6_core0_list[i] + delta_site6_core0_list[i] for i in range(len(dut6_core0_list))]
            after_site6_core0_list = np.round(after_site6_core0_list, 2)

            after_site6_core1_list = [dut6_core1_list[i] + delta_site6_core1_list[i] for i in range(len(dut6_core1_list))]
            after_site6_core1_list = np.round(after_site6_core1_list, 2)

        else:
            print('Nothing')

        if site7 == 1:

            after_site7_core0_list = [dut7_core0_list[i] + delta_site7_core0_list[i] for i in range(len(dut7_core0_list))]
            after_site7_core0_list = np.round(after_site7_core0_list, 2)

            after_site7_core1_list = [dut7_core1_list[i] + delta_site7_core1_list[i] for i in range(len(dut7_core1_list))]
            after_site7_core1_list = np.round(after_site7_core1_list, 2)

        else:
            print('Nothing')

        if site8 == 1:

            after_site8_core0_list = [dut8_core0_list[i] + delta_site8_core0_list[i] for i in range(len(dut8_core0_list))]
            after_site8_core0_list = np.round(after_site8_core0_list, 2)

            after_site8_core1_list = [dut8_core1_list[i] + delta_site8_core1_list[i] for i in range(len(dut8_core1_list))]
            after_site8_core1_list = np.round(after_site8_core1_list, 2)

        else:
            print('Nothing')

        if site9 == 1:

            after_site9_core0_list = [dut9_core0_list[i] + delta_site9_core0_list[i] for i in range(len(dut9_core0_list))]
            after_site9_core0_list = np.round(after_site9_core0_list, 2)

            after_site9_core1_list = [dut9_core1_list[i] + delta_site9_core1_list[i] for i in range(len(dut9_core1_list))]
            after_site9_core1_list = np.round(after_site9_core1_list, 2)

        else:
            print('Nothing')

        if site10 == 1:

            after_site10_core0_list = [dut10_core0_list[i] + delta_site10_core0_list[i] for i in range(len(dut10_core0_list))]
            after_site10_core0_list = np.round(after_site10_core0_list, 2)

            after_site10_core1_list = [dut10_core1_list[i] + delta_site10_core1_list[i] for i in range(len(dut10_core1_list))]
            after_site10_core1_list = np.round(after_site10_core1_list, 2)

        else:
            print('Nothing')

        if site11 == 1:

            after_site11_core0_list = [dut11_core0_list[i] + delta_site11_core0_list[i] for i in range(len(dut11_core0_list))]
            after_site11_core0_list = np.round(after_site11_core0_list, 2)

            after_site11_core1_list = [dut11_core1_list[i] + delta_site11_core1_list[i] for i in range(len(dut11_core1_list))]
            after_site11_core1_list = np.round(after_site11_core1_list, 2)

        else:
            print('Nothing')

        if site12 == 1:

            after_site12_core0_list = [dut12_core0_list[i] + delta_site12_core0_list[i] for i in range(len(dut12_core0_list))]
            after_site12_core0_list = np.round(after_site12_core0_list, 2)

            after_site12_core1_list = [dut12_core1_list[i] + delta_site12_core1_list[i] for i in range(len(dut12_core1_list))]
            after_site12_core1_list = np.round(after_site12_core1_list, 2)

        else:
            print('Nothing')

        if site13 == 1:

            after_site13_core0_list = [dut13_core0_list[i] + delta_site13_core0_list[i] for i in range(len(dut13_core0_list))]
            after_site13_core0_list = np.round(after_site13_core0_list, 2)

            after_site13_core1_list = [dut13_core1_list[i] + delta_site13_core1_list[i] for i in range(len(dut13_core1_list))]
            after_site13_core1_list = np.round(after_site13_core1_list, 2)

        else:
            print('Nothing')

        if site14 == 1:

            after_site14_core0_list = [dut14_core0_list[i] + delta_site14_core0_list[i] for i in range(len(dut14_core0_list))]
            after_site14_core0_list = np.round(after_site14_core0_list, 2)

            after_site14_core1_list = [dut14_core1_list[i] + delta_site14_core1_list[i] for i in range(len(dut14_core1_list))]
            after_site14_core1_list = np.round(after_site14_core1_list, 2)

        else:
            print('Nothing')

        if site15 == 1:

            after_site15_core0_list = [dut15_core0_list[i] + delta_site15_core0_list[i] for i in range(len(dut15_core0_list))]
            after_site15_core0_list = np.round(after_site15_core0_list, 2)

            after_site15_core1_list = [dut15_core1_list[i] + delta_site15_core1_list[i] for i in range(len(dut15_core1_list))]
            after_site15_core1_list = np.round(after_site15_core1_list, 2)

        else:
            print('Nothing')

        # ========================================================== after list 파일 DataFrame으로 만들기
        if site0 == 1:
            after_site0_core0_df = pd.DataFrame(after_site0_core0_list)
            after_site0_core1_df = pd.DataFrame(after_site0_core1_list)

        if site1 == 1:
            after_site1_core0_df = pd.DataFrame(after_site1_core0_list)
            after_site1_core1_df = pd.DataFrame(after_site1_core1_list)

        if site2 == 1:
            after_site2_core0_df = pd.DataFrame(after_site2_core0_list)
            after_site2_core1_df = pd.DataFrame(after_site2_core1_list)

        if site3 == 1:
            after_site3_core0_df = pd.DataFrame(after_site3_core0_list)
            after_site3_core1_df = pd.DataFrame(after_site3_core1_list)

        if site4 == 1:
            after_site4_core0_df = pd.DataFrame(after_site4_core0_list)
            after_site4_core1_df = pd.DataFrame(after_site4_core1_list)

        if site5 == 1:
            after_site5_core0_df = pd.DataFrame(after_site5_core0_list)
            after_site5_core1_df = pd.DataFrame(after_site5_core1_list)

        if site6 == 1:
            after_site6_core0_df = pd.DataFrame(after_site6_core0_list)
            after_site6_core1_df = pd.DataFrame(after_site6_core1_list)

        if site7 == 1:
            after_site7_core0_df = pd.DataFrame(after_site7_core0_list)
            after_site7_core1_df = pd.DataFrame(after_site7_core1_list)

        if site8 == 1:
            after_site8_core0_df = pd.DataFrame(after_site8_core0_list)
            after_site8_core1_df = pd.DataFrame(after_site8_core1_list)

        if site9 == 1:
            after_site9_core0_df = pd.DataFrame(after_site9_core0_list)
            after_site9_core1_df = pd.DataFrame(after_site9_core1_list)

        if site10 == 1:
            after_site10_core0_df = pd.DataFrame(after_site10_core0_list)
            after_site10_core1_df = pd.DataFrame(after_site10_core1_list)
 
        if site11 == 1:
            after_site11_core0_df = pd.DataFrame(after_site11_core0_list)
            after_site11_core1_df = pd.DataFrame(after_site11_core1_list)

        if site12 == 1:
            after_site12_core0_df = pd.DataFrame(after_site12_core0_list)
            after_site12_core1_df = pd.DataFrame(after_site12_core1_list)

        if site13 == 1:
            after_site13_core0_df = pd.DataFrame(after_site13_core0_list)
            after_site13_core1_df = pd.DataFrame(after_site13_core1_list)

        if site14 == 1:
            after_site14_core0_df = pd.DataFrame(after_site14_core0_list)
            after_site14_core1_df = pd.DataFrame(after_site14_core1_list)

        if site15 == 1:
            after_site15_core0_df = pd.DataFrame(after_site15_core0_list)
            after_site15_core1_df = pd.DataFrame(after_site15_core1_list)

        ch_list = [2412, 2442, 2472, 5180, 5220, 5260, 5320, 5500, 5540, 5580, 5620, 5660, 5700, 5745, 5785, 5805, 5825]
        ch_df = pd.DataFrame(ch_list)

        if site0 == 1:
            after_site0_df = pd.concat([ch_df, after_site0_core0_df, after_site0_core1_df], axis=1)
            print(after_site0_df)
        if site1 == 1:   
            after_site1_df = pd.concat([ch_df, after_site1_core0_df, after_site1_core1_df], axis=1)
            print(after_site1_df)
        if site2 == 1:   
            after_site2_df = pd.concat([ch_df, after_site2_core0_df, after_site2_core1_df], axis=1)
            print(after_site2_df)
        if site3 == 1:   
            after_site3_df = pd.concat([ch_df, after_site3_core0_df, after_site3_core1_df], axis=1)
            print(after_site3_df)
        if site4 == 1:   
            after_site4_df = pd.concat([ch_df, after_site4_core0_df, after_site4_core1_df], axis=1)
            print(after_site4_df)
        if site5 == 1:
            after_site5_df = pd.concat([ch_df, after_site5_core0_df, after_site5_core1_df], axis=1)
            print(after_site5_df)
        if site6 == 1:
            after_site6_df = pd.concat([ch_df, after_site6_core0_df, after_site6_core1_df], axis=1)
            print(after_site6_df)
        if site7 == 1:
            after_site7_df = pd.concat([ch_df, after_site7_core0_df, after_site7_core1_df], axis=1)
            print(after_site7_df)
        if site8 == 1:
            after_site8_df = pd.concat([ch_df, after_site8_core0_df, after_site8_core1_df], axis=1)
            print(after_site8_df)
        if site9 == 1:
            after_site9_df = pd.concat([ch_df, after_site9_core0_df, after_site9_core1_df], axis=1)
            print(after_site9_df)
        if site10 == 1:
            after_site10_df = pd.concat([ch_df, after_site10_core0_df, after_site10_core1_df], axis=1)
            print(after_site10_df)
        if site11 == 1:
            after_site11_df = pd.concat([ch_df, after_site11_core0_df, after_site11_core1_df], axis=1)
            print(after_site11_df)
        if site12 == 1:
            after_site12_df = pd.concat([ch_df, after_site12_core0_df, after_site12_core1_df], axis=1)
            print(after_site12_df)
        if site13 == 1:
            after_site13_df = pd.concat([ch_df, after_site13_core0_df, after_site13_core1_df], axis=1)
            print(after_site13_df)
        if site14 == 1:
            after_site14_df = pd.concat([ch_df, after_site14_core0_df, after_site14_core1_df], axis=1)
            print(after_site14_df)
        if site15 == 1:
            after_site15_df = pd.concat([ch_df, after_site15_core0_df, after_site15_core1_df], axis=1)
            print(after_site15_df)

        # after_list = after_df.values.tolist()

        # ========================================================== DataFrame 파일 Excel로 만들기
        if site0 == 1:
            after_site0_df.to_csv('Dut0\Path_loss_ATE0.csv', index=False, header=False)
        if site1 == 1:   
            after_site1_df.to_csv('Dut1\Path_loss_ATE1.csv', index=False, header=False)
        if site2 == 1:
            after_site2_df.to_csv('Dut2\Path_loss_ATE2.csv', index=False, header=False)
        if site3 == 1:
            after_site3_df.to_csv('Dut3\Path_loss_ATE3.csv', index=False, header=False)
        if site4 == 1:
            after_site4_df.to_csv('Dut4\Path_loss_ATE4.csv', index=False, header=False)
        if site5 == 1:
            after_site5_df.to_csv('Dut5\Path_loss_ATE5.csv', index=False, header=False)
        if site6 == 1:
            after_site6_df.to_csv('Dut6\Path_loss_ATE6.csv', index=False, header=False)
        if site7 == 1:
            after_site7_df.to_csv('Dut7\Path_loss_ATE7.csv', index=False, header=False)
        if site8 == 1:
            after_site8_df.to_csv('Dut8\Path_loss_ATE8.csv', index=False, header=False)
        if site9 == 1:   
            after_site9_df.to_csv('Dut9\Path_loss_ATE9.csv', index=False, header=False)
        if site10 == 1:
            after_site10_df.to_csv('Dut10\Path_loss_ATE10.csv', index=False, header=False)
        if site11 == 1:
            after_site11_df.to_csv('Dut11\Path_loss_ATE11.csv', index=False, header=False)
        if site12 == 1:
            after_site12_df.to_csv('Dut12\Path_loss_ATE12.csv', index=False, header=False)
        if site13 == 1:
            after_site13_df.to_csv('Dut13\Path_loss_ATE13.csv', index=False, header=False)
        if site14 == 1:
            after_site14_df.to_csv('Dut14\Path_loss_ATE14.csv', index=False, header=False)
        if site15 == 1:
            after_site15_df.to_csv('Dut15\Path_loss_ATE15.csv', index=False, header=False)

#-------------------------------------------------------------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = GroupBoxWindow()
    myWindow.show()
    app.exec_()
    # sys.exit(app.exec_())