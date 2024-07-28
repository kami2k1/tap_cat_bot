import requests , time , threading , sys
token = input(str("TOKen You: "))
sle = input(str("Time Thu Thập Tối Thiểu 100s: "))
if float(sle) <100:
   print("lỗi : Time >100 ?")
   sys.exit()
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
stattickce = False
def MiNIGame():
 global stattickce
 print("Play MiNiGame")
 kami = True
 while kami:
     response = requests.get("https://cat-backend.pro/v1/games/mines-start", headers=headers)
     print(response.status_code)
     if response.status_code != 200:
          kami = False
          stattickce = False
          continue
     dataz = response.json()
     ztrue = sum(sum(row) for row in dataz["playing_board"])
     data ={"right_answers_amount":int(ztrue),"is_bombed":False}
     response = requests.post("https://cat-backend.pro/v1/games/mines-start", headers=headers,json=data)
     print(f"{response.json()}") 
     time.sleep(3)
game_run = True
while game_run:
    try:
        msg =""
        response = requests.get(url, headers=headers)
        def kami(response , type) -> None:
          global msg , stattickce , game_run
          if response.status_code == 200:  
            print("Success!")
            kami = response.json()
            for key, value in kami.items():
                  msg += f"{key} : {value}\n"
            if int(type) ==1:
              data =  int(kami['playing_tickets_amount'])
              if data > 0 and stattickce == False:
                 stattickce = True
                 thread1 = threading.Thread(target=MiNIGame, args=())
                 thread1.start()
          else:
            game_run = False
        kami(response,2)
        time.sleep(float(sle))
        response = requests.post(url, headers=headers)
        kami(response,2)
        
        response = requests.get("https://cat-backend.pro/v1/auth/profile", headers=headers)
        kami(response,type=1)
        my = f'''
      ---------------------------------------------
                                                  
                  Kami
      data:
      {msg}
      
      
      
      ---------------------------------------------
      '''
        print(my)
    except:
       print("Vui Lòng Kiểm Tra Lại kiết Nối mạng Của Bạn ?")
       sys.exit()     
print("Lỗi Token Hoặc Api Của Game Đã Thay đổi Vui Long Kiểm Tra Lại Thank ")