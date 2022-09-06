
from placares_alfa_ui import *
from jogador_alfa import Jogador
from datetime import datetime

class MyWin(QtWidgets.QMainWindow, Ui_Scores):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        '''Botões maximizar, fechar, minimizar'''
        self.btn_close.clicked.connect(lambda:w.close()) # isso fechou a janela
        self.btn_minimize.clicked.connect(lambda:w.showMinimized())
        self.btn_maximize.clicked.connect(self.maximize_restore)
        '''Atributos para marcar o tempo'''
        self.timer = QTimer(self.centralwidget)
        self.timer.timeout.connect(self.showTime)
        self.PB_Scores_Time.clicked.connect(self.tempo_start)
        self.PB_Scores_pause.clicked.connect(self.tempo_pause)
        self.inicio_pause = 0
        self.final_pause = 0
        self.lista_minutos_jogo = []
        '''Definindo nomes de cada jogador'''
        self.PB_Jogadores_ok.clicked.connect(self.nomesoponente)
        self.nomes_flag = 0 #Informa quantas vezes apertei o ok
        self.flag = 0 # Informa qual jogador esta selecionaddo
        self.PB_Jogadores_clear.clicked.connect(self.reset_nomes)
        self.Nome_Vai.clicked.connect(lambda: self.CadastroJogadores.setCurrentIndex(1))
        self.Nome_Volta.clicked.connect(lambda: self.CadastroJogadores.setCurrentIndex(0))

        '''Scores Menus de Acréscimo'''
        self.qualBT = False #Coordenadas do botao pressinado. Fundamento, classificação e label correspondente

        self.PB_ataque_green.clicked.connect(   lambda:self.abreposition('ataque', 0, self.N_ataque_green) )
        self.PB_ataque_blue.clicked.connect(    lambda:self.abreposition('ataque', 1, self.N_ataque_blue)  )
        self.PB_ataque_red.clicked.connect(     lambda:self.abreposition('ataque', 2, self.N_ataque_red)   )

        self.PB_CA_green.clicked.connect(   lambda:self.abreposition('cataque', 0, self.N_CA_green) )
        self.PB_CA_blue.clicked.connect(    lambda:self.abreposition('cataque', 1, self.N_CA_blue)  )
        self.PB_CA_red.clicked.connect(     lambda:self.abreposition('cataque', 2, self.N_CA_red)   )

        self.PB_bloqueio_green.clicked.connect(lambda:self.abreposition('bloqueio', 0 ,self.N_bloqueio_green))
        self.PB_bloqueio_blue.clicked.connect(lambda:self.abreposition('bloqueio', 1, self.N_bloqueio_blue))
        self.PB_bloqueio_red.clicked.connect(lambda:self.abreposition('bloqueio', 2, self.N_bloqueio_red))

        self.PB_saque_green.clicked.connect(lambda:self.abreposition('saque', 0, self.N_saque_green))
        self.PB_saque_blue.clicked.connect(lambda:self.abreposition('saque', 1, self.N_saque_blue))
        self.PB_saque_ora.clicked.connect(lambda:self.abreposition('saque', 2, self.N_saque_ora))
        self.PB_saque_red.clicked.connect(lambda:self.abreposition('saque', 3, self.N_saque_red))

        self.PB_passe_A.clicked.connect(lambda:self.nposition('passe',0,self.N_passe_A))
        self.PB_passe_B.clicked.connect(lambda:self.nposition('passe',1,self.N_passe_B))
        self.PB_passe_C.clicked.connect(lambda:self.nposition('passe',2,self.N_passe_C))
        self.PB_passe_D.clicked.connect(lambda:self.nposition('passe',3,self.N_passe_D))

        self.PB_defesa_A.clicked.connect(lambda:self.abreposition('defesa',0,self.N_defesa_A))
        self.PB_defesa_B.clicked.connect(lambda:self.abreposition('defesa',1,self.N_defesa_B))
        self.PB_defesa_C.clicked.connect(lambda:self.abreposition('defesa',2,self.N_defesa_C))

        self.PB_rede.clicked.connect(lambda:self.nposition('penalidades',0,self.N_rede))
        self.PB_cartao.clicked.connect(lambda:self.nposition('penalidades',1,self.N_cartao))
        self.PB_2t.clicked.connect(lambda:self.nposition('penalidades',2,self.N_2t))
        self.PB_conducao.clicked.connect(lambda:self.nposition('penalidades',3,self.N_cond))

        self.PB_placar_time_mais.clicked.connect(lambda:self.acress_placar_extra(1))
        self.PB_placar_time_menos.clicked.connect(lambda:self.acress_placar_extra(2))
        self.PB_placar_oponente_mais.clicked.connect(lambda:self.acress_placar_extra(3))
        self.PB_placar_oponente_menos.clicked.connect(lambda:self.acress_placar_extra(4))

        self.poissonA = [(0,0)]
        self.poissonB = [(0,0)]

        self.PB_Score_reset.clicked.connect(self.ResetBox_abre)
        self.PB_AlternarJogadores.clicked.connect(self.mudatime)
        self.QB_S.clicked.connect(self.reset_scores)
        self.QB_N.clicked.connect(self.ResetBox_fecha)

        ''' Botoes de correcao '''
        self.CAC_green.clicked.connect(lambda: self.corrige(0, 'cataque',self.N_CA_green))
        self.CAC_blue.clicked.connect(lambda: self.corrige(1, 'cataque',self.N_CA_blue))
        self.CAC_red.clicked.connect(lambda: self.corrige(2, 'cataque',self.N_CA_red))

        self.ATA_green.clicked.connect(lambda: self.corrige(0, 'ataque',self.N_ataque_green))
        self.ATA_blue.clicked.connect(lambda: self.corrige(1, 'ataque',self.N_ataque_blue))
        self.ATA_red.clicked.connect(lambda: self.corrige(2, 'ataque',self.N_ataque_red))

        self.BLO_green.clicked.connect(lambda: self.corrige(0, 'bloqueio',self.N_bloqueio_green))
        self.BLO_blue.clicked.connect(lambda: self.corrige(1, 'bloqueio',self.N_bloqueio_blue))
        self.BLO_red.clicked.connect(lambda: self.corrige(2, 'bloqueio',self.N_bloqueio_red))

        self.DEF_A.clicked.connect(lambda: self.corrige(0, 'defesa',self.N_defesa_A))
        self.DEF_B.clicked.connect(lambda: self.corrige(1, 'defesa',self.N_defesa_B))
        self.DEF_C.clicked.connect(lambda: self.corrige(2, 'defesa',self.N_defesa_C))

        self.PASS_A.clicked.connect(lambda: self.corrige(0, 'passe',self.N_passe_A))
        self.PASS_B.clicked.connect(lambda: self.corrige(1, 'passe',self.N_passe_B))
        self.PASS_C.clicked.connect(lambda: self.corrige(2, 'passe',self.N_passe_C))
        self.PASS_D.clicked.connect(lambda: self.corrige(3, 'passe',self.N_passe_D))

        self.SAQ_A.clicked.connect(lambda: self.corrige(0, 'saque',self.N_saque_green))
        self.SAQ_B.clicked.connect(lambda: self.corrige(1, 'saque',self.N_saque_blue))
        self.SAQ_C.clicked.connect(lambda: self.corrige(2, 'saque',self.N_saque_ora))
        self.SAQ_D.clicked.connect(lambda: self.corrige(3, 'saque',self.N_saque_red))

        self.PNL_rede.clicked.connect(lambda: self.corrige(0, 'penalidades',self.N_rede))
        self.PNL_cartao.clicked.connect(lambda: self.corrige(1, 'penalidades',self.N_cartao))
        self.PNL_2t.clicked.connect(lambda: self.corrige(2, 'penalidades',self.N_2t))
        self.PNL_cond.clicked.connect(lambda: self.corrige(3, 'penalidades',self.N_cond))

        ''' Quando algum jogador for clicado e barra de menu superior '''
        self.PB_1.clicked.connect(self.page_1_mostra)
        self.PB_2.clicked.connect(self.page_2_mostra)
        self.PB_3.clicked.connect(self.page_3_mostra)
        self.PB_4.clicked.connect(self.page_4_mostra)
        self.PB_5.clicked.connect(self.page_5_mostra)
        self.PB_6.clicked.connect(self.page_6_mostra)
        self.PB_7.clicked.connect(self.page_7_mostra)
        self.PB_8.clicked.connect(self.page_8_mostra)
        self.PB_9.clicked.connect(self.page_9_mostra)
        self.estilos_aba_pressionada = ("QPushButton{\n"
                                        "font: 12pt \"Cortoba\";\n"
                                        "color: rgb(238, 238, 236);\n"
                                        "border-radius: 0px;\n"
                                        "border-top: 1px solid  rgb(0, 225, 255);\n"
                                        "border-left: 1px solid  rgb(0, 225, 255);\n"
                                        "border-right: 1px solid  rgb(0, 225, 255);\n""}\n"
                                        "QPushButton:hover{;\n"
                                        "border-top: 1px solid  rgb(0, 225, 255);\n"
                                        "border-left: 1px solid  rgb(0, 225, 255);\n"
                                        "border-right: 1px solid rgb(0, 225, 255);\n"
                                        "background-color: rgb(0, 144, 153);\n""}\n"
                                        "QPushButton:pressed {background-color: rgb(85, 87, 83);}")
        self.estilos_aba_Npressionada = ("QPushButton{\n"
                                        "font: 12pt \"Cortoba\";\n"
                                        "color: rgb(238, 238, 236);\n"
                                        "border-radius: 0px;\n""}\n"
                                        "QPushButton:hover{;\n"
                                        "border-top: 1px solid  rgb(0, 225, 255);\n"
                                        "border-left: 1px solid  rgb(0, 225, 255);\n"
                                        "border-right: 1px solid  rgb(0, 225, 255);\n"
                                        "background-color: rgb(0, 144, 153);\n""}\n"
                                        "QPushButton:pressed {background-color: rgb(85, 87, 83);}")
        self.estilos_iguais_click = ("font: 11pt \"Cortoba\";\n"
                                    "border: 1px solid  rgb(85, 87, 83);\n"
                                    "color: rgb(238, 238, 236);\n"
                                    "border-radius: 5px;\n""}\n"
                                    "QPushButton:hover{background-color: rgb(85, 87, 83);}\n""")
        self.estilos_diferentes_click = ("QPushButton{\n"
                                         "background-color: rgb(85, 87, 83);\n"
                                         "font: 11pt \"Cortoba\";\n"
                                         "border: 1px solid  rgb(5, 255, 0);\n"
                                         "color: rgb(5, 255, 0);\n"
                                         "border-radius: 5px;\n""}\n"
                                         "QPushButton:hover{background-color: rgb(85, 87, 83);}\n""")
        #--------------------------------------------------------------------
        self.meutime = True #Informa em qual time estou marcando os dados
        self.PB_J1.clicked.connect(lambda:self.jogador_clicado(self.t1, 1))
        self.PB_J2.clicked.connect(lambda:self.jogador_clicado(self.t2, 2))
        self.PB_J3.clicked.connect(lambda:self.jogador_clicado(self.t3, 3))
        self.PB_J4.clicked.connect(lambda:self.jogador_clicado(self.t4, 4))
        self.PB_J5.clicked.connect(lambda:self.jogador_clicado(self.t5, 5))
        self.PB_J6.clicked.connect(lambda:self.jogador_clicado(self.t6, 6))
        self.PB_J7.clicked.connect(lambda:self.jogador_clicado(self.t7, 7))
        self.PB_J8.clicked.connect(lambda:self.jogador_clicado(self.t8, 8))
        self.PB_J9.clicked.connect(lambda:self.jogador_clicado(self.t9, 9))
        self.PB_J10.clicked.connect(lambda:self.jogador_clicado(self.t10, 10))
        self.PB_J11.clicked.connect(lambda:self.jogador_clicado(self.t11, 11))
        self.PB_J12.clicked.connect(lambda:self.jogador_clicado(self.t12, 12))
        self.PB_J13.clicked.connect(lambda:self.jogador_clicado(self.t13, 13))
        self.PB_J14.clicked.connect(lambda:self.jogador_clicado(self.t14, 14))
        #----------------OPONENTES--------------------------------------------
        self.PB_O1.clicked.connect(lambda:self.jogador_clicado(self.o1, 15))
        self.PB_O2.clicked.connect(lambda:self.jogador_clicado(self.o2, 16))
        self.PB_O3.clicked.connect(lambda:self.jogador_clicado(self.o3, 17))
        self.PB_O4.clicked.connect(lambda:self.jogador_clicado(self.o4, 18))
        self.PB_O5.clicked.connect(lambda:self.jogador_clicado(self.o5, 19))
        self.PB_O6.clicked.connect(lambda:self.jogador_clicado(self.o6, 20))
        self.PB_O7.clicked.connect(lambda:self.jogador_clicado(self.o7, 21))
        self.PB_O8.clicked.connect(lambda:self.jogador_clicado(self.o8, 22))
        self.PB_O9.clicked.connect(lambda:self.jogador_clicado(self.o9, 23))
        self.PB_O10.clicked.connect(lambda:self.jogador_clicado(self.o10, 24))
        self.PB_O11.clicked.connect(lambda:self.jogador_clicado(self.o11, 25))
        self.PB_O12.clicked.connect(lambda:self.jogador_clicado(self.o12, 26))
        self.PB_O13.clicked.connect(lambda:self.jogador_clicado(self.o13, 27))
        self.PB_O14.clicked.connect(lambda:self.jogador_clicado(self.o14, 28))
        '''Relatorio Botões'''
        self.meutimerelatorio = True
        self.pararelatorio = 0 # para mudar o time na tabela e continuar no mesmo fundamento
        self.PB_Time_Relatorio.clicked.connect(lambda: self.mudatimerelatorio(self.pararelatorio))
        self.PB_Save_Relatorio.clicked.connect(lambda:self.directory('relatorio'))
        self.PB_Relatorio_Ataque.clicked.connect(lambda:self.tabela(1))
        self.PB_Relatorio_Bloqueio.clicked.connect(lambda:self.tabela(2))
        self.PB_Relatorio_Defesa.clicked.connect(lambda:self.tabela(3))
        self.PB_Relatorio_Saque.clicked.connect(lambda:self.tabela(4))
        self.PB_Relatorio_Passe.clicked.connect(lambda:self.tabela(5))
        self.PB_Relatorio_Penalidade.clicked.connect(lambda:self.tabela(6))
        self.PB_Relatorio_Cataque.clicked.connect(lambda:self.tabela(7))
        '''Graficos Botões'''
        self.equipe_graficos = True
        self.PB_Save_Saque.clicked.connect(lambda:self.directory('saque'))
        self.PB_Equipe_Saque.clicked.connect(self.draw_saque)
        self.PB_Save_Defesa.clicked.connect(lambda:self.directory('defesa'))
        self.PB_Equipe_Defesa.clicked.connect(self.draw_defesa)
        self.PB_Save_Pontos.clicked.connect(lambda:self.directory('acoes'))
        self.PB_Save_Ataque.clicked.connect(lambda:self.directory('ataque'))
        self.PB_Equipe_Ataque.clicked.connect(self.draw_ataque)
        self.PB_Save_Bloqueio.clicked.connect(lambda:self.directory('bloqueio'))
        self.PB_Equipe_Bloqueio.clicked.connect(self.draw_bloqueio)
        self.PB_Save_Passe.clicked.connect(lambda:self.directory('passe'))
        self.PB_Equipe_Passe.clicked.connect(self.draw_passe)
        '''Posiciometro'''
        self.xy = [False, False]
        self.posicaoxy = ''
        self.tenhoposicao = False
        self.A1_3.clicked.connect(lambda:self.position(1))
        self.A2_3.clicked.connect(lambda:self.position(2))
        self.A3_3.clicked.connect(lambda:self.position(3))
        self.A4_3.clicked.connect(lambda:self.position(4))
        self.A5_3.clicked.connect(lambda:self.position(5))
        self.A6_3.clicked.connect(lambda:self.position(6))
        self.B1_3.clicked.connect(lambda:self.position(1))
        self.B2_3.clicked.connect(lambda:self.position(2))
        self.B3_3.clicked.connect(lambda:self.position(3))
        self.B4_3.clicked.connect(lambda:self.position(4))
        self.B5_3.clicked.connect(lambda:self.position(5))
        self.B6_3.clicked.connect(lambda:self.position(6))
    #------------------------------------------------------------------------
    def acress_placar_extra(self, x):
        ''' Acrescenta e retira pontos do placar manualmente '''
        if x == 1:
            i = int(self.label_Plagreen.text()) + 1
            self.label_Plagreen.setText(str(i))
        if x == 3:
            i = int(self.label_Plared.text()) + 1
            self.label_Plared.setText(str(i))
        if x == 2 :
            i = int(self.label_Plagreen.text()) - 1
            if i < 0:
                i = 0
            self.label_Plagreen.setText(str(i))
        if x == 4:
            i = int(self.label_Plared.text()) - 1
            if i < 0:
                i = 0
            self.label_Plared.setText(str(i))

    def draw_pontos(self):
        ''' Só esta fazendo para 8 jogadores '''
        self.graphicsView_Pontos.clear()
        self.graphicsView_Pontos.show()
        viewBox = self.graphicsView_Pontos.getViewBox()
        viewBox.setMouseEnabled(x = False, y = False)
        self.graphicsView_Pontos.setMenuEnabled(enableViewBoxMenu = False)
        self.graphicsView_Pontos.hideButtons()
        self.graphicsView_Pontos.setBackground((46, 52, 54))
        self.graphicsView_Pontos.showGrid(x = True, y = True, alpha = 0.5)
        self.graphicsView_Pontos.setTitle("Frequência de Pontuação")
        self.graphicsView_Pontos.addLegend()
        #self.graphicsView_Pontos.setYRange(0, 60, padding = 0)
        self.graphicsView_Pontos.setLabel('left', 'Pontos', units='')
        self.graphicsView_Pontos.setLabel('right')
        self.graphicsView_Pontos.setLabel('bottom', '(s)', units='')

        Xgreen = []
        Ygreen = []
        Xred = []
        Yred = []

        duracao_t = self.PB_Scores_Time.text()
        pontos_a = self.label_Plagreen.text()
        pontos_b = self.label_Plared.text()
        if duracao_t == "Iniciar Tempo":
            taxa_a = 0
            taxa_b = 0
        else:
            duracao_t = int(duracao_t.split(":")[0])
            if duracao_t == 0:
                taxa_a = 0
                taxa_b = 0
            else:
                taxa_a = round(float(pontos_a)/duracao_t, 2)
                taxa_b = round(float(pontos_b)/duracao_t, 2)

        for d in self.poissonA:
            Xgreen.append(d[1])
            Ygreen.append(d[0])
        for d in self.poissonB:
            Xred.append(d[1])
            Yred.append(d[0])

        if self.nome_time.text().strip() == '':
            timeA = 'Time A - Taxa: '  + str(taxa_a) + " pts/min."
        else: timeA = self.nome_time.text() + " - Taxa: "+str(taxa_a) + " pts/min."
        if self.nome_oponente.text().strip() == '':
            timeB = 'Time B - Taxa: ' + str(taxa_b) + " pts/min."
        else: timeB =self.nome_oponente.text() + " - Taxa: "+str(taxa_b) + " pts/min."

        self.graphicsView_Pontos.plot(Xgreen, Ygreen, pen=pg.mkPen(color=(0,255,174,230), width=3), name=timeA)
        self.graphicsView_Pontos.plot(Xred, Yred, pen=pg.mkPen(color=(255,124,0,230), width=3), name=timeB)
    def draw_defesa(self):
        self.graphicsView_Defesa.clear()
        self.graphicsView_Defesa.show()
        viewBox = self.graphicsView_Defesa.getViewBox()
        viewBox.setMouseEnabled(x=False, y=False)
        self.graphicsView_Defesa.setMenuEnabled(enableViewBoxMenu= False)
        self.graphicsView_Defesa.hideButtons()
        self.graphicsView_Defesa.setBackground((46, 52, 54))
        self.graphicsView_Defesa.showGrid(x = True, y = True, alpha = 0.1)
        self.graphicsView_Defesa.setTitle("Taxa Sucesso Defesa")
        self.graphicsView_Defesa.setYRange(-110, 110, padding=0)
        self.graphicsView_Defesa.setLabel('left', '%', units='')
        self.graphicsView_Defesa.setLabel('right')
        self.graphicsView_Defesa.setLabel('bottom', '', units='')

        if self.equipe_graficos:
            if self.nome_time.text() == "": self.graphicsView_Defesa.setTitle("Taxa Sucesso Defesa % - Time A" )
            else: self.graphicsView_Defesa.setTitle("Taxa Sucesso Defesa % - " + self.nome_time.text())
            self.meutimerelatorio = True
            nomes = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                     self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                     self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                     self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                     self.nome_j13.text(),self.nome_j14.text()]
        else:
            if self.nome_oponente.text() == "": self.graphicsView_Defesa.setTitle("Taxa Sucesso Defesa % - Time B")
            else: self.graphicsView_Defesa.setTitle("Taxa Sucesso Defesa % - " + self.nome_oponente.text())
            self.meutimerelatorio = False
            nomes = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                     self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                     self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                     self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                     self.nome_o13.text(),self.nome_o14.text()]

        ingame = []
        for n in nomes:
            if n.strip() != '':
                ingame.append( self.index_player( 1 + nomes.index(n)) )
        defendeu = []
        for j in ingame:
            if j.totais()[3] != 0:
                defendeu.append(j)

        nomes_usar = []
        y_positivos = []
        x_positivos = []
        y_negativos = []
        x_negativos = []
        totais = []#[(total de defesas, eficiencia %, n)]
        n = 0
        for i in defendeu:
            nomes_usar.append((n+1, i.nome))
            if i.ef_defesa() > 0:
                n += 1
                totais.append((i.totais()[3], 100*i.ef_defesa(), n))
                y_positivos.append(100*i.ef_defesa())
                x_positivos.append(n)
            else:
                n += 1
                totais.append((i.totais()[3], 100*i.ef_defesa(), n))
                y_negativos.append(100*i.ef_defesa())
                x_negativos.append(n)
        nomes = [nomes_usar]
        #legendas totais Blue / Red
        legenda_b = pg.TextItem(html='<span style="color: #FFF; font-size: 9pt;">Ganho</span>', anchor=(0.5,0.9), angle=0, border=(0, 225, 255) , fill=(0, 112, 114))
        legenda_r = pg.TextItem(html='<span style="color: #FFF; font-size: 9pt;">Perda</span>', anchor=(0.5,0.9), angle=0, border=(255, 0, 0) , fill=(255, 106, 106))
        self.graphicsView_Defesa.addItem(legenda_b)
        self.graphicsView_Defesa.addItem(legenda_r)
        legenda_b.setPos(0, 90)
        legenda_r.setPos(0, -90)
        for i in totais:
            if i[1] >= 0:
                text = pg.TextItem(html='<span style="color: #FFF; font-size: 7pt;">Total de: %d</span>'%(i[0]), anchor=(0.5,0.9), angle=0)
                self.graphicsView_Defesa.addItem(text)
                text.setPos(i[2], i[1])
            else:
                text = pg.TextItem(html='<span style="color: #FFF; font-size: 7pt;">Total de: %d</span>'%(i[0]), anchor=(0.5,-0.1), angle=0)
                self.graphicsView_Defesa.addItem(text)
                text.setPos(i[2], i[1])

        if nomes != [[]]:
            x = [*range(1,n+1)]
            bg1 = pg.BarGraphItem(x = x_positivos, height = y_positivos, width = 0.3, brush=(0, 112, 114), pen=(0, 225, 255))
            bg2 = pg.BarGraphItem(x = x_negativos, height = y_negativos, width = 0.3, brush=(255, 106, 106), pen=(255, 0, 0))

            self.graphicsView_Defesa.getAxis('bottom').setTicks(nomes)
            self.graphicsView_Defesa.addItem(bg1)
            self.graphicsView_Defesa.addItem(bg2)
        self.equipe_graficos = not self.equipe_graficos
    def draw_saque(self):
        self.graphicsView_Saque.clear()
        self.graphicsView_Saque.show()
        viewBox = self.graphicsView_Saque.getViewBox()
        viewBox.setMouseEnabled(x = False, y = False)
        self.graphicsView_Saque.setMenuEnabled(enableViewBoxMenu = False)
        self.graphicsView_Saque.hideButtons()
        self.graphicsView_Saque.setBackground((46, 52, 54))
        self.graphicsView_Saque.showGrid(x = True, y = True, alpha = 0.1)
        self.graphicsView_Saque.setTitle("Classificação de Saque")
        #self.graphicsView_Saque.setYRange(-110, 110, padding=0)
        self.graphicsView_Saque.setLabel('left','%',units='')
        self.graphicsView_Saque.setLabel('right')
        self.graphicsView_Saque.setLabel('bottom','',units='')

        if self.equipe_graficos:
            if self.nome_time.text() == "": self.graphicsView_Saque.setTitle("Classificação de Saque - Time A" )
            else: self.graphicsView_Saque.setTitle("Classificação de Saque - " + self.nome_time.text())
            self.meutimerelatorio = True
            nomes = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                     self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                     self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                     self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                     self.nome_j13.text(),self.nome_j14.text()]
        else:
            if self.nome_oponente.text() == "": self.graphicsView_Saque.setTitle("Classificação de Saque - Time B")
            else: self.graphicsView_Saque.setTitle("Classificação de Saque - " + self.nome_oponente.text())
            self.meutimerelatorio = False
            nomes = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                     self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                     self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                     self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                     self.nome_o13.text(),self.nome_o14.text()]

        ingame = []
        for n in nomes:
            if n.strip() != '':
                ingame.append( self.index_player( 1 + nomes.index(n)) )
        passou = []
        for j in ingame:
            if j.totais()[6] != 0:
                passou.append(j)

        nomes_eixo_x = []
        x = 1
        for n in passou:
            nomes_eixo_x.append((x, n.nome))
            x += 1

        esp = 0.85
        self.graphicsView_Saque.getAxis("bottom").setTicks([nomes_eixo_x])


        for j in passou:
            self.graphicsView_Saque.addItem(pg.BarGraphItem(x = [esp]        ,height = len(j.saque[0]),width = 0.1,brush=(111, 219, 1), pen='k'))
            self.graphicsView_Saque.addItem(pg.BarGraphItem(x = [esp + 0.125],height = len(j.saque[1]),width = 0.1,brush=(0, 112, 114), pen='k'))
            self.graphicsView_Saque.addItem(pg.BarGraphItem(x = [esp + 0.250],height = len(j.saque[2]),width = 0.1,brush=(255, 140, 0), pen='k'))
            self.graphicsView_Saque.addItem(pg.BarGraphItem(x = [esp + 0.375],height = len(j.saque[3]),width = 0.1,brush=(255, 106, 106),pen='k'))

            text_A  = pg.TextItem(html='<span style="color:rgb(111, 219, 1);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[0])+'%'), anchor=(0,0), angle=90)
            text_B  = pg.TextItem(html='<span style="color:rgb(0, 225, 255);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[1])+'%'), anchor=(0,0), angle=90)
            text_C  = pg.TextItem(html='<span style="color:rgb(255, 140, 0);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[2])+'%'), anchor=(0,0), angle=90)
            text_D  = pg.TextItem(html='<span style="color:rgb(255,106,106);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[3])+'%'), anchor=(0,0), angle=90)

            text_A_bot  = pg.TextItem(html='<span style="color:rgb(111, 219, 1); font-size: 9pt;"><strong>A</strong></span>', anchor=(0,0), angle=0)
            text_B_bot  = pg.TextItem(html='<span style="color:rgb(0, 225, 255); font-size: 9pt;"><strong>B</strong></span>', anchor=(0,0), angle=0)
            text_C_bot  = pg.TextItem(html='<span style="color:rgb(255, 140, 0); font-size: 9pt;"><strong>C</strong></span>', anchor=(0,0), angle=0)
            text_D_bot  = pg.TextItem(html='<span style="color:rgb(255,106,106); font-size: 9pt;"><strong>D</strong></span>', anchor=(0,0), angle=0)

            self.graphicsView_Saque.addItem(text_A)
            self.graphicsView_Saque.addItem(text_B)
            self.graphicsView_Saque.addItem(text_C)
            self.graphicsView_Saque.addItem(text_D)
            self.graphicsView_Saque.addItem(text_A_bot)
            self.graphicsView_Saque.addItem(text_B_bot)
            self.graphicsView_Saque.addItem(text_C_bot)
            self.graphicsView_Saque.addItem(text_D_bot)

            text_A.setPos(esp -0.05        , len(j.saque[0]) + 0.2)
            text_B.setPos(esp -0.05 + 0.120, len(j.saque[1]) + 0.2)
            text_C.setPos(esp -0.05 + 0.250, len(j.saque[2]) + 0.2)
            text_D.setPos(esp -0.05 + 0.375, len(j.saque[3]) + 0.2)

            text_A_bot.setPos(esp-0.04,         0)
            text_B_bot.setPos(esp-0.04 + 0.125, 0)
            text_C_bot.setPos(esp-0.04 + 0.250, 0)
            text_D_bot.setPos(esp-0.04 + 0.375, 0)

            esp += 1

        self.equipe_graficos = not self.equipe_graficos
    def draw_ataque(self):
        self.graphicsView_Ataque.clear()
        self.graphicsView_Ataque.show()
        viewBox = self.graphicsView_Ataque.getViewBox()
        viewBox.setMouseEnabled(x=False, y=False)
        self.graphicsView_Ataque.setMenuEnabled(enableViewBoxMenu= False)
        self.graphicsView_Ataque.hideButtons()
        self.graphicsView_Ataque.setBackground((46, 52, 54))
        self.graphicsView_Ataque.showGrid(x = True, y = True, alpha = 0.1)
        self.graphicsView_Ataque.setTitle("Taxa de Sucesso Ataque %")
        self.graphicsView_Ataque.setYRange(-110, 110, padding=0)
        self.graphicsView_Ataque.setLabel('left', '%', units='')
        self.graphicsView_Ataque.setLabel('right')
        self.graphicsView_Ataque.setLabel('bottom', '', units='')

        if self.equipe_graficos:
            if self.nome_time.text() == "": self.graphicsView_Ataque.setTitle("Taxa de Sucesso Ataque % - Time A" )
            else: self.graphicsView_Ataque.setTitle("Taxa de Sucesso Ataque % - " + self.nome_time.text())
            self.meutimerelatorio = True
            nomes = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                     self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                     self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                     self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                     self.nome_j13.text(),self.nome_j14.text()]
        else:
            if self.nome_oponente.text() == "": self.graphicsView_Ataque.setTitle("Taxa de Sucesso Ataque % - Time B")
            else: self.graphicsView_Ataque.setTitle("Taxa de Sucesso Ataque % - " + self.nome_oponente.text())
            self.meutimerelatorio = False
            nomes = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                     self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                     self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                     self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                     self.nome_o13.text(),self.nome_o14.text()]

        ingame = []
        for n in nomes:
            if n.strip() != '':
                ingame.append( self.index_player( 1 + nomes.index(n)) )
        atacou = []
        for j in ingame:
            if j.totais()[0] != 0:
                atacou.append(j)

        nomes_usar = []
        y_positivos = []
        x_positivos = []
        y_negativos = []
        x_negativos = []
        totais = []#[(total de ataques, eficiencia %, n)]
        n = 0
        for i in atacou:
            nomes_usar.append((n+1, i.nome))
            if i.ef_ataque() > 0:
                n += 1
                totais.append((i.totais()[0], 100*i.ef_ataque(), n))
                y_positivos.append(100*i.ef_ataque())
                x_positivos.append(n)
            else:
                n += 1
                totais.append((i.totais()[0], 100*i.ef_ataque(), n))
                y_negativos.append(100*i.ef_ataque())
                x_negativos.append(n)
        nomes = [nomes_usar]
       #legendas totais
        legenda_b = pg.TextItem(html='<span style="color: #FFF; font-size: 9pt;">Ganho de Pontos</span>', anchor=(0.5,0.9), angle=0, border=(0, 225, 255) , fill=(0, 112, 114))
        legenda_r = pg.TextItem(html='<span style="color: #FFF; font-size: 9pt;">Perda de Pontos</span>', anchor=(0.5,0.9), angle=0, border=(255, 0, 0) , fill=(255, 106, 106))
        self.graphicsView_Ataque.addItem(legenda_b)
        self.graphicsView_Ataque.addItem(legenda_r)
        legenda_b.setPos(0, 90)
        legenda_r.setPos(0, -90)
        for i in totais:
            if i[1] >= 0:
                text = pg.TextItem(html='<span style="color: #FFF; font-size: 7pt;">Total de: %d</span>'%(i[0]), anchor=(0.5,0.9), angle=0)
                self.graphicsView_Ataque.addItem(text)
                text.setPos(i[2], i[1])
            else:
                text = pg.TextItem(html='<span style="color: #FFF; font-size: 7pt;">Total de: %d</span>'%(i[0]), anchor=(0.5,-0.1), angle=0)
                self.graphicsView_Ataque.addItem(text)
                text.setPos(i[2], i[1])

        if nomes != [[]]:
            x = [*range(1,n+1)]
            bg1 = pg.BarGraphItem(x = x_positivos, height = y_positivos, width = 0.3, brush=(0, 112, 114), pen=(0, 225, 255))
            bg2 = pg.BarGraphItem(x = x_negativos, height = y_negativos, width = 0.3, brush=(255, 106, 106), pen=(255, 0, 0))
            self.graphicsView_Ataque.getAxis('bottom').setTicks(nomes)
            self.graphicsView_Ataque.addItem(bg1)
            self.graphicsView_Ataque.addItem(bg2)
        self.equipe_graficos = not self.equipe_graficos
    def draw_bloqueio(self):
        self.graphicsView_Bloqueio.clear()
        self.graphicsView_Bloqueio.show()
        viewBox = self.graphicsView_Bloqueio.getViewBox()
        viewBox.setMouseEnabled(x=False, y=False)
        self.graphicsView_Bloqueio.setMenuEnabled(enableViewBoxMenu= False)
        self.graphicsView_Bloqueio.hideButtons()
        self.graphicsView_Bloqueio.setBackground((46, 52, 54))
        self.graphicsView_Bloqueio.showGrid(x = True, y = True, alpha = 0.1)
        self.graphicsView_Bloqueio.setTitle("Taxa de Bloqueio %")
        self.graphicsView_Bloqueio.setYRange(-110, 110, padding=0)
        self.graphicsView_Bloqueio.setLabel('left', '%', units='')
        self.graphicsView_Bloqueio.setLabel('right')
        self.graphicsView_Bloqueio.setLabel('bottom', '', units='')

        if self.equipe_graficos:
            if self.nome_time.text() == "": self.graphicsView_Bloqueio.setTitle("Taxa Sucesso Bloqueio % - Time A" )
            else: self.graphicsView_Bloqueio.setTitle("Taxa de Bloqueio % - " + self.nome_time.text())
            self.meutimerelatorio = True
            nomes = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                     self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                     self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                     self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                     self.nome_j13.text(),self.nome_j14.text()]
        else:
            if self.nome_oponente.text() == "": self.graphicsView_Bloqueio.setTitle("Taxa Sucesso Bloqueio % - Time B")
            else: self.graphicsView_Bloqueio.setTitle("Taxa Sucesso Bloqueio % - " + self.nome_oponente.text())
            self.meutimerelatorio = False
            nomes = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                     self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                     self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                     self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                     self.nome_o13.text(),self.nome_o14.text()]

        ingame = []
        for n in nomes:
            if n.strip() != '':
                ingame.append( self.index_player( 1 + nomes.index(n)) )
        bloqueou = []
        for j in ingame:
            if j.totais()[1] != 0:
                bloqueou.append(j)

        nomes_usar = []
        y_positivos = []
        x_positivos = []
        y_negativos = []
        x_negativos = []
        totais = []#[(total de ataques, eficiencia %, n)]
        n = 0
        for i in bloqueou:
            nomes_usar.append((n+1, i.nome))
            if i.ef_bloqueio() > 0:
                n += 1
                totais.append((i.totais()[1], 100*i.ef_bloqueio(), n))
                y_positivos.append(100*i.ef_bloqueio())
                x_positivos.append(n)
            else:
                n += 1
                totais.append((i.totais()[1], 100*i.ef_bloqueio(), n))
                y_negativos.append(100*i.ef_bloqueio())
                x_negativos.append(n)
        nomes = [nomes_usar]
        #legendas totais Azul/vermelho
        legenda_b = pg.TextItem(html='<span style="color: #FFF; font-size: 9pt;">Ganho</span>', anchor=(0.5,0.9), angle=0, border=(0, 225, 255) , fill=(0, 112, 114))
        legenda_r = pg.TextItem(html='<span style="color: #FFF; font-size: 9pt;">Perda</span>', anchor=(0.5,0.9), angle=0, border=(255, 0, 0) , fill=(255, 106, 106))
        self.graphicsView_Bloqueio.addItem(legenda_b)
        self.graphicsView_Bloqueio.addItem(legenda_r)
        legenda_b.setPos(0, 90)
        legenda_r.setPos(0, -90)
        for i in totais:
            if i[1] >= 0:
                text = pg.TextItem(html='<span style="color: #FFF; font-size: 7pt;">Total de: %d</span>'%(i[0]), anchor=(0.5,0.9), angle=0)
                self.graphicsView_Bloqueio.addItem(text)
                text.setPos(i[2], i[1])
            else:
                text = pg.TextItem(html='<span style="color: #FFF; font-size: 7pt;">Total de: %d</span>'%(i[0]), anchor=(0.5,-0.1), angle=0)
                self.graphicsView_Bloqueio.addItem(text)
                text.setPos(i[2], i[1])
        if nomes != [[]]:
            x = [*range(1,n+1)]
            bg1 = pg.BarGraphItem(x = x_positivos, height = y_positivos, width = 0.3, brush=(0, 112, 114), pen=(0, 225, 255))
            bg2 = pg.BarGraphItem(x = x_negativos, height = y_negativos, width = 0.3, brush=(255, 106, 106), pen=(255, 0, 0))

            self.graphicsView_Bloqueio.getAxis('bottom').setTicks(nomes)
            self.graphicsView_Bloqueio.addItem(bg1)
            self.graphicsView_Bloqueio.addItem(bg2)
        self.equipe_graficos = not self.equipe_graficos
    def draw_passe(self):
        self.graphicsView_Passe.clear()
        self.graphicsView_Passe.show()
        viewBox = self.graphicsView_Passe.getViewBox()
        viewBox.setMouseEnabled(x=False, y=False)
        self.graphicsView_Passe.setMenuEnabled(enableViewBoxMenu= False)
        self.graphicsView_Passe.hideButtons()
        self.graphicsView_Passe.setBackground((46, 52, 54))
        self.graphicsView_Passe.showGrid(x = True, y = True, alpha = 0.1)
        self.graphicsView_Passe.setTitle("Classificação de Passe")
        #self.graphicsView_Passe.setYRange(0, 110, padding=0)
        self.graphicsView_Passe.setLabel('left','Número de Passes', units='')
        self.graphicsView_Passe.setLabel('right')
        self.graphicsView_Passe.setLabel('bottom','',units='')

        if self.equipe_graficos:
            if self.nome_time.text() == "": self.graphicsView_Passe.setTitle("Classificação de Passe - Time A" )
            else: self.graphicsView_Passe.setTitle("Classificação de Passe - " + self.nome_time.text())
            self.meutimerelatorio = True
            nomes = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                     self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                     self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                     self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                     self.nome_j13.text(),self.nome_j14.text()]
        else:
            if self.nome_oponente.text() == "": self.graphicsView_Passe.setTitle("Classificação de Passe - Time B")
            else: self.graphicsView_Passe.setTitle("Classificação de Passe - " + self.nome_oponente.text())
            self.meutimerelatorio = False
            nomes = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                     self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                     self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                     self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                     self.nome_o13.text(),self.nome_o14.text()]

        ingame = []
        for n in nomes:
            if n.strip() != '':
                ingame.append( self.index_player( 1 + nomes.index(n)) )
        passou = []
        for j in ingame:
            if j.totais()[4] != 0:
                passou.append(j)

        nomes_eixo_x = []
        x = 1
        for n in passou:
            nomes_eixo_x.append((x, n.nome))
            x += 1

        esp = 0.85
        self.graphicsView_Passe.getAxis("bottom").setTicks([nomes_eixo_x])

        legendar = [] # para guardar as coordenadas e dados de cada passe para fazer a % de A,B,C,D
        for j in passou:
            self.graphicsView_Passe.addItem(pg.BarGraphItem(x = [esp]        ,height = len(j.passe[0]),width = 0.1,brush=(111, 219, 1), pen='k'))
            self.graphicsView_Passe.addItem(pg.BarGraphItem(x = [esp + 0.125],height = len(j.passe[1]),width = 0.1,brush=(0, 112, 114), pen='k'))
            self.graphicsView_Passe.addItem(pg.BarGraphItem(x = [esp + 0.250],height = len(j.passe[2]),width = 0.1,brush=(255, 140, 0), pen='k'))
            self.graphicsView_Passe.addItem(pg.BarGraphItem(x = [esp + 0.375],height = len(j.passe[3]),width = 0.1,brush=(255, 106, 106),pen='k'))
            #------------teste-------------
            text_A  = pg.TextItem(html='<span style="color:rgb(111, 219, 1);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[0])+'%'), anchor=(0,0), angle=90)
            text_B  = pg.TextItem(html='<span style="color:rgb(0, 225, 255);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[1])+'%'), anchor=(0,0), angle=90)
            text_C  = pg.TextItem(html='<span style="color:rgb(255, 140, 0);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[2])+'%'), anchor=(0,0), angle=90)
            text_D  = pg.TextItem(html='<span style="color:rgb(255,106,106);font-size: 8pt;">%s</span>'%(str(j.porcentagem_passe()[3])+'%'), anchor=(0,0), angle=90)

            text_A_bot  = pg.TextItem(html='<span style="color:rgb(111, 219, 1); font-size: 9pt;"><strong>A</strong></span>', anchor=(0,0), angle=0)
            text_B_bot  = pg.TextItem(html='<span style="color:rgb(0, 225, 255); font-size: 9pt;"><strong>B</strong></span>', anchor=(0,0), angle=0)
            text_C_bot  = pg.TextItem(html='<span style="color:rgb(255, 140, 0); font-size: 9pt;"><strong>C</strong></span>', anchor=(0,0), angle=0)
            text_D_bot  = pg.TextItem(html='<span style="color:rgb(255,106,106); font-size: 9pt;"><strong>D</strong></span>', anchor=(0,0), angle=0)

            self.graphicsView_Passe.addItem(text_A)
            self.graphicsView_Passe.addItem(text_B)
            self.graphicsView_Passe.addItem(text_C)
            self.graphicsView_Passe.addItem(text_D)
            self.graphicsView_Passe.addItem(text_A_bot)
            self.graphicsView_Passe.addItem(text_B_bot)
            self.graphicsView_Passe.addItem(text_C_bot)
            self.graphicsView_Passe.addItem(text_D_bot)

            text_A.setPos(esp -0.05        , len(j.passe[0]) + 0.2)
            text_B.setPos(esp -0.05 + 0.120, len(j.passe[1]) + 0.2)
            text_C.setPos(esp -0.05 + 0.250, len(j.passe[2]) + 0.2)
            text_D.setPos(esp -0.05 + 0.375, len(j.passe[3]) + 0.2)

            text_A_bot.setPos(esp-0.04,         0)
            text_B_bot.setPos(esp-0.04 + 0.125, 0)
            text_C_bot.setPos(esp-0.04 + 0.250, 0)
            text_D_bot.setPos(esp-0.04 + 0.375, 0)

            esp += 1
            #------------------------------
            #legendar.append((esp, j))
            #esp += 1
        # Plota a % de cada tipo de passe para cada jogador que realizou passes
        self.equipe_graficos = not self.equipe_graficos
        '''
        for i in legendar:
            if len(legendar) <= 6:
                text_A  = pg.TextItem(html='<span style="color:rgb(111, 219, 1);font-size: 8pt;">%s</span>'%(str(i[1].porcentagem_passe()[0])+'%'), anchor=(0,0), angle=90)
                text_B  = pg.TextItem(html='<span style="color:rgb(0, 225, 255);font-size: 8pt;">%s</span>'%(str(i[1].porcentagem_passe()[1])+'%'), anchor=(0,0), angle=90)
                text_C  = pg.TextItem(html='<span style="color:rgb(255, 140, 0);font-size: 8pt;">%s</span>'%(str(i[1].porcentagem_passe()[2])+'%'), anchor=(0,0), angle=90)
                text_D  = pg.TextItem(html='<span style="color:rgb(255,106,106);font-size: 8pt;">%s</span>'%(str(i[1].porcentagem_passe()[3])+'%'), anchor=(0,0), angle=90)

                text_A_bot  = pg.TextItem(html='<span style="color:rgb(111, 219, 1); font-size: 9pt;"><strong>A</strong></span>', anchor=(0,0), angle=0)
                text_B_bot  = pg.TextItem(html='<span style="color:rgb(0, 225, 255); font-size: 9pt;"><strong>B</strong></span>', anchor=(0,0), angle=0)
                text_C_bot  = pg.TextItem(html='<span style="color:rgb(255, 140, 0); font-size: 9pt;"><strong>C</strong></span>', anchor=(0,0), angle=0)
                text_D_bot  = pg.TextItem(html='<span style="color:rgb(255,106,106); font-size: 9pt;"><strong>D</strong></span>', anchor=(0,0), angle=0)

                self.graphicsView_Passe.addItem(text_A)
                self.graphicsView_Passe.addItem(text_B)
                self.graphicsView_Passe.addItem(text_C)
                self.graphicsView_Passe.addItem(text_D)
                self.graphicsView_Passe.addItem(text_A_bot)
                self.graphicsView_Passe.addItem(text_B_bot)
                self.graphicsView_Passe.addItem(text_C_bot)
                self.graphicsView_Passe.addItem(text_D_bot)

                text_A.setPos(i[0] -0.05        , len(i[1].passe[0]) + 0.2)
                text_B.setPos(i[0] -0.05 + 0.120, len(i[1].passe[1]) + 0.2)
                text_C.setPos(i[0] -0.05 + 0.250, len(i[1].passe[2]) + 0.2)
                text_D.setPos(i[0] -0.05 + 0.375, len(i[1].passe[3]) + 0.2)

                text_A_bot.setPos(i[0]-0.04,         0)
                text_B_bot.setPos(i[0]-0.04 + 0.125, 0)
                text_C_bot.setPos(i[0]-0.04 + 0.250, 0)
                text_D_bot.setPos(i[0]-0.04 + 0.375, 0)

            elif len(legendar) > 6 :
                text_A  = pg.TextItem(html='<span style="color:rgb(111, 219, 1);font-size: 7pt;">%s</span>'%(str(round(100*i[1]/i[5],1))+'%'), anchor=(0,0), angle=90)
                text_B  = pg.TextItem(html='<span style="color:rgb(0, 225, 255);font-size: 7pt;">%s</span>'%(str(round(100*i[2]/i[5],1))+'%'), anchor=(0,0), angle=90)
                text_C  = pg.TextItem(html='<span style="color:rgb(255, 140, 0);font-size: 7pt;">%s</span>'%(str(round(100*i[3]/i[5],1))+'%'), anchor=(0,0), angle=90)
                text_D  = pg.TextItem(html='<span style="color:rgb(255,106,106);font-size: 7pt;">%s</span>'%(str(round(100*i[4]/i[5],1))+'%'), anchor=(0,0), angle=90)

                text_A_bot  = pg.TextItem(html='<span style="color:rgb(111, 219, 1); font-size: 8pt;"><strong>A</strong></span>', anchor=(0,0), angle=0)
                text_B_bot  = pg.TextItem(html='<span style="color:rgb(0, 225, 255); font-size: 8pt;"><strong>B</strong></span>', anchor=(0,0), angle=0)
                text_C_bot  = pg.TextItem(html='<span style="color:rgb(255, 140, 0); font-size: 8pt;"><strong>C</strong></span>', anchor=(0,0), angle=0)
                text_D_bot  = pg.TextItem(html='<span style="color:rgb(255,106,106); font-size: 8pt;"><strong>D</strong></span>', anchor=(0,0), angle=0)

                self.graphicsView_Passe.addItem(text_A)
                self.graphicsView_Passe.addItem(text_B)
                self.graphicsView_Passe.addItem(text_C)
                self.graphicsView_Passe.addItem(text_D)
                self.graphicsView_Passe.addItem(text_A_bot)
                self.graphicsView_Passe.addItem(text_B_bot)
                self.graphicsView_Passe.addItem(text_C_bot)
                self.graphicsView_Passe.addItem(text_D_bot)

                text_A.setPos(i[0] -0.07        , i[1] + 0.2)
                text_B.setPos(i[0] -0.07 + 0.120, i[2] + 0.2)
                text_C.setPos(i[0] -0.07 + 0.250, i[3] + 0.2)
                text_D.setPos(i[0] -0.07 + 0.375, i[4] + 0.2)

                text_A_bot.setPos(i[0]-0.05,         0)
                text_B_bot.setPos(i[0]-0.05 + 0.125, 0)
                text_C_bot.setPos(i[0]-0.05 + 0.250, 0)
                text_D_bot.setPos(i[0]-0.05 + 0.375, 0)
            '''

    def tempo_pause(self):
        global PAUSE_RESUME
        global DELTA_PAUSE
        if PAUSE_RESUME:
            self.inicio_pause = QTime.currentTime() # Momento que dei pause
            PAUSE_RESUME = False
            self.timer.stop()
            self.PB_Scores_pause.setStyleSheet("QPushButton{\n"
"font: 12pt \"Cortoba\";\n"
"background-color: rgb(26, 27, 28);\n"
"border: 1px solid  rgb(236, 14, 14);\n"
"color: rgb(236, 14, 14);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{;\n"
"background-color: rgb(0, 144, 153);\n"
"}\n"
"QPushButton:pressed {background-color: rgb(1, 57, 62);}")
            self.PB_Scores_Time.setStyleSheet("QPushButton{\n"
"font: 12pt \"Cortoba\";\n"
"background-color: rgb(26, 27, 28);\n"
"border: 1px solid  rgb(236, 14, 14);\n"
"color: rgb(236, 14, 14);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{;\n"
"background-color: rgb(0, 144, 153);\n"
"}\n"
"QPushButton:pressed {background-color: rgb(1, 57, 62);}")

            self.PB_Scores_pause.setText("Resume")
        else:
            self.final_pause = QTime.currentTime() # Momento que sai do pause
            PAUSE_RESUME = True
            self.tempo_start()
            self.PB_Scores_pause.setStyleSheet("QPushButton{\n"
"font: 12pt \"Cortoba\";\n"
"border: 1px solid  rgb(0, 225, 255);\n"
"color: rgb(238, 238, 236);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{;\n"
"background-color: rgb(0, 144, 153);\n"
"}\n"
"QPushButton:pressed {background-color: rgb(1, 57, 62);}")
            self.PB_Scores_Time.setStyleSheet("QPushButton{\n"
"font: 12pt \"Cortoba\";\n"
"background-color: rgb(26, 27, 28);\n"
"border: 1px solid  rgb(5, 255, 0);\n"
"color: rgb(5, 255, 0);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{;\n"
"background-color: rgb(0, 144, 153);\n"
"}\n"
"QPushButton:pressed {background-color: rgb(85, 87, 83);}")
            self.PB_Scores_pause.setText("Pause")
            # Delta
            DELTA_PAUSE += (self.inicio_pause.secsTo(self.final_pause))
    def tempo_start(self):
        global TEMPO_INICIADO
        global DELTA_ZERA_TEMPO
        if not TEMPO_INICIADO: # Para nao marcar mais que um tempo de start
            xi = QTime.currentTime() # Guarda tempo que dei start
            DELTA_ZERA_TEMPO = 3600*xi.hour() + 60*xi.minute() + xi.second()
            TEMPO_INICIADO = True
        # update the timer every second
        if PAUSE_RESUME:
            self.timer.start(1000)
        self.PB_Scores_Time.setStyleSheet("QPushButton{\n"
"font: 12pt \"Cortoba\";\n"
"background-color: rgb(26, 27, 28);\n"
"border: 1px solid  rgb(5, 255, 0);\n"
"color: rgb(5, 255, 0);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{;\n"
"background-color: rgb(0, 144, 153);\n"
"}\n"
"QPushButton:pressed {background-color: rgb(85, 87, 83);}")
    def showTime(self, tempo_pausa = 0):
        global DELTA_PAUSE
        global DELTA_ZERA_TEMPO
        # getting current time
        current_time = QTime.currentTime()
        # converting QTime object to string
        S_Totais = 3600*current_time.hour() + 60*current_time.minute() + current_time.second()
        S_Totais -= (DELTA_PAUSE + DELTA_ZERA_TEMPO)
        minutos_totais = S_Totais // 60
        minutos = S_Totais // 60
        S_Totais -= (S_Totais // 60) * 60
        segundos = S_Totais
        label_time = "%d : %d"%(minutos,segundos)
        # showing it to the label
        self.PB_Scores_Time.setText(label_time) # Seta o tempo no texto do botão

        # guarda os dados do tempo e do placar para eu usar
        if (segundos + minutos*60)%5 == 0:
            self.poissonA.append( (int(self.label_Plagreen.text()), segundos + minutos*60))
            self.poissonB.append( (int(self.label_Plared.text()), segundos + minutos*60))

    def mudatime(self):
        ''' Alterna o valor do self.meutime para sinalizar qual é o time que
            que irei cadastrar dados
        '''
        self.meutime = not self.meutime
        if self.meutime:
            self.PB_AlternarJogadores.setText('Oponente')
            self.stackedWidget_2.setCurrentIndex(0)
        else:
            self.PB_AlternarJogadores.setText('Meu time')
            self.stackedWidget_2.setCurrentIndex(1)

        self.flag = 0 # Desmarco qualquer jogador selecionado anteriormente

    def define_jogadores(self):
        ''' Joga os nomes digitados para cada botao que representa um jogador '''

        ''' Meu Time'''
        if self.nome_j1.text().strip() == '':
            self.PB_J1.hide()
        else:
            self.PB_J1.show()
            self.PB_J1.setText(self.nome_j1.text())
            self.t1 = Jogador(self.nome_j1.text())

        if self.nome_j2.text().strip() == '':
            self.PB_J2.hide()
        else:
            self.PB_J2.show()
            self.PB_J2.setText(self.nome_j2.text())
            self.t2 = Jogador(self.nome_j2.text())

        if self.nome_j3.text().strip() == '':
            self.PB_J3.hide()
        else:
            self.PB_J3.show()
            self.PB_J3.setText(self.nome_j3.text())
            self.t3 = Jogador(self.nome_j3.text())

        if self.nome_j4.text().strip() == '':
            self.PB_J4.hide()
        else:
            self.PB_J4.show()
            self.PB_J4.setText(self.nome_j4.text())
            self.t4 = Jogador(self.nome_j4.text())

        if self.nome_j5.text().strip() == '':
            self.PB_J5.hide()
        else:
            self.PB_J5.show()
            self.PB_J5.setText(self.nome_j5.text())
            self.t5 = Jogador(self.nome_j5.text())

        if self.nome_j6.text().strip() == '':
            self.PB_J6.hide()
        else:
            self.PB_J6.show()
            self.PB_J6.setText(self.nome_j6.text())
            self.t6 = Jogador(self.nome_j6.text())

        if self.nome_j7.text().strip() == '':
            self.PB_J7.hide()
        else:
            self.PB_J7.show()
            self.PB_J7.setText(self.nome_j7.text())
            self.t7 = Jogador(self.nome_j7.text())

        if self.nome_j8.text().strip() == '':
            self.PB_J8.hide()
        else:
            self.PB_J8.show()
            self.PB_J8.setText(self.nome_j8.text())
            self.t8 = Jogador(self.nome_j8.text())

        if self.nome_j9.text().strip() == '':
            self.PB_J9.hide()
        else:
            self.PB_J9.show()
            self.PB_J9.setText(self.nome_j9.text())
            self.t9 = Jogador(self.nome_j9.text())

        if self.nome_j10.text().strip() == '':
            self.PB_J10.hide()
        else:
            self.PB_J10.show()
            self.PB_J10.setText(self.nome_j10.text())
            self.t10 = Jogador(self.nome_j10.text())

        if self.nome_j11.text().strip() == '':
            self.PB_J11.hide()
        else:
            self.PB_J11.show()
            self.PB_J11.setText(self.nome_j11.text())
            self.t11 = Jogador(self.nome_j11.text())

        if self.nome_j12.text().strip() == '':
            self.PB_J12.hide()
        else:
            self.PB_J12.show()
            self.PB_J12.setText(self.nome_j12.text())
            self.t12 = Jogador(self.nome_j12.text())

        if self.nome_j13.text().strip() == '':
            self.PB_J13.hide()
        else:
            self.PB_J13.show()
            self.PB_J13.setText(self.nome_j13.text())
            self.t13 = Jogador(self.nome_j13.text())

        if self.nome_j14.text().strip() == '':
            self.PB_J14.hide()
        else:
            self.PB_J14.show()
            self.PB_J14.setText(self.nome_j14.text())
            self.t14 = Jogador(self.nome_j14.text())

        ''' Time Adversário'''
        if self.nome_o1.text().strip() == '':
            self.PB_O1.hide()
        else:
            self.PB_O1.show()
            self.PB_O1.setText(self.nome_o1.text())
            self.o1 = Jogador(self.nome_o1.text())

        if self.nome_o2.text().strip() == '':
            self.PB_O2.hide()
        else:
            self.PB_O2.show()
            self.PB_O2.setText(self.nome_o2.text())
            self.o2 = Jogador(self.nome_o2.text())

        if self.nome_o3.text().strip() == '':
            self.PB_O3.hide()
        else:
            self.PB_O3.show()
            self.PB_O3.setText(self.nome_o3.text())
            self.o3 = Jogador(self.nome_o3.text())

        if self.nome_o4.text().strip() == '':
            self.PB_O4.hide()
        else:
            self.PB_O4.show()
            self.PB_O4.setText(self.nome_o4.text())
            self.o4 = Jogador(self.nome_o4.text())

        if self.nome_o5.text().strip() == '':
            self.PB_O5.hide()
        else:
            self.PB_O5.show()
            self.PB_O5.setText(self.nome_o5.text())
            self.o5 = Jogador(self.nome_o5.text())

        if self.nome_o6.text().strip() == '':
            self.PB_O6.hide()
        else:
            self.PB_O6.show()
            self.PB_O6.setText(self.nome_o6.text())
            self.o6 = Jogador(self.nome_o6.text())

        if self.nome_o7.text().strip() == '':
            self.PB_O7.hide()
        else:
            self.PB_O7.show()
            self.PB_O7.setText(self.nome_o7.text())
            self.o7 = Jogador(self.nome_o7.text())

        if self.nome_o8.text().strip() == '':
            self.PB_O8.hide()
        else:
            self.PB_O8.show()
            self.PB_O8.setText(self.nome_o8.text())
            self.o8 = Jogador(self.nome_o8.text())

        if self.nome_o9.text().strip() == '':
            self.PB_O9.hide()
        else:
            self.PB_O9.show()
            self.PB_O9.setText(self.nome_o9.text())
            self.o9 = Jogador(self.nome_o9.text())

        if self.nome_o10.text().strip() == '':
            self.PB_O10.hide()
        else:
            self.PB_O10.show()
            self.PB_O10.setText(self.nome_o10.text())
            self.o10 = Jogador(self.nome_o10.text())

        if self.nome_o11.text().strip() == '':
            self.PB_O11.hide()
        else:
            self.PB_O11.show()
            self.PB_O11.setText(self.nome_o11.text())
            self.o11 = Jogador(self.nome_o11.text())

        if self.nome_o12.text().strip() == '':
            self.PB_O12.hide()
        else:
            self.PB_O12.show()
            self.PB_O12.setText(self.nome_o12.text())
            self.o12 = Jogador(self.nome_o12.text())

        if self.nome_o13.text().strip() == '':
            self.PB_O13.hide()
        else:
            self.PB_O13.show()
            self.PB_O13.setText(self.nome_o13.text())
            self.o13 = Jogador(self.nome_o13.text())

        if self.nome_o14.text().strip() == '':
            self.PB_O14.hide()
        else:
            self.PB_O13.show()
            self.PB_O14.setText(self.nome_o14.text())
            self.o14 = Jogador(self.nome_o14.text())


        self.page_2_mostra() # Isso é para direcionar para próxima aba apos definir jogadores

    def positivos(self, x, y):
        ''' Retonar True se [x][y] representa o endereço de uma '''
        ''' Ação positiva no conjunto de dados dos jogadores '''
        ''' Retorna False cado contrário '''
        # ordem_dados = [[ataque],[bloqueio],[saque],[passe],[defesa],[ação_time],[penalidades]]
        #self.dados_J1 =  [[0,0,0],[0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0],[0,0,0,0]]
        positivas = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1)]
        for dupla in positivas:
            if dupla == (x,y):
                return True
        return False

    def equivale(self, cord):
        '''Recebe (x,y) ou (y,x) e retorna (x,y)
           onde x <= y
        '''
        if cord[0] <= cord[1]:
            return cord
        else:
            return (cord[1], cord[0])

    def position(self, valor):
        ''' retorna a posição (x,y) da acao na quadra
        '''
        if self.xy[0] == False:
            self.xy[0] = valor
        else:
            self.xy[1] = valor
            pos = self.equivale((self.xy[0], self.xy[1]))
            self.xy = [False, False]

            if self.flag == 1:
                self.t1.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t1.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 2:
                self.t2.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t2.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 3:
                self.t3.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t3.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 4:
                self.t4.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t4.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 5:
                self.t5.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t5.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 6:
                self.t6.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t6.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 7:
                self.t7.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t7.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 8:
                self.t8.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t8.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 9:
                self.t9.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t9.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 10:
                self.t10.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t10.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 11:
                self.t11.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t11.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 12:
                self.t12.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t12.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 13:
                self.t13.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t13.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 14:
                self.t14.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.t14.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 15:
                self.o1.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o1.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 16:
                self.o2.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o2.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 17:
                self.o3.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o3.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 18:
                self.o4.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o4.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 19:
                self.o5.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o5.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 20:
                self.o6.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o6.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 21:
                self.o7.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o7.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 22:
                self.o8.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o8.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 23:
                self.o9.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o9.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 24:
                self.o10.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o10.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 25:
                self.o11.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o11.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 26:
                self.o12.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o12.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 27:
                self.o13.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o13.fund(self.qualBT[0])[self.qualBT[1]]) )
            elif self.flag == 28:
                self.o14.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
                self.qualBT[2].setValue( len(self.o14.fund(self.qualBT[0])[self.qualBT[1]]) )

            self.toogglehover_fecha2()

    def abreposition(self, fundamento, c, label):
        ''' Seta os parametros de acordo com o botao pressionado e abre o posiciometro
            fundamento: fundamento correspondente
            c é a classificação do fundamento, ex: ataque verde
            label: 'label', campo onde vou mostrar o texto 'novo valor'
        '''
        if self.flag != 0:
            self.toogglehover_abre2() # abre posiciometro
            self.qualBT = (fundamento, c, label) # fundamento e classe e label correspondente

    def corrige(self, c, fundamento, label):
        ''' corrige uma marcacao, removendo o ultimo dado adicionado
            e mostrando o novo valor na label correspondente
        '''
        if self.flag == 1:
            self.t1.fund(fundamento)[c].pop()
            label.setValue( len(self.t1.fund(fundamento)[c]) )
        elif self.flag == 2:
            self.t2.fund(fundamento)[c].pop()
            label.setValue( len(self.t2.fund(fundamento)[c]) )
        elif self.flag == 3:
            self.t3.fund(fundamento)[c].pop()
            label.setValue( len(self.t3.fund(fundamento)[c]) )
        elif self.flag == 4:
            self.t4.fund(fundamento)[c].pop()
            label.setValue( len(self.t4.fund(fundamento)[c]) )
        elif self.flag == 5:
            self.t5.fund(fundamento)[c].pop()
            label.setValue( len(self.t5.fund(fundamento)[c]) )
        elif self.flag == 6:
            self.t6.fund(fundamento)[c].pop()
            label.setValue( len(self.t6.fund(fundamento)[c]) )
        elif self.flag == 7:
            self.t7.fund(fundamento)[c].pop()
            label.setValue( len(self.t7.fund(fundamento)[c]) )
        elif self.flag == 8:
            self.t8.fund(fundamento)[c].pop()
            label.setValue( len(self.t8.fund(fundamento)[c]) )
        elif self.flag == 9:
            self.t9.fund(fundamento)[c].pop()
            label.setValue( len(self.t9.fund(fundamento)[c]) )
        elif self.flag == 10:
            self.t10.fund(fundamento)[c].pop()
            label.setValue( len(self.t10.fund(fundamento)[c]) )
        elif self.flag == 11:
            self.t11.fund(fundamento)[c].pop()
            label.setValue( len(self.t11.fund(fundamento)[c]) )
        elif self.flag == 12:
            self.t12.fund(fundamento)[c].pop()
            label.setValue( len(self.t12.fund(fundamento)[c]) )
        elif self.flag == 13:
            self.t13.fund(fundamento)[c].pop()
            label.setValue( len(self.t13.fund(fundamento)[c]) )
        elif self.flag == 14:
            self.t14.fund(fundamento)[c].pop()
            label.setValue( len(self.t14.fund(fundamento)[c]) )
        elif self.flag == 15:
            self.o1.fund(fundamento)[c].pop()
            label.setValue( len(self.o1.fund(fundamento)[c]) )
        elif self.flag == 16:
            self.o2.fund(fundamento)[c].pop()
            label.setValue( len(self.o2.fund(fundamento)[c]) )
        elif self.flag == 17:
            self.o3.fund(fundamento)[c].pop()
            label.setValue( len(self.o3.fund(fundamento)[c]) )
        elif self.flag == 18:
            self.o4.fund(fundamento)[c].pop()
            label.setValue( len(self.o4.fund(fundamento)[c]) )
        elif self.flag == 19:
            self.o5.fund(fundamento)[c].pop()
            label.setValue( len(self.o5.fund(fundamento)[c]) )
        elif self.flag == 20:
            self.o6.fund(fundamento)[c].pop()
            label.setValue( len(self.o6.fund(fundamento)[c]) )
        elif self.flag == 21:
            self.o7.fund(fundamento)[c].pop()
            label.setValue( len(self.o7.fund(fundamento)[c]) )
        elif self.flag == 22:
            self.o8.fund(fundamento)[c].pop()
            label.setValue( len(self.o8.fund(fundamento)[c]) )
        elif self.flag == 23:
            self.o9.fund(fundamento)[c].pop()
            label.setValue( len(self.o9.fund(fundamento)[c]) )
        elif self.flag == 24:
            self.o10.fund(fundamento)[c].pop()
            label.setValue( len(self.o10.fund(fundamento)[c]) )
        elif self.flag == 25:
            self.o11.fund(fundamento)[c].pop()
            label.setValue( len(self.o11.fund(fundamento)[c]) )
        elif self.flag == 26:
            self.o12.fund(fundamento)[c].pop()
            label.setValue( len(self.o12.fund(fundamento)[c]) )
        elif self.flag == 27:
            self.o13.fund(fundamento)[c].pop()
            label.setValue( len(self.o13.fund(fundamento)[c]) )
        elif self.flag == 28:
            self.o14.fund(fundamento)[c].pop()
            label.setValue( len(self.o14.fund(fundamento)[c]) )

    def nposition(self, fundamento, c, label):
        self.qualBT = (fundamento, c, label) # fundamento e classe e label correspondente
        pos = 1
        if self.flag == 1:
            self.t1.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t1.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 2:
            self.t2.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t2.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 3:
            self.t3.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t3.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 4:
            self.t4.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t4.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 5:
            self.t5.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t5.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 6:
            self.t6.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t6.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 7:
            self.t7.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t7.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 8:
            self.t8.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t8.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 9:
            self.t9.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t9.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 10:
            self.t10.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t10.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 11:
            self.t11.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t11.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 12:
            self.t12.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t12.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 13:
            self.t13.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t13.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 14:
            self.t14.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.t14.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 15:
            self.o1.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o1.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 16:
            self.o2.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o2.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 17:
            self.o3.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o3.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 18:
            self.o4.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o4.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 19:
            self.o5.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o5.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 20:
            self.o6.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o6.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 21:
            self.o7.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o7.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 22:
            self.o8.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o8.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 23:
            self.o9.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o9.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 24:
            self.o10.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o10.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 25:
            self.o11.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o11.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 26:
            self.o12.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o12.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 27:
            self.o13.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o13.fund(self.qualBT[0])[self.qualBT[1]]) )
        elif self.flag == 28:
            self.o14.fund(self.qualBT[0])[self.qualBT[1]].append( pos )
            self.qualBT[2].setValue( len(self.o14.fund(self.qualBT[0])[self.qualBT[1]]) )

    def jogador_clicado(self, jogador, flag):
        ''' Muda o estilo do botão que representa o jogador clicado
            Atualiza as Labels com os valores do jogador clicado
        '''
        #self.quando_marco_sem_clicar()
        self.flag = flag
        if 1 == flag:
            self.PB_J1.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J1.setStyleSheet(self.estilos_iguais_click)

        if 2 == flag:
            self.PB_J2.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J2.setStyleSheet(self.estilos_iguais_click)

        if 3 == flag:
            self.PB_J3.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J3.setStyleSheet(self.estilos_iguais_click)

        if 4 == flag:
            self.PB_J4.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J4.setStyleSheet(self.estilos_iguais_click)

        if 5 == flag:
            self.PB_J5.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J5.setStyleSheet(self.estilos_iguais_click)

        if 6 == flag:
            self.PB_J6.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J6.setStyleSheet(self.estilos_iguais_click)

        if 7 == flag:
            self.PB_J7.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J7.setStyleSheet(self.estilos_iguais_click)

        if 8 == flag:
            self.PB_J8.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J8.setStyleSheet(self.estilos_iguais_click)

        if 9 == flag:
            self.PB_J9.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J9.setStyleSheet(self.estilos_iguais_click)

        if 10 == flag:
            self.PB_J10.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J10.setStyleSheet(self.estilos_iguais_click)

        if 11 == flag:
            self.PB_J11.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J11.setStyleSheet(self.estilos_iguais_click)

        if 12 == flag:
            self.PB_J12.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J12.setStyleSheet(self.estilos_iguais_click)

        if 13 == flag:
            self.PB_J13.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J13.setStyleSheet(self.estilos_iguais_click)

        if 14 == flag:
            self.PB_J14.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_J14.setStyleSheet(self.estilos_iguais_click)

        if 15 == flag:
            self.PB_O1.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O1.setStyleSheet(self.estilos_iguais_click)

        if 16 == flag:
            self.PB_O2.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O2.setStyleSheet(self.estilos_iguais_click)

        if 17 == flag:
            self.PB_O3.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O3.setStyleSheet(self.estilos_iguais_click)

        if 18 == flag:
            self.PB_O4.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O4.setStyleSheet(self.estilos_iguais_click)

        if 19 == flag:
            self.PB_O5.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O5.setStyleSheet(self.estilos_iguais_click)

        if 20 == flag:
            self.PB_O6.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O6.setStyleSheet(self.estilos_iguais_click)

        if 21 == flag:
            self.PB_O7.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O7.setStyleSheet(self.estilos_iguais_click)

        if 22 == flag:
            self.PB_O8.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O8.setStyleSheet(self.estilos_iguais_click)

        if 23 == flag:
            self.PB_O9.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O9.setStyleSheet(self.estilos_iguais_click)

        if 24 == flag:
            self.PB_O10.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O10.setStyleSheet(self.estilos_iguais_click)

        if 25 == flag:
            self.PB_O11.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O11.setStyleSheet(self.estilos_iguais_click)

        if 26 == flag:
            self.PB_O12.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O12.setStyleSheet(self.estilos_iguais_click)

        if 27 == flag:
            self.PB_O13.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O13.setStyleSheet(self.estilos_iguais_click)

        if 28 == flag:
            self.PB_O14.setStyleSheet(self.estilos_diferentes_click)
        else:
            self.PB_O14.setStyleSheet(self.estilos_iguais_click)


        self.N_ataque_green.setValue( len(jogador.ataque[0]) )
        self.N_ataque_blue.setValue( len(jogador.ataque[1]) )
        self.N_ataque_red.setValue( len(jogador.ataque[2]) )

        self.N_CA_green.setValue( len(jogador.cataque[0]) )
        self.N_CA_blue.setValue( len(jogador.cataque[1]) )
        self.N_CA_red.setValue( len(jogador.cataque[2]) )

        self.N_bloqueio_green.setValue(len(jogador.bloqueio[0]))
        self.N_bloqueio_blue.setValue(len(jogador.bloqueio[1]))
        self.N_bloqueio_red.setValue(len(jogador.bloqueio[2]))

        self.N_saque_green.setValue(len(jogador.saque[0]))
        self.N_saque_blue.setValue(len(jogador.saque[1]))
        self.N_saque_ora.setValue(len(jogador.saque[2]))
        self.N_saque_red.setValue(len(jogador.saque[3]))

        self.N_passe_A.setValue(len(jogador.passe[0]))
        self.N_passe_B.setValue(len(jogador.passe[1]))
        self.N_passe_C.setValue(len(jogador.passe[2]))
        self.N_passe_D.setValue(len(jogador.passe[3]))

        self.N_defesa_A.setValue(len(jogador.defesa[0]))
        self.N_defesa_B.setValue(len(jogador.defesa[1]))
        self.N_defesa_C.setValue(len(jogador.defesa[2]))

        self.N_rede.setValue(len(jogador.penalidades[0]))
        self.N_cartao.setValue(len(jogador.penalidades[1]))
        self.N_2t.setValue(len(jogador.penalidades[2]))
        self.N_cond.setValue(len(jogador.penalidades[3]))

    def resumo_relatorio(self):
        tgreen = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                 self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                 self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                 self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                 self.nome_j13.text(),self.nome_j14.text()]
        tred = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                 self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                 self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                 self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                 self.nome_o13.text(),self.nome_o14.text()]
        jgreen = []
        jred = []

        self.meutimerelatorio = True
        for j in tgreen:
            if j.strip() != '':
                jgreen.append( self.index_player( 1 + tgreen.index(j)) )
        self.meutimerelatorio = False
        for j in tred:
            if j.strip() != '':
                jred.append( self.index_player( 1 + tred.index(j)) )

        #(a_t,b_t,ca_t,d_t,p_t,pen_t,s_t) ordem do return do .totais()
        # Greens
        AG = 0
        BG = 0
        DG = 0
        PG = 0
        PEG = 0
        SG = 0
        for j in jgreen:
            AG += (j.totais()[0] + j.totais()[2])
            BG += j.totais()[1]
            DG += j.totais()[3]
            PG += j.totais()[4]
            PEG += j.totais()[5]
            SG += j.totais()[6]

        #Reds
        AR = 0
        BR = 0
        DR = 0
        PR = 0
        PER = 0
        SR = 0
        for j in jred:
            AR += (j.totais()[0] + j.totais()[2])
            BR += j.totais()[1]
            DR += j.totais()[3]
            PR += j.totais()[4]
            PER += j.totais()[5]
            SR += j.totais()[6]
        self.meutimerelatorio = True
        return [AG, AR, BG, BR, DG, DR, PG, PR, PEG, PER, SG, SG]

    def mostra_relatorio(self):
        ''' Ordem x do return .resumo_relatorio()[x]
            [AG, AR, BG, BR, DG, DR, PG, PR, PEG, PER, SG, SG]
        '''
        if self.nome_time.text().strip() == '':
            timeA = 'Time A'
        else: timeA = self.nome_time.text()
        if self.nome_oponente.text().strip() == '':
            timeB = 'Time B'
        else: timeB =self.nome_oponente.text()

        self.label_pla_time.setText(self.label_Plagreen.text())
        self.label_pla_oponente.setText(self.label_Plared.text())
        self.label_time.setText(timeA)
        self.label_oponente.setText(timeB)

        #ataques time x oponente
        self.label_t0.setText(str(self.resumo_relatorio()[0]))
        self.label_t1.setText(str(self.resumo_relatorio()[1]))
        #bloqueios time x oponente
        self.label_t2.setText(str(self.resumo_relatorio()[2]))
        self.label_t3.setText(str(self.resumo_relatorio()[3]))
        #defesa time x oponente
        self.label_t4.setText(str(self.resumo_relatorio()[4]))
        self.label_t5.setText(str(self.resumo_relatorio()[5]))
        #saques time x oponente
        self.label_t6.setText(str(self.resumo_relatorio()[10]))
        self.label_t7.setText(str(self.resumo_relatorio()[11]))
        #passes time x oponente
        self.label_t8.setText(str(self.resumo_relatorio()[6]))
        self.label_t9.setText(str(self.resumo_relatorio()[7]))
        #penalidades time x oponente
        self.label_t10.setText(str(self.resumo_relatorio()[8]))
        self.label_t11.setText(str(self.resumo_relatorio()[9]))

    def directory(self, parametro):
        # Obs: A variavel "teste" ira conter o caminho do diretorio que desejo salvar os arquivos
        if parametro == 'defesa':
            #dialog = QtGui.QFileDialog()
            dialog = QtGui.QFileDialog()
            teste = dialog.getSaveFileName(None, 'Save PNG File','Gráfico_Defesa',"(*.png)")
            #folder_path = dialog.getExistingDirectory(None, "Select Folder")
            #print(folder_path+'/Defesa_graph.png')
            #return folder_path
            exporter = pg.exporters.ImageExporter(self.graphicsView_Defesa.plotItem)
            exporter.export(teste[0])
        if parametro == 'ataque':
            dialog = QtGui.QFileDialog()
            teste = dialog.getSaveFileName(None, 'Save PNG File','Gráfico_Ataque',"(*.png)")
            exporter = pg.exporters.ImageExporter(self.graphicsView_Ataque.plotItem)
            exporter.export(teste[0])
        if parametro == 'bloqueio':
            dialog = QtGui.QFileDialog()
            teste = dialog.getSaveFileName(None, 'Save PNG File','Gráfico_Bloqueio',"(*.png)")
            exporter = pg.exporters.ImageExporter(self.graphicsView_Bloqueio.plotItem)
            exporter.export(teste[0])
        if parametro == 'saque':
            dialog = QtGui.QFileDialog()
            teste = dialog.getSaveFileName(None, 'Save PNG File','Gráfico_Saque',"(*.png)")
            exporter = pg.exporters.ImageExporter(self.graphicsView_Saque.plotItem)
            exporter.export(teste[0])
        if parametro == 'passe':
            dialog = QtGui.QFileDialog()
            teste = dialog.getSaveFileName(None, 'Save PNG File','Gráfico_Passe',"(*.png)")
            exporter = pg.exporters.ImageExporter(self.graphicsView_Passe.plotItem)
            exporter.export(teste[0])
        if parametro == 'acoes':
            dialog = QtGui.QFileDialog()
            teste = dialog.getSaveFileName(None, 'Save PNG File','Gráfico_Ações',"(*.png)")
            exporter = pg.exporters.ImageExporter(self.graphicsView_Pontos.plotItem)
            exporter.export(teste[0])
        if parametro == 'relatorio':
            ''' ----Separando / Trabalhando Dados------ '''
            tgreen = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                     self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                     self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                     self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                     self.nome_j13.text(),self.nome_j14.text()]
            tred = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                     self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                     self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                     self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                     self.nome_o13.text(),self.nome_o14.text()]

            j_green = [] #ATAQUES GREEN
            self.meutimerelatorio = True
            for name in tgreen:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tgreen.index(name)).ataque
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        j_green.append( self.index_player( 1 + tgreen.index(name)) )
            j_red = []  #ATAQUES RED
            self.meutimerelatorio = False
            for name in tred:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tred.index(name)).ataque
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        j_red.append( self.index_player( 1 + tred.index(name)) )
            b_green = [] #BLOQUEIO GREEN
            self.meutimerelatorio = True
            for name in tgreen:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tgreen.index(name)).bloqueio
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        b_green.append( self.index_player( 1 + tgreen.index(name)) )
            b_red = [] #BLOQUEIO RED
            self.meutimerelatorio = False
            for name in tred:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tred.index(name)).bloqueio
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        b_red.append( self.index_player( 1 + tred.index(name)) )
            c_green = [] #CONTRA ATAQUES GREEN
            self.meutimerelatorio = True
            for name in tgreen:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tgreen.index(name)).cataque
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        c_green.append( self.index_player( 1 + tgreen.index(name)) )
            c_red = []  #CONTRA ATAQUES RED
            self.meutimerelatorio = False
            for name in tred:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tred.index(name)).cataque
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        c_red.append( self.index_player( 1 + tred.index(name)) )
            d_green = [] #DEFESA GREEN
            self.meutimerelatorio = True
            for name in tgreen:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tgreen.index(name)).defesa
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        d_green.append( self.index_player( 1 + tgreen.index(name)) )
            d_red = [] #DEFESA RED
            self.meutimerelatorio = False
            for name in tred:
                if name.strip() != '':
                    A_totais = self.index_player( 1 + tred.index(name)).defesa
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) != 0:
                        d_red.append( self.index_player( 1 + tred.index(name)) )
            p_green = [] #PASSE GREEN
            self.meutimerelatorio = True
            for name in tgreen:
                if name.strip() != '':
                    A_totais = self.index_player( 1 +  tgreen.index(name)).passe
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) + len(A_totais[3]) != 0:
                        p_green.append( self.index_player( 1 + tgreen.index(name)) )
            p_red = [] #PASSE RED
            self.meutimerelatorio = False
            for name in tred:
                if name.strip() != '':
                    A_totais = self.index_player( 1 +  tred.index(name)).passe
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) + len(A_totais[3]) != 0:
                        p_red.append( self.index_player( 1 + tred.index(name)) )
            s_green = [] #SAQUE GREEN
            self.meutimerelatorio = True
            for name in tgreen:
                if name.strip() != '':
                    A_totais = self.index_player( 1 +  tgreen.index(name)).saque
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) + len(A_totais[3]) != 0:
                        s_green.append( self.index_player( 1 + tgreen.index(name)) )
            s_red = [] #SAQUE RED
            self.meutimerelatorio = True
            for name in tred:
                if name.strip() != '':
                    A_totais = self.index_player( 1 +  tred.index(name)).saque
                    if len(A_totais[0]) + len(A_totais[1]) + len(A_totais[2]) + len(A_totais[3]) != 0:
                        s_red.append( self.index_player( 1 + tred.index(name)) )


            if self.nome_partida.text().strip() != "": #So faz Relatorio se a Partida Tiver nome
                ''' ------Salvando em um PDF------ '''
                dialog = QtGui.QFileDialog()
                teste = dialog.getSaveFileName(None, 'Save PDF File','Relatório',"(*.pdf)")
                pdf = PDF()
                pdf.add_page() # create new page
                ''' Top Title '''
                nome_partida = self.nome_partida.text()
                pdf.set_font("Courier", size=16, style='B') # font and textsize
                ''' -------------Tabela Resumo-------------'''
                pdf.set_font("Courier", size=12, style='B')
                pdf.cell(200, 10, txt="R e s u m o", ln=1, align="L")
                s1 = "{:<12} {:<11} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Equipe','Pontos','Ataques','Bloqueios',' Defesas',' Saques','Passes', 'Penalidades')
                s2 = "{:<12} {:<11} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('----------','----------','-------','-------','-------','-------','-------','-------')
                pdf.set_font("Courier", size=9)
                pdf.cell(10) # distancia da margem esquerda
                pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                pdf.cell(10) # distancia da margem esquerda
                pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                equipe_a = self.label_time.text()
                pontos_a = self.label_pla_time.text()
                ataques_a = self.label_t0.text()
                bloqueios_a = self.label_t2.text()
                defesa_a = self.label_t4.text()
                saque_a = self.label_t6.text()
                passes_a = self.label_t8.text()
                penalidades_a = self.label_t10.text()

                equipe_b = self.label_oponente.text()
                pontos_b = self.label_pla_oponente.text()
                ataques_b = self.label_t1.text()
                bloqueios_b = self.label_t3.text()
                defesa_b = self.label_t5.text()
                saque_b = self.label_t7.text()
                passes_b = self.label_t9.text()
                penalidades_b = self.label_t11.text()
                s_a = "{:<12} {:<11} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(equipe_a,pontos_a,ataques_a,bloqueios_a,defesa_a,saque_a,passes_a,penalidades_a)
                s_b = "{:<12} {:<11} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(equipe_b,pontos_b,ataques_b,bloqueios_b,defesa_b,saque_b,passes_b,penalidades_b)
                pdf.cell(10) # distancia da margem esquerda
                pdf.cell(200, 5, s_a, ln=1, align="L", border = 0)
                pdf.cell(10) # distancia da margem esquerda
                pdf.cell(200, 5, s_b, ln=1, align="L", border = 0)


                duracao_t = self.PB_Scores_Time.text()
                pdf.set_font("Courier", size=8)
                pdf.cell(200, 5,"", ln=1, align="L", border = 0)
                if duracao_t == "Iniciar Tempo":
                    duracao_t = "Parabéns! Você não marcou a duração das pontuações..."
                    pdf.cell(200, 5,"Tempo de marcação: "+ duracao_t, ln=1, align="L", border = 0)
                    pdf.cell(200, 5,equipe_a+": Pontuação média: Não sei. Você não marcou o tempo.", ln=1, align="L", border = 0)
                    pdf.cell(200, 5,equipe_b+": Pontuação média: Não sei. Você não marcou o tempo.", ln=1, align="L", border = 0)
                else:
                    duracao_t = int(duracao_t.split(":")[0])
                    if duracao_t == 0:
                        pdf.cell(200, 5,"Tempo de marcação: Menos de 1 min.", ln=1, align="L", border = 0)
                        pdf.cell(200, 5,equipe_a+": Pontuação média: Período muito curto, não vale a pena calcular.", ln=1, align="L", border = 0)
                        pdf.cell(200, 5,equipe_b+": Pontuação média: Período muito curto, não vale a pena calcular.", ln=1, align="L", border = 0)
                    else:
                        taxa_a = round(float(pontos_a)/duracao_t, 2)
                        taxa_b = round(float(pontos_b)/duracao_t, 2)
                        pdf.cell(200, 5,"Tempo de marcação: "+ str(duracao_t) + " min.", ln=1, align="L", border = 0)
                        pdf.cell(200, 5,equipe_a+": Pontuação média de "+ str(taxa_a) + " pts/min.", ln=1, align="L", border = 0)
                        pdf.cell(200, 5,equipe_b+": Pontuação média de "+ str(taxa_b) + " pts/min.", ln=1, align="L", border = 0)
                if j_green != []: #ATAQUE GREEN
                    ''' Eficiencia de Ataques '''
                    ef_ataques = {}
                    sorted_ef_ataques = {}
                    for atqs in j_green:
                        total = len(atqs.ataque[0]) + len(atqs.ataque[1]) + len(atqs.ataque[2])
                        mais_erra = str(atqs.MaxPosi(atqs.ataque[2])[0]) + atqs.MaxPosi(atqs.ataque[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.ataque[0])[0]) + atqs.MaxPosi(atqs.ataque[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_ataque()
                        ef_ataques.update({nome:[ef,len(atqs.ataque[0]),len(atqs.ataque[1]),len(atqs.ataque[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_ataques, key=ef_ataques.get)
                    for w in sorted_keys:
                        sorted_ef_ataques[w] = ef_ataques[w]

                    ''' -------------Top Ataque GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="A t a q u e s   -   " + self.label_time.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Ataque '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_ataques.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if j_red != []: #ATAQUE RED
                    ef_ataquesred = {}
                    sorted_ef_ataquesred = {}
                    for atqs in j_red:
                        total = len(atqs.ataque[0]) + len(atqs.ataque[1]) + len(atqs.ataque[2])
                        mais_erra = str(atqs.MaxPosi(atqs.ataque[2])[0]) + atqs.MaxPosi(atqs.ataque[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.ataque[0])[0]) + atqs.MaxPosi(atqs.ataque[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_ataque()
                        ef_ataquesred.update({nome:[ef,len(atqs.ataque[0]),len(atqs.ataque[1]),len(atqs.ataque[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_ataquesred, key=ef_ataquesred.get)
                    for w in sorted_keys:
                        sorted_ef_ataquesred[w] = ef_ataquesred[w]
                    ''' -------------Top Ataque RED------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="A t a q u e s   -   " + self.label_oponente.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Ataque '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_ataquesred.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if b_green != []: #BLOQUEIO GREEN
                    ef_bg = {}
                    sorted_ef_bg = {}
                    for atqs in b_green:
                        total = len(atqs.bloqueio[0]) + len(atqs.bloqueio[1]) + len(atqs.bloqueio[2])
                        mais_erra = str(atqs.MaxPosi(atqs.bloqueio[2])[0]) + atqs.MaxPosi(atqs.bloqueio[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.bloqueio[1])[0]) + atqs.MaxPosi(atqs.bloqueio[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_bloqueio()
                        ef_bg.update({nome:[ef,len(atqs.bloqueio[0]),len(atqs.bloqueio[1]),len(atqs.bloqueio[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_bg, key=ef_bg.get)
                    for w in sorted_keys:
                        sorted_ef_bg[w] = ef_bg[w]

                    ''' -------------Top bloqueio GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="B l o q u e i o s   -   " + self.label_time.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Bloquieo '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_bg.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if b_red != []: #BLOQUEIO RED
                    ef_br = {}
                    sorted_ef_br = {}
                    for atqs in b_red:
                        total = len(atqs.bloqueio[0]) + len(atqs.bloqueio[1]) + len(atqs.bloqueio[2])
                        mais_erra = str(atqs.MaxPosi(atqs.bloqueio[2])[0]) + atqs.MaxPosi(atqs.bloqueio[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.bloqueio[1])[0]) + atqs.MaxPosi(atqs.bloqueio[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_bloqueio()
                        ef_br.update({nome:[ef,len(atqs.bloqueio[0]),len(atqs.bloqueio[1]),len(atqs.bloqueio[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_br, key=ef_br.get)
                    for w in sorted_keys:
                        sorted_ef_br[w] = ef_br[w]

                    ''' -------------Top bloqueio GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="B l o q u e i o s   -   " + self.label_oponente.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Bloquieo '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_br.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if c_green != []: #CONTRA ATAQUE GREEN
                    ''' Eficiencia de CAtaques '''
                    ef_cataques = {}
                    sorted_ef_cataques = {}
                    for atqs in c_green:
                        total = len(atqs.cataque[0]) + len(atqs.cataque[1]) + len(atqs.cataque[2])
                        mais_erra = str(atqs.MaxPosi(atqs.cataque[2])[0]) + atqs.MaxPosi(atqs.cataque[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.cataque[0])[0]) + atqs.MaxPosi(atqs.cataque[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_cataque()
                        ef_cataques.update({nome:[ef,len(atqs.cataque[0]),len(atqs.cataque[1]),len(atqs.cataque[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_cataques, key=ef_cataques.get)
                    for w in sorted_keys:
                        sorted_ef_cataques[w] = ef_cataques[w]

                    ''' -------------Top CAtaque GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="C o n t r a   A t a q u e s   -   " + self.label_time.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela CAtaque '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_cataques.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if c_red != []: #CONTRA ATAQUE RED
                    ef_cataquesred = {}
                    sorted_ef_cataquesred = {}
                    for atqs in c_red:
                        total = len(atqs.cataque[0]) + len(atqs.cataque[1]) + len(atqs.cataque[2])
                        mais_erra = str(atqs.MaxPosi(atqs.cataque[2])[0]) + atqs.MaxPosi(atqs.cataque[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.cataque[0])[0]) + atqs.MaxPosi(atqs.cataque[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_cataque()
                        ef_cataquesred.update({nome:[ef,len(atqs.cataque[0]),len(atqs.cataque[1]),len(atqs.cataque[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_cataquesred, key=ef_cataquesred.get)
                    for w in sorted_keys:
                        sorted_ef_cataquesred[w] = ef_cataquesred[w]
                    ''' -------------Top CAtaque RED------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="C o n t r a   A t a q u e s   -   " + self.label_oponente.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela CAtaque '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_cataquesred.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if d_green != []: #DEFESA GREEN
                    ef_dg = {}
                    sorted_ef_dg = {}
                    for atqs in d_green:
                        total = len(atqs.defesa[0]) + len(atqs.defesa[1]) + len(atqs.defesa[2])
                        mais_erra = str(atqs.MaxPosi(atqs.defesa[2])[0]) + atqs.MaxPosi(atqs.defesa[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.defesa[1])[0]) + atqs.MaxPosi(atqs.defesa[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_defesa()
                        ef_dg.update({nome:[ef,len(atqs.defesa[0]),len(atqs.defesa[1]),len(atqs.defesa[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_dg, key=ef_dg.get)
                    for w in sorted_keys:
                        sorted_ef_dg[w] = ef_dg[w]

                    ''' -------------Top bloqueio GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="D e f e s a s   -   " + self.label_time.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Bloquieo '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_dg.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if d_red != []: #DEFESA RED
                    ef_dr = {}
                    sorted_ef_dr = {}
                    for atqs in d_red:
                        total = len(atqs.defesa[0]) + len(atqs.defesa[1]) + len(atqs.defesa[2])
                        mais_erra = str(atqs.MaxPosi(atqs.defesa[2])[0]) + atqs.MaxPosi(atqs.defesa[2])[1]
                        mais_acerta = str(atqs.MaxPosi(atqs.defesa[1])[0]) + atqs.MaxPosi(atqs.defesa[0])[1]
                        nome = atqs.nome
                        ef = atqs.ef_defesa()
                        ef_dr.update({nome:[ef,len(atqs.defesa[0]),len(atqs.defesa[1]),len(atqs.defesa[2]), mais_erra, mais_acerta,total]}) #{Nome:[ef, acerto,neutro,erro,total]}
                    sorted_keys = sorted(ef_dr, key=ef_dr.get)
                    for w in sorted_keys:
                        sorted_ef_dr[w] = ef_dr[w]

                    ''' -------------Top bloqueio GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="D e f e s a s   -   " + self.label_oponente.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Bloquieo '''
                    s1 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('Jogadores','Sucesso','Acertos','Neutros','Erros','Mais Erra','Mais Acerta','Total')
                    s2 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format('----------','----------','--------','--------','-------','-------------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for nome, k in sorted_ef_dr.items():
                        ef, verde, azul, red, mais_erra, mais_acerta, total = k[0],k[1],k[2],k[3],k[4],k[5],k[6]
                        s3 = "{:<11} {:<11} {:<9} {:<9} {:<9} {:<15} {:<14} {:<11}".format(nome, ef, verde, azul,red, mais_erra, mais_acerta, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if p_green != []: #PASSE GREEN
                    ''' -------------Top PASSE GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="P a s s e s   -   " + self.label_time.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Bloquieo '''
                    s1 = "{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format('Jogadores','Passe A','Passe B','Passe C','Passe D','Total')
                    s2 = "{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format('----------','---------','---------','---------','---------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for j in p_green:
                        nome = j.nome
                        pa = str(len(j.passe[0]))+ ":" + str(j.porcentagem_passe()[0]) + "%"
                        pb = str(len(j.passe[1]))+ ":" + str(j.porcentagem_passe()[1]) + "%"
                        pc = str(len(j.passe[2]))+ ":" + str(j.porcentagem_passe()[2]) + "%"
                        pd = str(len(j.passe[3]))+ ":" + str(j.porcentagem_passe()[3]) + "%"
                        total = str(len(j.passe[0]) + len(j.passe[1]) + len(j.passe[2]) + len(j.passe[3]))
                        s3 = "{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format(nome, pa, pb, pc, pd, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if p_red != []: #PASSE RED
                    ''' -------------Top PASSE RED------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="P a s s e s   -   " + self.label_oponente.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela Bloquieo '''
                    s1 = "{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format('Jogadores','Passe A','Passe B','Passe C','Passe D','Total')
                    s2 = "{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format('----------','---------','---------','---------','---------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for j in p_red:
                        nome = j.nome
                        pa = str(len(j.passe[0]))+ ":" + str(j.porcentagem_passe()[0]) + "%"
                        pb = str(len(j.passe[1]))+ ":" + str(j.porcentagem_passe()[1]) + "%"
                        pc = str(len(j.passe[2]))+ ":" + str(j.porcentagem_passe()[2]) + "%"
                        pd = str(len(j.passe[3]))+ ":" + str(j.porcentagem_passe()[3]) + "%"
                        total = str(len(j.passe[0]) + len(j.passe[1]) + len(j.passe[2]) + len(j.passe[3]))
                        s3 = "{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format(nome, pa, pb, pc, pd, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if s_green != []: #SAQUE GREEN
                    ''' -------------Top SAQUE GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="S a q u e s   -   " + self.label_time.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela SAQUE '''
                    s1 = "{:<11} {:<10} {:<10} {:<10} {:<11} {:<14} {:<11}".format('Jogadores','Saque A','Saque B','Saque C','Saque D','Melhor Saque','Total')
                    s2 = "{:<11} {:<10} {:<10} {:<10} {:<11} {:<14} {:<11}".format('----------','--------','--------','--------','--------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for j in s_green:
                        nome = j.nome
                        sa = str(len(j.saque[0]))+ ":" + str(j.porcentagem_saque()[0]) + "%"
                        sb = str(len(j.saque[1]))+ ":" + str(j.porcentagem_saque()[1]) + "%"
                        sc = str(len(j.saque[2]))+ ":" + str(j.porcentagem_saque()[2]) + "%"
                        sd = str(len(j.saque[3]))+ ":" + str(j.porcentagem_saque()[3]) + "%"
                        total = str(len(j.saque[0]) + len(j.saque[1]) + len(j.saque[2]) + len(j.saque[3]))
                        melhor_saque = str(j.MaxPosi(j.saque[0] + j.saque[1])[0]) + j.MaxPosi(j.saque[0] + j.saque[1])[1]
                        s3 = "{:<11} {:<10} {:<10} {:<10} {:<11} {:<14} {:<11}".format(nome, sa, sb, sc, sd, melhor_saque, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                if s_red != []: #SAQUE GREEN
                    ''' -------------Top SAQUE GREEN------------- '''
                    pdf.set_font("Courier", size=12, style='B') # font and textsize
                    pdf.cell(200, 10, txt="S a q u e s   -   " + self.label_oponente.text(), ln=1, align="L")
                    ''' Content '''
                    pdf.set_font("Courier", size=9)

                    ''' Tabela SAQUE '''
                    s1 = "{:<11} {:<10} {:<10} {:<10} {:<11} {:<14} {:<11}".format('Jogadores','Saque A','Saque B','Saque C','Saque D','Melhor Saque','Total')
                    s2 = "{:<11} {:<10} {:<10} {:<10} {:<11} {:<14} {:<11}".format('----------','--------','--------','--------','--------','-------------','------')
                    pdf.cell(10)
                    pdf.cell(200, 5, s1, ln=1, align="L", border = 0)
                    pdf.cell(10)
                    pdf.cell(200, 5, s2, ln=1, align="L", border = 0)
                    for j in s_red:
                        nome = j.nome
                        sa = str(len(j.saque[0]))+ ":" + str(j.porcentagem_saque()[0]) + "%"
                        sb = str(len(j.saque[1]))+ ":" + str(j.porcentagem_saque()[1]) + "%"
                        sc = str(len(j.saque[2]))+ ":" + str(j.porcentagem_saque()[2]) + "%"
                        sd = str(len(j.saque[3]))+ ":" + str(j.porcentagem_saque()[3]) + "%"
                        total = str(len(j.saque[0]) + len(j.saque[1]) + len(j.saque[2]) + len(j.saque[3]))
                        melhor_saque = str(j.MaxPosi(j.saque[0] + j.saque[1])[0]) + j.MaxPosi(j.saque[0] + j.saque[1])[1]
                        s3 = "{:<11} {:<10} {:<10} {:<10} {:<11} {:<14} {:<11}".format(nome, sa, sb, sc, sd, melhor_saque, total)
                        pdf.cell(10)
                        pdf.cell(200, 5, s3, ln=1, align="L", border = 0)
                '''Salva o pdf no diretorio que escolhi '''
                pdf.output(teste[0], 'F')

    def index_player(self, i):
        ''' Usada em conjunto com def tabela para saber qual jogador esta no jogo
        '''
        if i == 1:
            if self.meutimerelatorio:
                return self.t1
            else:
                return self.o1
        elif i == 2:
            if self.meutimerelatorio:
                return self.t2
            else:
                return self.o2
        elif i == 3:
            if self.meutimerelatorio:
                return self.t3
            else:
                return self.o3
        elif i == 4:
            if self.meutimerelatorio:
                return self.t4
            else:
                return self.o4
        elif i == 5:
            if self.meutimerelatorio:
                return self.t5
            else:
                return self.o5
        elif i == 6:
            if self.meutimerelatorio:
                return self.t6
            else:
                return self.o6
        elif i == 7:
            if self.meutimerelatorio:
                return self.t7
            else:
                return self.o7
        elif i == 8:
            if self.meutimerelatorio:
                return self.t8
            else:
                return self.o8
        elif i == 9:
            if self.meutimerelatorio:
                return self.t9
            else:
                return self.o9
        elif i == 10:
            if self.meutimerelatorio:
                return self.t10
            else:
                return self.o10
        elif i == 11:
            if self.meutimerelatorio:
                return self.t11
            else:
                return self.o11
        elif i == 12:
            if self.meutimerelatorio:
                return self.t12
            else:
                return self.o12
        elif i == 13:
            if self.meutimerelatorio:
                return self.t13
            else:
                return self.o13
        elif i == 14:
            if self.meutimerelatorio:
                return self.t14
            else:
                return self.o14

    def mudatimerelatorio(self, parametro):
        self.meutimerelatorio = not self.meutimerelatorio
        self.tabela(parametro)

    def tabela(self, parametro):
        row = 0
        ingame = []
        if self.meutimerelatorio:
            nomes = [self.nome_j1.text(), self.nome_j2.text(), self.nome_j3.text(),
                     self.nome_j4.text(), self.nome_j5.text(), self.nome_j6.text(),
                     self.nome_j7.text(), self.nome_j8.text(), self.nome_j9.text(),
                     self.nome_j10.text(),self.nome_j11.text(),self.nome_j12.text(),
                     self.nome_j13.text(),self.nome_j14.text()]
        else:
            nomes = [self.nome_o1.text(), self.nome_o2.text(), self.nome_o3.text(),
                     self.nome_o4.text(), self.nome_o5.text(), self.nome_o6.text(),
                     self.nome_o7.text(), self.nome_o8.text(), self.nome_o9.text(),
                     self.nome_o10.text(),self.nome_o11.text(),self.nome_o12.text(),
                     self.nome_o13.text(),self.nome_o14.text()]

        if parametro == 1: #(1) Ataques dos Jogadores
            self.pararelatorio = 1
            self.PB_Relatorio_Ataque.setStyleSheet(self.estilos_diferentes_click)
            self.PB_Relatorio_Cataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Defesa.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Bloqueio.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Saque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Passe.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Penalidade.setStyleSheet(self.estilos_iguais_click)
            jogadores = []
            # Jogadores no jogo
            for n in nomes:
                if n.strip() != '':
                    ingame.append( self.index_player( 1 + nomes.index(n)) )
            # Header da tabela
            jogadores.append({'nome':'Nome','at_p':'Acertos','at_n':'Neutros','at_e':'Erros','MP_G':'Maior Sucesso','MP_F':'Tentou Mais','MP_E':'Errou Mais','total':'Total'})
            for i in ingame:
                t = len(i.ataque[0]) + len(i.ataque[1]) + len(i.ataque[2])
                if t != 0: # apenas jogadores que realizaram ataque
                    freqS = i.MaxPosi(i.ataque[0]) #posição que da certo "maior sucesso"
                    freqT = i.MaxFreq(i.ataque) #posição mais jogada
                    freqE = i.MaxPosi(i.ataque[2]) #posição que mais errou
                    jogadores.append({
                        'nome':str(i.nome),
                        'at_p':str(len(i.ataque[0])),
                        'at_n':str(len(i.ataque[1])),
                        'at_e':str(len(i.ataque[2])),
                        'MP_G':str(freqS[0]) + ' : ' + str(freqS[1]),
                        'MP_F':str(freqT[0]) + ' : ' + str(freqT[1]),
                        'MP_E':str(freqE[0]) + ' : ' + str(freqE[1]),
                        'total':str( t )})
            self.tableWidget.setRowCount(len(jogadores))
            self.tableWidget.setColumnCount(8)
            for j in jogadores:
                #Note que 'jogadores' é uma lista com dicionarios dentro
                #self.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(j[nome da chave]))
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(j['nome']))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(j['at_p']))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(j['at_n']))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(j['at_e']))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(j['MP_G']))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(j['MP_F']))
                self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(j['MP_E']))
                self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(j['total']))
                row += 1
            self.tableWidget.setColumnWidth(0,100)
            self.tableWidget.setColumnWidth(1,60)
            self.tableWidget.setColumnWidth(2,60)
            self.tableWidget.setColumnWidth(3,50)
            self.tableWidget.setColumnWidth(4,150)
            self.tableWidget.setColumnWidth(5,150)
            self.tableWidget.setColumnWidth(6,150)
            self.tableWidget.setColumnWidth(7,40)
        if parametro == 2: #Bloqueio dos Jogadores
            self.pararelatorio = 2
            self.PB_Relatorio_Ataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Cataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Defesa.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Bloqueio.setStyleSheet(self.estilos_diferentes_click)
            self.PB_Relatorio_Saque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Passe.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Penalidade.setStyleSheet(self.estilos_iguais_click)
            jogadores = []
            # Jogadores no jogo
            for n in nomes:
                if n.strip() != '':
                    ingame.append( self.index_player( 1 + nomes.index(n)) )
            # Header da tabela
            jogadores.append({'nome':'Nome','b_p':'Convertido','b_n':'Neutros','b_e':'Erros','MP_G':'Maior Sucesso','MP_F':'Mais Jogada','total':'Total'})
            for i in ingame:
                t = len(i.bloqueio[0]) + len(i.bloqueio[1]) + len(i.bloqueio[2])
                if t != 0: # apenas jogadores que realizaram ataque
                    freqS = i.MaxPosi(i.bloqueio[0]) #posição que da certo "maior sucesso"
                    freqT = i.MaxFreq(i.bloqueio) #posição mais jogada
                    jogadores.append({
                        'nome':str(i.nome),
                        'b_p':str(len(i.bloqueio[0])),
                        'b_n':str(len(i.bloqueio[1])),
                        'b_e':str(len(i.bloqueio[2])),
                        'MP_G':str(freqS[0]) + ' : ' + str(freqS[1]),
                        'MP_F':str(freqT[0]) + ' : ' + str(freqT[1]),
                        'total':str( t )})
            self.tableWidget.setRowCount(len(jogadores))
            self.tableWidget.setColumnCount(7)
            for j in jogadores:
                #Note que 'jogadores' é uma lista com dicionarios dentro
                #self.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(j[nome da chave]))
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(j['nome']))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(j['b_p']))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(j['b_n']))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(j['b_e']))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(j['MP_G']))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(j['MP_F']))
                self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(j['total']))
                row += 1
            self.tableWidget.setColumnWidth(0,100)
            self.tableWidget.setColumnWidth(1,80)
            self.tableWidget.setColumnWidth(2,60)
            self.tableWidget.setColumnWidth(3,50)
            self.tableWidget.setColumnWidth(4,150)
            self.tableWidget.setColumnWidth(5,150)
            self.tableWidget.setColumnWidth(6,40)
        if parametro == 3: #Defesa dos Jogadores
            self.pararelatorio = 3
            self.PB_Relatorio_Ataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Cataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Defesa.setStyleSheet(self.estilos_diferentes_click)
            self.PB_Relatorio_Bloqueio.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Saque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Passe.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Penalidade.setStyleSheet(self.estilos_iguais_click)
            jogadores = []
            # Jogadores no jogo
            for n in nomes:
                if n.strip() != '':
                    ingame.append( self.index_player( 1 + nomes.index(n)) )
            # Header da tabela
            jogadores.append({'nome':'Nome','d_a':'A','d_b':'B','d_c':'Erros','MP_G':'Melhor Defesa','MP_F':'Mais Defendida','MP_E':'Maior Falha','total':'Total'})
            for i in ingame:
                t = len(i.defesa[0]) + len(i.defesa[1]) + len(i.defesa[2])
                if t != 0: # apenas jogadores que realizaram ataque
                    freqS = i.MaxPosi(i.defesa[0]) #posição que da certo "maior sucesso"
                    freqT = i.MaxFreq(i.defesa) #posição mais jogada
                    freqE = i.MaxPosi(i.defesa[2]) #posição que mais errou
                    jogadores.append({
                        'nome':str(i.nome),
                        'd_a':str(len(i.defesa[0])),
                        'd_b':str(len(i.defesa[1])),
                        'd_c':str(len(i.defesa[2])),
                        'MP_G':str(freqS[0]) + ' : ' + str(freqS[1]),
                        'MP_F':str(freqT[0]) + ' : ' + str(freqT[1]),
                        'MP_E':str(freqE[0]) + ' : ' + str(freqE[1]),
                        'total':str( t )})
            self.tableWidget.setRowCount(len(jogadores))
            self.tableWidget.setColumnCount(8)
            for j in jogadores:
                #Note que 'jogadores' é uma lista com dicionarios dentro
                #self.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(j[nome da chave]))
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(j['nome']))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(j['d_a']))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(j['d_b']))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(j['d_c']))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(j['MP_G']))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(j['MP_F']))
                self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(j['MP_E']))
                self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(j['total']))
                row += 1
            self.tableWidget.setColumnWidth(0,100)
            self.tableWidget.setColumnWidth(1,40)
            self.tableWidget.setColumnWidth(2,40)
            self.tableWidget.setColumnWidth(3,50)
            self.tableWidget.setColumnWidth(4,150)
            self.tableWidget.setColumnWidth(5,150)
            self.tableWidget.setColumnWidth(6,150)
            self.tableWidget.setColumnWidth(7,40)
        if parametro == 4: #Saque dos Jogadores
            self.pararelatorio = 4
            self.PB_Relatorio_Ataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Cataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Defesa.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Bloqueio.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Saque.setStyleSheet(self.estilos_diferentes_click)
            self.PB_Relatorio_Passe.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Penalidade.setStyleSheet(self.estilos_iguais_click)
            jogadores = []
            # Jogadores no jogo
            for n in nomes:
                if n.strip() != '':
                    ingame.append( self.index_player( 1 + nomes.index(n)) )
            # Header da tabela
            jogadores.append({'nome':'Nome','s_a':'A','s_b':'B','s_c':'C','s_d':'Erros','MP_G':'Melhor Defesa','MP_F':'Mais Defendida','MP_E':'Errou Mais','total':'Total'})
            for i in ingame:
                t = len(i.saque[0]) + len(i.saque[1]) + len(i.saque[2]) + len(i.saque[3])
                if t != 0: # apenas jogadores que realizaram ataque
                    freqS = i.MaxPosi(i.saque[0]) #posição que da certo "maior sucesso"
                    freqT = i.MaxFreq(i.saque) #posição mais jogada
                    freqE = i.MaxPosi(i.saque[3]) #posição que mais errou
                    jogadores.append({
                        'nome':str(i.nome),
                        's_a':str(len(i.saque[0])),
                        's_b':str(len(i.saque[1])),
                        's_c':str(len(i.saque[2])),
                        's_d':str(len(i.saque[3])),
                        'MP_G':str(freqS[0]) + ' : ' + str(freqS[1]),
                        'MP_F':str(freqT[0]) + ' : ' + str(freqT[1]),
                        'MP_E':str(freqE[0]) + ' : ' + str(freqE[1]),
                        'total':str( t )})
            self.tableWidget.setRowCount(len(jogadores))
            self.tableWidget.setColumnCount(9)
            for j in jogadores:
                #Note que 'jogadores' é uma lista com dicionarios dentro
                #self.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(j[nome da chave]))
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(j['nome']))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(j['s_a']))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(j['s_b']))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(j['s_c']))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(j['s_d']))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(j['MP_G']))
                self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(j['MP_F']))
                self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(j['MP_E']))
                self.tableWidget.setItem(row,8,QtWidgets.QTableWidgetItem(j['total']))
                row += 1
            self.tableWidget.setColumnWidth(0,100)
            self.tableWidget.setColumnWidth(1,30)
            self.tableWidget.setColumnWidth(2,30)
            self.tableWidget.setColumnWidth(3,30)
            self.tableWidget.setColumnWidth(4,50)
            self.tableWidget.setColumnWidth(5,150)
            self.tableWidget.setColumnWidth(6,150)
            self.tableWidget.setColumnWidth(7,150)
            self.tableWidget.setColumnWidth(8,40)
        if parametro == 5: #Passe dos Jogadores
            self.pararelatorio = 5
            self.PB_Relatorio_Ataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Cataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Defesa.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Bloqueio.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Saque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Passe.setStyleSheet(self.estilos_diferentes_click)
            self.PB_Relatorio_Penalidade.setStyleSheet(self.estilos_iguais_click)
            jogadores = []
            # Jogadores no jogo
            for n in nomes:
                if n.strip() != '':
                    ingame.append( self.index_player( 1 + nomes.index(n)) )
            # Header da tabela
            jogadores.append({'nome':'Nome','p_a':'Passe A','p_b':'Passe B','p_c':'Passe C','p_d':'Passe D','total':'Total'})
            for i in ingame:
                t = len(i.passe[0]) + len(i.passe[1]) + len(i.passe[2]) + len(i.passe[3])
                if t != 0: # apenas jogadores que realizaram ataque
                    jogadores.append({
                        'nome':str(i.nome),
                        'p_a':str(len(i.passe[0])) + " : " + str(i.porcentagem_passe()[0])+"%",
                        'p_b':str(len(i.passe[1])) + " : " + str(i.porcentagem_passe()[1])+"%",
                        'p_c':str(len(i.passe[2])) + " : " + str(i.porcentagem_passe()[2])+"%",
                        'p_d':str(len(i.passe[3])) + " : " + str(i.porcentagem_passe()[3])+"%",
                        'total':str( t )})
            self.tableWidget.setRowCount(len(jogadores))
            self.tableWidget.setColumnCount(6)
            for j in jogadores:
                #Note que 'jogadores' é uma lista com dicionarios dentro
                #self.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(j[nome da chave]))
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(j['nome']))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(j['p_a']))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(j['p_b']))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(j['p_c']))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(j['p_d']))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(j['total']))
                row += 1
            self.tableWidget.setColumnWidth(0,100)
            self.tableWidget.setColumnWidth(1,100)
            self.tableWidget.setColumnWidth(2,100)
            self.tableWidget.setColumnWidth(3,100)
            self.tableWidget.setColumnWidth(4,100)
            self.tableWidget.setColumnWidth(8,40)
        if parametro == 6: #Penalidades dos Jogadores
            self.pararelatorio = 6
            self.PB_Relatorio_Ataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Cataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Defesa.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Bloqueio.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Saque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Passe.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Penalidade.setStyleSheet(self.estilos_diferentes_click)
            jogadores = []
            # Jogadores no jogo
            for n in nomes:
                if n.strip() != '':
                    ingame.append( self.index_player( 1 + nomes.index(n)) )
            # Header da tabela
            jogadores.append({'nome':'Nome','pnR':'Rede','pnC':'Cartão','pnDT':'D.Toques','pnCO':'Cond.','total':'Total'})
            for i in ingame:
                t = len(i.penalidades[0]) + len(i.penalidades[1]) + len(i.penalidades[2]) + len(i.penalidades[3])
                if t != 0: # apenas jogadores que realizaram ataque
                    jogadores.append({
                        'nome':str(i.nome),
                        'pnR':str(len(i.penalidades[0])),
                        'pnC':str(len(i.penalidades[1])),
                        'pnDT':str(len(i.penalidades[2])),
                        'pnCO':str(len(i.penalidades[3])),
                        'total':str( t )})
            self.tableWidget.setRowCount(len(jogadores))
            self.tableWidget.setColumnCount(6)
            for j in jogadores:
                #Note que 'jogadores' é uma lista com dicionarios dentro
                #self.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(j[nome da chave]))
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(j['nome']))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(j['pnR']))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(j['pnC']))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(j['pnDT']))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(j['pnCO']))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(j['total']))
                row += 1
            self.tableWidget.setColumnWidth(0,100)
            self.tableWidget.setColumnWidth(1,60)
            self.tableWidget.setColumnWidth(2,60)
            self.tableWidget.setColumnWidth(3,90)
            self.tableWidget.setColumnWidth(4,60)
            self.tableWidget.setColumnWidth(5,40)
        if parametro == 7: #Contra Ataque dos Jogadores
            self.pararelatorio = 7
            self.PB_Relatorio_Ataque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Cataque.setStyleSheet(self.estilos_diferentes_click)
            self.PB_Relatorio_Defesa.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Bloqueio.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Saque.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Passe.setStyleSheet(self.estilos_iguais_click)
            self.PB_Relatorio_Penalidade.setStyleSheet(self.estilos_iguais_click)
            jogadores = []
            # Jogadores no jogo
            for n in nomes:
                if n.strip() != '':
                    ingame.append( self.index_player( 1 + nomes.index(n)) )
            # Header da tabela
            jogadores.append({'nome':'Nome','cat_p':'Acertos','cat_n':'Neutros','cat_e':'Erros','MP_G':'Maior Sucesso','MP_F':'Mais Jogada','MP_E':'Errou Mais','total':'Total'})
            for i in ingame:
                t = len(i.cataque[0]) + len(i.cataque[1]) + len(i.cataque[2])
                if t != 0: # apenas jogadores que realizaram ataque
                    freqS = i.MaxPosi(i.cataque[0]) #posição que da certo "maior sucesso"
                    freqT = i.MaxFreq(i.cataque) #posição mais jogada
                    freqE = i.MaxPosi(i.cataque[2]) #posição que mais errou
                    jogadores.append({
                        'nome':str(i.nome),
                        'cat_p':str(len(i.cataque[0])),
                        'cat_n':str(len(i.cataque[1])),
                        'cat_e':str(len(i.cataque[2])),
                        'MP_G':str(freqS[0]) + ' : ' + str(freqS[1]),
                        'MP_F':str(freqT[0]) + ' : ' + str(freqT[1]),
                        'MP_E':str(freqE[0]) + ' : ' + str(freqE[1]),
                        'total':str( t )})
            self.tableWidget.setRowCount(len(jogadores))
            self.tableWidget.setColumnCount(8)
            for j in jogadores:
                #Note que 'jogadores' é uma lista com dicionarios dentro
                #self.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(j[nome da chave]))
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(j['nome']))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(j['cat_p']))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(j['cat_n']))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(j['cat_e']))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(j['MP_G']))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(j['MP_F']))
                self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(j['MP_E']))
                self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(j['total']))
                row += 1
            self.tableWidget.setColumnWidth(0,100)
            self.tableWidget.setColumnWidth(1,60)
            self.tableWidget.setColumnWidth(2,60)
            self.tableWidget.setColumnWidth(3,50)
            self.tableWidget.setColumnWidth(4,150)
            self.tableWidget.setColumnWidth(5,150)
            self.tableWidget.setColumnWidth(6,150)
            self.tableWidget.setColumnWidth(7,40)

    def reset_scores(self):
        self.ResetBox_fecha() # Fecha a janela que abriu ao clicar no botao de reset
        global PAUSE_RESUME
        global DELTA_PAUSE
        global TEMPO_INICIADO
        global DELTA_ZERA_TEMPO
        self.N_ataque_green.setValue(0)
        self.N_ataque_blue.setValue(0)
        self.N_ataque_red.setValue(0)
        self.N_bloqueio_green.setValue(0)
        self.N_bloqueio_blue.setValue(0)
        self.N_bloqueio_red.setValue(0)
        self.N_saque_green.setValue(0)
        self.N_saque_blue.setValue(0)
        self.N_saque_ora.setValue(0)
        self.N_saque_red.setValue(0)
        self.N_passe_A.setValue(0)
        self.N_passe_B.setValue(0)
        self.N_passe_C.setValue(0)
        self.N_passe_D.setValue(0)
        self.N_defesa_A.setValue(0)
        self.N_defesa_B.setValue(0)
        self.N_defesa_C.setValue(0)
        self.N_rede.setValue(0)
        self.N_cartao.setValue(0)
        self.N_2t.setValue(0)
        self.N_cond.setValue(0)

        self.label_Plagreen.setText('00')
        self.label_Plared.setText('00')
        self.flag = 0


        self.PB_J1.setStyleSheet(self.estilos_iguais_click)
        self.PB_J2.setStyleSheet(self.estilos_iguais_click)
        self.PB_J3.setStyleSheet(self.estilos_iguais_click)
        self.PB_J4.setStyleSheet(self.estilos_iguais_click)
        self.PB_J5.setStyleSheet(self.estilos_iguais_click)
        self.PB_J6.setStyleSheet(self.estilos_iguais_click)
        self.PB_J7.setStyleSheet(self.estilos_iguais_click)
        self.PB_J8.setStyleSheet(self.estilos_iguais_click)
        self.PB_J9.setStyleSheet(self.estilos_iguais_click)
        self.PB_J10.setStyleSheet(self.estilos_iguais_click)
        self.PB_J11.setStyleSheet(self.estilos_iguais_click)
        self.PB_J12.setStyleSheet(self.estilos_iguais_click)
        self.PB_J13.setStyleSheet(self.estilos_iguais_click)
        self.PB_J14.setStyleSheet(self.estilos_iguais_click)
        # Redefine Estilos botao iniciar tempo
        self.PB_Scores_Time.setText("Iniciar Tempo")
        self.PB_Scores_Time.setStyleSheet("QPushButton{\n"
"font: 12pt \"Cortoba\";\n"
"border: 1px solid  rgb(0, 225, 255);\n"
"color: rgb(238, 238, 236);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{;\n"
"background-color: rgb(0, 144, 153);\n"
"}\n"
"QPushButton:pressed {background-color: rgb(85, 87, 83);}")
        # Redefine Estilos botao pause
        self.PB_Scores_pause.setText("Pausar")
        self.PB_Scores_pause.setStyleSheet("QPushButton{\n"
"font: 12pt \"Cortoba\";\n"
"border: 1px solid  rgb(0, 225, 255);\n"
"color: rgb(238, 238, 236);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{;\n"
"background-color: rgb(0, 144, 153);\n"
"}\n"
"QPushButton:pressed {background-color: rgb(85, 87, 83);}")
        # Para a contagem do tempo
        self.timer.stop()
        # Redefine Globais para funçoes de tempo
        PAUSE_RESUME = True
        DELTA_PAUSE = 0
        TEMPO_INICIADO = False
        DELTA_ZERA_TEMPO = 0

        try: del self.t1
        except: pass
        try: del self.t2
        except: pass
        try: del self.t3
        except: pass
        try: del self.t4
        except: pass
        try: del self.t5
        except: pass
        try: del self.t6
        except: pass
        try: del self.t7
        except: pass
        try: del self.t8
        except: pass
        try: del self.t9
        except: pass
        try: del self.t10
        except: pass
        try: del self.t11
        except: pass
        try: del self.t12
        except: pass
        try: del self.t13
        except: pass
        try: del self.t14
        except: pass
        try: del self.o1
        except: pass
        try: del self.o2
        except: pass
        try: del self.o3
        except: pass
        try: del self.o4
        except: pass
        try: del self.o5
        except: pass
        try: del self.o6
        except: pass
        try: del self.o7
        except: pass
        try: del self.o8
        except: pass
        try: del self.o9
        except: pass
        try: del self.o10
        except: pass
        try: del self.o11
        except: pass
        try: del self.o12
        except: pass
        try: del self.o13
        except: pass
        try: del self.o14
        except: pass
        self.reset_nomes()
        self.CadastroJogadores.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.page_1_mostra()
        self.nomes_flag = 0
        self.PB_J1.hide()
        self.PB_J2.hide()
        self.PB_J3.hide()
        self.PB_J4.hide()
        self.PB_J5.hide()
        self.PB_J6.hide()
        self.PB_J7.hide()
        self.PB_J8.hide()
        self.PB_J9.hide()
        self.PB_J10.hide()
        self.PB_J11.hide()
        self.PB_J12.hide()
        self.PB_J13.hide()
        self.PB_J14.hide()
        self.PB_O1.hide()
        self.PB_O2.hide()
        self.PB_O3.hide()
        self.PB_O4.hide()
        self.PB_O5.hide()
        self.PB_O6.hide()
        self.PB_O7.hide()
        self.PB_O8.hide()
        self.PB_O9.hide()
        self.PB_O10.hide()
        self.PB_O11.hide()
        self.PB_O12.hide()
        self.PB_O13.hide()
        self.PB_O14.hide()
    def reset_nomes(self):
        '''Meu Time'''
        self.nome_j1.clear()
        self.nome_j2.clear()
        self.nome_j3.clear()
        self.nome_j4.clear()
        self.nome_j5.clear()
        self.nome_j6.clear()
        self.nome_j7.clear()
        self.nome_j8.clear()
        self.nome_j9.clear()
        self.nome_j10.clear()
        self.nome_j11.clear()
        self.nome_j12.clear()
        self.nome_j13.clear()
        self.nome_j14.clear()
        '''Time Adversário'''
        self.nome_o1.clear()
        self.nome_o2.clear()
        self.nome_o3.clear()
        self.nome_o4.clear()
        self.nome_o5.clear()
        self.nome_o6.clear()
        self.nome_o7.clear()
        self.nome_o8.clear()
        self.nome_o9.clear()
        self.nome_o10.clear()
        self.nome_o11.clear()
        self.nome_o12.clear()
        self.nome_o13.clear()
        self.nome_o14.clear()

        self.ResetBox_fecha

    def nomesoponente(self): # mostra página para nomes do time oponente
        if self.nomes_flag == 1:
            self.define_jogadores()
        else:
            self.CadastroJogadores.setCurrentIndex(1)
            self.nomes_flag += 1

    def page_1_mostra(self): #Definindo Jogadores
        self.PB_1.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(0)
    def page_2_mostra(self): #Scores, botões das ações
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(1)
    def page_3_mostra(self): #Relatório
        self.tabela(1)
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(2)
        self.mostra_relatorio() #Atualiza o display de resumos do jogo
    def page_4_mostra(self): #Saque
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(3)
        self.equipe_graficos = True
        self.draw_saque()
    def page_5_mostra(self): #Defesa
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(4)
        self.equipe_graficos = True
        self.draw_defesa()
    def page_6_mostra(self): #Ações
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(5)
        self.draw_pontos()
    def page_7_mostra(self): #Ataque
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(6)
        self.equipe_graficos = True
        self.draw_ataque()
    def page_8_mostra(self): #Bloqueio
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_pressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_Npressionada)
        self.stackedWidget.setCurrentIndex(7)
        self.equipe_graficos = True
        self.draw_bloqueio()
    def page_9_mostra(self): #Passe
        self.PB_1.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_2.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_3.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_4.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_5.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_6.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_7.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_8.setStyleSheet(self.estilos_aba_Npressionada)
        self.PB_9.setStyleSheet(self.estilos_aba_pressionada)
        self.stackedWidget.setCurrentIndex(8)
        self.equipe_graficos = True
        self.draw_passe()

    def toogglehover_abre2(self):
        self.animation = QPropertyAnimation(self.frame_OP2, b"geometry")
        self.animation.setDuration(100)
        self.animation.setStartValue(QtCore.QRect(0, 630, 1271, 41))
        self.animation.setEndValue(QtCore.QRect(0, 0, 1271, 671))
        self.animation.start()

    def toogglehover_fecha2(self):
        self.animation = QPropertyAnimation(self.frame_OP2, b"geometry")
        self.animation.setDuration(100)
        self.animation.setStartValue(QtCore.QRect(0, 0, 1271, 671))
        self.animation.setEndValue(QtCore.QRect(0, 630, 1271, 41))
        self.animation.start()

    def CA_abre(self):
        self.animation = QPropertyAnimation(self.ContraAtaque, b"geometry")
        self.animation.setDuration(150)
        self.animation.setStartValue(QtCore.QRect(10, 590, 341, 31))
        self.animation.setEndValue(QtCore.QRect(10, 360, 341, 261))
        self.animation.start()

    def CA_fecha(self):
        self.animation = QPropertyAnimation(self.ContraAtaque, b"geometry")
        self.animation.setDuration(150)
        self.animation.setStartValue(QtCore.QRect(10, 590, 341, 31))
        self.animation.setEndValue(QtCore.QRect(10, 590, 341, 31))
        self.animation.start()

    def ResetBox_abre(self):
        self.animation = QPropertyAnimation(self.frame_Reset, b"geometry")
        self.animation.setDuration(90)
        self.animation.setStartValue(QtCore.QRect(0, -20, 1271, 16))
        self.animation.setEndValue(QtCore.QRect(0, -20, 1271, 651))
        self.animation.start()

    def ResetBox_fecha(self):
        self.animation = QPropertyAnimation(self.frame_Reset, b"geometry")
        self.animation.setDuration(90)
        self.animation.setStartValue(QtCore.QRect(0, -20, 1271, 651))
        self.animation.setEndValue(QtCore.QRect(0, -20, 1271, 16))
        self.animation.start()

    def eventFilter(self, object, event):
        if object.objectName() == 'ContraAtaque':
            if event.type() == QtCore.QEvent.Enter:
                self.CA_abre()
                return True
            elif event.type() == QtCore.QEvent.Leave:
                self.CA_fecha()
            return False

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            GLOBAL_STATE = 1
            return w.showMaximized()
        else:
            GLOBAL_STATE = 0
            return w.showNormal()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        if GLOBAL_STATE == 0:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

class PDF(fpdf.FPDF):
    def header(self):
        titulo_jogo = w.nome_partida.text()
        self.image('vball.png', 95, 15, 200) #LOGO
        self.set_font("Courier", size=16, style='B')
        self.cell(200, 10,titulo_jogo, ln=1, align="C")
    # Page footer
    def footer(self):
        data = str(datetime.today().strftime('%Y-%m-%d'))
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Courier', 'I', 8)
        # Page number
        self.cell(0, 10, 'Relatório gerado por Scores - Versão alfinha - '+data, 0, 0, 'L')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
