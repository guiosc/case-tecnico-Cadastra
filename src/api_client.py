import requests
from requests.exceptions import RequestException
from src.config import API_KEY
from src.models import transformation_assets, transformation_assets_history

def get_data(path: str, params: dict=None) -> dict:
    url = f"https://rest.coincap.io/v3/{path}"

    if params:
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        url += f"?{query_string}"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()
    except RequestException as e:
        print(f"[ERRO] Falha na requisição: {e}")
        return None
    



if __name__ == "__main__":
    # print(transformation_assets(get_data("assets", params={"limit": 100, "apiKey": API_KEY})))
    # print(transformation_assets_history(get_data(f"assets/bitcoin/history", params={"interval": "d1", "apiKey": API_KEY})))
    
    raw_assets = get_data("assets", params={"limit": 10, "apiKey": API_KEY})
    df_assets = transformation_assets(raw_assets["data"])
    print("🟢 Assets Transformados:")
    print(df_assets.head())

    # Testar histórico do primeiro asset
    first_crypto_id = df_assets.iloc[0]["crypto_id"]
    raw_history = get_data(f"assets/{first_crypto_id}/history", params={"interval": "d1", "apiKey": API_KEY})
    df_history = transformation_assets_history(raw_history["data"], crypto_id=first_crypto_id)
    print(f"\n📈 Histórico de {first_crypto_id}:")
    print(df_history.head())