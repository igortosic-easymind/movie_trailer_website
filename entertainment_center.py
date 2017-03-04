import fresh_tomatoes
import media

guardians = media.Movie("Guardians of the Galaxy",
                        "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                        "https://www.youtube.com/watch?v=4hdv_6gl4gk&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-&index=3")

belko = media.Movie("The Belko Experiment",
                     "In a twisted social experiment, 80 Americans are locked in their high-rise corporate office in Bogota, Colombia and ordered by an unknown voice coming from the company's intercom system to participate in a deadly game of kill or be killed.",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcRSCIJTwFLmqfnoDCMGAU9McTpLci3r7hkSfbBi0drCr3AzhIQR",
                     "https://www.youtube.com/watch?v=mWXeVFeca34&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-&index=9")

ottoman = media.Movie("The Ottoman Lieutenant",
                      "The Ottoman Lieutenant is a love story between an idealistic American nurse and a Turkish officer in World War I.",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcRBeWiUyul0Y9qPP6FKnAMLgbDnVDWK9GSaWD29ozMz9s8Y_WuE",
                      "https://www.youtube.com/watch?v=7BJyAgU5Yr8&index=15&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-")

alien = media.Movie("Alien: Covenant",
                      "The crew of a colony ship discover an uncharted paradise, with a threat beyond their imagination, and must attempt a harrowing escape.",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcQRt8pTolQP2qXqhrD0U7opEiJXDeeT7zfyO7t5QPkYTRpUE10g",
                      "https://www.youtube.com/watch?v=XZ0Rx4aqWr0&index=6&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-")

wilson = media.Movie("Wilson",
                      "A lonely, neurotic and hilariously honest middle-aged man reunites with his estranged wife and meets his teenage daughter for the first time.",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcRi47pTh3hhYxkywFFq3AZSgya7r-d-nnxuLrzGPJkDL3w_bd4c",
                      "https://www.youtube.com/watch?v=AKHFZumOS94&index=33&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-")

live_by_night = media.Movie("Live by Night",
                      "A group of Boston-bred gangsters set up shop in balmy Florida during the Prohibition era, facing off against the competition and the Ku Klux Klan.",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcQyDgzA7Q3OZ4quuoFkSPxx8qPhCDdetEdvNpxu_lr6k216GYJS",
                      "https://www.youtube.com/watch?v=a-Z1E4XFucE&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-&index=63")



movies = [guardians, belko, ottoman, alien, wilson, live_by_night]
fresh_tomatoes.open_movies_page(movies)

