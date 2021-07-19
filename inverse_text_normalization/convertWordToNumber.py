list_month = \
[
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December',
]

from os import read, replace
from word2number import w2n
import word2number

def getAllDayFromMonth():
    with open('day.txt','r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def readDictDay():
    result = {}
    with open('dict_day.txt','r') as f:
        for line in f:
            line = line.strip()
            date , num = " ".join(line.split()[:-1] ), line.split()[-1]
            result[date] = num 
    return result

list_day = getAllDayFromMonth()
list_month = [month.lower() for month in list_month]
list_day = list_day[::-1]
dict_day = readDictDay()

def splitDateString(string):
    pass

def convertDateFromStringToNum(string):
    pass 

def decompositDate(string):
    string = string.lower()
    day , month , year = '' , '' , ''
    for d in list_day:
        if d in string:
            day = d 
            string = string.replace(d,'')
    for m in list_month:
        if m in string:
            month = m 
            string = string.replace(m ,'')
    string = string.replace('of','').replace('the','')
    string =string.strip()
    if string!= '':
        year = string 
    return day , month , year 


def readYear(string):
    if 'thousand' in string :
        return str(w2n.word_to_num(string))
    else:
        head , tail = string.split()[0] , " ".join(string.split()[1:])
        return str(w2n.word_to_num(head)) + str(w2n.word_to_num(tail))

def readDay(string):
    try:
        return dict_day[string]
    except:
        return string

def readDate(string):
    #type date 
    result = ''
    day , month , year = decompositDate(string)
    if day != '':
        d = readDay(day)
    else:
        d = ''
    if month != '':
        m = month.capitalize()
    else:
        m =''
    if year != '':
        y = readYear(year)
    else:
        y =''
    if string.split()[0].lower() == month.lower():
        return m + " " +  d +"," +" " + y 
    else:
        return d +" "+m + " "+y

def testDate():
    with open('test_date.txt','r') as f:
        for line in f:
            line = line.strip()
            print('>>>>>>>>>>>>>>>>>>>>>>>>>..', line)
            print(readDate(line))

def readNumber(string):
    #type : CARDINAL , DECIMAL 
    return str(w2n.word_to_num(string))

def readDigit(string):
    #DIGIT
    dict_digit  = {'o': 0 ,'one':1, 'two':2 , 'three':3,'four':4 \
        ,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

    list_token = string.split()
    result = []
    for token in list_token :
        result.append(str(dict_digit[token]))
    return "".join(result)

def readVERBATIM(string):
    #VERBATIM
    pass 

# text = 'one hundred twenty four point one'
# text = 'one hundred sixty six'
# print(readNumber(text))

# text = 'one nine nine o o seven one six'
# text = 'one o six one'
# print(readDigit(text))

# def splitMeasure():
    
# def splitMeasure(stringin , stringout):
#     try:
#         list_token = stringout.split()
#         init_number = w2n.word_to_num(stringout.split()[0])
#         index_number = 1
#         if len(stringout.split()) > 2:
#             for i in range(2 , len(list_token)):
#                 if list_token[i-1] =='point':
#                     continue
#                 else:
#                     temp_number = w2n.word_to_num(" ".join(list_token[:i]))
#                     if str(temp_number) == str(init_number):
#                         break 
#                     else:
#                         init_number = temp_number
#             index_number = i 
#         number = " ".join(list_token[:index_number])
#         number = str( w2n.word_to_num(number))
#         measure_in = stringin.replace(number,'')
#         measure_out = " ".join(list_token[index_number:])
#         return measure_in , measure_out
#     except:
#         return stringin, stringout
def splitMeasure(stringin , stringout):
    stringout = stringout.replace(' o ',' zero ')
    stringin = stringin.replace(',','.')
    # try:
    index_number = 0
    list_token = stringout.split()
    for i in range(len(list_token) -1 , -1 , -1 ):
        # print(i)
        try :
            num = w2n.word_to_num(" ".join(list_token[i:]))
            # print('num ', num)
            index_number = i + 1
            # print('fdfd', index_number)
            break
        except:
            continue
    # print('inx' ,index_number)
    if index_number > 0 :
        number = " ".join(list_token[:index_number])
        number = str( w2n.word_to_num(number))
        measure_in = stringin.replace(number,'')
        measure_out = " ".join(list_token[index_number:])
        return measure_in , measure_out
    else:
        return stringin , stringout
    # except:
    #     return stringin, stringout

def filterMeasure(filein , fileout):
    list_measure = {}
    c =0 
    with open(filein , 'r') as f_in , open(fileout , 'w') as f_out:
        for line in f_in :
            try:
                c +=1 
                print(c)
                inp , out = line.strip().split('\t')[0], line.strip().split('\t')[1] 
                mein , meout = splitMeasure(inp , out)
                if mein not in list_measure:
                    list_measure[mein] = meout 
            except:
                continue
        for mein in list_measure:
            f_out.write(mein +"\t"+list_measure[mein] +"\n")

# filterMeasure('data_process/all_line_measure.txt', 'data_process/measure.txt')
# print(w2n.word_to_num('six kilometers per hour'))
# stringin ,stringout = '3500/3400 cal' , 'three thousand five hundred three thousand four hundredths of a cal'
# print(splitMeasure(stringin , stringout))

# with open('data_process/measure.txt','r') as f_in , open('a.txt','w') as f_out:
#     result = [] 
#     for line in f_in :
#         line = line.strip()
#         inp, out = line.split('\t')
#         if len(inp.split()) > 1 :
#             result.append(" ".join(inp.split()[1:]) +"\t" + out)
#     f_out.write("\n".join(set(result)))


# print(w2n.word_to_num('two thousand eight hundred eighty firsts'))

def splitUnitMeasure(string):
    pass 

def readMeasureFromFile():
    c = 0
    result = {}
    with open('data_process/measure_tail.txt' , 'r') as f_r:

        lines = f_r.readlines()
        lines = [t.strip() for t in lines]
        for line in lines:
            abb , full = line.split('\t')[0] , line.split('\t')[1]
            result[full] = abb 
    return result

def readMeasureWithNum(string, dict_measure):
    list_measure = [t for t in dict_measure]
    reverse_list_measure = sorted(list_measure , key = len , reverse=True)
    valid_measure = False
    for measure in reverse_list_measure:
        if measure in string:
            valid_measure= True 
            number = string.replace(measure , '')
            unit_measure = dict_measure[measure]
            break
    if valid_measure == False:
        return string 
    else:
        string_number = str(w2n.word_to_num(number))
        if unit_measure[0] == '/' or unit_measure == '%':
            return string_number+unit_measure
        else:
            return string_number +" "+unit_measure


def decompotionNumberString(string):
    dict_value = {'billion':'','million':'','thousand':'','hundred':'','unit':''}
    unit = ['billion','million','thousand','hundred']
    current_string = string

    list_token = current_string.split('billion',1)
    if len(list_token) > 1 : 
        dict_value['billion'] = list_token[0].strip()
        current_string = " ".join(list_token[1:])

    list_token = current_string.split('million',1)
    if len(list_token) > 1 :
        dict_value['million'] = list_token[0].strip()
        current_string = " ".join(list_token[1:])

    list_token = current_string.split('thousand',1)
    if len(list_token) >  1:
        dict_value['thousand'] = list_token[0].strip()
        current_string = " ".join(list_token[1:])

    list_token = current_string.split('hundred',1)
    if len(list_token) >  1:
        dict_value['hundred'] = list_token[0].strip()
        current_string = " ".join(list_token[1:])   

    dict_value['unit'] = current_string.strip()


    return dict_value
    
def checkValidUnit(string):
    if string =='':
        return True

    list_token = string.split()
    if len(list_token) > 2:
        return False
    else:
        try:
            num = w2n.word_to_num(string)
            if len(list_token) == 1:
                if num > 100:
                    return False
            else:
                if 'ten' in string or 'eleven' in string or 'twelve' in string:
                    return False

                else:
                    if float(computeValue(list_token[0])) < 10 and float(computeValue(list_token[1])) < 10 :
                        return False
                    if float(computeValue(list_token[0])) < float(computeValue(list_token[1]))  :
                        return False
                    if float(computeValue(list_token[0])) > 9 and float(computeValue(list_token[0])) < 20:
                        return False
                    if float(computeValue(list_token[0])) > 9 and float(computeValue(list_token[1])) > 9:
                        return False
        except:
            return False
    return True

def checkValidNumber(string):

    if string == '':
        return False

    unit = ['billion','million','thousand','hundred']

    if string.split()[0] in unit:
        return False

    decom_number = decompotionNumberString(string)

    # print('decom ', decom_number)

    if checkValidThousand(decom_number['billion']) == True \
        and checkValidThousand(decom_number['million']) == True \
            and checkValidThousand(decom_number['thousand']) ==True \
                and checkValidUnit(decom_number['hundred']) == True \
                    and checkValidUnit(decom_number['unit']) == True :
                    return True
    return False

def computeValue(token):
    return str(w2n.word_to_num(token))

def replaceOrdinalToNumberInFraction(string):

    def replaceSpecialWord(stri):
        special_oridinary = {'first':'one','second':'two','third':'three' ,'fifth':'five','eighth':'eight',\
            'ninth':'nine','twelfth':'twelve','a':'one','an':'one','quarter':'four','fourth':'four','half':'two','halve':'two'}
        result = []
        for token in stri.split():
            if token in special_oridinary:
                result.append(special_oridinary[token])
            else:
                result.append(token)
        return " ".join(result)

    string = string.lower()

    last_token = string.split()[-1]

    if last_token[-1] == 's':
        last_token = last_token[:-1]
    
    temp = " ".join(string.split()[:-1]) + " " + last_token

    temp = replaceSpecialWord(temp)

    last_token = temp.split()[-1]

    last_token = last_token.replace('ieth','y')
    if last_token[-2:] == 'th':
        last_token = last_token[:-2]

    return   " ".join(temp.split()[:-1]) +" " + last_token


def splitRawFraction(string):

    if ' over ' in string :
        list_segment = string.split('over')
        return [list_segment[0] , list_segment[1]]

    num_replace = replaceOrdinalToNumberInFraction(string)

    print('num ', num_replace)

    if len(num_replace.split()) == 1 :
        return [num_replace]

    if len(num_replace.split()) == 2:
        return num_replace.split()

    # if num_replace.split()[-1] in ['billion','million','thousand','hundred']:
    #     return [ " ".join(num_replace.split()[:-1]) , num_replace.split()[-1] ]

    list_token = num_replace.split()

    if string.split()[-1] == 'firsts' :
        index_start = len(list_token) - 2
    else:
        index_start = len(list_token) - 1

    for i in range(index_start , -1 , -1):
        print(i, '  ', " ".join(list_token[:i]), '   ', " ".join(list_token[i:]))
        if checkValidNumber(" ".join(list_token[:i])) == True and checkValidNumber(" ".join(list_token[i:])) == True:
            break 
    
    
    if i == 0:
        return [string]
    else:
        return [" ".join(list_token[:i]) , " ".join(list_token[i:])]

def checkValidThousand(string):
    decom = decompotionNumberString(string)
    hun, unit = decom['hundred'] , decom['unit']
    if checkValidUnit(unit) == False:
        return False
    else:
        if hun == '':
            return True
        else:
            if w2n.word_to_num(hun) > 9 :
                return False 
            else:
                return True

def readRawFraction(string):
    list_segment = splitRawFraction(string)
    print('list segment ', list_segment)
    if len(list_segment) == 1:
        return string
    else:
        try:
            return str(w2n.word_to_num(list_segment[0])) +"/" + str(w2n.word_to_num(list_segment[1]))
        except:
            print('error read raw fraction')
            return string 

def readFraction(raw_string):
    if 'minus' in raw_string:
        isMinus = True
    else:
        isMinus = False
    string = raw_string.replace('minus','')
    if ' and ' not in string:
        temp = readRawFraction(string) 
        print('temp ',temp)
        if isMinus == True:
            return '-'+temp
        else:
            return temp
    else:
        mix = string.split(' and ')
        try :
            inte = str(w2n.word_to_num(mix[0]))
            fraction = readRawFraction(mix[1])
            if isMinus == True:
                return '-'+inte+" and " + fraction
            else:
                return inte+" and " + fraction
        except:
            print('error read mixed number ')
            return raw_string

def readOdinal(string):
    tail = string.split()[-1][-2:]
    def replaceSpecialWord(stri):
        special_oridinary = {'first':'one','second':'two','third':'three' ,'fifth':'five','eighth':'eight',\
            'ninth':'nine','twelfth':'twelve','a':'one','an':'one','quarter':'four','fourth':'four','half':'two','halve':'two'}
        result = []
        for token in stri.split():
            if token in special_oridinary:
                result.append(special_oridinary[token])
            else:
                result.append(token)
        return " ".join(result)
    
    temp = replaceSpecialWord(string)
    last_token = temp.split()[-1]
    last_token = last_token.replace('ieth','y')
    if last_token[-2:] == 'th':
        last_token = last_token[:-2]
    head = " ".join(temp.split()[:-1]) +" " + last_token
    print(head)
    try:
        return str(w2n.word_to_num(head)) + tail
    except:
        print('error convert ordinal ')
        return string

def splitNumberTimeAndTail(str2):
    number , tail = [] , [] 
    for token in str2.split():
        if len(token) > 1:
            number.append(token)
        else:
            tail.append(token)
    if len(tail) > 0 :
        return [" ".join(number), "".join(tail)]
    else:
        return [" ".join(number)]

def readHourAndMinute(string):    
    pattern = ['am','pm','gmt','cest']
    

    

if __name__ == "__main__":

    text = 'one fifty seven a m'
    print(splitNumberTimeAndTail(text))