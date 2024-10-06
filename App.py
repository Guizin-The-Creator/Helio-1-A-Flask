from flask import Flask, jsonify
from control.HoraController import HoraController

app = Flask("API Hora")

# Função auxiliar para lidar com validações
def handle_validation_error(e):
    return jsonify({"erro": str(e)}), 400

# Endpoint GET: /horas/minutos/<float:horas>
@app.route('/horas/minutos/<float:horas>', methods=['GET'])
def get_horas_para_minutos(horas):
    try:
        horaController = HoraController()
        horaController.hora_converter.horas = horas
        minutos = horaController.converter_horas_para_minutos()
        jsonResposta = {
            "horas": horas,
            "minutos": minutos
        }
        return jsonify(jsonResposta), 200
    except ValueError as e:
        return handle_validation_error(e)

# Inicia o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
