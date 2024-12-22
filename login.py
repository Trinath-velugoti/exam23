# login.py

def login(username, password):
    # Simple check for username and password
    if username == "admin" and password == "password123":
        return "Login successful"
    else:
        return "Invalid username or password"
