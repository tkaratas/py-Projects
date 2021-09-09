"""File write and read practice. It is an example for Web site blocker path muss be changed"""


path = "path/to/hosts"  # CHANGE

redirect = "127.0.0.1"

websites = ["www.facebook.com", "facebook.com",
            "www.gmail.com", "gmail.com", "www.twitter.com"]  # CHANGE

with open(path, "r+") as host:
    content = host.read()
    for website in websites:
        if website in content:
            pass
        else:
            host.write("\n" + redirect + " " + website)
