def lines():
    f = open("data.txt", "w")
    while True:
        string = input()
        if string == "":
            f.closed
            break
        else:
            f.write(string + "\n")

            
#lines()


def readfile():
    with open("data.txt", "r") as f:
        for index, line in enumerate(f):
            print(f"{index+1} {line}")


#readfile()


def Spliting():
    lines = []
    counter = 0 #считает количество созданных файлов
    maxlines = int(input("Введите максимальное количество строк: "))
    with open ("data.txt", "r") as f:
        for line in f:
            lines.append(line)

            if len(lines) >= maxlines:
                counter += 1
                outfile = f"{str(counter)}.txt"
                with open(outfile, "w") as out_file:
                    out_file.writelines(lines)
                lines = []
        if lines:
            counter += 1
            outfile = f"{str(counter)}.txt"
            with open(outfile, "w") as output:
                output.writelines(lines)

#Spliting()


def unification():
    lines = []
    i = int(input("Введите количество файлов для объединения: "))
    for n in range(1, i+1):
        with open(f"{n}.txt", "r") as f:
            for line in f:
                lines.append(line)
    newfile = f"{input("Введите название нового файла: ")}.txt"
    with open(newfile, "w") as f:
        f.writelines(lines)

unification()

def firstlines():
    n = int(input("Введите желаемое количество строк: "))
    counter = 0
    with open("data.txt", "r") as f:
        for line in f:
            if(counter < n):
                print(f"{line}")
                counter+= 1

                
#firstlines()

def lastlines():
    n = int(input("Введите желаемое количество строк: "))
    counter = 0
    lines = []
    with open("data.txt", "r") as f:
        for line in f:
            lines.append(line)
    for line in range(len(lines)-1, 0, -1):
                if(counter < n):
                    print(f"{lines[line]}")
                    counter += 1



#lastlines()



