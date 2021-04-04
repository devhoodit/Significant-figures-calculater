a = [[]]
def sigplus(num1, sig1, num2, sig2):
    return num1 + num2




def symbol_to_num (symbol, sym_string):
    sym_string = sym_string.replace(" ","")
    dump_sig_digit = symbol[sym_string]
    dump_sig_num = len(dump_sig_digit.replace(".", ""))
    return [dump_sig_digit, dump_sig_num]



def calculate_sig(symbol, fomular_list):
    """
    이 구간에서는 모든 table_name의 대응 값들을 모두 유효숫자 값과 유효숫자의 갯수로 변환 해줍니다
    절대 정수는 유효숫자 자릿수를 99로 만들어 줍니다.
    
    """
    
    print("formular list - ", fomular_list)
    multi_cal_list = [[fomular_list[0]]]
    multi_syntax = [[]]
    plus_cal_list = []
    multi_result = []
    
    n3 = 1
    
        
    while True:
        if n3 == len(fomular_list):
            break
        
        cur_sym = fomular_list[n3]
        if len(cur_sym) == 1:
            if cur_sym[0] == "+" or cur_sym[0] == "-":
                multi_cal_list.append([])
                multi_syntax.append([])
                if cur_sym[0] == "+":
                    plus_cal_list.append("+")
                else:
                    plus_cal_list.append("-")
                    
            else:
            
                if cur_sym[0] == "*":
                    multi_syntax[-1].append("*")
                
                else:
                    multi_syntax[-1].append("/")
        
        else:
            multi_cal_list[-1].append(cur_sym)
        
        n3 += 1
        
    #calculating 먼저 곱하기 연산 다하고 그 값들을 더하기 연산
    print(multi_cal_list)
    print(multi_syntax)
    n4 = 0
    
    for index in multi_cal_list:
        if len(index) >= 3:
            #곱셈 나눗셈 연산 연속 3번이상일시 규칙대로
            pass
            
        else:
            
            n3 = 0
            if len(index) == 1:
                multi_result.append(index)
            
            else:
                
                dump_sig_slice = 0
                
                if multi_syntax[n4][0] == "*":
                    dump_float = float(index[0][0]) * float(index[1][0])
                    print(dump_float)
                    
                    
                elif  multi_syntax[n4][0] == "/":
                    dump_float = float(index[0][0]) / float(index[1][0])
                    
                    
                if index[0][1] > index[1][1]:
                    dump_sig_slice = index[1][1]
                    
                else:
                    dump_sig_slice = index[0][1]

                dump_string = str(dump_float)
                if dump_sig_slice == 99:
                    print("int detected")
                    multi_result.append([int(dump_float), 99])
                else:
                    if "." == dump_string[dump_sig_slice - 1]:
                        print("demical detected")
                        multi_result.append([float(dump_string[:dump_sig_slice+1]), dump_sig_slice])
                    else:
                        print("float detected", [float(dump_string[:dump_sig_slice]), dump_sig_slice])
                        multi_result.append([float(dump_string[:dump_sig_slice]), dump_sig_slice])
        
                    
                
        n4 += 1
    
    
    print("multi result", multi_result)
    if len(multi_result) == 1:
        print(str(multi_result[0][0]), multi_result[0][1])
        return [str(multi_result[0][0]), multi_result[0][1]]
        
    else:
        n4 = 0
        sum_result = float(multi_result[0][0][0])
        for num1 in range(len(multi_result) - 1):
            if plus_cal_list[n4] == "+":
                sum_result += float(multi_result[n4+1][0][0])
            elif plus_cal_list[n4] == "-":
                sum_result -= float(multi_result[n4+1][0][0])
            
            n4 += 1
        
        min_list = []
        
        for index in multi_result:
            min_list.append(index[0][1])
        

        dump_string = str(sum_result)
        dump_sig_slice = min(min_list) 
        if "." == dump_string[dump_sig_slice]:
            return [str(sum_result)[:dump_sig_slice+1], min(min_list)]
        else:
            return [str(sum_result)[:dump_sig_slice], min(min_list)]
        
                    
                    
                    
                    
                    
                
                    
                    
    
        
def seperate_fo(fomular_str, symbol, n2, floor):
    caling = True
    
    
    global n, form_list
    
    sym_string = ""
    print(n)
    while caling:
        if n == len(fomular_str):
            form_list[floor].append(symbol_to_num(symbol, sym_string))
            break
        issym = True
        if fomular_str[n] == "[":
            
            dump_num = ""
            n += 1
            while fomular_str[n] == "]":
                
                dump_num += fomular_str[n]
                n += 1
            form_list[floor].append([dump_num, 99]) #-1은 유효 숫자가 없음을 의미(유효숫자 무한대)
        
        elif fomular_str[n] == "{":
            
            dump_num = ""
            dump_sig = 1
            n += 1
            
            while fomular_str[n] == "}":
                
                if fomular_str[n] == ".":
                    n += 1
                    continue
                
                dump_num += fomular_str[n]
                n += 1
                dump_sig -= 1
                
            dump_sig -= 1
            form_list[floor].append([dump_num, dump_sig])
        
        elif fomular_str[n] == "(":
            n += 1
            form_list.append([])
            form_list[floor].append(seperate_fo(fomular_str, symbol, n, floor + 1))

        elif fomular_str[n] == ")":
            n += 1
            form_list[floor].append(symbol_to_num(symbol, sym_string))
            sym_string = ""
            return calculate_sig(symbol, form_list.pop())

        elif fomular_str[n] == "*":
            if sym_string != "":
                form_list[floor].append(symbol_to_num(symbol, sym_string))
                sym_string = ""
            n += 1
            form_list[floor].append(["*"])
            
        elif fomular_str[n] == "/":
            if sym_string != "":
                form_list[floor].append(symbol_to_num(symbol, sym_string))
                sym_string = ""
            n += 1
            form_list[floor].append(["/"])
        
        elif fomular_str[n] == "+":
            if sym_string != "":
                form_list[floor].append(symbol_to_num(symbol, sym_string))
                sym_string = ""
            n += 1
            form_list[floor].append(["+"])
        
        elif fomular_str[n] == "-":
            if sym_string != "":
                form_list[floor].append(symbol_to_num(symbol, sym_string))
                sym_string = ""
            n += 1
            form_list[floor].append(["-"])
        
        else:
            sym_string += fomular_str[n]
            n += 1
            issym = False

        
            
    print("calculating")
    return calculate_sig(symbol, form_list.pop())
    
    
    
    
    
    

def calculate(fomular_str, symbol):
    fomular_str.replace(" ", "")
    formular_length = len(fomular_str)
    
    global n, form_list
    n = 0
    caling = True
    
    cal_result = []
    cal_num = 0
    form_list = [[]]
    brace_list = []
    breace_num = 0
    braket = ""
    braket_num = 0
    parenth_list = []
    parenth_num = 0
    
    n2 = 0
    
    result_sig, result_sig_length = seperate_fo(fomular_str, symbol, n2, 0)
    
    print("result - ", result_sig, result_sig_length)
            
        
