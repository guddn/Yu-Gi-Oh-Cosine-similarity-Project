from load_api import load_card_data

def create_card_data(card_names):
    card_datas_json = {}
    card_datas_string = []

    for card_name in card_names:
        card_data_json, card_data_string = load_card_data(card_name)
        
        card_datas_json[card_name] = card_data_json
        card_datas_string.append(card_data_string)

    return card_datas_json, card_datas_string
    

