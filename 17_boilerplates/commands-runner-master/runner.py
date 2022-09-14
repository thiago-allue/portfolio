import subprocess
import yaml


def log(*args):
    print('{}'.format(args))


def read_job():
    with open('job.yaml') as f:
        job = yaml.load(f.read())
    return job


def example1():

    job = read_job()

    # config
    shell_flag = job.get('shell', True)
    timeout = job.get('timeout', 5)

    # Run commands
    for cmd in job.get('commands', []):
        log(cmd)
        res = subprocess.call(cmd, timeout=timeout, shell=shell_flag)
        log(res)


def example2():

    job = read_job()

    # config
    shell_flag = job.get('shell', True)
    timeout = job.get('timeout', 5)

    # Run commands
    for cmd in job.get('commands', []):
        log(cmd)
        cmds_params = cmd.split()
        print(cmds_params)
        res = subprocess.check_output(cmd, timeout=timeout, shell=shell_flag)
        print(res.decode('utf-8'))


def example3():
    # Recommended approach in Python 3.5+ ?
    from subprocess import PIPE, run
    job = read_job()

    # config
    shell_flag = job.get('shell', True)
    timeout = job.get('timeout', 5)

    # Run commands
    for cmd in job.get('commands', []):
        log(cmd)
        result = run(cmd, 
                    stdout=PIPE, 
                    stderr=PIPE, 
                    universal_newlines=True, 
                    shell=shell_flag,
                    timeout=timeout)
        print(result.returncode, result.stdout, result.stderr)

def main():
    example3()


if __name__ == '__main__':
    main()
