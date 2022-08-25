import csv
with open('films.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["SN", "Movie", "FirstChar"])
  writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
  writer.writerow([2, "Harry Potter", "Harry Potter"])
  writer.writerow([3, "Charlie's Factory", "Charlie Chaplin"])