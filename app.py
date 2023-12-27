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

        if plano == 'enfermaria (pessoa física)' or plano == 'ambulatorial (pessoa física)':
            if len(idades) >= 2 and not desconto_aplicado:
                valor = valor * 0.95
                desconto_aplicado = True

        if plano == 'enfermaria (pessoa física)':
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
        elif plano == 'ambulatorial (pessoa física)':
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
        elif plano == 'enfermaria (pessoa jurídica)':
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
        elif plano == 'ambulatorial (pessoa jurídica)':
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
