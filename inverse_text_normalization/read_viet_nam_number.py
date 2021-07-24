# from convertWordToNumber import readDigit
from vietnam_number import w2n , w2n_couple , w2n_single

dict_link = {'phần':'/' , 'chấm':'.' , 'phẩy':',','mỗi':'/'}

text = 'một triệu không trăm năm mươi ba nghìn không trăm linh năm'

def isCardinal(string):
    try:
        w2n(string)
        return True 
    except:
        return False

def isInNumber(word):
    number = ['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín','mười','tư','lăm','linh','lẻ','mốt']
    decima = ['tỷ','triệu','nghìn','trăm','chục','mươi']
    if word in number or word in decima:
        return True 
    else:
        return False

def checkNumberSegment(segment):
    list_token = segment.split()
    for token in list_token:
        if isInNumber(token) == False:
            return False
    return True

def splitStringToSegment(string):
    list_token = string.split()
    result = []
    current_non_number  , current_number = [] , [] 
    for i in range(len(list_token)):
        if isInNumber(list_token[i]) == True :
            current_number.append(list_token[i])
            if len(current_non_number) > 0 :
                result.append(" ".join(current_non_number))
                current_non_number = []
        else:
            current_non_number.append(list_token[i])
            if len(current_number) > 0 :
                result.append(" ".join(current_number))
                current_number = []
    if current_number != [] :
        result.append(" ".join(current_number))
    if current_non_number != []:
        result.append(" ".join(current_non_number))

    return result

def isSegmentNumber(string):
    if isInNumber(string.split()[0]) == True :
        return True 
    else:
        return False


def isTimeString(string):
    list_token = string.split()
    if 'giờ' in list_token:
        return string 

def readSegmentDigit(string):
    list_token = string.split()
    dict_digit = {'không':'0','một':'1','hai':'2','ba':'3','bốn':'4','năm':'5','sáu':'6','bảy':'7','tám':'8','chín':'9'}
    result = []
    for token in list_token:
        result.append(dict_digit[token])
    return "".join(result)

def readDate(string):
    #phải có tháng thì mới là date , string not contain punctuation
    segment_month = string.split('tháng')
    tail_month = " ".join(segment_month[1:])
    containYear = False
    if len(tail_month.split()) > 2 :
        containYear = True
    if containYear == False:
        list_segment = splitStringToSegment(string)
        result = [] 
        for segment in list_segment:
            if isCardinal(segment) == True :
                result.append(str(w2n(segment)))
            else:
                if segment == 'tháng':
                    result.append('/')
        return "".join(result)
    else:
        #split year 
        segment_year = []
        result = []
        if tail_month.split()[0] =='năm':
            if tail_month.split()[1] =='năm':
                try:
                    segment_year = ['năm','năm'," ".join(tail_month.split()[2:])]

                    list_segment_head_month = splitStringToSegment(segment_month[0])

                    for segment in list_segment_head_month:
                        if isCardinal(segment) == True :
                            result.append(str(w2n(segment)))
                    result.append('/')
                    result.append('5')
                    result.append('/')
                    result.append(str(w2n(" ".join(tail_month.split()[2:]))))
                    print(result)
                    return "".join(result)
                except: 
                    return string 
            else:
                return string 
        else:
            segment_year = tail_month.split('năm', 1)
            month = segment_year[0]
            year = segment_year[1]
            try : 
                w2n(month)
                w2n(year)
                result = [] 
                list_segment_head_month = splitStringToSegment(segment_month[0])
                for segment in list_segment_head_month:
                    if isCardinal(segment) == True :
                        result.append(str(w2n(segment)))
                result.append('/')
                result.append(str(w2n(month)))
                result.append('/')
                result.append(str(w2n(year)))
                print('result ' , result)
                if result[0] == '/':
                    return "".join(result[1:])
                return "".join(result)
            except: 
                return string 

#phan ra 3 loai so co the doc : cardinal , telephone , date , time , currency (số có đi kèm đơn vị), số có kèm chữ

def readTimeString(string):
    list_segment = splitStringToSegment(string)
    result = []
    for i in range(len(list_segment)):
        if list_segment[i] == 'giờ':
            if i == len(list_segment) - 1:
                result.append('h')
            else:
                result.append(':')
        if list_segment[i] == 'phút':
            if i < len(list_segment) - 1 :
                result.append(':')
        if list_segment[i] not in ['phút','giờ','giây']:
            result.append(str(w2n(list_segment[i])))
    return "".join(result)
        

def readStringNumber(string):
    if 'tháng' in string:
        if 'tháng' == string.split()[-1]:
            return readNormalNumber(string)
        else:
            return readDate(string)
    else:
        if 'giờ' in string:
            return readTimeString(string)
        else:
            return readNormalNumber(string)

def readTailNumberFromFile():
    result = {}
    with open('tail_number.txt' ,'r') as f_r:
        lines = f_r.readlines()
        lines = [t.strip() for t in lines]
        for line in lines :
            result[" ".join(line.split()[:-1])] = line.split()[-1]
    return result

def readAllAlphaFromFile():
    result = {}
    with open('alphabe.txt','r') as f_r:
        lines = f_r.readlines()
        lines = [t.strip() for t in lines]
    for line in lines :
        result[" ".join(line.split()[:-1])] = line.split()[-1]
    return result

def readSegmentAlpha(segment):
    all_alphabet = readAllAlphaFromFile()
    all_tail = readTailNumberFromFile()
    print()
    #can phai sap xep lai thu tu cac tail va alpha 
    
    list_token = segment.split()
    for tail in all_tail :
        if tail in segment :
            segment = segment.replace(tail , all_tail[tail])
    for alpha in all_alphabet:
        if alpha in segment:
            if len(alpha) > 1:
                segment = segment.replace(alpha , all_alphabet[alpha])
    return "".join(segment)

def mergeSingleToken(segment):
    list_token = segment.split()
    result , temp = [] , []
    for token in list_token :
        if len(token) > 1:
            if temp != []:
                result.append("".join(temp).upper())
                temp = []
            result.append(token)
        else:
            temp.append(token)
    if temp != []:
        result.append(''.join(temp).upper())
    return "".join(result)

def checkDigitSegment(segment):
    list_token = segment.split()
    number = ['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín','lăm']
    for token in list_token :
        if token not in number:
            return False 
    return True 

def readCardinalNumber(segment):
    return str(w2n(segment))

def insertCommaToStringNumber(string):
    list_character = list(string)
    inverse_list_character = list_character[::-1]
    chunks = ["".join(inverse_list_character[i:i + 3]) for i in range(0, len(inverse_list_character), 3)]
    return ".".join(chunks)[::-1]

def readDigitNumber(segment):
    list_token = segment.split()
    return "".join([str(w2n(token)) for token in list_token])

def readNormalNumber(string):
    list_segment = splitStringToSegment(string)
    print('list segment ' ,list_segment)
    result = []
    for segment in list_segment:
        print(segment)
        if segment in dict_link:
            result.append(dict_link[segment])
        else:
            if checkNumberSegment(segment) == True :
                if checkDigitSegment(segment) == True:
                    result.append(readDigitNumber(segment))
                else:
                    result.append(insertCommaToStringNumber(readCardinalNumber(segment)))
            else:
                result.append(mergeSingleToken(readSegmentAlpha(segment)))
    return "".join(result)


# def mergeNumber(string):


text = 'ba chín tỷ năm trăm triệu phẩy không ba hai bốn ki lô gam a bê xê _.'
text ='mùng sáu tháng mười năm hai nghìn không trăm mười chín'
text = 'không chín một ba hai tám tám sáu chín sáu'
print(readStringNumber(text))