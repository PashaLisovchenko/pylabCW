import socketserver


class MyHandler(socketserver.StreamRequestHandler):
                            # BaseRequestHandler

    def handle(self):
        print('connected: ', self.request,
              '\nclient_address: ', self.client_address)
        data = self.rfile.readline()
        # data = self.request.recv(1024)
        self.wfile.write(data.upper())
        # self.request.sendall(data.upper())


class Server(socketserver.ThreadingMixIn,
             socketserver.TCPServer):
    pass


if __name__ == "__main__":
    server = Server(('localhost', 50000), MyHandler)
    server.serve_forever()
