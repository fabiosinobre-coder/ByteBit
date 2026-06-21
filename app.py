from flask import Flask
from routes import inventory_bp

app = Flask(__name__)

# Registrando o módulo de rotas na nossa aplicação
app.register_blueprint(inventory_bp)

if __name__ == '__main__':
    # No Cloud Shell, rodamos na porta 8080 (padrão do Web Preview)
    app.run(host='0.0.0.0', port=8080, debug=True)
