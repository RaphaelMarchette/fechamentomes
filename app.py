import os
from database.carregador import carregar_dados
from flask import Flask, render_template
from database.classes import Grupo
from website.controllers import website_bp


app = Flask(__name__)
app.secret_key = 'SEGREDO-TOTAL'

app.register_blueprint(website_bp)


@app.context_processor
def listar_grupos():
    return dict(grupos_menu=Grupo.listar())

carregar_dados(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
            'database'
        )
    )

if __name__ == "__main__":
    app.run(debug=True)
    