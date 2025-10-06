from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_listener():
    # Obtenha os dados enviados pelo Mercado Pago
    data = request.json
    print("Webhook recebido:", data)

    # Valide a origem do webhook (opcional, mas recomendado)
    # Você precisará da assinatura secreta e validar o cabeçalho X-Signature
    # Para mais informações, consulte a documentação do Mercado Pago.

    # Processar os dados da notificação
    # Exemplo: Verificar o status do pagamento e atualizar o status no seu banco de dados
    if 'type' in data and data['type'] == 'payment':
        if 'data' in data and 'id' in data['data']:
            payment_id = data['data']['id']
            # Faça uma requisição à API do Mercado Pago para obter os detalhes do pagamento e confirmar o status
            print(f"Detalhes do pagamento: {payment_id}")
            # Adicione sua lógica aqui para processar o pagamento

    # Responda com um status 200 OK para confirmar o recebimento
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    # Para ambientes de produção, use um servidor WSGI como Gunicorn
    app.run(port=5000)
