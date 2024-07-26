import requests
import os

try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')

def get_balance(api_key):
    url = "https://api.capmonster.cloud/getBalance"
    payload = {"clientKey": api_key}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    while True:
        api_key = input("Veuillez entrer votre clé API CapMonster: ")
        balance_response = get_balance(api_key)
        if balance_response and 'balance' in balance_response:
            balance = balance_response['balance']
            print(f"Votre solde est de {balance} USD.")
            if balance > 0:
                break
            else:
                print("Votre solde est insuffisant. Veuillez entrer une autre clé API.")
        else:
            print("Erreur de connexion ou clé API invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
