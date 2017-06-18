from urllib import request, parse

def read_text():
    file = open("D:\Classes\Python\\text.txt")
    file_contents = file.read()
    #print(file_contents)
    file.close()
    check_profanity(file_contents)

def check_profanity(text_check):
    url = "http://www.wdylike.appspot.com/?q="
    url = url + parse.quote(text_check)
    req = request.urlopen(url)
    answer = req.read()
    #print(answer)
    req.close()
    if b'true' in answer:
        print('PROFANITY!')
    elif b'false' in answer:
        print('No profane words detected')
    else:
        print('Failed to detect a true or false.')
    print('\n')

read_text()    
