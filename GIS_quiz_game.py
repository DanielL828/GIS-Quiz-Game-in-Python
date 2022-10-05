print("Welcome to my computer game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :)")
score = 0

answer = input("What does GIS stand for? ")
if answer.lower() == "geographic information system":
    print('Correct, Good Job!')
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does shp stand for? ")
if answer.lower() == "shapefile":
    print('Correct, Good Job!')
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What is ArcGIS Pro? ")
if answer.lower() == "gis software":
    print('Correct, Good Job!')
    score += 1
else:
    print("Incorrect! Try again.")

answer = input("What does CRS stand for? ")
if answer.lower() == "coordinate reference system":
    print('Correct, Good Job!')
    score += 1
else:
    print("Incorrect! Try again.")

print("You got " + str(score) + " Questions Correct!")
print("You got " + str((score / 4) * 100) + "%.")
