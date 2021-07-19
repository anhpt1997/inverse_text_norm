import pandas as pd 
from convertWordToNumber import * 

def readDataCSV(filein , filesrc , filetgt):
    data = pd.read_csv(filein, header=None).values
    with  open(filesrc , 'w') as f_src , open(filetgt,'w') as f_tgt:
        temp_src, temp_tgt = [] , [] 
        for line in data :
            cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
            if cla == '<eos>' :
                f_src.write(" ".join(temp_src) +"\n" )
                f_tgt.write(' '.join(temp_tgt) +"\n")
                temp_tgt , temp_src = [] , []
            else:
                if cla == 'PLAIN' :
                    temp_src.append(input)
                    temp_tgt.append(input)
                else:
                    if  output == 'sil':
                        temp_src.append(output)
                        temp_tgt.append(input)
                    else:
                        temp_src.append(output)
                        temp_tgt.append('<'+cla+'>' + " "+output +" " + '</'+cla+'>')

def getAllCla(filein , fileout):
    result = [] 
    with open(filein , 'r') as f_in , open(fileout , 'w') as f_out:
        for line in f_in :
            line = line.strip()
            # cla , input , output= line.split(',')[0].replace('"',"")  , line.split(',')[1].replace('"',"")  ,line.split(',')[2].replace('"',"") 
            result.append(cla)
        result = set(result)
        f_out.write("\n".join(result))

def removeTagInSentence(filein, fileout):
    with open(filein , 'r') as f_in , open(fileout , 'w') as f_out:
        for line in f_in:
            line = line.strip()
            list_token = line.split()
            result = []
            for token in list_token:
                if '<' not in token :
                    result.append(token)
            f_out.write(" ".join(result)+"\n")

def readDictWordFromFile(file):
    result = {}
    with open(file ,'r') as f:
        for line in f:
            line = line.strip()
            result[line] = 1
    return result

def handleOOVSentence(sentence, dict_word):
    list_token = sentence.split()
    result = []
    for token in list_token:
        if '<' not in token and token.lower() not in english_word and len(token) > 1:
            result.append('<oov> ' + " ".join(token) +" </oov>")
        else:
            result.append(token)
    return " ".join(result)

english_word = readDictWordFromFile('words_alpha.txt')

# text = 'david Alaba <date> '

# print(handleOOVSentence(text , english_word))

def insertTagToOOV(filein , fileout):
    with open(filein , 'r') as f_in , open(fileout , 'w') as f_out:
        for line in f_in:
            line = line.strip()
            f_out.write(handleOOVSentence(line , english_word) +"\n")


def getRawSourceAndTarget(filein , filesrc, filetgt):
    data = pd.read_csv(filein, header=None).values
    with  open(filesrc , 'w') as f_src , open(filetgt,'w') as f_tgt:
        temp_src, temp_tgt = [] , [] 
        for line in data :
            cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
            if cla == '<eos>' :
                f_src.write(" ".join(temp_src) +"\n" )
                f_tgt.write(' '.join(temp_tgt) +"\n")
                temp_tgt , temp_src = [] , []
            else:
                if output == '<self>':
                    temp_src.append(input)
                    temp_tgt.append(input)
                else:
                    temp_src.append(output)
                    temp_tgt.append(input)

def readAllLineMeasure(filein , fileout):
    data = pd.read_csv(filein, header=None).values
    with  open(fileout , 'w') as f_out:
        for line in data :
            cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
            if cla == 'MEASURE':
                f_out.write(input +"\t"+output+"\n")

def readAllLineFraction(filein , fileout):
    data = pd.read_csv(filein, header=None).values
    with  open(fileout , 'w') as f_out:
        for line in data :
            cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
            if cla == 'FRACTION':
                f_out.write(input +"\t"+output+"\n")

def readAllLineOrdinal(filein , fileout):
    data = pd.read_csv(filein, header=None).values
    with  open(fileout , 'w') as f_out:
        for line in data :
            cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
            if cla == 'ORDINAL':
                f_out.write(input +"\t"+output+"\n")

def readAllLineTime(filein , fileout):
    data = pd.read_csv(filein, header=None).values
    with  open(fileout , 'w') as f_out:
        for line in data :
            cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
            if cla == 'TIME':
                f_out.write(input +"\t"+output+"\n")
# insertTagToOOV(filein='src.txt' , fileout='src_oov.txt')
# insertTagToOOV(filein='tgt.txt' , fileout='tgt_oov.txt')
# getRawSourceAndTarget('data_craw/data_english_tts/output_1.csv' , 'data_process/input_raw/src_raw.txt', \
#     'data_process/input_raw/tgt_raw.txt')
# readAllLineMeasure('data_craw/data_english_tts/output_1.csv','data_process/all_line_measure.txt')

# readAllLineTime('data_craw/data_english_tts/output_1.csv','data_process/all_line_time.txt')
# with open('data_process/all_line_ordinary.txt','r') as f_r, \
#     open('test_ordinal.txt','w') as f_w:
#     for line in f_r:
#         line = line.strip()
#         true , input = line.split('\t')[0] , line.split('\t')[1]
#         f_w.write(true+"\t"+input+"\t"+readOdinal(input)+"\n")