def countwordfromfile():
    filename=input("enterthefilename: ")
    f=open(filename,"r")
    word=0
    for line in f : 
        words=line.split()
        word=word+len(words)
    print(word) 
countwordfromfile()