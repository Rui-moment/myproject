import re

xmas_regex = re.compile(r'\d+\s\w+')
xmas_regex.findall('12 days of Christmas 1 partridge in a pear tree 2 turtle doves 3 French hens 4 calling birds 5 golden rings 6 geese a laying 7 swans a swimming 8 maids a milking 9 ladies dancing 10 lords a leaping 11 pipers piping 12 drummers drumming')
print(xmas_regex.findall('12 days of Christmas 1 partridge in a pear tree 2 turtle doves 3 French hens 4 calling birds 5 golden rings 6 geese a laying 7 swans a swimming 8 maids a milking 9 ladies dancing 10 lords a leaping 11 pipers piping 12 drummers drumming'))

