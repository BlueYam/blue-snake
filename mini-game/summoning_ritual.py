import requests

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

def get_card_data(card_name, filename):
    params = {'name': card_name, 'misc': 'yes'}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        card = data['data'][0]
        print(f"Name: {card['name']}")
        print(f"Type: {card['type']}")
        print(f"Description: {card['desc']}")

        img_url = response.json()['data'][0]['card_images'][0]['image_url']
        img_data = requests.get(img_url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)
        print(f"Image saved as {filename}")

        if 'misc_info' in card:
            info = card['misc_info'][0]
            print(f"TCG Date: {info.get('tcg_date', 'N/A')}")
            print(f"Konami ID: {info.get('konami_id', 'N/A')}")
            print(f"Views: {info.get('views', '0')}")
    else:
        print(f"Error: {response.status_code}")
        

get_card_data("Dark Magician", "dark_magician.jpg")