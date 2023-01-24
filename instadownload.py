from datetime import datetime
from instaloader import Instaloader, Profile

ins = Instaloader()

# Login e senha
ins.login("///", "|||")

posts = Profile().from_username(ins.context, "luigitramontin").get_posts()

# Periodo dos posts
DESDE = datetime(2019, 1, 1)
ATE = datetime(2022, 1, 1)

for post in posts:
    if post.date >= DESDE and post.date <= ATE:
        print(post.date)
        ins.download_post(post, "insta")
