import nltk
import pymorphy2


list_perfomance = ['меня','да это','зовут']
list_gretings = ['здравствуйте','добрый']
list_farewall = ['свидания','доброго','хорошего']
list_company = ['компания']
prob_thresh = 0.4
list_check = []
morph = pymorphy2.MorphAnalyzer()

def extract_gretings(number_dialog,number_replic,text):
    if list_gretings[0] in text:
        print(number_dialog,number_replic,text)
        list_check.append(True)

def extract_perfomance_and_name(number_dialog,number_replic,text):
    if (list_perfomance[0] in text and list_perfomance[2] in text) or list_perfomance[1] in text:
        print(number_dialog,number_replic,text)
        for word in nltk.word_tokenize(text):
            for p in morph.parse(word):
                #print(p.tag,'-------',word)
                if 'Name' in p.tag and p.score >= prob_thresh:
                    print(word)

def extract_company(number_dialog,number_replic,text):
    if list_company[0] in text:
        print(number_dialog,number_replic,text)
        list_text = text.split()
        index = list_text.index(list_company[0])
        next_index = index + 1
        p = morph.parse(list_text[next_index])
        if 'NOUN' in p[0].tag or 'ADJF' in p[0].tag:
            print(p[0].tag,'----',list_text[next_index])

def extract_farewall(number_dialog,number_replic,text):
    if list_farewall[0] in text or list_farewall[1] in text or list_farewall[2] in text:
        print(number_dialog,number_replic,text)
        list_check.append(True)

def check_gretings_and_repfomance(number_dialog):
    if len(list_check) == 2: 
        if list_check[0] and list_check[1]:
            print('Номер диалога',number_dialog, 'поздаровался и попрощался')
            list_check.clear()

def find_element(data_dialog):
    number_dialog = data_dialog[0]
    number_replic = data_dialog[1]
    text = data_dialog[3].lower()
    extract_gretings(number_dialog,number_replic,text)
    extract_perfomance_and_name(number_dialog,number_replic,text)
    extract_company(number_dialog,number_replic,text)
    extract_farewall(number_dialog,number_replic,text)
    check_gretings_and_repfomance(number_dialog)


def read_file():    
    with open('test_data.csv','r',encoding='utf-8') as file:
        data_text = file.readlines()
    return data_text

def main():
    for dialog in read_file():
        data_dialog = dialog.split(',')
        if data_dialog[2] == 'client':
            #print(data_dialog)
            find_element(data_dialog)

if __name__ == '__main__':
    main()
