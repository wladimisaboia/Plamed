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

        if plano == 'PLAMED EXCLUSIVE Enf CCO' or plano == 'MAIS VOCÊ' or plano == 'PLAMED GOLD I CO-PARTICIPAÇÃO (ENFERMARIA)' or plano == 'PLAMED GOLD II CO-PARTICIPAÇÃO (APARTAMENTO)' :
            if len(idades) >= 2 and not desconto_aplicado:
                valor = valor * 0.95
                desconto_aplicado = True

        if plano == 'PLAMED EXCLUSIVE Enf CCO':
            if idade <= 18:
                valor = 177.86
            elif idade <= 23:
                valor = 233.59
            elif idade <= 28:
                valor = 268.08
            elif idade <= 33:
                valor = 299.80
            elif idade <= 38:
                valor = 314.60
            elif idade <= 43:
                valor = 355.02
            elif idade <= 48:
                valor = 432.31
            elif idade <= 53:
                valor = 595.17
            elif idade <= 58:
                valor = 802.19
            else:
                valor = 989.65
        elif plano == 'MAIS VOCÊ':
            if idade <= 18:
                valor = 233.54
            elif idade <= 23:
                valor = 268.57
            elif idade <= 28:
                valor = 319.60
            elif idade <= 33:
                valor = 367.54
            elif idade <= 38:
                valor = 393.27
            elif idade <= 43:
                valor = 456.18
            elif idade <= 48:
                valor = 574.80
            elif idade <= 53:
                valor = 735.75
            elif idade <= 58:
                valor = 985.89
            else:
                valor = 1350.71
        elif plano == 'PLAMED GOLD I CO-PARTICIPAÇÃO (ENFERMARIA)':
            if idade <= 18:
                valor = 331.78
            elif idade <= 23:
                valor = 381.54
            elif idade <= 28:
                valor = 454.02
            elif idade <= 33:
                valor = 522.15
            elif idade <= 38:
                valor = 558.72
            elif idade <= 43:
                valor = 648.07
            elif idade <= 48:
                valor = 816.58
            elif idade <= 53:
                valor = 1045.21
            elif idade <= 58:
                valor = 1400.57
            else:
                valor = 1918.96
        elif plano == 'PLAMED GOLD II CO-PARTICIPAÇÃO (APARTAMENTO)':
            if idade <= 18:
                valor = 447.88
            elif idade <= 23:
                valor = 515.05
            elif idade <= 28:
                valor = 612.94
            elif idade <= 33:
                valor = 704.87
            elif idade <= 38:
                valor = 754.22
            elif idade <= 43:
                valor = 874.86
            elif idade <= 48:
                valor = 1102.38
            elif idade <= 53:
                valor = 1411.00
            elif idade <= 58:
                valor = 1890.73
            else:
                valor = 2590.35
        elif plano == 'EMPRESARIAL PREFERENCIAL I CECM CP':
            if idade <= 18:
                valor = 160.56
            elif idade <= 23:
                valor = 210.86
            elif idade <= 28:
                valor = 241.99
            elif idade <= 33:
                valor = 270.63
            elif idade <= 38:
                valor = 283.99
            elif idade <= 43:
                valor = 320.46
            elif idade <= 48:
                valor = 390.24
            elif idade <= 53:
                valor = 537.25
            elif idade <= 58:
                valor = 724.13
            else:
                valor = 893.34
        elif plano == 'EMPRESARIAL BASICO SERGIPE II CP (ENFERMARIA)':
            if idade <= 18:
                valor = 200.10
            elif idade <= 23:
                valor = 230.12
            elif idade <= 28:
                valor = 273.83
            elif idade <= 33:
                valor = 314.91
            elif idade <= 38:
                valor = 336.96
            elif idade <= 43:
                valor = 390.86
            elif idade <= 48:
                valor = 492.49
            elif idade <= 53:
                valor = 630.39
            elif idade <= 58:
                valor = 844.72
            else:
                valor = 1157.29
        elif plano == 'EMPRESARIAL ESPECIAL SERGIPE II (APARTAMENTO)':
            if idade <= 18:
                valor = 220.11
            elif idade <= 23:
                valor = 253.13
            elif idade <= 28:
                valor = 301.22
            elif idade <= 33:
                valor = 346.40
            elif idade <= 38:
                valor = 370.65
            elif idade <= 43:
                valor = 429.94
            elif idade <= 48:
                valor = 541.74
            elif idade <= 53:
                valor = 693.43
            elif idade <= 58:
                valor = 929.19
            else:
                valor = 1273.02
        elif plano == 'EMPRESARIAL GOLD I (ENFERMARIA)':
            if idade <= 18:
                valor = 299.43
            elif idade <= 23:
                valor = 344.34
            elif idade <= 28:
                valor = 409.75
            elif idade <= 33:
                valor = 471.24
            elif idade <= 38:
                valor = 504.24
            elif idade <= 43:
                valor = 584.88
            elif idade <= 48:
                valor = 736.96
            elif idade <= 53:
                valor = 943.30
            elif idade <= 58:
                valor = 1264.02
            else:
                valor = 1731.86
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
