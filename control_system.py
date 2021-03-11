"""Control System Server to respond to device commands."""

import socket
import os
import subprocess
import logging
import board
import digitalio

from http import HttpRequest

logging.basicConfig(level=logging.INFO)

# Server config
host = ''
port = 80

# Device config
led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT


logging.info("Starting deploy control system...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

while True:
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        request = HttpRequest(conn.recv(1024).decode())
        logging.info(f"[terrarium] Request: {request.method} {request.path}")

        if request.method == "GET":
            conn.send("HTTP/1.1 200 OK\n".encode())
            conn.send("Content-Type: text/html\n".encode())
            conn.send("Connection: keep-alive\n".encode())
            conn.send("\n".encode())
            conn.send("You've reached terrarium!".encode())

        if request.method == "POST":
            device = request.device
            state = request.state

            logging.info(f"[terrarium] Received command for {device}: {state}")

            if device == 'led':
                led.value = state == 'on'

            conn.send("HTTP/1.1 200 OK\n\nExecuted".encode())



