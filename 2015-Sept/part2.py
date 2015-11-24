import sys

class TagSuggester:

    def __init__(self):
        self.items = dict()

    def addNote(self, content, tagLine):
        temp = [i.strip() for i in tagLine.split(",") if i != '']
        tags = []
        for i in temp:
            if i.upper() not in map(str.upper, tags):
                tags.append(i)
        note = (content, tags)
        for tag in tags:
            tag = tag.lower()
            if tag in self.items:
                notes = self.items[tag]
            else:
                notes = []
                self.items[tag] = notes
            notes.append(note)

    def getSuggestions(self, prefix):
        prefix = prefix.lower()
        suggestions = []
        for tag in self.items:
            if tag.startswith(prefix):
                edits = 0
            elif equalsIgnoreTypo(prefix, tag[0:min(len(tag), len(prefix))]):
                edits = 1
            else:
                edits = 2
            if edits < 2:
                for i in self.items[tag][-1][-1]:
                    if tag == i.lower():
                        return_tag = i
                s = (return_tag, edits, len(self.items[tag]))
                suggestions.append(s)
        suggestions.sort(key=lambda suggestion: suggestion[0].lower(), reverse=False)
        suggestions.sort(key=lambda suggestion: suggestion[2], reverse=True)
        suggestions.sort(key=lambda suggestion: suggestion[1])
        return [s[0] for s in suggestions]

def equalsIgnoreTypo(suspect, word):
    typo = suspect == word

    # letter deletion
    # try deleting letter from suspect to see if it equals word
    typo = typo or equalIfDeleteLetter(suspect, word)

    # letter addition
    # adding to suspect is the same as deleting from word
    typo = typo or equalIfDeleteLetter(word, suspect)

    # letter substitution
    # count how many letters are different between the two words.
    if not typo and len(suspect) == len(word):
        diff = 0
        for i in range(len(suspect)):
            if suspect[i] != word[i]:
                diff += 1
        typo = diff == 1
    return typo

def equalIfDeleteLetter(deletable, word):
    if len(deletable) - len(word) != 1:
        return False
    i = 0
    while i < len(word) and deletable[i] == word[i]:
        i += 1
    while i + 1 < len(deletable) and i < len(word) and deletable[i] == word[i]:
        i += 1
    return i == len(word)

#main
suggester = TagSuggester()
noteCount = int(sys.stdin.readline().strip())
for i in range(noteCount):
    suggester.addNote("", sys.stdin.readline().strip())
queryCount = int(sys.stdin.readline().strip())
for i in range(queryCount):
    suggestions = suggester.getSuggestions(sys.stdin.readline().strip())
    output = ""
    for tag in suggestions:
        output += tag + ","
    print(output[: -1])