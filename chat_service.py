from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

messages = defaultdict(list)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    receiver = data['receiver']
    message = data['message']
    messages[receiver].append(message)
    return jsonify({"status": "Message sent"}), 200

@app.route('/receive/<username>', methods=['GET'])
def receive_messages(username):
    user_messages = messages[username]
    return jsonify({"messages": user_messages}), 200

if __name__ == '__main__':
    app.run(debug=True)
