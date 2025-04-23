import time


def main():
    print("starting main")
    i=0
    while True:
        time.sleep(0.01)
        i+=1
        if i==1001:
            raise Exception("i too high")
    print("i=",i)
    print("done")


if __name__=="__main__":
    main()