import wget


def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

print("Please send the download url in console.")
url = input("Downloading: ")
wget.download(url, bar=bar_custom)
