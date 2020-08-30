import subprocess as sb

def print_whoami():
    sb.check_output('whoami')


if __name__ == "__main__":
    print(print_whoami())