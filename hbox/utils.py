import os
import platform
import subprocess
import sys
import threading


def reader(pipe, func):
    for line in iter(pipe.readline, b''):
        func(line.decode())
    pipe.close()


def execute_command(command, can_be_interactive: bool = False):
    stdin_data = None

    if can_be_interactive:
        if not sys.stdin.isatty():
            stdin_data = sys.stdin.read()

        if stdin_data:
            command.insert(2, "-i")
        else:
            command.insert(2, "-it")
            is_windows = platform.system().lower() == "windows"
            is_git_bash = bool(os.getenv('MSYSTEM'))
            if is_windows and is_git_bash:
                command.insert(0, "winpty")

    if not can_be_interactive or stdin_data:
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
    else:
        process = subprocess.Popen(command, shell=True)

    try:
        return_code = process.wait()
    except KeyboardInterrupt as e:
        return -1
    else:
        return return_code


def resolve_path(path):
    return os.path.abspath(os.path.expanduser(path))
