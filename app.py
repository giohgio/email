from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook_listener():
    if request.method == 'GET':
        return jsonify({'status': 'ok'}), 200

    # POST
    data = request.json
    print("Webhook recebido:", data)

    # Valide a origem do webhook (opcional, mas recomendado)
    # Você precisará da assinatura secreta e validar o cabeçalho X-Signature
    # Para mais informações, consulte a documentação do Mercado Pago.

    # Processar os dados da notificação
    if 'type' in data and data['type'] == 'payment':
        if 'data' in data and 'id' in data['data']:
            payment_id = data['data']['id']
            print(f"Detalhes do pagamento: {payment_id}")
            # Adicione sua lógica aqui para processar o pagamento

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
