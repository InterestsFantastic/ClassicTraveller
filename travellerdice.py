#!/usr/bin/env python3

'''This module handles a d66 roll, conversion of numbers to Traveller
letternumbers and back, and generates random character stats, returning
a list or a string, depending on your preference.
It also rolls d6, 2d6, and does 1/3 and 1/2 checks.'''


letternumbers = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'

def letter_to_number(letter):
    '''Returns the number corresponding to a Traveller numberletter.
    This includes 0 through 9.'''
    assert len(letter) == 1, 'Single letter required.'
    letter = letter.upper()
    out = letternumbers.find(letter)
    assert out != -1, 'Unknown character requested for translation.'
    return out

def number_to_letter(num):
    return letternumbers[num]

def numbers_to_letters(numbers):
    '''Returns a string of all numbers converted to characters.'''
    out = ''
    for n in map(number_to_letter, numbers):
        out += n
    return out
