def xor_shellcode(hex_string, xor_value):
    # Convert Hex chain in byte list
    shellcode_bytes = bytes.fromhex(hex_string)

    # Convert xor in byte
    xor_byte = bytes([xor_value])

    # applying xor for each bit
    result_bytes = [byte ^ xor_byte[0] for byte in shellcode_bytes]

    # convert modified byte to hex list
    result_hex = ''.join(format(byte, '02x') for byte in result_bytes)

    return result_hex

# PUT THE HEX CHAIN YOU WANNA XOR THERE
hex_string = ""

# Encoding key definition (CHANGE KEY IF YOU WANT)
key = 0xE

result_encoded = xor_shellcode(hex_string, key)

# Vérification with XOR decode
result_decoded = xor_shellcode(result_encoded, key)

# show results
final_result = f"\nEncoded shellcode : {result_encoded}\n\n############################################################################################\n\nDecoded shellcode : {result_decoded}"
print(final_result)

