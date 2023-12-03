import requests

base_url = "http://localhost:5000"

def send_message(receiver, message):
    url = f"{base_url}/send"
    data = {"receiver": receiver, "message": message}
    response = requests.post(url, json=data)
    return response.json()

def receive_messages(username):
    url = f"{base_url}/receive/{username}"
    response = requests.get(url)
    return response.json()

print("Sending messages...")
send_message("alice", "Hello Alice! 1")
send_message("bob", "Hello Bob! 1")

print("\nAlice's messages:")
print(receive_messages("alice"))

print("\nBob's messages:")
print(receive_messages("bob"))
