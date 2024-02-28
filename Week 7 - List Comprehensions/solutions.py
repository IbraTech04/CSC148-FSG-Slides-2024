class Song:
  title: str
  _liked: bool
  genre: str
  _explicit: bool
  _popularity: int

  def __init__(self, title: str, liked: bool, genre: str, explicit: bool = False, popularity: int = 0):
    self.title = title
    self._liked = liked
    self.genre = genre
    self._explicit = explicit
    self._popularity = popularity

  def is_liked(self):
    return self._liked

  def is_explicit(self):
    return self._explicit

  def get_popularity(self):
    return self._popularity

  def __str__(self):
    return f'Song("{self.title}", {self._liked}, "{self.genre}", {self._explicit}, {self._popularity}), '

# Example List (Scraped from Spotify)
songs = [Song("Take on Me", False, "Love", False, 90), Song("7 rings", False, "Pop", True, 87), Song("I Kissed A Girl", False, "Pop", False, 74), Song("Get Lucky (feat. Pharrell Williams and Nile Rodgers)", False, "Electro", False, 77), Song("One More Night", False, "Pop", False, 75), Song("Happy - From Despicable Me 2", False, "Dance pop", False, 83), Song("I Gotta Feeling", False, "Dance pop", False, 79), Song("Sugar", False, "Pop", False, 52), Song("INDUSTRY BABY (feat. Jack Harlow)", False, "Lgbtq+ hip hop", True, 81), Song("YESSIR!", True, "Rap", False, 57), Song("Payphone", False, "Pop", True, 71), Song("Shape of You", False, "Pop", False, 89), Song("Roar", False, "Pop", False, 83), Song("Teenage Dream", False, "Pop", False, 78), Song("Where Have You Been", False, "Barbadian pop", False, 56), Song("Last Friday Night (T.G.I.F.)", False, "Pop", False, 79), Song("California Gurls", False, "Pop", False, 77), Song("Good Time", True, "Indietronica", False, 79), Song("Y.M.C.A.", True, "Disco", False, 65), Song("Call Me Maybe", False, "Canadian pop", False, 63), Song("Locked out of Heaven", True, "Dance pop", False, 92), Song("Replay", False, "Dance pop", False, 80), Song("Dynamite", True, "Dance pop", False, 75), Song("Pump It", False, "Dance pop", True, 73), Song("Wake Me Up", False, "Dance pop", False, 89), Song("Radioactive", False, "Modern rock", False, 76), Song("Pompeii", False, "Metropopolis", False, 78), Song("Thunder", False, "Modern rock", False, 89), Song("Shake It Off", False, "Pop", False, 76), Song("Die Young", False, "Dance pop", False, 81), Song("Sound Of Your Heart", False, "Canadian pop", False, 45), Song("Never Change", True, "Rap", True, 54), Song("SO LONG", False, "Rap", True, 55), Song("MVP", True, "Rap", False, 56), Song("Livin' la Vida Loca", True, "Latin pop", False, 78), Song("Demons", False, "Modern rock", False, 78), Song("Best Day Of My Life", False, "Modern rock", False, 83), Song("What Makes You Beautiful", False, "Boy band", False, 87), Song("Beauty And A Beat", False, "Canadian pop", False, 85), Song("Troublemaker (feat. Flo Rida)", True, "Dance pop", False, 79), Song("Shut Up and Dance", False, "Rock", False, 87), Song("Mr. Brightside", False, "Rock", False, 90), Song("Uptown Funk (feat. Bruno Mars)", False, "Pop soul", True, 86), Song("Break Free", False, "Pop", False, 80), Song("I Really Like You", False, "Canadian pop", False, 48), Song("Can't Hold Us (feat. Ray Dalton)", False, "Pop rap", False, 86), Song("Thrift Shop (feat. Wanz)", False, "Pop rap", True, 81), Song("Grenade", False, "Dance pop", False, 83), Song("DJ Got Us Fallin' In Love (feat. Pitbull)", False, "Atl hip hop", False, 86), Song("Problem", False, "Pop", False, 79), Song("Counting Stars", False, "Piano rock", False, 78), Song("Good Feeling", False, "Dance pop", False, 81), Song("The Fox (What Does the Fox Say?)", False, "Comic", False, 67), Song("In the End", False, "Alternative metal", False, 69), Song("My House", False, "Dance pop", False, 80), Song("Like A G6", False, "Asian american hip hop", False, 73), Song("GDFR (feat. Sage the Gemini & Lookas)", False, "Dance pop", False, 76), Song("Hall of Fame (feat. will.i.am)", True, "Celtic rock", False, 84), Song("Firework", False, "Pop", False, 75), Song("TiK ToK", False, "Dance pop", False, 86), Song("Poker Face", False, "Art pop", False, 81), Song("Sunroof", False, "Singer-songwriter pop", False, 23), Song("Dubai Freestyle", True, "Deep underground hip hop", True, 43), Song("Blacklist", True, "Rap", True, 32), Song("Everyday", False, "Conscious hip hop", True, 68), Song("Feel This Moment (feat. Christina Aguilera)", True, "Dance pop", False, 83), Song("City of Angels", True, "Rap", True, 24), Song("Party Rock Anthem", True, "Dance pop", False, 72), Song("Wavin' Flag - Coca-Cola® Celebration Mix", True, "Reggae fusion", False, 68), Song("Titanium (feat. Sia)", True, "Big room", False, 84), Song("Hips Don't Lie (feat. Wyclef Jean)", True, "Colombian pop", False, 88), Song("Break Your Heart", True, "Dance pop", False, 72), Song("Breaking Me", True, "German dance", False, 78), Song("Lose Control", True, "Canadian pop", True, 43), Song("Tonight Tonight", False, "Dance rock", False, 73), Song("Classic", True, "Pop", False, 84), Song("Stereo Hearts (feat. Adam Levine)", False, "Dance pop", False, 83), Song("Cheerleader (Felix Jaehn Remix) - Radio Edit", False, "Reggae fusion", False, 82), Song("Timber (feat. Ke$ha)", False, "Dance pop", False, 86), Song("Hiya Hiya", True, "Classic arab pop", False, 53), Song("Day Ones", True, "Rap", True, 42), Song("I'm Still Standing", True, "Glam rock", False, 88), Song("Sah Sah", True, "Afghan pop", False, 52), Song("Me And My Broken Heart", True, "Post-teen pop", False, 81), Song("Only Girl (In The World)", True, "Barbadian pop", False, 87), Song("Rap God", True, "Detroit hip hop", True, 51), Song("Dangerous Bitch", True, "Rap", True, 53), Song("This and That", True, "Rap", True, 39), Song("Hills", True, "Alberta hip hop", True, 40), Song("Stitches", False, "Canadian pop", False, 79), Song("Stone Cold", True, "Rap", True, 41), Song("Eish'ha B Afia", True, "Arab pop", False, 49), Song("Made 4 This", True, "Alberta hip hop", True, 32), Song("Level Up", True, "Rap", False, 0), Song("In My Feelings", True, "Canadian hip hop", True, 78), Song("Seven Nation Army", True, "Electro Rock", False, 72), Song("Tesla X", True, "Rap", True, 34), Song("Magic in the Air (feat. Ahmed Chawki)", False, "Afropop", False, 72), Song("GTA 2", True, "Rap", False, 50), Song("Pisces", True, "Hip hop", True, 29)]

# Practice Problem I

# Q1:
lst = []
for i in songs: # songs is an arbitrary list of Song objects; implementation is irrelevant for this question 
  lst.append(i.title)

#Equivalent list comprehension
lst = [i.title for i in songs]

# Q2: 
filter = []
for song in songs:
    if song.is_liked():
        filter.append(song)
#Equivalent list comprehension
filter = [song for song in songs if song.is_liked()]

# Q3:
lst = []
for song in songs:
  if song.genre == "Rock":
    filter.append("Rock on!")
  elif song.genre == "Pop":
    filter.append("Pop on!")
  elif song.genre == "Love":
    filter.append("No Swifties Allowed")
  else:
    filter.append("euuuh, brother euuuh")
#Equivalent list comprehension

lst = ["Rock on!" if song.genre == "Rock" else "Pop on!" if song.genre == "Pop" else "No Swifties Allowed" if song.genre == "Love" else "euuuh, brother euuuh" for song in songs]
# Tip: Notice how theres a difference in the ordering when we use if/else versus just if in the list comprehension.

# Practice Problem II
# Q1: Create a list comprehension that returns the first 10 even numbers
# Hint: We're going to use a MAT102 concept here

lst = [2*i for i in range(1, 11)] # Preferred answer
# OR
lst = [i for i in range(2, 21, 2)] # Also correct
# OR
lst = [i for i in range(1, 21) if i % 2 == 0][:10] # If this was on a midterm I would not recommend this answer, but it's *technically* correct

# Q2: Create a list comprehension that returns the first 10 odd numbers
# Hint: We're going to use a MAT102 concept here

lst = [2*i-1 for i in range(1, 11)] # Preferred answer
# OR
lst = [i for i in range(1, 21, 2)] # Also correct
# OR
lst = [i for i in range(1, 21) if i % 2 != 0][:10] # If this was on a midterm I would not recommend this answer, but it's *technically* correct

# Q3: Create a list comprehension that flattens a 2D list

# Example 2D list
lst2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst1d = [i for sublist in lst2d for i in sublist] 
# Notice how we chained together the iterables in the list comprehension. This is a common pattern when flattening 2D lists.

# Note:
# The following is a common mistake:
# lst1d = [i for i in sublist for sublist in lst2d]
# This will result in a NameError: name 'sublist' is not defined

# This is an issue because you're jumping through layers. It's like an onion. You have to peel it one layer at a time.
# You can't just jump to the elements in the sublist first; You have to first "peel" the list apart into the sublists and then "peel" the sublists into the elements.