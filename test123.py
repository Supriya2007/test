import requests
import time
def main():
    r = requests.get('https://api.ipify.org?format=json')
    print(r.text)
    print(F'time now is {time.time()}')
if __name__ == "__main__":
    main()