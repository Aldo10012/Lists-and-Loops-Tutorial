# Question 1
songs = ["ROCKSTAR", "Do It", "For The Night"]

# Question 2
print( songs[0] )                   # printing first element
print( songs[2] )                   # printing last element
print( songs[1:3] )

# Question 3
songs[2] = "Battle Symphony"
print(songs)

# Question 4
songs.append("Old Town Road")
songs.append("Foot Loose")
songs.append("Honey I'm Good")
del songs[1]

# Question 5
# the two loop methods basically do the same thing. 

# Question 6
animals = ['lion', 'tiger', 'panther']
animals.append('bob cat')
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)
