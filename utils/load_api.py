import requests
import json
import urllib.parse

def load_card_data(card_name = "하루 우라라"):
    # 1. API 기본 정보
    BASE_URL = "http://localhost:8080/card/"

    # 2. URL 경로 구성 
    encoded_card_name = urllib.parse.quote(card_name)
    full_url = BASE_URL + encoded_card_name

    # 3. GET 요청 실행
    try:
        response = requests.get(full_url)
        
        # HTTP 상태 코드 확인
        response.raise_for_status() 

        # 4. 응답 결과를 JSON 객체(파이썬 딕셔너리)로 저장
        card_data_json = response.json()

        # 5. 응답 결과를 문자열(String) 객체로 저장
        card_data_string = response.text
        
    except requests.exceptions.HTTPError as err:
        print(f"HTTP 오류 발생: {err}")
    except requests.exceptions.ConnectionError as err:
        print(f"연결 오류 발생: {err}")
    except json.JSONDecodeError:
        print("JSON 디코딩 오류")
    
    return card_data_json, card_data_string

