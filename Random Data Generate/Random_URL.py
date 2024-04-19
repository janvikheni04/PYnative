#Generate random secure token of 64 bytes and random URL
import secrets

print("Random secure token is: ", secrets.token_hex(64))
print("Random URL is: ", secrets.token_urlsafe(64))

