#!/usr/bin/env python3
'''Converts between letters and numbers for Traveller, when referring to
numbers in letter form. '''

ordered_numbers_string = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'

def letter_to_number(letter):
    '''Returns the number corresponding to a Traveller numberletter.
    This includes 0 through 9.'''
    assert len(letter) == 1, 'Single letter required.'
    letter = letter.upper()
    out = ordered_numbers_string.find(letter)
    assert out != -1, 'Unknown character requested for translation.'
    return out

def number_to_letter(num):
    '''Returns the Traveller numberletter corresponding to a number.'''
    return ordered_numbers_string[num]

def numbers_to_letters(numbers):
    '''Returns a string of all numbers converted to characters.'''
    out = ''
    for n in map(number_to_letter, numbers):
        out += n
    return out

def letters_to_numbers(letters):
    '''Returns a list of numbers parsed from string of Traveller letternumbers.'''
    out = []
    for n in map(letter_to_number, letters):
        out.append(n)
    return out

assert letter_to_number('c') == 12
assert letter_to_number('C') == 12
assert letter_to_number('3') == 3
assert number_to_letter(12) == 'C'
assert numbers_to_letters([7,10,5,12,6,3]) == '7A5C63'
assert letters_to_numbers('7A5C63') == [7,10,5,12,6,3]
