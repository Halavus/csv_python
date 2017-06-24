#TODO 
# Prevent false input formating on each func

# Straight and clear. Cannot fail.
def Cleanup(number):
    number=number.replace(' ', '')
    number=number.replace('/', '')
    return number

# DONE
def Cut(number):
    if len(number)>8:
        cut_number=number[len(number)-9:]
        return cut_number
    else:
        return number

# on a Cut() number
def Mobile(cut_number):
    try:
        mob=int(''.join((cut_number[0], cut_number[1])))
        if 74 < mob < 80 and len(cut_number)==9:
            return True
        else:
            return False

    except ValueError:
        '''In case the number isn't with int formated'''
        return False

    except IndexError:
        '''In case no value is passed: cut_number == '''
        return False


# number as to be the number without starting 0 as a str of 9 digits
def CHFormat(cut_number):
    '''Formats the number to swiss (CH) readable format: XXX XXX XX XX
    The last append is 'open ended' because if the number is wrong it will be 
    detected in the Do() function later on.
    '''
    
    with_zero=''.join(('0', cut_number))
    lst=list(with_zero)
    digformated=[]
    digformated.append(''.join(lst[:3]))
    digformated.append(''.join(lst[3:6]))
    digformated.append(''.join(lst[6:8]))
    digformated.append(''.join(lst[8:]))

    formatednumber=' '.join(digformated)
    return formatednumber

def Do(number, CH=True):
    if CH==True:
        '''Formats only if the client is CH'''
        clean_number=Cleanup(number)
        clean_number=Cut(clean_number)
        if Mobile(clean_number)==True:
            output=clean_number
        else:
            CH_fix_number=CHFormat(clean_number)
            if len(CH_fix_number)==13:
                '''A right formated CH-Number is 13 long'''
                output=CH_fix_number
            else:
                '''If not the case, the number is definitly corrupted 
                and not usable. In that case we just don't edit it.
                '''

                output=number
        
            return output

        return output

    else:
        '''If the client is not CH, his number wont be formated at all'''
        return number
