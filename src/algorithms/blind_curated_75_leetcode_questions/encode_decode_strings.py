def encode_string_len_to_bytes_string(string):
    length = len(string)
    bytes = []
    for i in range(4):
        # bit shift the length to the right
        byte_length = length >> (i * 8)
        # grab the last 8 bits
        byte_length = byte_length & 0xFF
        # convert to the hexadecimal string representation
        byte_length = chr(byte_length)
        bytes.append(byte_length)

    bytes.reverse()
    return "".join(bytes)


def encode(strs):
    encoded_string = ""

    for string in strs:
        encode_workaround = string.encode("utf-8")
        encoded_chunk = encode_string_len_to_bytes_string(string) + encode_workaround
        encoded_string = encoded_string.join(encoded_chunk)

    return encoded_string


def decode_bytes_string_to_int(bytes_str):
    result = 0
    for ch in bytes_str:
        result = result * 256 + ord(ch)
    return result


def decode(string):
    start = 0
    end = len(string)
    result = []

    while start < end:
        bytes_string = string[start : start + 4]
        length_chunk = decode_bytes_string_to_int(bytes_string)

        chunk = string[start : start + length_chunk]
        result.append(chunk)
        start += length_chunk

    return result
