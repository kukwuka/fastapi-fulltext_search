import csv




with open("./posts.csv" , 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    gen = (i for i in csv_reader)
    next(gen)

    for line in gen:
        text = line[0]
        date = line[1]
        rubrics = line[2]
        print (text)
        print(date)
        print(rubrics)






