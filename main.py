from flask import Flask, request, jsonify
from suggest_activity import get_activity_advice_as_json

app = Flask(__name__)

if __name__ == "__app__":
    app.run(debug=True)

@app.route("/activity_advice", methods = ["POST"])
def get_activity_advice():
    
    if "index_area" not in request.form:
        return jsonify({"error": "No index area found in POST request."}), 400
    
    index_area = request.form["index_area"]

    if "index_question" not in request.form:
        return jsonify({"error": "No index question found in POST request."}), 400
    index_question = request.form["index_question"]

    text = get_activity_advice_as_json(index_area, index_question)

    return text
