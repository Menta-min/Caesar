import sys
abc:str='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'  #26 букв англ алфавита a-0 индекс, z-25 индекс
ABC:str='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers:str='123456789.,!? '
sym:str='.,!?'
error:int=0

def encryptionCaesar(text: str,shifr: int)-> str:
    encripted:str='' #изначально зашифрованная строка пуста
    global error 
    for i in text:
        if i in abc: #если то, что мы ввели - прописная буква
            encripted=encripted+str(abc[abc.find(i)+shifr])   
        elif i in ABC: #если то, что мы ввели - заглавная буква
            encripted=encripted+str(ABC[ABC.find(i)+shifr])
        elif i in sym or i in numbers: #если символ - число,пробел или ".!?" то оставляем его как есть
            encripted=encripted+i
        else:
            error+=1 #если введенный символ не из нашего списка a-z, A-Z, 0-9, ".,!?" то введем счетчик ошибок, если будет !=0 то выведем, что какое-то символ не шифровался
    print('Зашифрованный текст:', encripted)
    return encripted
   
def decryptionCaesar(text: str,shifr: int)-> str:
    decripted=''#изначально расшифрованная строка пуста
    for i in text:
        if i in sym or i in numbers: #если символ - число, пробел или ".!?"
            decripted=decripted+i
        elif i in ABC:
            decripted=decripted+str(ABC[ABC.find(i,26,51)-shifr]) # в этот раз поиск find начинаем не с 1 символа, а с 26 по 51 (2 часть алфавита, так как для дешифра мы отнимаем)
        elif i in abc:
            decripted=decripted+str(abc[abc.find(i,26,51)-shifr])
        
    print('Обратно расшифрованный текст: ',decripted)
    return decripted
            
print('Введите текст для шифрования (Используйте заглавные и строчные буквы англ. алфавита, а также цифры и символы .,!?)')
textinput=input() 

print('Введите число смещения шифра от 1 до 25')
shifr=input() #1-25

if shifr not in numbers or shifr=='':#проверка введения пустой строки, или не 1-25
    print('Вы не ввели число смещения шифра,или ввели число не от 1 до 25. Попробуйте заново')
    sys.exit()
    
encrypt=encryptionCaesar(textinput,int(shifr)) #вызов функции шифрования
decryptionCaesar(encrypt,int(shifr)) #вызов функции дешифровки

if error!=0: #проверка на ввод недопустимых символов
    print('Вы ввели недостустимый символ, который не входит в список a-z, A-Z, 0-9, ".,!?",он не был зашифрован, остальные символы были зашифрованы')