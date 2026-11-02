def cipher(text, shift, mode = 'encrypt'):
    result = []

    if mode == 'decrypt':
    	shift = -shift

    for char in text:
    	if char.isupper():
    		shifted_char = chr((ord(char) + shift - 65) % 26 + 65)
    		result.append(shifted_char)
    	elif char.islower():
    		shifted_char = chr((ord(char) + shift -97) % 26 + 97)
    		result.append(shifted_char)
    	else:
    		result.append(char)

    return "".join(result)


if __name__ == "__main__":
	print("\n<--- Caesar Cipher CLI --->\n")

	while True:
		user_mode = input("Input mode (encrypt/decrypt or e/d): ").strip().lower()
		if user_mode in ['encrypt', 'e']:
			mode = 'encrypt'
			break
		elif user_mode in ['decrypt', 'd']:
			mode = 'decrypt'
			break
		print("Invalid choice. Please enter 'e' or 'd'.")

	message = input("Enter your message: ")

	while True:
		try:
			shift_key = int(input("Enter shift key (integer): "))
			break
		except ValueError:
			print("Please enter a valid integer.")

	output = cipher(message, shift_key, mode)
	print(f"\nResulting Text:\n{output}")
