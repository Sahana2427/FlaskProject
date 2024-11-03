import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os

save_dir = "images/"
if not os.path.exists(save_dir): #try to access dir structure 
    os.mkdir(save_dir) # if does not exists creates directory

query = "puneeth rajkumar"
response = requests.get(f"https://www.google.com/search?q={query}&sca_esv=36885d2c0b4f145e&sxsrf=ADLYWIIDSGattKQh4IcJFLLb22Y_6YzPbw:1730465055086&source=hp&biw=1042&bih=676&ei=H80kZ5ORA96OseMP287NmQ8&iflsig=AL9hbdgAAAAAZyTbLxivq_6QmrqG7c_atuQNt07jatQh&oq=puneeth+rajk&gs_lp=EgNpbWciDHB1bmVldGggcmFqayoCCAAyCxAAGIAEGLEDGIMBMggQABiABBixAzILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAESOklUPUDWNwYcAF4AJABAJgBtwGgAZEMqgEEMC4xMrgBAcgBAPgBAYoCC2d3cy13aXotaW1nmAINoAKKDagCCsICBxAjGCcY6gLCAgQQIxgnwgIOEAAYgAQYsQMYgwEYigXCAgsQABiABBixAxiKBZgDE5IHBDEuMTKgB_VE&sclient=img&udm=2")

#Execute this url through python code = how? so we use request to execute url with my own query

print(response) # Running perfectly fine -- means no error found

soup = BeautifulSoup(response.content,'html.parser') 
print(soup) # Gets HTML response
# Give contents in form of html format

"""BeautifulSoup is a class in the BeautifulSoup library.

response.content is the raw HTML content fetched from a website.

'html.parser' specifies the parser to be used for parsing the HTML content."""


# If u click on any image every image is available on particular image address so we have to extract those images and 
# also right click view page source

images_tags = soup.find_all("img") # Fetched the length of images present for 21 images we hav image tags
print(len(images_tags))

print(images_tags) # We don't need first line which contains image so delete it as it has no url

del images_tags[0]

print(len(images_tags)) # So number of image tags is 20 now 

#In all src = link is available so extract only data which has src tag

for i in images_tags:
    image_url = i['src'] #Extracts all src 
    images_data = requests.get(image_url).content
    with open(os.path.join(save_dir, f"{query}_{images_tags.index(i)}.jpg"), "wb") as f:
        f.write(images_data)


print(requests.get(images_tags[1]['src']).content)
