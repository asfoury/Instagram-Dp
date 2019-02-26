from bs4 import BeautifulSoup
import urllib.request
import urllib
import json
import random
from PIL import Image




def get_ID(username):
    url = urllib.request.urlopen("http://instagram.com/"+username)
    soup = BeautifulSoup(url,"html.parser")
    scr = soup.findAll('script')

    lis = str(scr[2]).split(',')
    id_string = str(lis[22]).split(':')
    id_string = id_string[1].split('"')
    id = int(id_string[1])
    return id


def get_PP(id,username):
    id_string = str(id)
    url = "https://i.instagram.com/api/v1/users/"+id_string+"/info/"
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    url = data['user']['hd_profile_pic_url_info']['url']
    image_name = username + str(random.randrange(100000))+".jpg"
    urllib.request.urlretrieve(url,image_name)
    return image_name




def getPP(username):
    name = get_PP(get_ID(username),username)
    im = Image.open(name)
    im.show()

print("Enter username to get PP: ")
name = str(input())
getPP(name)
