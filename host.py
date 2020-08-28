import requests
class search:
    def whois(URL):
        payload = {"api_token":"09nrw1W5vbLadepf8ki2JpEnyMxRJVNv","domain":URL}
        data = {"domain":URL}
        f = open("response.txt","w+")
        r = requests.get("https://api.spyse.com/v1/subdomains",params=payload)
        f.write(str(r.text))
        f.close()
        f = open("response.txt","r")
        print(f.read())
        f.close()


