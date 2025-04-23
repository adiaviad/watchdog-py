def main():
    print("starting main")
    text=input("enter some text")
    print("writing text to file")
    text=int(text)
    with open("text.txt",'w') as f:
        f.write(str(text))
    print("done")


if __name__=="__main__":
    main()