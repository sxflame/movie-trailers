import fresh_tomatoes
import media

borat = media.Movie("Borat",
                    "Borat: Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan  \
                    is a 2006 British-American mockumentary comedy film. The film was written and produced by  \
                    British comedian Sacha Baron Cohen who also plays the title character, Borat Sagdiyev,  \
                    a fictitious Kazakh journalist travelling through the United States recording real-life interactions with Americans.",
                    "https://upload.wikimedia.org/wikipedia/en/3/39/Borat_ver2.jpg" ,
                    "https://www.youtube.com/watch?v=vlnUa_dNsRQ")

bruno = media.Movie("Bruno",
                    "Bruno is a 2009 American mockumentary comedy film directed by Larry Charles and starring Sacha Baron Cohen,  \
                    who produced, co-wrote, and played the gay Austrian fashion journalist Bruno.",
                    "https://upload.wikimedia.org/wikipedia/en/d/de/Bruno_poster.jpg",
                    "https://www.youtube.com/watch?v=9dAc_sfTpFs")

jack_ass = media.Movie("Jackass",
                       "Jackass: The Movie is a 2002 American reality comedy film directed by Jeff Tremaine with the tagline  \
                       Do not attempt this at home.",
                       "https://upload.wikimedia.org/wikipedia/en/4/47/Jackass_poster.jpg",
                       "https://www.youtube.com/watch?v=FD5JulSi4RQ")

jack_ass2= media.Movie("Jackass 2",
                       "Jackass Number Two is a 2006 American reality comedy film. It is the sequel to Jackass: The Movie (2002),  \
                        both based upon the MTV series Jackass.",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Jackass_Number_Two_movie_poster.jpg",
                       "https://www.youtube.com/watch?v=9Gv1r889qAo")

jack_ass3d= media.Movie("Jackass 3D",
                       "Jackass 3D is a 2010 American 3D adult comedy film and the third film in the Jackass film series.",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Jackass_3d_poster.jpg",
                       "https://www.youtube.com/watch?v=2slL7L5FMQU")

tropic_thunder = media.Movie("Tropic Thunder",
                            "American satirical action comedy film co-written, produced, directed by, and starring Ben Stiller.  \
                            The film also stars Robert Downey Jr. and Jack Black. The main plot revolves around a group of prima donna actors  \
                            who are making a fictional Vietnam War film.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d6/Tropic_thunder_ver3.jpg",
                            "https://www.youtube.com/watch?v=T-6YhRZowgc")

new_groove = media.Movie("the Emperor's New Groove",
                        "The film follows a teenage emperor who is transformed into a llama by his ex-advisor and henchman.  \
                        In order for the emperor to change back into a human, he trusts a village leader who escorts him back to the palace. ",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Grooveposter.jpg",
                        "https://www.youtube.com/watch?v=Hjvy8vc39kw")

mary_poppins = media.Movie("Mary Poppins",
                            "Mary Poppins is a 1964 American musical fantasy comedy film directed by Robert Stevenson and produced by Walt Disney,  \
                            with songs written and composed by the Sherman Brothers. The screenplay is by Bill Walsh and Don DaGradi,  \
                            loosely based on P. L. Travers' book series Mary Poppins. ",
                            "https://upload.wikimedia.org/wikipedia/en/7/78/Marypoppins.jpg",
                            "https://www.youtube.com/watch?v=9kKXYjOD-AI")

beavis_butthead = media.Movie("Beavis and Butt-Head Do America",
                            "Beavis and Butt-Head Do America is a 1996 American animated road comedy film based on  \
                            the MTV television series Beavis and Butt-Head.",
                            "https://upload.wikimedia.org/wikipedia/en/c/cc/Beavis_And_Butthead_Do_America.jpg",
                            "https://www.youtube.com/watch?v=RvRvzzpZ3G8")

team_america = media.Movie("Team America: World Police",
                            "Team America: World Police is a 2004 American-German satirical action comedy film starring puppets  \
                            produced by Scott Rudin, Matt Stone, and Trey Parker, written by Parker, Stone and Pam Brady  \
                            and directed by Parker, all of whom are also known for the popular animated television series South Park. ",
                            "https://upload.wikimedia.org/wikipedia/en/5/53/Team_america_poster_300px.jpg",
                            "https://www.youtube.com/watch?v=rRV3H4AcM7Y")

matrix = media.Movie("The Matrix",
                    "The Matrix is a 1999 science fiction film written and directed by The Wachowskis, starring Keanu Reeves,  \
                    Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano.  \
                    It depicts a dystopian future in which reality as perceived by most humans is actually a  \
                    simulated reality called the Matrix, created by sentient machines to subdue the human population,  \
                    while their bodies' heat and electrical activity are used as an energy source.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                    "https://www.youtube.com/watch?v=a94b1yZOBes")

south_park = media.Movie("South Park: Bigger, Longer & Uncut",
                        "The film follows the four boys Stan Marsh, Kyle Broflovski, Eric Cartman, and Kenny McCormick  \
                        as they sneak into an R-rated film featuring Canadian actors Terrance and Phillip and begin cursing incessantly.  \
                        Eventually their parents pressure the United States to wage war against Canada for allegedly corrupting their children. ",
                        "https://upload.wikimedia.org/wikipedia/en/8/83/SouthParkbiggerlongeruncut.jpg",
                        "https://www.youtube.com/watch?v=aav9EyVjtWc")

athf = media.Movie("Aqua Teen Hunger Force Colon Movie Film for Theaters",
                   "Aqua Teen Hunger Force Colon Movie Film for Theaters is a 2007 American Flash animated surreal comedy film  \
                   based on the Adult Swim animated series Aqua Teen Hunger Force. ",
                   "https://upload.wikimedia.org/wikipedia/en/8/80/AquaTeenPosterColonMovie.jpg",
                   "https://www.youtube.com/watch?v=80Zg2guCzgU")

movies = [borat, bruno, jack_ass, jack_ass2, jack_ass3d, tropic_thunder,
new_groove, mary_poppins, beavis_butthead, team_america, matrix, south_park, athf]

#Creates an HTML to a browser of movies listed with trailers and poster art
fresh_tomatoes.open_movies_page(movies)


