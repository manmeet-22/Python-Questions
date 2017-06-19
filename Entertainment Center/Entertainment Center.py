# This is the main file to be to executed which contains all the attributes of the movies
import media
import fresh_tomatoes

def main():
    toy_story = media.Movie("Toy Story",
                            "A story of a boy and his toys that come to life",
                            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=4KPTXpQehio",
                            "November 19, 1995")
    print(toy_story.storyline)
    #toy_story.show_trailer()

    avatar = media.Movie("Avatar",
                         "A marine on an alien planet",
                         "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                         "December 18, 2009")
    #avatar.show_trailer()

    walle = media.Movie("Wall•e",
                        "After hundreds of lonely years of doing what he was built for, WALL•E (short for Waste Allocation Load Lifter Earth-Class) discovers a new purpose in life when he meets a sleek robot named EVE",
                        "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                        "https://www.youtube.com/watch?v=alIq_wG9FNk",
                        "June 21, 2008")
    #walle.show_trailer()

    contact = media.Movie("Contact",
                          "We make contact with aliens",
                          "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
                          "https://www.youtube.com/watch?v=d9C2cF3KvP8",
                          "July 11, 1997")

    res_evil = media.Movie("Resident Evil",
                           "Zombie-causing virus escapes from the lab",
                           "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
                           "https://www.youtube.com/watch?v=u6uDnd_v5Bw",
                           "March 15, 2002")

    matrix = media.Movie("The Matrix",
                          "The world is a simulation",
                          "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                          "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                          "March 31, 1999")

    movies = [toy_story, avatar, walle, contact, res_evil, matrix]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)
    print("__doc__ : "+media.Movie.__doc__ +"\n__module__ : "+ media.Movie.__module__)

if __name__ == '__main__':
    main()
