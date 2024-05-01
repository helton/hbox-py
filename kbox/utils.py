import os
import subprocess
import sys
import threading


def reader(pipe, func):
    for line in iter(pipe.readline, b''):
        func(line.decode())
    pipe.close()


def execute_command(command):
    stdin_data = None
    if not sys.stdin.isatty():
        stdin_data = sys.stdin.read()
        if stdin_data:
            # Insert the '-i' option into the command to allow pipe
            command.insert(2, '-i')

    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if stdin_data:
        process.stdin.write(stdin_data.encode())
        process.stdin.close()

    out_thread = threading.Thread(target=reader, args=[process.stdout, sys.stdout.write])
    err_thread = threading.Thread(target=reader, args=[process.stderr, sys.stderr.write])
    out_thread.start()
    err_thread.start()
    out_thread.join()
    err_thread.join()

    process.stdout.close()
    process.stderr.close()
    return_code = process.wait()

    if return_code != 0:
        raise subprocess.CalledProcessError(return_code, command)


def resolve_path(path):
    return os.path.abspath(os.path.expanduser(path))
