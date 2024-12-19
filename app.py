from flask import Flask, request, jsonify

import spacy

def load_spacy_model():
  global nlp
  nlp = spacy.load("en_core_web_lg")

# Load the model before creating the app
load_spacy_model()

# Create the Flask app.
app = Flask(__name__)

# Define the health check endpoint; this was added for future deployment to AWS App Runner.
@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy"), 200

# Define the NER service endpoint.
@app.route('/process', methods=['POST'])
def process_string():
    # Get the input string from the request
    input_data = request.json.get('input_string', '')
    
    # Peform NER on the string
    doc = nlp(input_data)

    # Extract the ORG entities from the document.
    org_entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    result = org_entities
    
    # Return the result as JSON.
    return jsonify(result)

# Run the app.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
