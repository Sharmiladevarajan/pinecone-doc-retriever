def split_text_into_chunks(text_file,chunk_size):
    with open(text_file, 'r') as file:
        text = file.read()
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks