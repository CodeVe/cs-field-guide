"""System Functions Module - CSFG
    -Contains: Helper functions for guide creation
    -Authors: Jordan Griffiths, Jack Morgan
"""

import string
import configparser
import pip
import argparse
import sys

def to_kebab_case(text):
    """Returns the given text as kebab case.
    The text is lower case, has spaces replaced as dashes.
    All punctuation is also removed.
    """
    text = ''.join(letter for letter in text if letter in set(string.ascii_letters + string.digits + ' -'))
    text = text.replace(' ', '-').lower()
    return text


def from_kebab_case(text):
    """Returns given kebab case text to plain text.
    Text is camel case, with dashs replaced with spaces
    """
    return text.replace('-', ' ').title()


def read_settings(settings_location):
    """Read the given setting file
    and return the configparser
    """
    settings = configparser.ConfigParser()
    settings.optionxform = str
    #settings.default_section = 'Main'
    settings.read(settings_location)
    return settings


def command_line_args():
    """Setup arg parser, and add required argument handling. Return
    namespace generated by parser arguments
    """
    argsparser = argparse.ArgumentParser(description='guide generator args')
    argsparser.add_argument('--ignore-pip', dest='install_dependencies', action='store_false', default='store_true')
    argsparser.add_argument('--pdf', dest='include_pdf', action='store_true')
    return argsparser.parse_args()


def install_dependencies():
    """Install project dependencies, if required"""
    pip.main(['install',  '-r', 'generator/dependencies.conf'])
