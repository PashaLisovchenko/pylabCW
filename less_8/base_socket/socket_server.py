import socket

with socket.socket(socket.AF_INET,
                   socket.SOCK_STREAM) as s:
    s.bind(('localhost', 50000))
    # количество слушателей
    s.listen(1)
    # ждет клиента
    conn, addr = s.accept()
    with conn:
        print('connected', addr)
        while True:
            # максимальное количестно байт
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
