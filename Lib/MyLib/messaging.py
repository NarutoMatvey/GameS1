import socket
import pickle


def get_answer(sender):
    data = []
    waiting_ratio = 0
    while True:
        try:
            packet = sender.recv(1024)
            data.append(packet)
        except socket.error:
            if data == [] and waiting_ratio < 5:
                sender.setblocking(60)
                waiting_ratio += 1
                continue
            else:
                break
        sender.setblocking(0)
    response = pickle.loads(b"".join(data))
    return response


def send_message(recipient, massage, error=False):
    packet = {}
    if error:
        packet['error'] = massage
    else:
        packet['data'] = massage

    response = pickle.dumps(packet)
    recipient.send(response)
