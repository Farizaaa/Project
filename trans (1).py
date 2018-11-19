import time
import os

csvfile = "files.csv"

def ReadDict(csv_file):
    with open(csv_file) as raw_data:
        for item in raw_data:
            if ':' in item:
                key,value = item.split(':',1)
                print('%s - %s' %(key,value))
            else:
                print("No data found")

def WriteDict(csv_file, dictionary):
    with open(csv_file,'w') as f:
        for key, value in dictionary.items():
            f.write('%s:%s\n' %(key,value))

def DeleteWord(csv_file,word):
    new_dict={}
    with open(csv_file) as raw_data:
        for item in list(raw_data):
            key = item.split(":")[0]
            value = item.split(":")[1].rstrip("\n")
            if key == word:
                del item
                print("Deleted")
            else:
                new_dict.update({key:value})
        WriteDict(csvfile,new_dict)
        return new_dict

def EditWord(csv_file,word):
    new_dict={}
    with open(csv_file) as raw_data:
        for item in list(raw_data):
            key = item.split(":")[0]
            value = item.split(":")[1].rstrip("\n")
            if key == word:
                translate= input('Translation of %s: ' %(word))
                new_dict.update({key:translate})
            else:
                new_dict.update({key:value})
        WriteDict(csvfile,new_dict)
        return new_dict

def CheckWord(csv_file, word):
    with open(csv_file) as raw_data:
        result = False
        for item in raw_data:
            if ':' in item:
                key,value = item.split(':',1)
                if key == word:
                    result = True
                else:
                    result = False
        return result

def SearchWord(csv_file,word):
    with open(csv_file) as raw_data:
        for item in raw_data:
            if ':' in item:
                key,value = item.split(':',1)
                if word in key:
                    print('%s - %s' %(key,value))
            else:
                print('No such data found')

while True:
    print("""
	1. Add words
	2. Edit words
	3. Delete words
	4. Search words
	5. Show all words
	6. Exit """)

    menu = int(input('Choose an option: '))
    if menu == 1:
        if os.path.isfile(csvfile):
            with open(csvfile,'a') as f:
                word = input('Enter your word: ')
                if CheckWord(csvfile, word) is False:
                    translate = input('Enter translation of word: ')
                    f.write('%s:%s\n' %(word, translate))
                else:
                    print('Already exists')
        else:
            with open(csvfile,'w') as f:
                word = input('Enter your word: ')
                if CheckWord(csvfile, word) is False:
                    translate = input('Enter translation of word: ')
                    f.write('%s:%s\n' %(word, translate))
                else:
                    print('Already exists')

    elif menu == 2:
        word = input('Enter the word: ')
        print(EditWord(csvfile,word))

    elif menu == 3:
        print(DeleteWord(csvfile,input('Enter the word: ')))

    elif menu == 4:
        word = input('Enter the word: ')
        SearchWord(csvfile,word)

    elif menu == 5:
        ReadDict(csvfile)
        time.sleep(2)

    elif menu == 6:
        print('Bye-bye!!!')
        break

    else:
        print('No such number in menu')
        time.sleep(2)
