books = [
    "Precise & Perfect Python - Paul PepperPuddle",
    "Automate the Boring Stuff with Python - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
    "World of Warcraft: Orcs vs Humans",
]


def display_wishlist(display_name, wishes):
    print(display_name + ": ")
    suggested_gift = wishes.pop(0)
    print("======>", suggested_gift, "<======")
    for wish in wishes:
        print("* " + wish)
    print()

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)

        
 