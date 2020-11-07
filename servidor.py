import socket
from _thread import start_new_thread

points = list()
clientes = list()


def init_server():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 55000
    thread_count = 0

    try:
        socket_server.bind((host, port))
    except socket.error as e:
        print(str(e))
    else:
        print('Waiting for a connection...')
        socket_server.listen(5)

        while True:
            client, address = socket_server.accept()
            print('Connected to: ', address)
            start_new_thread(threaded_client, (client, ))
            thread_count += 1
            print('Thread number: ', thread_count)
        socket_server.close()


def threaded_client(connection):
    while True:
        try:
            data = connection.recv(1024)
        except socket.error as e:
            print(str(e))
            break
        else:
            if connection not in clientes:
                clientes.append(connection)
            info = data.decode('ascii')
            points.append(info)
            print(points)
            for c in clientes:
                c.sendall(str(points).encode('ascii'))
    connection.close()


init_server()
