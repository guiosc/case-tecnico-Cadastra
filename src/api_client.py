import requests
from requests.exceptions import RequestException
from src.config import API_KEY

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
    

def get_assets(limit: int=100) -> list:
    result = get_data("assets", params={"limit": limit, "apiKey": API_KEY})
    if result and "data" in result:
        return result["data"]
    return []


def get_assets_history(asset_id: str, interval: str="d1") -> list:
    result = get_data(f"assets/{asset_id}/history", params={"interval": interval})
    if result and "data" in result:
        return result["data"]
    return []


if __name__ == "__main__":
    print("Testando get_assets()")
    assets = get_assets()
    print(assets)
    #print(get_data("assets", params={"limit": 100, "apiKey": API_KEY}))
    

    # print("\n📈 Testando get_asset_history('bitcoin')")
    # history = get_assets_history("bitcoin", interval="d1")
    # print(history)
    