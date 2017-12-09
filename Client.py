from Class_Socket.Client_socket import Client

player = Client("127.0.0.1", 7000)
print(player.player)  # Либо белые либо чёрные

player.send('Готов')

while True:
    player.view_board(player.player)
    whose_move = player.recv()
    if whose_move['data'] == 'Ваш ход':
        while 1:
            while 1:
                line_item = input("Введите клетку с которой будите ходить: ")
                if player.board[line_item] == 0:
                    print('Вы не выбрали фигуру')
                    continue
                elif player.board[line_item].color != player.player:
                    print('В этой клетки стоит не ваша фигура!')
                    continue
                break
            new_line_item = input("Введите клетку в которую будите ходить: ")
            massage = line_item + ' ' + new_line_item
            player.send(massage)
            permission_to_move = player.recv()
            if 'error' in permission_to_move:
                print('Ошибка: ' + permission_to_move['error'])
                continue
            else:
                print(permission_to_move['data'])
            player.update_boarder(line_item, new_line_item)
            player.send('Передаю ход')
            break
    elif whose_move == 'Победа':
        print("Ты победил!")
        player.send('Спасибо за игру!')
        break
    elif whose_move == 'Проигрыш':
        print("Ты проиграл!")
        player.send('Спасибо за игру!')
        break
    else:
        end_move = player.recv()
        end_move = end_move['data'].split(',')
        end_move, line_item, new_line_item = end_move[0], end_move[1], end_move[2]
        print(end_move)
        player.update_boarder(line_item, new_line_item)
        player.send('Спасибо')
end_end = player.recv()
print(end_move['data'])
del player
