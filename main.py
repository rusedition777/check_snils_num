import re


def get_snils(snils):
    num_snils = re.sub(r'\D', '', snils)
    if len(num_snils) != 11:
        print('Номер снился введен некорректно!')
    else:
        if int(num_snils[0:9]) > 1001998:
            print('OK')
            res = 0
            for j, num in enumerate(num_snils):
                i = 9 - j
                if i != 0:
                    res = res + (int(num) * i)
                else:
                    break
            if res == 99 and num_snils[9:11] == '99':
                print('Номер СНИЛС корректный')
            elif (res == 100 or res == 101) and num_snils[9:11] == '00':
                print('Номер СНИЛС корректный')
            elif res == 102 and num_snils[9:11] == '01':
                print('Номер СНИЛС корректный')
            elif (res % 101) == int(num_snils[9:11]):
                print('Номер СНИЛС корректный')
            else:
                print('Номер СНИЛС некорректный')
        else:
            print('Номер СНИЛС введен некорректно!')


if __name__ == '__main__':
    get_snils(input('Введите номер СНИЛС: '))
