from load_api import load_card_data
from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity():
    # Load card data
    card_names = ["섬도희-카가리", "섬도희-시즈쿠", "섬도희-하야테", "섬도희-카이나"]

    for card_name in card_names:
        card_data_object = load_card_data(card_name)
        print(f"\nCard Name: {card_name}")
        print("Card Data Object:", card_data_object)
