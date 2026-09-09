import socket

# параметры сервера
ip = '127.0.0.1'
port = 9001
endpoint = (ip, port)
# Сокет сервера
server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(endpoint)
server.listen(10)

#Режим ожидания запросов
print(f'Сервер запущен на IP: {ip} PORT: {port}')
print('Ожидание запросов...')
connection, address = server.accept()
# обмен данными с клиентом
try:
    print(f'Установлено соединение с клиентом {address}')
    while True:
        client_message = connection.recv(1024).decode(encoding='utf-8')
        if client_message == 'stop_server' or not client_message:
            break
        print(f'Сообщение от клиента: [{client_message}]')
        # отправляем сообщение клиенту
        server_message = input('Сообщение клиенту: ')
        connection.send(server_message.encode(encoding='utf-8'))
        print('Сообщение отправлено')
except BaseException as err:
    print(err)
finally:
    connection.close()
    print('Сервер остановлен')


