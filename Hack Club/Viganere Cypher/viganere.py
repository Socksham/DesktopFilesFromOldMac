# The set of characters we support
characters = "abcdefghijklmnopqrstuvwxyz"

# How many characters we have
character_count = len(characters)

# List all our supported characters
def encrypt_character(plain, key):
  # Turn plain character and key character into number codes. a=0, b=1...
  key_code = characters.index(key)
  plain_code = characters.index(plain)

  # Combine plain + key, and loop back to zero at character_count
  cipher_code = (key_code + plain_code) % character_count

  # Turn cipher_code back into a character
  cipher = characters[cipher_code]

  # Done. Return our ciphertext character
  return cipher

def encrypt(plain, key):
  # An empty string, which we'll fill with our ciphertext
  cipher = ""

  # Loop over every character in our plaintext
  for (plain_index, plain_character) in enumerate(plain):
    # Use the index of our plain character to get the corresponding key character
    key_index = plain_index % len(key)
    key_character = key[key_index]

    # Encrypt our plain character with our key character
    cipher_character = encrypt_character(plain_character, key_character)

    # Add our new cipher character to the end of our ciphertext
    cipher += cipher_character

  # Done. Return our full ciphertext
  return cipher

plaintext = input("text: ")
keytext = input("key: ")
ciphertext = encrypt(plaintext, keytext)

print("\n" + "Output: " + ciphertext)