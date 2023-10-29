from urllib.request import urlopen

WEB = "https://shawnzsf.github.io/"
WEB_AS = urlopen(WEB)
print(WEB_AS.read().decode("utf-8", errors = "strict"))
WEB_AS.close()
