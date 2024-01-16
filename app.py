from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cotacao.html')

@app.route('/cotacao', methods=['POST'])
def cotar():
    idades_str = request.form['idade']
    idades = [int(age.strip()) for age in idades_str.split(',')]
    plano = request.form['plano'].strip()

    valores = {}
    total_valor = 0
    desconto_aplicado = False

    for idade in idades:
        valor = 0

        if plano == 'enfermaria (pessoa física) - Coparticipação parcial' or plano == 'enfermaria (pessoa física) - Coparticipação total' or plano == 'ambulatorial (pessoa física) - Coparticipação parcial' or plano == 'ambulatorial (pessoa física) - Coparticipação total' or plano == 'apartamento (pessoa física) - Coparticipação parcial' or plano == 'apartamento (pessoa física) - Coparticipação total' or plano == 'Mix enfermaria (pessoa física) - Coparticipação parcial' or plano == 'Mix apartamento (pessoa física) - Coparticipação parcial':
            if len(idades) >= 2 and not desconto_aplicado:
                valor = valor * 0.95
                desconto_aplicado = True

        if plano == 'enfermaria (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 200.08
            elif idade <= 23:
                valor = 259.02
            elif idade <= 28:
                valor = 295.49
            elif idade <= 33:
                valor = 329.04
            elif idade <= 38:
                valor = 344.70
            elif idade <= 43:
                valor = 387.44
            elif idade <= 48:
                valor = 469.18
            elif idade <= 53:
                valor = 641.43
            elif idade <= 58:
                valor = 860.37
            else:
                valor = 1113.71
        elif plano == 'enfermaria (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 163.24
            elif idade <= 23:
                valor = 210.39
            elif idade <= 28:
                valor = 239.56
            elif idade <= 33:
                valor = 266.40
            elif idade <= 38:
                valor = 278.93
            elif idade <= 43:
                valor = 313.12
            elif idade <= 48:
                valor = 378.51
            elif idade <= 53:
                valor = 516.30
            elif idade <= 58:
                valor = 691.44
            else:
                valor = 894.10
        elif plano == 'ambulatorial (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 172.23
            elif idade <= 23:
                valor = 226.73
            elif idade <= 28:
                valor = 258.43
            elif idade <= 33:
                valor = 288.26
            elif idade <= 38:
                valor = 303.35
            elif idade <= 43:
                valor = 340.53
            elif idade <= 48:
                valor = 416.36
            elif idade <= 53:
                valor = 577.38
            elif idade <= 58:
                valor = 778.24
            else:
                valor = 1010.66
        elif plano == 'ambulatorial (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 110.67
            elif idade <= 23:
                valor = 145.29
            elif idade <= 28:
                valor = 165.42
            elif idade <= 33:
                valor = 184.36
            elif idade <= 38:
                valor = 193.95
            elif idade <= 43:
                valor = 217.57
            elif idade <= 48:
                valor = 265.74
            elif idade <= 53:
                valor = 368.01
            elif idade <= 58:
                valor = 495.59
            else:
                valor = 643.22
        elif plano == 'apartamento (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 292.17
            elif idade <= 23:
                valor = 380.58
            elif idade <= 28:
                valor = 435.28
            elif idade <= 33:
                valor = 485.61
            elif idade <= 38:
                valor = 509.10
            elif idade <= 43:
                valor = 573.22
            elif idade <= 48:
                valor = 695.83
            elif idade <= 53:
                valor = 954.20
            elif idade <= 58:
                valor = 1282.61
            else:
                valor = 1662.62
        elif plano == 'apartamento (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 236.91
            elif idade <= 23:
                valor = 307.63
            elif idade <= 28:
                valor = 351.39
            elif idade <= 33:
                valor = 391.65
            elif idade <= 38:
                valor = 410.44
            elif idade <= 43:
                valor = 461.73
            elif idade <= 48:
                valor = 559.81
            elif idade <= 53:
                valor = 766.50
            elif idade <= 58:
                valor = 1029.21
            else:
                valor = 1333.20
        elif plano == 'Mix enfermaria (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 490.82
            elif idade <= 23:
                valor = 642.79
            elif idade <= 28:
                valor = 736.82
            elif idade <= 33:
                valor = 823.33
            elif idade <= 38:
                valor = 863.70
            elif idade <= 43:
                valor = 973.91
            elif idade <= 48:
                valor = 1184.67
            elif idade <= 53:
                valor = 1628.80
            elif idade <= 58:
                valor = 2193.32
            else:
                valor = 0
        elif plano == 'Mix apartamento (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 728.31
            elif idade <= 23:
                valor = 956.28
            elif idade <= 28:
                valor = 1097.34
            elif idade <= 33:
                valor = 1227.11
            elif idade <= 38:
                valor = 1287.67
            elif idade <= 43:
                valor = 1453.00
            elif idade <= 48:
                valor = 1769.16
            elif idade <= 53:
                valor = 2435.40
            elif idade <= 58:
                valor = 3282.23
            else:
                valor = 0
        elif plano == 'enfermaria (pessoa jurídica) - Coparticipação parcial':
            if idade <= 18:
                valor = 165.55
            elif idade <= 23:
                valor = 185.42
            elif idade <= 28:
                valor = 207.67
            elif idade <= 33:
                valor = 238.82
            elif idade <= 38:
                valor = 274.64
            elif idade <= 43:
                valor = 326.82
            elif idade <= 48:
                valor = 408.53
            elif idade <= 53:
                valor = 510.66
            elif idade <= 58:
                valor = 868.12
            else:
                valor = 972.29
        elif plano == 'enfermaria (pessoa jurídica) - Coparticipação total':
            if idade <= 18:
                valor = 129.41
            elif idade <= 23:
                valor = 144.94
            elif idade <= 28:
                valor = 162.33
            elif idade <= 33:
                valor = 186.68
            elif idade <= 38:
                valor = 214.68
            elif idade <= 43:
                valor = 255.47
            elif idade <= 48:
                valor = 319.34
            elif idade <= 53:
                valor = 399.18
            elif idade <= 58:
                valor = 678.61
            else:
                valor = 760.04
        elif plano == 'ambulatorial (pessoa jurídica) - Coparticipação parcial':
            if idade <= 18:
                valor = 122.75
            elif idade <= 23:
                valor = 137.48
            elif idade <= 28:
                valor = 153.98
            elif idade <= 33:
                valor = 177.08
            elif idade <= 38:
                valor = 203.64
            elif idade <= 43:
                valor = 242.33
            elif idade <= 48:
                valor = 302.91
            elif idade <= 53:
                valor = 378.64
            elif idade <= 58:
                valor = 643.69
            else:
                valor = 720.93
        elif plano == 'ambulatorial (pessoa jurídica) - Coparticipação total':
            if idade <= 18:
                valor = 90.68
            elif idade <= 23:
                valor = 101.56
            elif idade <= 28:
                valor = 113.75
            elif idade <= 33:
                valor = 130.81
            elif idade <= 38:
                valor = 150.43
            elif idade <= 43:
                valor = 179.01
            elif idade <= 48:
                valor = 223.76
            elif idade <= 53:
                valor = 279.70
            elif idade <= 58:
                valor = 475,49
            else:
                valor = 532.55
        elif plano == 'apartamento (pessoa jurídica) - Coparticipação parcial':
            if idade <= 18:
                valor = 247.58
            elif idade <= 23:
                valor = 277.29
            elif idade <= 28:
                valor = 310.56
            elif idade <= 33:
                valor = 357.14
            elif idade <= 38:
                valor = 410.71
            elif idade <= 43:
                valor = 488.74
            elif idade <= 48:
                valor = 610.93
            elif idade <= 53:
                valor = 763.66
            elif idade <= 58:
                valor = 1298.22
            else:
                valor = 1454.01
        elif plano == 'apartamento (pessoa jurídica) - Coparticipação total':
            if idade <= 18:
                valor = 193.34
            elif idade <= 23:
                valor = 216.54
            elif idade <= 28:
                valor = 242.52
            elif idade <= 33:
                valor = 278.90
            elif idade <= 38:
                valor = 320.74
            elif idade <= 43:
                valor = 381.68
            elif idade <= 48:
                valor = 477.10
            elif idade <= 53:
                valor = 596.38
            elif idade <= 58:
                valor = 1013.85
            else:
                valor = 1135.51
        elif plano == 'allcare Ambulatorial - Sem Coparticipação':
            if idade <= 18:
                valor = 158.38
            elif idade <= 23:
                valor = 208.49
            elif idade <= 28:
                valor = 237.63
            elif idade <= 33:
                valor = 265.06
            elif idade <= 38:
                valor = 278.94
            elif idade <= 43:
                valor = 313.13
            elif idade <= 48:
                valor = 382.86
            elif idade <= 53:
                valor = 530.92
            elif idade <= 58:
                valor = 715.63
            else:
                valor = 929.35
        elif plano == 'allcare Enfermaria - Sem Coparticipação':
            if idade <= 18:
                valor = 285.31
            elif idade <= 23:
                valor = 369.62
            elif idade <= 28:
                valor = 421.80
            elif idade <= 33:
                valor = 469.79
            elif idade <= 38:
                valor = 492.18
            elif idade <= 43:
                valor = 553.34
            elif idade <= 48:
                valor = 670.27
            elif idade <= 53:
                valor = 916.69
            elif idade <= 58:
                valor = 1229.90
            else:
                valor = 1592.33
        elif plano == 'allcare Apartamento - Sem Coparticipação':
            if idade <= 18:
                valor = 417.08
            elif idade <= 23:
                valor = 543.55
            elif idade <= 28:
                valor = 621.81
            elif idade <= 33:
                valor = 693.83
            elif idade <= 38:
                valor = 727.43
            elif idade <= 43:
                valor = 819.15
            elif idade <= 48:
                valor = 994.57
            elif idade <= 53:
                valor = 1364.21
            elif idade <= 58:
                valor = 1834.06
            else:
                valor = 2377.73
        else:
            return 'Plano inválido'

        if idade not in valores:
            valores[idade] = {'plano': [], 'qtd': 0}

        valores[idade]['plano'].append(valor)
        total_valor += valor
        valores[idade]['qtd'] += 1

    if desconto_aplicado:
        total_valor = total_valor * 0.95

    total_valor = '{:.2f}'.format(total_valor)

    return render_template('resposta.html', valores=valores, total_valor=total_valor, desconto_aplicado=desconto_aplicado, plano_selecionado=plano)

if __name__ == '__main__':
    app.run(debug=True)
