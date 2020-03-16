import socket
from concurrent import futures

def check_port(targetIp, portNumber, timeout):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(timeout)
    try:
        TCPsock.connect((targetIp, portNumber))
        return (portNumber)
    except:
        return

def port_scanner(targetIp, timeout):
    threadPoolSize = 500
    portsToCheck = 10000

    executor = futures.ThreadPoolExecutor(max_workers=threadPoolSize)
    checks = [
        executor.submit(check_port, targetIp, port, timeout)
        for port in range(0, portsToCheck, 1)
    ]

    for response in futures.as_completed(checks):
        if (response.result()):
            print('Listening on port: {}'.format(response.result()))

def main():
    targetIp = input("Enter the target IP address: ")
    timeout = int(input("How long before the connection times out: "))
    port_scanner(targetIp, timeout)

if __name__ == "__main__":
    main()
