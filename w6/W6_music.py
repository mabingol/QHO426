import csv

def writing(path):
    with open (path, "w") as music :
        csv_writer = csv.writer(music)
        for i in range(3):
            name = input("Enter your name: ")
            a_name = input("Name of your favourite artist: ")
            genre = input("Enter favourite genre: ")
            csv_writer.writerow([name, a_name, genre])

def reading(path):
    with open(path) as music:
        csv_r = csv.reader(music)
        for line in csv_r:
            for item in line:
                print(item, end = ",")
            print()
          
  reading("tastesofmusic.csv")