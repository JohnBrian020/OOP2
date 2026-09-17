def save_user(name, callback):
    print(f"Saving {name}...")
    
    #fake save
    print("User saved")
    callback()
    
def send_email():
    print("SEnding email...")
    
save_user("brian", send_email)