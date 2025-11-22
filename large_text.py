def split_message(text, max_length=4096):
    parts = []
    while len(text) > max_length:
        part = text[:max_length]
        parts.append(part)
        text = text[max_length:]
    parts.append(text)
    return parts
