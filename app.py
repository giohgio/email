from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
CORS(app)  # permite requisições do frontend em outra porta

# Configurações
PP_PASSWORD = os.getenv("PP_PASSWORD", "kzgk szfq brzm nbqm")  # senha do app Gmail
DEST_EMAIL = "instagramcomentarysuportemetas@gmail.com"

@app.route("/enviado", methods=["POST"])
def enviado():
    data = request.get_json(force=True)
    if not data or "email" not in data or "comentario" not in data:
        return jsonify({"error": "Campos obrigatórios!"}), 400

    email = data["email"]
    comentario = data["comentario"]

    try:
        # Criação do e-mail
        msg = MIMEMultipart()
        msg["From"] = DEST_EMAIL
        msg["To"] = DEST_EMAIL
        msg["Subject"] = "Novo comentário recebido"
        msg.attach(MIMEText(f"Email/Nome: {email}\nComentário: {comentario}", "plain"))

        # Envio via SMTP Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(DEST_EMAIL, PP_PASSWORD)
        server.send_message(msg)
        server.quit()

        return jsonify({"message": "Comentário enviado com sucesso!"}), 200

    except Exception as e:
        print("Erro enviando email:", e)
        return jsonify({"error": "Falha ao enviar e-mail", "detail": str(e)}), 500

if __name__ == "__main__":
    # Roda acessível na rede local, porta 3000
    app.run(host="0.0.0.0", port=3000, debug=True)
