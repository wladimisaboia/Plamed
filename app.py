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
                valor = 207.18
            elif idade <= 23:
                valor = 266.02
            elif idade <= 28:
                valor = 302.49
            elif idade <= 33:
                valor = 336.04
            elif idade <= 38:
                valor = 351.70
            elif idade <= 43:
                valor = 394.44
            elif idade <= 48:
                valor = 476.18
            elif idade <= 53:
                valor = 648.43
            elif idade <= 58:
                valor = 867.37
            else:
                valor = 1120.71
        elif plano == 'enfermaria (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 170.24
            elif idade <= 23:
                valor = 217.39
            elif idade <= 28:
                valor = 246.56
            elif idade <= 33:
                valor = 273.40
            elif idade <= 38:
                valor = 285.93
            elif idade <= 43:
                valor = 320.12
            elif idade <= 48:
                valor = 385.51
            elif idade <= 53:
                valor = 523.30
            elif idade <= 58:
                valor = 698.44
            else:
                valor = 901.10
        elif plano == 'ambulatorial (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 172.33
            elif idade <= 23:
                valor = 226.83
            elif idade <= 28:
                valor = 258.53
            elif idade <= 33:
                valor = 288.36
            elif idade <= 38:
                valor = 303.45
            elif idade <= 43:
                valor = 340.63
            elif idade <= 48:
                valor = 416.46
            elif idade <= 53:
                valor = 577.48
            elif idade <= 58:
                valor = 778.34
            else:
                valor = 1010.76
        elif plano == 'ambulatorial (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 110.77
            elif idade <= 23:
                valor = 145.39
            elif idade <= 28:
                valor = 165.52
            elif idade <= 33:
                valor = 184.46
            elif idade <= 38:
                valor = 194.05
            elif idade <= 43:
                valor = 217.67
            elif idade <= 48:
                valor = 265.84
            elif idade <= 53:
                valor = 368.11
            elif idade <= 58:
                valor = 495.69
            else:
                valor = 643.32
        elif plano == 'apartamento (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 299.17
            elif idade <= 23:
                valor = 387.58
            elif idade <= 28:
                valor = 442.28
            elif idade <= 33:
                valor = 492.61
            elif idade <= 38:
                valor = 516.10
            elif idade <= 43:
                valor = 580.22
            elif idade <= 48:
                valor = 702.83
            elif idade <= 53:
                valor = 961.20
            elif idade <= 58:
                valor = 1289.61
            else:
                valor = 1669.62
        elif plano == 'apartamento (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 243.91
            elif idade <= 23:
                valor = 314.63
            elif idade <= 28:
                valor = 358.39
            elif idade <= 33:
                valor = 398.65
            elif idade <= 38:
                valor = 417.44
            elif idade <= 43:
                valor = 468.73
            elif idade <= 48:
                valor = 566.81
            elif idade <= 53:
                valor = 773.50
            elif idade <= 58:
                valor = 1036.21
            else:
                valor = 1340.20
        elif plano == 'Mix enfermaria (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 497.82
            elif idade <= 23:
                valor = 649.79
            elif idade <= 28:
                valor = 743.82
            elif idade <= 33:
                valor = 830.33
            elif idade <= 38:
                valor = 870.70
            elif idade <= 43:
                valor = 980.91
            elif idade <= 48:
                valor = 1191.67
            elif idade <= 53:
                valor = 1635.80
            elif idade <= 58:
                valor = 2200.32
            else:
                valor = 0
        elif plano == 'Mix apartamento (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 735.31
            elif idade <= 23:
                valor = 963.28
            elif idade <= 28:
                valor = 1104.34
            elif idade <= 33:
                valor = 1234.11
            elif idade <= 38:
                valor = 1294.67
            elif idade <= 43:
                valor = 1460.00
            elif idade <= 48:
                valor = 1776.16
            elif idade <= 53:
                valor = 2442.40
            elif idade <= 58:
                valor = 3289.23
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
