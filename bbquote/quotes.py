import requests

def get_quote():
    url = 'https://movie-quote-api.herokuapp.com/v1/quote/'
    res = requests.get(url).json()
    return f"'{res['quote']}', by {res['role']}"
    
if __name__ == '__main__': 
    print(get_quote())