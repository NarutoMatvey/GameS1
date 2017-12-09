from Class_Socket.Server_socket import Server
import Game_board

socket = Server("127.0.0.1", 7000)

conn_index_player1 = socket.accepts()
conn_index_player2 = socket.accepts()
socket.send('Белый', conn_index_player1)
socket.send('Чёрный', conn_index_player2)

border = Game_board.Game_board()
print("DOSKA")
socket.send(border.board, conn_index_player1)
socket.send(border.board, conn_index_player2)

print(socket.recv(conn_index_player1))
print(socket.recv(conn_index_player2))

player1 = conn_index_player1
player2 = conn_index_player2

while True:
    socket.send('Ваш ход', player1)
    socket.send('Не ваш ход', player2)
    while True:
        respons = socket.recv(player1).split(' ')
        line_item, new_line_item = respons[0], respons[1]
        inform_check = border.check_course(line_item, new_line_item)
        if "успешно" in inform_check:
            socket.send(inform_check, player1)
            respons = [socket.recv(player1), respons[0], respons[1]]
            socket.send(','.join(respons), player2)
            respons = socket.recv(player2)
            print(respons)
            player1, player2 = player2, player1
            break
        elif "Мат" in inform_check:
            socket.send(inform_check, player1)
            respons = [socket.recv(player1), respons[0], respons[1]]
            socket.send(','.join(respons), player2)
            socket.send('Победа', player1)
            socket.send('Проигрыш', player2)
            break
        else:
            socket.send(inform_check, player1, True)

    if "Мат" in inform_check:
        break