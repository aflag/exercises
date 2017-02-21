def parse(text):
    entries = []
    for entry in text.split(","):
        entry = entry.strip()
        a = entry[0]
        b = entry[1]
        distance = int(entry[2:])
        entries.append((a, b, distance))
    return entries
