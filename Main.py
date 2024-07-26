import requests , time
token = input(str("TOKen You: "))
sle = input(str("Thời gian Thu Thập tính bằng s: "))
url = "https://cat-backend.pro/v1/points/mining"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "vi-VN,vi;q=0.9,en;q=0.8",
    "Authorization": f"Token {token}",
    "Content-Type": "application/json",
    "Origin": "https://tg-purr-tap.vercel.app",
    "Referer": "https://tg-purr-tap.vercel.app/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
}

response = requests.get(url, headers=headers)
def kami(response):
  if response.status_code == 200:  
    print("Success!")
    print(response.json())
kami(response)
time.sleep(float(sle))
response = requests.post(url, headers=headers)
kami(response)
response = requests.post("https://cat-backend.pro/v1/auth/profile", headers=headers)
kami(response)