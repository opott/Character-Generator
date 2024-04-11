# import libaries
import random

# define name segments in lists
np1 = ["Ab", "Cd", "Ef", "Gh", "Ij", "Kl", "Mn", "Op", "Qr", "St", "Uv", "Wx", "Yz"]
np2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
np3 = ["zY", "xW", "vU", "tS", "rQ", "pO", "nM", "lK", "jI", "hG", "fE", "dC", "bA"]

# randomly join name segments and store in name variable
name = random.choice(np1) + random.choice(np2) + random.choice(np3)

# define genders in list
genders = ["Male", "Female"]

# randomly choose a gender and store in gender variable
gender = random.choice(genders)

# randomly generate an age in range 1-100 and store in age variable
age = random.randint(1, 100)

# define classes in a list
classes = ["Barbarian - Melee Damage" , "Cleric - Healing", "Knight - Defending", "Mage - Casts Elemental Spells", "Ranger - Ranged Damage", "Rogue - Stealing Gold"]

# randomly select a class and store in charclass variable
charclass = random.choice(classes)

# randomly generate strenth level in range 1-10 and store in strength variable
strength = random.randint(1, 10)

# randomly generate strenth level in range 1-10 and store in intelligence variable
intelligence = random.randint(1, 10)

# randomly generate bravery level in range 1-10 and store in bravery variable
bravery = random.randint(1, 10)
