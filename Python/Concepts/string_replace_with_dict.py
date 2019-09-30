string = "abcdef"

char_map = {
    ord('a') : '1',
    ord('c') : '3',
    ord('e') : '5',
    ord('f') : None
}

string.translate(char_map) # result is "1b3d5"


user_input = "This\nstring has\tsome whitespaces...\r\n"

char_map = {
	ord('\n') : ' ',
	ord('\t') : ' ',
	ord('\r') : None
}
user_input.translate(char_map)  # result is "This string has some whitespaces..."