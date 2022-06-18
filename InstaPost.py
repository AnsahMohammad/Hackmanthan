'''
                READ THIS!

                caption have been exracted into the variable 'caption'
                
'''

import os
import shutil
from instaloader import Post
import instaloader

url = 'https://www.instagram.com/reel/Ce85ucDFx_F/?utm_source=ig_web_copy_link'


k = url.split("/")
url = k[4]
i = instaloader.Instaloader()
post = Post.from_shortcode(i.context,url)
i.download_post(post,target='download_')

#geting filename
arr = os.listdir('download_')
global name
for word in arr:
    if word[-1:-3] == "txt":
        name=word

f = open("download_/"+word, "r",encoding="utf8")
caption = f.read()
print(caption)

#deleting folder
mydir= "download_"
try:
    shutil.rmtree(mydir)
except OSError as e:
    print("Unable to remove cache file")