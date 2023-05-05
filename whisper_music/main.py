import utils 

def main():
    while True:
        user_request = utils.listen()
        if(user_request is None):
            continue
        structured_request = utils.structure_request(user_request)
        if(structured_request is None):
            continue
        utils.play_song(structured_request)

if __name__ == "__main__":
    main()