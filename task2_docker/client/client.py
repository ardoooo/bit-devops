import requests

server_url = "http://server:5000"

def store_data(server_url, text):
    response = requests.post(f"{server_url}/store", data=text)
    return response.json()

def retrieve_data(server_url, data_id):
    response = requests.get(f"{server_url}/retrieve/{data_id}")
    return response.text

print("Commands:")
print("STORE <text>")
print("RETRIEVE <data_id>")
print("EXIT")
print("====================")

while True:
    user_input = input("Enter command: ").split(" ", 1)
    command = user_input[0].upper()

    if command == "STORE" and len(user_input) > 1:
        input_text = user_input[1]
        data_id = store_data(server_url, input_text)["id"]
        print(f"Data ID: {data_id}")
    elif command == "RETRIEVE" and len(user_input) > 1:
        data_id = user_input[1]
        retrieved_text = retrieve_data(server_url, data_id)
        print(f"Retrieved: {retrieved_text}")
    elif command == "EXIT":
        break
    else:
        print("Invalid command. Please try again.")
