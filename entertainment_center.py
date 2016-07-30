import fresh_tomatoes
import media

# Ghostbusters movie information
ghost_busters = media.Movie("Ghostbusters",
                            "Three former parapsychology professors set up"
                            " shop as a unique ghost removal service.",
                            "http://ia.media-imdb.com/images/M/MV5BMTkxMjYyNzgwMl5BMl5BanBnXkFtZTgwMTE3MjYyMTE@._V1_SY1000_CR0,0,650,1000_AL_.jpg",  # noqa
                            "https://www.youtube.com/watch?v=vntAEVjPBzQ")  # noqa

# Ghostbusers 2 movie information
ghost_busters2 = media.Movie("Ghostbusters 2",
                             "The discovery of a massive river of ectoplasm "
                             "and a resurgence of spectral activity allows "
                             "the staff of Ghostbusters to revive "
                             "the business.",
                             "http://vignette2.wikia.nocookie.net/ghostbusters/images/0/01/Ghostbusters_ii_poster.jpg/revision/latest?cb=20100531182552",  # noqa
                             "https://www.youtube.com/watch?v=-_GPiwqmUiA")  # noqa
# print(ghost_busters2.storyline)
# ghost_busters2.show_trailer()

# Black Hawk Down movie information
black_hawk_down = media.Movie("Black Hawk Down",
                              "123 elite U.S. soldiers drop into Somalia "
                              "to capture two top lieutenants of "
                              "a renegade warlord and find themselves "
                              "in a desperate battle with a large "
                              "force of heavily-armed Somalis.",
                              "http://ia.media-imdb.com/images/M/MV5BMTQxODgzMjYyN15BMl5BanBnXkFtZTgwNDU4NTYxMTE@._V1_.jpg",  # noqa
                              "https://www.youtube.com/watch?v=tnV6wM-vd9s")  # noqa
# JSA movie information
jsa = media.Movie("JSA: Joint Security Area",
                  "After a shootout at the common security "
                  "area at the border of the two Koreas, "
                  "when two soldiers were murdered, "
                  "Maj. Sophie E. Jean is assigned by "
                  "the Neutral Nations Supervisory "
                  "Commission to investigate the incident.",
                  "http://ia.media-imdb.com/images/M/MV5BMjEzOTYyODY4OV5BMl5BanBnXkFtZTcwNTk1NjEyMQ@@._V1_.jpg",  # noqa
                  "https://www.youtube.com/watch?v=fI8sx8qngRw")  # noqa
# A Moment to Remember movie information
a_moment_to_remember = media.Movie("A Moment to Remember",
                                   "A Korean love story about a young "
                                   "couple's enduring love, which is tested "
                                   "when 27 year old Sun-jin is diagnosed "
                                   "with a rare form of Alzheimer's disease.",
                                   "http://ia.media-imdb.com/images/M/MV5BODYzODg5Mjg3Ml5BMl5BanBnXkFtZTgwNDM1MDQ2MzE@._V1_SY1000_CR0,0,701,1000_AL_.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=LFLSwFEiANg")  # noqa
# My Sassy Girl movie information
my_sassy_girl = media.Movie("My Sassy Girl",
                            "Based on a series of true stories "
                            "posted by Ho-sik Kim on the Internet "
                            "describing his relationship with "
                            "his girlfriend.",
                            "http://ia.media-imdb.com/images/M/MV5BMjM2NTYxMTE3OV5BMl5BanBnXkFtZTgwNDgwNjgwMzE@._V1_.jpg",  # noqa
                            "https://www.youtube.com/watch?v=hz1TSKxbkcY")  # noqa
# movies list created
movies = [ghost_busters, ghost_busters2, black_hawk_down,
          jsa, a_moment_to_remember, my_sassy_girl]
# Function called to display movies list in a browser window
fresh_tomatoes.open_movies_page(movies)
