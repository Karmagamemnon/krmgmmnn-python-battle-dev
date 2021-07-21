# Python Battle Dev
# Groups compose of:
#    - Kevin PEETERS
#    - Gregory MOU KUI
import requests

if __name__ == "__main__":
    print('hello kevin peeters')
    response = requests.get("http://app.objco.com:8099/?account=BJ776QUVG0&limit=5")
    #print(response.json())
    for capteur in response.json():
        print(capteur)
