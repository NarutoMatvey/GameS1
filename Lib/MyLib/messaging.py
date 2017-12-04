import socket
import pickle


def get_answer(sender):
    data = []
    while True:
        packet = sender.recv(1024)
        if not packet:
            break
        data.append(packet)
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
