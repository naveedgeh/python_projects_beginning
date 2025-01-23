import requests
import json

def get_user_with_freeapi():
    limit=10
    page=1
    r=requests.get(f"https://api.freeapi.app/api/v1/public/randomusers?page={page}&limit={limit}")
    result=r.json()
    if result["success"] and result["data"]:
    #  we can also save data into file 
        with open("user.json","w") as file:
            json.dump(result["data"]["data"],file)
    else:
        raise Exception("User data not found")
    
    print("Data Successfully get from freeeapi")

def main():
    try:
       get_user_with_freeapi()
    except Exception as e:
        print(str(e))
    

if __name__=="__main__":
    main()