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

def findPairCurrencyFromFile(filein , fileout):
	with open(filein , 'r') as f_r , open(fileout , 'w') as f_w:
		c = 0
		result , currency  = [] , []
		for line in f_r:
			c += 1
			print(c)
			line = line.strip()
			if ' point ' not in line:
				output , input = line.split('\t')[0] , line.split('\t')[1]
				try:
					pair = findPairCurrency(output , input)
					result.append("\t".join(pair))
					currency.append(pair[0])
				except:
					continue
		f_w.write("\n".join(set(result)))
	with open('currecy.txt' , 'w') as f_w:
		f_w.write("\n".join(set(currency)))

def readAllLineMoney(filein , fileout):
	data = pd.read_csv(filein, header=None).values
	with  open(fileout , 'w') as f_out:
		for line in data :
			cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
			if cla == 'MONEY':
				f_out.write(input +"\t"+output+"\n")

def readAllLineAdDress(filein , fileout):
	data = pd.read_csv(filein, header=None).values
	with  open(fileout , 'w') as f_out:
		for line in data :
			cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
			if cla == 'ADDRESS':
				f_out.write(input +"\t"+output+"\n")

def readAllLineTelephone(filein , fileout):
	data = pd.read_csv(filein, header=None).values
	with  open(fileout , 'w') as f_out:
		for line in data :
			cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
			if cla == 'TELEPHONE':
				f_out.write(input +"\t"+output+"\n")

def readAllLineLetter(filein , fileout):
	data = pd.read_csv(filein, header=None).values
	with  open(fileout , 'w') as f_out:
		for line in data :
			cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
			if cla == 'LETTERS':
				f_out.write(input +"\t"+output+"\n")

def readAllLineVERBATIM(filein , fileout):
	data = pd.read_csv(filein, header=None).values
	with  open(fileout , 'w') as f_out:
		for line in data :
			cla, input, output = str(line[0]) , str(line[1]) , str(line[2])
			if cla == 'VERBATIM':
				f_out.write(input +"\t"+output+"\n")

# findPairCurrencyFromFile('data_process/all_line_money.txt','tail_money.txt')
# readAllLineMoney('data_craw/data_english_tts/output_1.csv','data_process/all_line_money.txt')
readAllLineVERBATIM('data_craw/data_english_tts/output_1.csv','data_process/all_line_VERBATIM.txt')
