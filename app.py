from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
 {
    "ano": 2013,
    "genero": "Ação",
    "id": 1,
    "plataforma": "PC",
    "titulo": "Grand Theft Auto V"
},
{
    "ano": 2015,
    "genero": "Aventura",
    "id": 2,
    "plataforma": "PC",
    "titulo": "The Witcher 3"
},
{
    "ano": 2011,
    "genero": "RPG",
    "id": 3,
    "plataforma": "PC",
    "titulo": "The Elder Scrolls V: Skyrim"
},
{
    "ano": 2018,
    "genero": "Ação e Aventura",
    "id": 4,
    "plataforma": "PC",
    "titulo": "God of War"
}
]

@app.route('/api/jogos', methods=['GET'])
def get_jogos():
    return jsonify(jogos)
    
@app.route('/api/jogos/<int:id>', methods=['GET'])
def buscar_jogos(id):
    jogos = next((j for j in jogos if jogos["id"] == id), None)
    if not jogos:

        return jsonify({"error": "Jogo não encontrado"}), 404

        return jsonify(jogos)

@app.route('/api/jogos', methods=['POST'])
def criar_jogos():
    dados = request.get_json()
    novo_jogo = {
        "id": len(jogos) + 1,
        "titulo": dados["titulo"],
        "genero": dados["genero"],
        "plataforma": dados["plataforma"],
        "ano": dados["ano"]
    }
    jogos.append(novo_jogo)
    return jsonify(novo_jogo), 201

@app.route('/api/Jogos/<int:id>', methods=['PUT'])
def update_jogos(id):
    jogos = next((j for j in jogos if jogos["id"] == id), None)
    if jogos:
        dados = request.get_json()
        jogos["titulo"] = dados.get("titulo", jogos["titulo"])
        jogos["genero"] = dados.get("genero", jogos["genero"])
        jogos["plataforma"] = dados.get("plataforma", jogos["plataforma"])
        jogos["ano"] = dados.get("ano", jogos["ano"])
       
        return jsonify(jogos)

@app.route('/api/jogos/<int:id>', methods=['DELETE'])
def delete_jogos(id):
    global jogos
    jogos = next((j for j in jogos if j["id"] == id), None)
    if not jogos:
        return jsonify({"error": "Jogo não encontrado"}), 404
           
    jogos= [j for j in jogos if jogos["id"] != id]
    return jsonify({"message": "jogo deletado com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)

