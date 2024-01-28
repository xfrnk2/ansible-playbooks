import argparse
import time
import os
import paramiko


# 인자 변환 (from pass_vars_to_python_script.yml)

parser = argparse.ArgumentParser()
parser.add_argument('--hostname', help='your hostname')
parser.add_argument('--password', help='your target password')

parser.parse_args()


# SSH 연결 설정

hostname = args.hostname
password = args.password
username = 'root'
port = 22


# SSH 클라이언트 객체 생성
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
paramiko.util.log_to_file('mylog.log')


# SSH 연결
ssh.connect(hostname, port, username, password, look_for_keys=False)
channel = ssh.invoke_shell()
time.sleep(1)

# 명령어 실행
commands = [
    'echo "Command 1"',
    'echo "Command 2"',
    'echo "Command 3"'
]

for command in commands:
    channel.send(command)
    time.sleep(1)
    response = channel.recv(9999)
    output = response.decode('ascii').split(',')

    # 명령어 실행 결과 출력
    print(f"Command: {command}")
    print("Output: ", ''.join(output))
    

# SSH 연결 종료
ssh.close()
