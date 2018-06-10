import urllib, json
import requests
from PIL import Image
from io import BytesIO

img = Image.open("z_Image.png")
output = BytesIO()
img.save(output, format='PNG')
hex_data = output.getvalue()

img_filename="mama.jpg"
img_url="http://www.happyfamilyneeds.com/wp-content/uploads/2017/08/angry8.jpg"
#print(data)
# Replace the subscription_key string value with your valid subscription key.
subscription_key = ''
with open(img_filename, 'rb') as f:
    img_data = f.read()

## Request headers.
'''header = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}'''

header = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}
# Request parameters.
params = urllib.parse.urlencode({
     'returnFaceId': 'true',
     'returnFaceLandmarks': 'false',
     'returnFaceAttributes': 'emotion',
})

api_url = "https://westus.api.cognitive.microsoft.com/face/v1.0/detect?%s"%params

r = requests.post(api_url,
#                  params=params,
                  headers=header,
				  data=hex_data
				  )
				  
data_1 = r.json()
types=["anger", 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
counter_types = 0
Result_dictionary = {}
Intermediate_dictionary = {}
#arr=[]
for i in types:
    if counter_types <= 7:
        score_1=data_1[0]['faceAttributes']['emotion'][i]
        Intermediate_dictionary[i]=float('%f'%score_1)
            #arr.append('%f'%score_1)
        Result_dictionary.update(Intermediate_dictionary)
        counter_types+=1
    #print(max(arr))
    #Max_value_found=max(Result_dictionary.values())

Emoji_text=list(Result_dictionary.keys())[list(Result_dictionary.values()).index(max(Result_dictionary.values()))]
print(Emoji_text)

'''
data_1 = r.json()
print(data_1[0]['faceAttributes'])
import operator
x = data_1[0]['faceAttributes']['emotion']
sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
print("Emotion")
print(sorted_x[0][0])
print("Value")
print(sorted_x[0][1])'''