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

from io import TextIOBase
from os import read, replace, write
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
        ,'five':5,'six':6,'seven':7,'eight':8,'nine':9 , 'zero':0}

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
	dict_value = {'trillion':'','billion':'','million':'','thousand':'','hundred':'','unit':''}
	current_string = string

	list_token = current_string.split('trillion',1)
	if len(list_token) > 1 : 
		dict_value['trillion'] = list_token[0].strip()
		current_string = " ".join(list_token[1:])

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

def readExtendTime(string):
    result = ''
    string = string.replace(' and ',' ')
    decompositTime = decompotionTimeString(string)
    if decompositTime['hour'] != '':
        result+=(str(w2n.word_to_num(decompositTime['hour'])))+":"
    if decompositTime['minute'] != '':
        result+=(str(w2n.word_to_num(decompositTime['minute'])))+":"
    else:
        result+=(str(00))
    if decompositTime['second'] != '':
        result+=(str(w2n.word_to_num(decompositTime['second'])))+"."
    else:
        result+=(str(00))
    if decompositTime['millisecond'] != '':
        result+=(str(w2n.word_to_num(decompositTime['millisecond'])))
    else:
        result= result.replace('.','')
    return result

def decompotionTimeString(string):
    string = string.replace(' and ', ' ')
    dict_value = {'hour':'','minute':'','second':'','millisecond':''}
    string = string.replace('hours','hour').replace('minutes','minute').replace('seconds','second').replace('milliseconds','millisecond')
    current_string = string

    list_token = current_string.split('hour',1)
    if len(list_token) > 1 : 
        dict_value['hour'] = list_token[0].strip()
        current_string = " ".join(list_token[1:])

    list_token = current_string.split('minute',1)
    if len(list_token) > 1 :
        dict_value['minute'] = list_token[0].strip()
        current_string = " ".join(list_token[1:])

    list_token = current_string.split('second',1)
    if len(list_token) >  1:
        dict_value['second'] = list_token[0].strip()
        current_string = " ".join(list_token[1:])

    list_token = current_string.split('millisecond',1)
    if len(list_token) >  1:
        dict_value['millisecond'] = list_token[0].strip()

    return dict_value


def readTailTime():
    with open('all_tail_time.txt','r') as f_r:
        lines = f_r.readlines()
        lines = [line.strip() for line in lines]
    return lines


def getListPattern(tail):
    pattern = readTailTime()
    result = []
    current_string = tail.lower()
    for pa in pattern:
        if pa.lower() in current_string:
            result.append(pa)
            current_string = current_string.replace(pa.lower(),'')
    return " ".join(result)


def readHourAndMinute(string):    
    pattern = ['am','pm','gmt','cest']
    list_segment = splitNumberTimeAndTail(string)
    number = list_segment[0]
    if len(list_segment) == 2:
        tail = list_segment[1]
    else:
        tail = ''
    list_num = splitRawFraction(number)
    if len(list_num) == 1:
        hour = str(w2n.word_to_num(list_num[0]))
        minute = ''
    else:
        hour = str(w2n.word_to_num(list_num[0]))
        minute = str(w2n.word_to_num(list_num[1]))
    
    pattern = getListPattern(tail)
    if minute == '':
        return hour + " " + pattern
    else:
        return hour+":"+minute +" "+ pattern

def readTime(string):
    if 'hour' in string or 'hours' in string or 'minute' in string or 'minutes' in string \
    or 'second' in string or 'seconds' in string or 'millisecond' in string or 'milliseconds' in string:
        return readExtendTime(string)
    else:
        return readHourAndMinute(string)
    
def removeNumberFromMoney(string):
    result = []
    for c in string:
        if c.isnumeric() == False and c != ',' and c != '.':
            result.append(c)
    return "".join(result).replace('million','').replace('billion','').strip()

def findNumberFromMoney(string):
    list_token = string.split()
    index_end = 0
    for i in range(len(list_token) - 1 , -1 , -1 ):
        current_string = " ".join(list_token[i:])
        try :
            w2n.word_to_num(current_string)
            index_end = i + 1
            break
        except:
            continue
    if index_end == 0 :
        return string 
    else:
        if list_token[index_end] =='trillion':
            return " ".join(list_token[:index_end+1])
        return " ".join(list_token[:index_end])

def findPairCurrency(output, input):
    number_string = findNumberFromMoney(input)
    number = str(w2n.word_to_num(number_string))
    unit_output = output.replace(',','').replace(number , '').strip()
    unit_input = input.replace(number_string,'').strip()
    return (unit_input , unit_output)

def readCurrencyFromFile():
    result = {}
    with open('tail_currency.txt','r') as f_r:
        for line in f_r:
            line = line.strip()
            if len(line.split()) == 1:
                result[line] = line 
            else:
                input = " ".join(line.split()[:-1])
                output = line.split()[-1]
                if input[-1] == 's' :
                    input = input[:-1]
                result[input] = output
    return result

def readNoneMixedMoney(string):
    list_unit = readCurrencyFromFile()
    number = findNumberFromMoney(string)
    unit = string.replace(number , '').strip()
    number = readNumberMoney(number)
    number = insertCommaToNumberMoney(number)
    if unit == '':
        return number
    if unit[-1] =='s':
        unit = unit[:-1]
    if unit in list_unit:
        unit = list_unit[unit]
        return unit+number
    else:
        return number +" "+ unit

def insertCommaToNumberMoney(string):

    if len(string.split()) == 1:
        list_character = list(string)
        inverse_list_character = list_character[::-1]
        chunks = ["".join(inverse_list_character[i:i + 3]) for i in range(0, len(inverse_list_character), 3)]
        return ",".join(chunks)[::-1]
    elif len(string.split()) == 2:
        unit = string.split()[1]
        true_number = string.split()[0]
        if '.' not in true_number:
            list_character = list(true_number)
            inverse_list_character = list_character[::-1]
            chunks = ["".join(inverse_list_character[i:i + 3]) for i in range(0, len(inverse_list_character), 3)]
            return ",".join(chunks)[::-1] + " " + unit 
        else:
            # . in string 
            seg_1= string.split('.')[0]
            seg_2=string.split('.')[1]
            list_character = list(seg_1)
            inverse_list_character = list_character[::-1]
            chunks = ["".join(inverse_list_character[i:i + 3]) for i in range(0, len(inverse_list_character), 3)]
            return ",".join(chunks)[::-1] + "."+seg_2
    else:
        return string

def readNumberMoney(string):
    if 'point' not in string:
        return str(w2n.word_to_num(string))
    else:
        #point in string 
        unit_number = string.split()[-1]
        number = " ".join(string.split()[:-1])
        return str(w2n.word_to_num(number)) + " " +unit_number

def readMixNumberMoney(string):
    list_unit = readCurrencyFromFile()
    if ' and ' not in string:
        return readNoneMixedMoney(string)
    else:
        #and in string
        money_1 = string.split(' and ')[0]
        money_2 = string.split(' and ')[1]
        number_1 = findNumberFromMoney(money_1)
        unit = money_1.replace(number_1 , '').strip()
        number_1 = readNumberMoney(number_1)
        number_2 = findNumberFromMoney(money_2)
        number_2 = str(w2n.word_to_num(number_2 ) / 100).split('.')[1]
        total_number = insertCommaToNumberMoney(number_1)+'.'+number_2

        if unit == '':
            return total_number
        if unit[-1] =='s':
            unit = unit[:-1]
        if unit in list_unit:
            unit = list_unit[unit]
            return unit+total_number
        else:
            return total_number +" "+ unit

def replaceZeroInAddress(string):
    list_token = string.split()
    result = []
    for token in list_token:
        if token =='o':
            result.append('zero')
        else:
            result.append(token)
    return " ".join(result)

def checkAddressType2(string):
    list_token = string.split()
    for token in list_token:
        if w2n.word_to_num(token) > 9 :
            return False
    return True

def readNumberAdsress(string):
    string  = replaceZeroInAddress(string)
    if 'million' in string or 'hundred' in string or 'thousand' in string or 'billion' in string:
        return readNumberAddressType1(string)
    if checkAddressType2(string) == True:
        return readNumberAddressType2(string)
    try:
        return readNumberAddressType3(string)
    except:
        return string

def readNumberAddressType1(string):
    return str(w2n.word_to_num(string))

def readNumberAddressType2(string):
    return "".join([str(w2n.word_to_num(t)) for t in string.split()])

def readNumberAddressType3(string):
    result, temp = [] , []
    list_token = string.split()
    for i in range(len(list_token)):
        if temp == [] :
            temp.append(list_token[i])
        else:
            current_element = temp[-1]
            if checkValidUnit(current_element +" "+list_token[i]) == False:
                result.append(str(w2n.word_to_num(current_element)))
                temp = [list_token[i]]
            else:
                temp = []
                result.append(str(w2n.word_to_num(current_element + " "+ list_token[i])))
    if temp != []:
        result.append(str(w2n.word_to_num(temp[-1])))
    return "".join(result)  

def readAddress(string):
    if string == '':
        return ''
    string = replaceZeroInAddress(string)
    unit = ['billion','million','thousand','hundred']
    list_token = string.split()
    result = []
    for i in range(len(list_token)):
        if checkValidNumber(list_token[i]) == True or list_token[i] in unit:
            result.append(list_token[i])
    total_num = " ".join(result)
    print('total num' ,total_num)
    list_segment = string.split(total_num)
    print('read number ',readNumberAdsress(total_num))
    if len(list_segment) == 0:
        return readNumberAdsress(total_num)
    if len(list_segment) == 1:
        return readCharacterInAddress(list_segment[0]) + readNumberAdsress(total_num)
    return readCharacterInAddress(list_segment[0]) + readNumberAdsress(total_num) + readCharacterInAddress(list_segment[1])

def readCharacterInAddress(string):
    if string == '':
        return ''
    list_token = string.split()
    result , temp = [], []
    for i in range(len(list_token)):
        if len(list_token[i]) > 1 :
            if temp != []:
                result.append("".join(temp).upper())
                temp = []
            result.append(list_token[i])
        else:
            temp.append(list_token[i])
    if temp != [] :
        result.append("".join(temp).upper())
    return " ".join(result)

def readTelePhone(string):
    string = replaceZeroInAddress(string)
    unit = ['billion','million','thousand','hundred']
    list_token = string.split()
    result = []
    for i in range(len(list_token)):
        if checkValidNumber(list_token[i]) == True or list_token[i] in unit or list_token[i] == 'sil':
            result.append(list_token[i])
    total_num = " ".join(result)
    list_segment = string.split(total_num)
    # print('read number ',readNumberAdsress(total_num))
    if len(list_segment) == 0:
        return readSegmentTelePhone(total_num)
    if len(list_segment) == 1:
        return readCharacterInAddress(list_segment[0]) + readSegmentTelePhone(total_num)
    return readCharacterInAddress(list_segment[0]) + readSegmentTelePhone(total_num) + readCharacterInAddress(list_segment[1])
 
def readSegmentTelePhone(string):
    list_segment = string.split('sil')
    return '-'.join([ readAddress(segment) for segment in list_segment])

def readLetter(string):
    return string.replace(' ','').upper()

def readVERBATIMFromFile():
    result = {}
    with open('data_process/all_line_VERBATIM.txt' , 'r') as f_r:
        for line in f_r:
            line = line.strip()
            output , input = line.split('\t')[0] , line.split('\t')[1]
            if input != 'sil' and len(input.split()) == 1:
                result[input] = output
    return result 

def readVERBATIM(string):
    list_verbatim = readVERBATIMFromFile()
    list_token = string.split()
    result = [] 
    for token in list_token:
        if token in list_verbatim:
            result.append(list_verbatim[token])
        else:
            result.append(token)
    return " ".join(result)


def readNumberEnglish(string):
	try:
		decompose = decompotionNumberString(string)
		result = 0 
		if decompose['trillion'] != '':
			result += w2n.word_to_num(decompose['trillion']) * pow(10,12)
		if decompose['billion'] != '':
			result += w2n.word_to_num(decompose['billion']) * pow(10,9)
		if decompose['million'] != '':
			result += w2n.word_to_num(decompose['million']) * pow(10,6)
		if decompose['thousand'] != '':
			result += w2n.word_to_num(decompose['thousand']) * pow(10,3)
		if decompose['hundred'] != '':
			result += w2n.word_to_num(decompose['hundred']) * pow(10,2)	
		if decompose['unit'] != '':
			result += w2n.word_to_num(decompose['unit'])
		return result
	except:
		return string

def readDecimal(string):
    
    string = replaceZeroInAddress(string)
    if 'minus' in string:
        isMinus = True
    else:
        isMinus = False
    string = string.replace('minus','')
    tail_num = string.split()[-1]
    if tail_num in ['trillion', 'billion','million', 'thousand', 'hundred']:
        string = " ".join(string.split()[:-1])
        containUnit = True 
        unit = tail_num
    else:
        containUnit = False
    if containUnit == False :
        result = readDecimalNum(string)
    else:
        result = readDecimalNum(string) +" "+unit
    if isMinus == True:
        return '-'+result
    else:
        return result

def readDecimalNum(string):
    if 'point' not in string:
        return str(readNumber(string))
    else:
        list_segment = string.split('point')
        if len(list_segment) != 2:
            return string 
        else:
            intege = list_segment[0]
            decima = list_segment[1]
            result_num = ''
            if intege != '':
                result_num += readNumber(intege)
            result_num+='.'
            if decima != '':
                result_num += readDigit(decima)
            return result_num  
    

if __name__ == "__main__":
	text = 'point two o o two'
	print(readDecimal(text))