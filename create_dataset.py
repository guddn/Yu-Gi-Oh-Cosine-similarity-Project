from load_api import load_card_data

def create_card_data(card_names):
    card_data = []

    for card_name in card_names:
        card_data_object, card_data_string = load_card_data(card_name)
        print(card_data_string, '\n')
        card_data.append(card_data_string)

    return card_data
    

