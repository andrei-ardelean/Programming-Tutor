import subprocess

if __name__ == '__main__':
    # modify line 3 in test.py: e.g. implementation -> c1
    try:
        r = subprocess.run(['python', 'test.py'], timeout=1)
    except subprocess.TimeoutExpired as e:
        print(e)
