def count_words(text):
        words= text.split() 
        return len(words) 

def numb_characters(text):
    c_characters=text.lower()
    char_c ={}
    for char in c_characters:
        if char in char_c:
            char_c[char]+=1
        else:
            char_c[char]=1 
    return char_c

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list