full_dot = '●'
empty_dot = '○'

def create_character(character_name ,STR,INT,CHA):
    character_name
    STR
    INT 
    CHA 
    if not isinstance(character_name, str):
        return'The character name should be a string'
    if not character_name  :
        return'The character should have a name'
    if len(character_name) > 10 : 
        return 'The character name is too long'
    if ' ' in character_name :
        return 'The character name should not contain spaces'
    if not isinstance(STR,int)or not isinstance (INT,int)or not isinstance (CHA,int):
        return 'All stats should be integers'
    if INT <1 or STR <1 or CHA<1 :
        return 'All stats should be no less than 1'
    if INT > 4 or STR >4 or CHA>4 :
        return 'All stats should be no more than 4'
    if INT + STR + CHA != 7 :
        return 'The character should start with 7 points'
    STRn =  + STR * full_dot + empty_dot * (10 - STR ) 
    INTn =  + INT * full_dot + empty_dot * (10 - INT )
    CHAn = + CHA * full_dot + empty_dot * (10 - CHA )
    return (f'{character_name}\nSTR {STRn}\nINT {INTn}\nCHA {CHAn}')

print(create_character('ren',4,2,1))
