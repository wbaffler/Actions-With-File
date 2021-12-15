import sys
from work_with_file import File
from codes import Codes, Error_codes
def check_input_file():
    try:
        f = open("filename.txt")
    # Сделайте что-нибудь с файлом
    except IOError:
        print("Файл недоступен")

def check_code(code):
    if code.isdigit():
        return True
    return False



def main():
    if len (sys.argv) == 1:
        print('''
        Задайте аргументы в следющем виде:\n
        входной_файл выходной_файл ключ_операции\n
        Ключи:
        1. Сортировка всех строк по возрастанию
        2. Сортировка всех строк по убыванию
        3. Рандомное перемешивание всех строк
        4. Сортировка всех строк по возрастанию их длины
        5. Сортировка всех строк по убыванию их длины''')
        sys.exit (1)
    else:
        if len (sys.argv) < 4:
            print ("Ошибка. Слишком мало параметров.")
            sys.exit (1)

        if len (sys.argv) > 4:
            print ("Ошибка. Слишком много параметров.")
            sys.exit (1)

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    code_str = sys.argv[3]

    file_action = File(inputPath, outputPath)
    error_code = file_action.result_of_work()
    if check_code(code_str):
        code = int(code_str)
        if code == Codes.sort_up:
            file_action.sort_up()
        elif code == Codes.sort_down:
            file_action.sort_down()
        elif code == Codes.shuffle:
            file_action.random()
        elif code == Codes.sort_len_up:
            file_action.sort_len_up()
        elif code == Codes.sort_len_down:
            file_action.sort_len_down()
        else:
            error_code = Error_codes.bad_request
        file_action.write_in_file()
    else:
        print('Код необходимо задавать числом')
    
    
    if error_code == Error_codes.no_file:
        print('Файл по заданному пути не найден')
    elif error_code == Error_codes.bad_request:
        print("Программа не выполнена. Ошибка в заданном коде")
    elif error_code == Error_codes.ok:
        print("Программа выполнена успешно")



if __name__ == "__main__":
    main()

