from flask import Flask, jsonify

# Create the Flask app.
app = Flask(__name__)

# Define the health check endpoint; this was added for future deployment to AWS App Runner.
@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy"), 200

# Run the app.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
