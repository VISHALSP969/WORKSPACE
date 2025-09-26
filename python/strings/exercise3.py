email="alice@example.com"
username,domain=email.split("@")
print(username)
print(domain)

i=email.index("@")
print(email[:i],email[i+1:])
