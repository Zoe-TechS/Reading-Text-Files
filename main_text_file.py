# Read text from a file, and count the occurence of words in that text

def read_file_content(filename):
    with open(filename, "r") as f:
        string_form = f.read()

    return string_form


def count_words():
    text = read_file_content("story.txt")
    word_count = {}
    count = 0
    for word in text.split():
        if word not in word_count:
            word_count[word] = count + 1
        else:
            word_count[word] +=1

    return word_count

print(read_file_content('story.txt'),'\n')
print(count_words())