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

        if plano == 'ambulatorial (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 182.56
            elif idade <= 23:
                valor = 240.33
            elif idade <= 28:
                valor = 273.93
            elif idade <= 33:
                valor = 305.55
            elif idade <= 38:
                valor = 321.55
            elif idade <= 43:
                valor = 360.96
            elif idade <= 48:
                valor = 441.34
            elif idade <= 53:
                valor = 612.02
            elif idade <= 58:
                valor = 824.93
            else:
                valor = 1071.30
        elif plano == 'ambulatorial (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 117.31
            elif idade <= 23:
                valor = 154.00
            elif idade <= 28:
                valor = 175.34
            elif idade <= 33:
                valor = 195.42
            elif idade <= 38:
                valor = 205.58
            elif idade <= 43:
                valor = 230.61
            elif idade <= 48:
                valor = 281.66
            elif idade <= 53:
                valor = 390.06
            elif idade <= 58:
                valor = 525.28
            else:
                valor = 681.75
        elif plano == 'enfermaria (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 218.82
            elif idade <= 23:
                valor = 281.29
            elif idade <= 28:
                valor = 319.95
            elif idade <= 33:
                valor = 355.51
            elif idade <= 38:
                valor = 372.11
            elif idade <= 43:
                valor = 417.42
            elif idade <= 48:
                valor = 504.06
            elif idade <= 53:
                valor = 686.64
            elif idade <= 58:
                valor = 918.71
            else:
                valor = 1187.25
        elif plano == 'enfermaria (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 179.77
            elif idade <= 23:
                valor = 229.75
            elif idade <= 28:
                valor = 260.67
            elif idade <= 33:
                valor = 289.12
            elif idade <= 38:
                valor = 302.40
            elif idade <= 43:
                valor = 338.65
            elif idade <= 48:
                valor = 371.96
            elif idade <= 53:
                valor = 554.02
            elif idade <= 58:
                valor = 739.67
            else:
                valor = 954.49
        elif plano == 'apartamento (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 316.44
            elif idade <= 23:
                valor = 410.15
            elif idade <= 28:
                valor = 468.13
            elif idade <= 33:
                valor = 521.47
            elif idade <= 38:
                valor = 546.36
            elif idade <= 43:
                valor = 614.32
            elif idade <= 48:
                valor = 744.28
            elif idade <= 53:
                valor = 1018.14
            elif idade <= 58:
                valor = 1366.23
            else:
                valor = 1769.02
        elif plano == 'apartamento (pessoa física) - Coparticipação total':
            if idade <= 18:
                valor = 257.86
            elif idade <= 23:
                valor = 332.83
            elif idade <= 28:
                valor = 379.22
            elif idade <= 33:
                valor = 421.90
            elif idade <= 38:
                valor = 441.82
            elif idade <= 43:
                valor = 496.19
            elif idade <= 48:
                valor = 600.16
            elif idade <= 53:
                valor = 819.26
            elif idade <= 58:
                valor = 1097.74
            else:
                valor = 1419.99
        elif plano == 'Mix enfermaria (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 527.01
            elif idade <= 23:
                valor = 688.10
            elif idade <= 28:
                valor = 787.78
            elif idade <= 33:
                valor = 879.48
            elif idade <= 38:
                valor = 922.27
            elif idade <= 43:
                valor = 1039.10
            elif idade <= 48:
                valor = 1262.51
            elif idade <= 53:
                valor = 1733.30
            elif idade <= 58:
                valor = 2331.70
            else:
                valor = 0
        elif plano == 'Mix apartamento (pessoa física) - Coparticipação parcial':
            if idade <= 18:
                valor = 778.74
            elif idade <= 23:
                valor = 1020.39
            elif idade <= 28:
                valor = 1169.91
            elif idade <= 33:
                valor = 1307.47
            elif idade <= 38:
                valor = 1371.66
            elif idade <= 43:
                valor = 1546.91
            elif idade <= 48:
                valor = 1882.04
            elif idade <= 53:
                valor = 2588.25
            elif idade <= 58:
                valor = 3485.88
            else:
                valor = 0
        
        elif plano == 'ambulatorial (pessoa jurídica) - Coparticipação parcial':
            if idade <= 18:
                valor = 130.03
            elif idade <= 23:
                valor = 145.63
            elif idade <= 28:
                valor = 163.11
            elif idade <= 33:
                valor = 187.58
            elif idade <= 38:
                valor = 215.72
            elif idade <= 43:
                valor = 256.71
            elif idade <= 48:
                valor = 320.89
            elif idade <= 53:
                valor = 401.11
            elif idade <= 58:
                valor = 681.89
            else:
                valor = 763.72
        elif plano == 'ambulatorial (pessoa jurídica) - Coparticipação total':
            if idade <= 18:
                valor = 96.03
            elif idade <= 23:
                valor = 107.55
            elif idade <= 28:
                valor = 120.46
            elif idade <= 33:
                valor = 138.53
            elif idade <= 38:
                valor = 159.31
            elif idade <= 43:
                valor = 189.58
            elif idade <= 48:
                valor = 236.98
            elif idade <= 53:
                valor = 296.23
            elif idade <= 58:
                valor = 503.59
            else:
                valor = 564.02
        elif plano == 'enfermaria (pessoa jurídica) - Coparticipação parcial':
            if idade <= 18:
                valor = 175.39
            elif idade <= 23:
                valor = 196.44
            elif idade <= 28:
                valor = 220.01
            elif idade <= 33:
                valor = 253.01
            elif idade <= 38:
                valor = 290.96
            elif idade <= 43:
                valor = 346.24
            elif idade <= 48:
                valor = 432.80
            elif idade <= 53:
                valor = 541.00
            elif idade <= 58:
                valor = 919.70
            else:
                valor = 1030.06
        elif plano == 'enfermaria (pessoa jurídica) - Coparticipação total':
            if idade <= 18:
                valor = 137.08
            elif idade <= 23:
                valor = 153.53
            elif idade <= 28:
                valor = 171.95
            elif idade <= 33:
                valor = 197.74
            elif idade <= 38:
                valor = 227.40
            elif idade <= 43:
                valor = 270.61
            elif idade <= 48:
                valor = 338.26
            elif idade <= 53:
                valor = 422.83
            elif idade <= 58:
                valor = 718.81
            else:
                valor = 805.07
        elif plano == 'apartamento (pessoa jurídica) - Coparticipação parcial':
            if idade <= 18:
                valor = 262.33
            elif idade <= 23:
                valor = 293.81
            elif idade <= 28:
                valor = 329.07
            elif idade <= 33:
                valor = 378.43
            elif idade <= 38:
                valor = 435.19
            elif idade <= 43:
                valor = 517.88
            elif idade <= 48:
                valor = 647.35
            elif idade <= 53:
                valor = 809.19
            elif idade <= 58:
                valor = 1375.62
            else:
                valor = 1540.69
        elif plano == 'apartamento (pessoa jurídica) - Coparticipação total':
            if idade <= 18:
                valor = 204.86
            elif idade <= 23:
                valor = 229.44
            elif idade <= 28:
                valor = 256.97
            elif idade <= 33:
                valor = 295.52
            elif idade <= 38:
                valor = 339.85
            elif idade <= 43:
                valor = 404.42
            elif idade <= 48:
                valor = 505.53
            elif idade <= 53:
                valor = 631.91
            elif idade <= 58:
                valor = 1074.25
            else:
                valor = 1203.16
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
