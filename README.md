# insta Bot

Follow the bot [Here!](https://www.instagram.com/insta_bot_1729/)

# Introduction

This is a fun little project created in python. It will fetch random image from [Unsplash](https://source.unsplash.com/) and random caption from [randomtextgenerator](https://randomtextgenerator.com/). Then it will post it on instagram using [Instabot](https://github.com/instagrambot/instabot).

First execition takes a little longer, it needs to cache your instagram account data

# How to run

1. Fulfill requirements in `requirements.txt`(i.e. `pip install -r requirements.txt` or `pip3 install -r requirements.txt`).
2. Replace username and password with your credentials and run it with
   `python main.py`. or `python3 main.py`
3. To run it every 24h just add it to your crontab with `crontab -l` after setting everything up (and double checking it works!)

# Troubleshooting

if you get following error `ImportError: libopenjp2.so.7: cannot open shared object file: No such file or directory` you probably need to install `libopenjp2-7`

# Tested on

- WSL
- Raspberry
- Windows 10
- well, it should work likely eberywhere pythons runs..

# Credits

Contributors :computer: :

- [Deep Raval](https://github.com/imdeep2905)
- [Alessandro Digilio](https://github.com/alsd4git)

Without these libraries :heart: this would not have been possible.

- pillow
- BeautifulSoup
- instabot
