email=input("Enter your email:").strip()
usern=email[:email.index("@")]
domain=email[email.index("@")+1:]
print("Entered Email:",email)
print(f"Username: {usern}\nDomain: {domain}")
