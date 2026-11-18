from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # ✅ HABILITA CORS PARA TODOS LOS ORÍGENES
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
EXCEL_NAME = "escalamientos.xlsx"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_excel():
    if "archivo" not in request.files:
        return jsonify({"ok": False, "msg": "No se recibió archivo"}), 400

    file = request.files["archivo"]

    if file.filename == "":
        return jsonify({"ok": False, "msg": "Nombre vacío"}), 400

    save_path = os.path.join(UPLOAD_FOLDER, EXCEL_NAME)

    # ✅ REEMPLAZA EL EXCEL ANTERIOR
    file.save(save_path)

    return jsonify({"ok": True, "msg": "Excel reemplazado correctamente"})

@app.route("/excel")
def get_excel():
    a = send_from_directory(UPLOAD_FOLDER, EXCEL_NAME, as_attachment=False)
    return a
@app.route("/")
def root():
    return "Servidor de Excel activo"

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    app.run(debug=True, port=5000)

