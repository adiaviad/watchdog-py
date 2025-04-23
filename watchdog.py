import subprocess
import time


def startWatchdog(args,maxTimeWithoutResponseSec):
    process=subprocess.Popen(args=args)
    while True:
        time.sleep(maxTimeWithoutResponseSec)
        if process.poll() is not None:
            print("killing subprocess")
            process.kill()
            outs, errs= process.communicate()
            print("subprocess stdout:", outs)
            print("subprocess error(s):", errs)
            process = subprocess.Popen(args=args)

def main():
    args=["python", "main.py"]
    startWatchdog(args,30)

if __name__=="__main__":
    main()