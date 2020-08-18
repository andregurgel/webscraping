from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
    print("O servidor retornou um Http Error")
except URLError as e:
    print("O servidor não foi encontrado")
else:
    print(html.read())