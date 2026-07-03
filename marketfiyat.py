import requests
import json

url = 'https://api.marketfiyati.org.tr/api/v2/searchByCategories'


headers ={
    "accept" : "application/json",
    "accept-encoding" : "gzip, deflate, br, zstd",
    "accept-language" : "en-US,en;q=0.9",
    "cache-control" : "no-cache",
    "connection" : "keep-alive",
    "content-type" : "application/json",
    "expires" : "0",
    "origin" : "https://marketfiyati.org.tr",
    "pragma" : "no-cache",
    "referer" : "https://marketfiyati.org.tr/",
    "sec-ch-ua" : '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
    "sec-ch-ua-mobile" : "?0",
    "sec-ch-ua-platform" : "Windows",
    "sec-fetch-dest" : "empty",
    "sec-fetch-mode" : "cors",
    "sec-fetch-site" : "same-site",
    "sec-gpc" : "1",
    "timeout" : "20000",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "withcredentials" : "true"
    }

payload = {
    "keywords": "Süt Ürünleri ve Kahvaltılık",
    "pages": 0,
    "size": 24,
    "menuCategory": True,
    "latitude": 41.0014154263743,
    "longitude": 39.7015262711726,
    "distance": 10,
    "depots": [
    "sok-6595", "bim-O709", "a101-8759", "a101-5021",
    "migros-7331", "migros-7351", "migros-1147", "sok-8367",
    "sok-10219", "a101-7646", "bim-2225", "bim-Q469",
    "bim-O591", "sok-9645", "bim-7710", "a101-3218",
    "sok-5469", "a101-H534", "tarim_kredi-5009", "migros-7485",
    "tarim_kredi-7083", "tarim_kredi-6129", "migros-7345",
    "tarim_kredi-7610", "tarim_kredi-5253"
]
}

r = requests.post(url, json=payload, headers=headers)

print(r.status_code)

data = r.json()
# print(data["content"][0]["title"])
print(r.text[:500])  # kac urun buldu
print(len(data["content"]))   # listedeki eleman sayisi





