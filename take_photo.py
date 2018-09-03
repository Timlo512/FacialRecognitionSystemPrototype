import json

def take_photo():
    """
    This function will take a photo from user and save it as embedding
    """

    with open('control/save_image.json',"r") as f:
        save_image = json.load(f)
    
    save_image["save_image"] = True

    def checking():
        while(True):
            name = input("What is your name?")
            try:
                with open("control/embedding.json","r") as f:
                    check = json.load(f)
                
                if name in check.keys():
                    print("Sorry, your name has been registered.\n Please type again.")
                else:
                    return name
            finally:
                return name
    save_image["name"] = checking()
    with open("control/save_image.json","w") as f:
        json.dump(save_image,f)

if __name__ == "__main__":
    take_photo()    
    