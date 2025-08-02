def number_of_words(content):
    list_words=content.split()
    return len(list_words)

def number_of_characters(content):
    content=content.lower()
    dic_of_content={}
    for letter in content:
        if letter in dic_of_content:
            dic_of_content[letter]+=1
        else:
            dic_of_content[letter]=1
    return dic_of_content

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    sorted_list=[]
    for letter in dictionary:
        if letter.isalpha():
            sorted_list.append({"char":letter,"num":dictionary[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

