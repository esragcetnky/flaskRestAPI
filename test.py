from flask import views
import requests
from requests.models import Response

BASE="http://127.0.0.1:5000/"

data=   [{'likes':10,'name':'Top 10 pop songs','views':10000},
        {'likes':2,'name':'DIY hair models','views':52},
        {'likes':12450,'name':'How to make Cheescake','views':84569},
        {'likes':4561,'name':'Brad Pitt Interview','views':58452},
        {'likes':123,'name':'Breaking News from the World','views':2564},
        {'likes':51134,'name':'"Official Music Video"','views':1567485},
        {'likes':7844,'name':'API Tutorial','views':100000},
        {'likes':10,'name':'Crash Course','views':654}]

# importing all the videos in the data   
for i in range (len(data)):
    put_request=requests.put(BASE+"video/"+str(i), data[i])
    print(put_request.json())

input()

# getting information for spesific video
print("Please enter id of video:")
number=int(input())
get_video=requests.get(BASE+f"video/{number}")
if get_video:    
    print(f"\nInformation about video {number}\n-----------------------------------------")
    print(get_video.json())
else:    
    print(get_video.json())

input()

# deleting spesific video 
print("Please enter id of video that you want to delete:")
del_number=int(input())
del_video=requests.delete(BASE+f"video/{del_number}")
if del_video:    
    print(f"\nInformation about video {del_number}\n-----------------------------------------")
    print(del_video.json())
else:    
    print(del_video.json())

input()

new_data=   [{"views":789},
            {"likes":163548},
            {"name":"This show is awesome!"}]

# updating spesific video 
print("Please enter id of video that you want to patch:")
upt_number=int(input())
upt_video=requests.patch(BASE+f"video/{upt_number}",new_data[2])
if upt_video:    
    print(f"\nInformation about video {upt_number}\n-----------------------------------------")
    print(upt_video.json())
else:    
    print(upt_video.json())


