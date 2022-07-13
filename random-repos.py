import random


if __name__ == "__main__":
   random_page = random.randint(1, 100)
   random_stars_greater_than = random.randint(3, 15)
   language = "Python"  # JavaScript, Go, etc
   new_link = f"https://gist.github.com/search?l={language}&p={random_page}&q=stars%3A%3E{random_stars_greater_than}"
   print(new_link)