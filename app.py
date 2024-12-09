from flask import Flask, request, jsonify

import spacy

app = Flask(__name__)

# Load the spaCy model globally
nlp = spacy.load("en_core_web_trf")

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy"), 200

@app.route('/process', methods=['POST'])
def process_string():
    # Get the input string from the request
    input_data = request.json.get('input_string', '')
    
    # Peform NER on the string
    doc = nlp(input_data)
    org_entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    result = org_entities
    
    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
