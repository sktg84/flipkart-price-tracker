import os
import requests
import re
import time
from bs4 import BeautifulSoup as bs


def generate_sound(inp):
    if inp == 1:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 5000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    elif inp == 2:
        beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
        beep(3)
    elif inp == 3:
        beep = lambda x: [print ("\a") for i in range (1,x)]
        beep(3)

def check_fk_price(url, amount):
    global lastScanPrice
    global lastScanPriceAllTime
    global cutOffPrice
    
    request = requests.get(url)
    soup = bs(request.content,'html.parser')
    
    product_name = soup.find("span",{"class":"B_NuCI"}).get_text()
    price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
    prince_int = int(''.join(re.findall(r'\d+', price)))
    print(product_name + " is at " + price + f" (with cut-off @ Rs {cutOffPrice})")

    if (prince_int < lastScanPrice) or (cutOffPrice > prince_int) :
        if (lastScanPriceAllTime != -1):
            print(f"Book Quickly!! [Now at Rs. {price}, In the last scan it was @ Rs. {lastScanPrice} with all time low since scan start @ Rs {lastScanPriceAllTime}]")
            generate_sound(3)
    else:
        print("No Slots found")
    
    lastScanPrice = prince_int 
    if lastScanPriceAllTime > lastScanPrice or lastScanPriceAllTime == -1:
        lastScanPriceAllTime = lastScanPrice   


def main():
    #URL = "https://www.flipkart.com/apple-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn93hn-a/p/itmb53580bb51a7e?pid=COMFXEKMXWUMGPHW&lid=LSTCOMFXEKMXWUMGPHW40HAM7&marketplace=FLIPKART&q=macbook+air+m1&store=search.flipkart.com&srno=s_1_3&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&fm=SEARCH&iid=cf486f4b-8d24-4747-8fa5-4b17cb4b3a7b.COMFXEKMXWUMGPHW.SEARCH&ppt=hp&ppn=homepage&ssid=npbt1mddr40000001622911909542&qH=be9862f704979d6e"
    URL="https://www.flipkart.com/syska-bolt-sw200-smartwatch/p/itm34d03e7b78aed?pid=SMWGY6VQHSJFG7EW&lid=LSTSMWGY6VQHSJFG7EWVX3N88&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_2&otracker=clp_banner_1_1.banner.BANNER_syskabolt-sw200-smartwatch-store_OSS9UD95JQFH&fm=neo%2Fmerchandising&iid=af6e6048-7b12-4052-88bd-0636f2b7db67.SMWGY6VQHSJFG7EW.SEARCH&ppt=clp&ppn=syskabolt-sw200-smartwatch-store&ssid=zfkjzzumi80000001623077771646"
    global cutOffPrice
    while True:
        check_fk_price(URL,cutOffPrice)
        time.sleep(3)

if __name__ == "__main__":
    lastScanPrice = 0
    lastScanPriceAllTime = -1
    cutOffPrice = 3000
    
    main()
