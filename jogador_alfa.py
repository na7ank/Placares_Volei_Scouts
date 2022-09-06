
class Jogador:
    ''' classe que representa um jogador durante a partida'''
    def __init__(self, nome):
        '''Fundamentos de cada jogador'''
        self.nome = nome
        self.cataque = [ [], [], [] ]   # Posicional
        self.ataque = [ [], [], [] ]    # Posicional
        self.bloqueio = [ [], [], [] ]  # Posicional
        self.defesa = [ [], [], [] ]    # Posicional
        self.passe = [ [], [], [], [] ] # Posicional
        self.penalidades = [ [], [], [], [] ]
        self.saque = [ [], [], [], [] ] # Posicional

    def totais(self):
        '''retorna a quantidade de ações dos Fundamentos
            ex: ataques totais, passes totais
        '''
        a_t = 0
        b_t = 0
        ca_t = 0
        d_t = 0
        p_t = 0
        pen_t = 0
        s_t = 0

        for ataq in self.ataque:
            a_t += len(ataq)

        for bloc in self.bloqueio:
            b_t += len(bloc)

        for cataq in self.cataque:
            ca_t += len(cataq)

        for defs in self.defesa:
            d_t += len(defs)

        for pas in self.passe:
            p_t += len(pas)

        for pen in self.penalidades:
            pen_t += len(pen)

        for saq in self.saque:
            s_t += len(saq)

        return [a_t, b_t, ca_t, d_t, p_t, pen_t, s_t]

    def MaxPosi(self, lista):
        # retorna a maior frequencia e a posição
        max = 0
        pos = (0, 0)
        total = len(lista)
        if total == 0:
            return (pos, '0%')

        for n in lista:
            x = lista.count(n)
            if max < x:
                max = x
                pos = n
        if pos == (0, 0):
            return (pos, "0%")
        else:
            return (pos, str(round(100*max/total,1))+'%')

    def MaxFreq(self, fundamento):
        # posicao mais jogada de todas
        max = 0
        pos = (0, 0)
        cords = []
        for c in fundamento:
            cords += c
        total = len(cords)
        if total == 0:
            return (pos, '0%')
        for n in cords:
            x = cords.count(n)
            if max < x:
                max = x
                pos = n
        return (pos, str(round(100*max/total,1))+'%')

    def ef_cataque(self):
        g = len(self.cataque[0])
        b = len(self.cataque[1])
        r = len(self.cataque[2])
        total = g + b + r
        if total == 0:
            return 0
        return round((g - r) / total, 1)
    def ef_bloqueio(self):
        g = len(self.bloqueio[0])
        b = len(self.bloqueio[1])
        r = len(self.bloqueio[2])
        total = g + b + r
        if total == 0:
            return 0
        return round((g + b - r) / total, 1)
    def ef_ataque(self):
        g = len(self.ataque[0])
        b = len(self.ataque[1])
        r = len(self.ataque[2])
        total = g + b + r
        if total == 0:
            return 0
        return round((g - r) / total, 1)
    def ef_defesa(self):
        g = len(self.defesa[0])
        b = len(self.defesa[1])
        r = len(self.defesa[2])
        total = g + b + r
        if total == 0:
            return 0
        return round((g + b - r) / total, 1)
    def ef_saque(self):
        a = len(self.saque[0])
        b = len(self.saque[1])
        c = len(self.saque[2])
        d = len(self.saque[3])
        total = a + b + c + d
        if total == 0:
            return 0
        return round((a+b-c-d) / total, 1)

    def porcentagem_passe(self):
        ''' Porcentagem de cada categoria do passe'''
        a = len(self.passe[0])
        b = len(self.passe[1])
        c = len(self.passe[2])
        d = len(self.passe[3])
        t = a + b + c + d
        if t != 0:
            pa = round(100*a/t, 1)
            pb = round(100*b/t, 1)
            pc = round(100*c/t, 1)
            pd = round(100*d/t, 1)
            return (pa, pb, pc, pd)
        else:
            return (0, 0, 0, 0)
    def porcentagem_saque(self):
        ''' Porcentagem de cada categoria do saque'''
        a = len(self.saque[0])
        b = len(self.saque[1])
        c = len(self.saque[2])
        d = len(self.saque[3])
        t = a + b + c + d
        if t != 0:
            sa = round(100*a/t, 1)
            sb = round(100*b/t, 1)
            sc = round(100*c/t, 1)
            sd = round(100*d/t, 1)
            return (sa, sb, sc, sd)
        else:
            return (0, 0, 0, 0)


    def fund(self, x):
        ''' Para ser possível acessar um atributo usando outra funcao
        '''
        if x == 'nome':
            return self.nome
        elif x == 'ataque':
            return self.ataque
        elif x == 'bloqueio':
            return self.bloqueio
        elif x == 'defesa':
            return self.defesa
        elif x == 'passe':
            return self.passe
        elif x == 'penalidades':
            return self.penalidades
        elif x == 'saque':
            return self.saque
        elif x == 'cataque':
            return self.cataque
