#!/usr/bin/python


class Menu(object):
    def __init__(self, user_input=None, test=False):
        loop = True
        while loop:
            print('-----------------------------------------')
            print('What would you like to do?: enter empty to exit')
            print('1: Check which gitrepos needs updating')
            print('2: Update, build and deploy all outdated gitrepos')
            print('3: Check for uncommitted changes')
            loop = False
