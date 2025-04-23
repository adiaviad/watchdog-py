import subprocess
import time


def startWatchdog(args,maxTimeWithoutResponseSec):
    process=subprocess.Popen(args=args)
    while True:
        time.sleep(maxTimeWithoutResponseSec)
        if process.poll() is not None:
            print("watchdog not fed. killing subprocess")
            process.kill()
            outs, errs= process.communicate()
            print("subprocess stdout:", outs)
            print("subprocess error(s):", errs)
            process = subprocess.Popen(args=args)
        else:
            print("watchdog fed")

def main():
    args=["python", "main.py"]
    startWatchdog(args,1)

if __name__=="__main__":
    main()