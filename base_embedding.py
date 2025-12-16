from utils.create_dataset import create_card_data

from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

'''
카드명, 속성 등을 full text로 담은 후 임베딩 
card_names 기준: 
사용 모델: all-MiniLM-L6-v2
'''

# 카드 이름 리스트
card_names = ["하루 우라라", "유령토끼", "부유벚꽃", "저택 와라시", "하나 미즈키", "사요 시구레",
              "증식의 G", "원시생명체 니비루", "이펙트 뵐러",
              "섬도희-카가리", "섬도희-시즈쿠", "섬도희-하야테", "섬도희-카이나", "섬도희-레이", "섬도희-로제", "섬도희=제로",
              "샐러맨그레이트 가젤", "샐러맨그레이트 미라지스탤리오", "샐러맨그레이트 울프", "샐러맨그레이트 베일링크스", "샐러맨그레이트 레이징 피닉스",
              "초뇌룡-썬더 드래곤", "뇌신룡-썬더 드래곤","뇌전룡-썬더 드래곤", "뇌수룡-썬더 드래곤",
              "액세스코드 토커", 
              "블랙 매지션", "푸른 눈의 백룡", "붉은 눈의 흑룡", "데몬 소환"]

# 모델 설정
model = SentenceTransformer('all-MiniLM-L6-v2')
card_data_json, card_data = create_card_data(card_names)
embeds = model.encode(card_data)

# PCA
pca = PCA(n_components=2)
coords = pca.fit_transform(embeds)

# 시각화
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(coords[:,0], coords[:,1])
for i, text in enumerate(card_names):
    plt.annotate(text, xy=(coords[i,0], coords[i,1]), fontsize=5)

plt.show()