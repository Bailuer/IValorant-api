import requests
import time
def main(username,password):
    import auth
    selfs = auth.Auth(username=username,password=password)
    #print(selfs)
    headers = {
        'Authorization': f'Bearer '+selfs.access_token,
        'X-Riot-Entitlements-JWT': selfs.entitlement
    }
    store = requests.get("https://pd.ap.a.pvp.net/store/v2/storefront/"+selfs.Sub,headers=headers)
    storeText = store.json()
    bundleslist=[]
    for i in range(4):
        params = {'language':'zh-TW'}
        uuid = storeText['SkinsPanelLayout']['SingleItemOffers'][i]
        bundles = requests.get("https://valorant-api.com/v1/weapons/skinlevels/"+uuid,params=params)
        bundlesText = bundles.json()
        bundleslist.append(bundlesText)
    return bundleslist