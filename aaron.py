from datetime import datetime
import os


url = "https://www.amazon.com.br/hz/wishlist/ls/2T9KJKD2CTGOG"

crab = url.split("/")[-1]
title = datetime.now().strftime('%Y-%m-%d')
path = os.path.join(os.getcwd(), crab, f"{title}.json")
print(path)