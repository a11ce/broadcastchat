import socket as sk
from threading import Thread


def rcv(pNum):
    inSk = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    inSk.bind(('', pNum))
    while True:
        print(inSk.recvfrom(1024)[0].decode("utf-8"), end="\n> ")


def main():

    cs = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    cs.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
    cs.setsockopt(sk.SOL_SOCKET, sk.SO_BROADCAST, 1)

    print(
        "Welcome to BChat.\nIf you're using a custom room number, enter it now. Otherwise, just press enter."
    )
    try:
        pNum = int(input("> "))
    except:
        pNum = 1224
    thread = Thread(target=rcv, args=(pNum, ))
    thread.start()
    nick = input("Username?\n> ")
    print("Connected to room " + ("default" if pNum == 1224 else str(pNum)) +
          " as " + nick + ".\n> ",
          end="")
    while True:
        inp = input()
        msg = nick + ": " + inp
        cs.sendto(msg.encode(), ('255.255.255.255', pNum))
    print("Bye!")


if __name__ == "__main__":
    main()
