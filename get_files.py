##############################################
# file: test.py                              #
# Author: Toygar Özel                        #
# E-mail: toygar_ozel1@hotmail.com           #
# Date: 2022-06-15                           #
# Version: 1.0                               #
##############################################

import os
import shutil
import sys
from colorama import Fore, init

author = "\033[34mToygar Özel\033[0m"
contact = "\033[34mtoygar_ozel1@hotmail.com\033[0m"
title = "\033[32mVTS Log Analyzer\033[0m"

vtsPath = r'\\arcrk03V\crk-ortak\Kurutucu\UGY\Sistem_Tasarım\UGY_LABORATUARI\performans_lab_VTS'
vtsLogPath = r'\\arcrk03V\crk-ortak\Kurutucu\UGY\Sistem_Tasarım\UGY_LABORATUARI\performans_lab_VTS\LOG'
perfFilesPath = r'.\PERFORMANS_FILES'
logFilesPath = './LOG'

ronaldoImage = ''' 
    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣷⣦⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣶⣾⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣟⠻⠋⠉⠉⠛⢿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⠁⠈⢻⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⡿⠋⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⢘⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣯⡹⣿⣿⣿⠋⠁⠒⣉⣭⣭⣽⣿⡶⠀⢀⣤⣶⣬⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣶⣿⠓⢻⡿⠀⠀⠀⠀⠛⠛⠛⠉⠀⠀⡿⢿⡿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠾⣆⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⣦⠤⠇⠀⡼⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡇⠀⡆⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣬⣄⠀⢠⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢳⡀⠀⠀⠀⠀⠀⠀⠣⣴⣤⣤⡼⠁⡎⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⡇⠀⠈⣿⠲⢤⣄⡀⠀⠀⠀⠀⠀⠈⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢓⠇⠀⠀⠘⢇⠀⠉⠻⢿⣶⣶⡿⠛⠛⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣶⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣾⠇⠀⠀⢸⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⠔⠊⠁⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⠀⠀⠀⢸⢀⣿⣿⠑⠦⣀⠀⠀⠀⠀
⠘⠁⠀⠀⡀⠀⠈⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⣼⣿⡿⠀⠀⠈⠑⢤⡀⠀
⠀⠀⣀⣴⠿⡄⠀⠀⠙⢿⣿⣿⣷⣤⣀⣀⠀⠀⠀⠀⠀⢀⣀⣠⣾⣿⠟⠁⠀⠀⢀⣀⣀⠈⠀
⠹⣟⢉⡧⢤⡷⣀⡀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⡔⠉⠈⠉⢳⠀
⠀⠀⡼⠁⣴⠋⠁⠉⢳⡄⢀⠀⠀⠀⠈⠉⠉⠛⠛⠋⠉⠉⠀⠀⠀⣀⣠⣤⣌⣧⡀⠀⠀⣸⠁
⠀⠀⠀⠀⢿⡀⠀⠀⣸⡟⢸⢷⡀⠀⢢⠄⠠⣤⡄⠀⠤⡔⠂⠐⢿⡀⠀⠀⠹⡏⠛⠛⠋⠀⠀
⠀⠀⠀⠀⠀⠙⠒⠚⠋⢀⡇⠈⢷⡀⡎⠀⣼⢸⣇⠀⠀⣷⠀⠀⠈⢷⡀⢀⠜⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠈⡿⠀⣰⡁⠀⢻⣆⣀⣿⡤⢴⠀⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀    
    '''

rickAndMortyImage = ''' 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠙⠳⣄⠀⠀⠀⠀⠀⡼⠋⢹⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠈⠳⣄⠀⣠⠞⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⣾⠀⠀⠀⣀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⠤⠤⣀⣠⠤⠤⠇⠀⠀⢀⣠⣤⣤⣤⣀⣀⡀⠙⠊⠉⠉⣹⠃⠀⠀
⠀⠀⢀⡖⠚⠙⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⣠⣾⠿⢚⡭⠤⠶⠦⠤⣉⣧⡀⠀⣰⠃⠀⠀⠀
⠀⠀⠘⣇⠀⠀⠐⢄⡈⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⣼⡟⣡⠞⠉⠀⠀⠀⠀⣀⠀⠹⡀⢰⣇⠀⠀⠀⠀
⠀⠀⠀⠘⣆⠀⠀⠀⠙⢦⡀⠙⠲⣄⠀⠀⠀⠀⠀⠀⠀⢀⣸⠆⠀⢰⠙⢋⠤⠤⠴⣶⠄⠀⣋⠤⠤⢤⣇⠀⠈⠓⣲⡦⠀
⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠙⢦⡀⠀⠙⠦⡀⠶⣞⡋⠉⠉⠀⠀⠀⢸⡴⠁⠀⠀⠀⠀⢣⡼⠁⠀⠀⠀⠘⡄⢠⠞⠁⠀⠀
⠀⠀⠀⠀⠀⠈⢧⡀⢠⡶⢋⣭⠿⠦⠤⢤⣈⡓⢄⡙⠲⢄⣀⠀⠀⢸⢧⠀⠀⠀⠈⠀⣸⢳⡀⠀⠀⠀⣠⠇⠻⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⣿⢿⡟⠀⡀⠀⠀⠀⢢⠙⢦⠙⠢⣤⠞⠀⠀⢸⡀⢑⡢⠤⢤⠞⠁⠰⠉⣒⢒⡊⢹⡀⠀⣩⡷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⠀⣤⡀⠀⡆⠈⣷⣌⣳⣞⣁⡀⠀⢀⢾⡇⠀⠉⠉⠁⠀⠰⣀⠇⠀⠉⠀⢸⢹⡏⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠼⡇⢻⣟⣒⡷⡤⠏⠙⣟⣧⠀⠉⣹⠾⡀⣷⠀⠀⠀⠀⠀⢀⣠⣴⣶⣶⣯⣿⣿⡽⠦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⣧⢸⣠⠼⠞⠛⠲⢦⣼⣸⡓⣤⠿⠤⢼⣿⣦⣀⣤⣶⣿⣿⣿⡿⠛⠛⣿⡿⠟⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⣤⣿⣼⣷⣤⡀⠀⠀⣾⣟⣻⣿⣿⠳⡀⠀⢿⣿⣿⣿⡿⣿⣷⠚⠁⠀⠀⣸⠓⢤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡞⠀⠀⡾⢿⣿⠟⠚⠛⢾⡆⠀⡟⠉⠀⠈⠙⣧⠈⠢⡀⠛⠛⡿⣅⣰⣿⣀⣠⡤⡞⠁⠀⠀⠱⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣇⠀⢰⠃⢸⡇⠀⠀⠀⠀⢳⠀⢇⠀⠀⠀⢀⡿⡆⠀⢹⣀⡜⠀⢸⠀⠉⠁⢹⠀⠘⣄⠀⠀⠀⢸⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⡄⢸⡄⠈⢧⣀⠀⠀⣠⣞⠀⠨⠷⣶⣖⣿⣗⣷⠀⠀⡿⣄⠀⢸⠀⠀⠀⠘⡇⠀⣼⡀⠀⠀⣸⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣾⠇⠀⠹⣿⣭⣉⣽⡟⠈⠉⡠⢽⡿⡯⢿⡿⠀⠀⡇⠈⡦⢸⠀⠀⠀⠀⡇⢸⠟⠀⠀⢠⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⣀⠀⠈⠉⢻⡝⣄⠀⠚⠋⠀⠃⢱⢸⠀⠀⠀⣷⡜⠁⢸⡄⠀⠀⠀⣽⠋⠀⠀⣰⠛⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠉⠣⣀⠀⠀⠻⣞⢦⣠⢤⡔⢶⣻⢸⠀⠀⠀⢸⣧⠀⠘⡇⠀⢀⡼⠁⠀⢀⣼⠁⠀⢣⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠖⠁⠀⠀⠀⠀⠈⠙⠒⠒⠻⣯⡿⠀⠀⠀⠁⢸⣄⡀⠀⠀⣏⢣⠀⢧⢠⠞⠀⠀⣠⠏⡏⠀⠀⠘⡀⠀⠀
⠀⠀⠀⢀⠔⠁⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⢹⠄⠀⠀⠀⠀⢈⣸⠇⠀⠀⠸⡀⠳⣸⠋⠀⠀⡴⢻⠀⡇⠀⠀⠀⢣⠀⠀
⠀⠀⠔⠙⢦⡀⠀⡠⠚⡟⠀⠀⠀⠀⠀⠀⠀⠘⠦⣤⡀⢀⣶⠋⠁⠀⠀⠀⠀⢳⡜⠁⠀⢀⠞⠁⠈⣇⠇⠀⠀⠀⠈⣇⠀
⠄⠀⠀⠀⠠⠟⠋⠁⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠿⠋⠙⠧⠀⠀⠀⠀⠰⠟⠀⠀⠰⠋⠀⠀⠀⠿⠆⠀⠀⠀⠀⠸⠄
'''

ronaldounicode = ' \n    \n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2880\u28f6\u28f7\u28e6\u28f6\u28c4\u28c0\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2880\u28c0\u28f6\u28fe\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28e6\u28c0\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2880\u28f4\u28f7\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28c4\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u28a0\u28fe\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28f7\u2840\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u28b8\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28df\u283b\u280b\u2809\u2809\u281b\u28bf\u28ff\u28ff\u28ff\u28ff\u2803\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u28fc\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u2800\u2800\u2800\u2800\u2800\u2800\u2808\u2801\u2808\u28bb\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2880\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u287f\u280b\u2800\u28c0\u28c0\u2840\u2800\u2800\u2800\u2800\u2800\u2800\u2898\u2847\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u28b0\u28ff\u28ef\u2879\u28ff\u28ff\u28ff\u280b\u2801\u2812\u28c9\u28ed\u28ed\u28fd\u28ff\u2876\u2800\u2880\u28e4\u28f6\u28ec\u2847\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2808\u28ff\u28f6\u28ff\u2813\u28bb\u287f\u2800\u2800\u2800\u2800\u281b\u281b\u281b\u2809\u2800\u2800\u287f\u28bf\u287f\u28ff\u2803\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2818\u28bf\u283e\u28c6\u28f8\u2801\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2818\u2844\u2800\u28b8\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2808\u28ff\u287f\u2803\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2813\u2812\u28e6\u2824\u2807\u2800\u287c\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u28c0\u2847\u2800\u2846\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u28c0\u28e4\u28e4\u28ec\u28c4\u2800\u28a0\u2803\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u28b8\u2847\u2800\u28b3\u2840\u2800\u2800\u2800\u2800\u2800\u2800\u2823\u28f4\u28e4\u28e4\u287c\u2801\u284e\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2880\u287f\u2847\u2800\u2808\u28ff\u2832\u28a4\u28c4\u2840\u2800\u2800\u2800\u2800\u2800\u2808\u2880\u281e\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u281b\u2893\u2807\u2800\u2800\u2818\u2887\u2800\u2809\u283b\u28bf\u28f6\u28f6\u287f\u281b\u281b\u284f\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2880\u28e0\u2814\u280b\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2818\u287f\u2800\u2800\u2800\u2847\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u28e0\u28f6\u28ff\u2845\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2820\u28e4\u28fe\u2807\u2800\u2800\u28b8\u28b3\u28c4\u2840\u2800\u2800\u2800\u2800\u2800\u2800\u2800\n\u2800\u2880\u28e0\u2814\u280a\u2801\u28bf\u28ff\u28f7\u28c4\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2808\u287f\u2800\u2800\u2800\u28b8\u2880\u28ff\u28ff\u2811\u2826\u28c0\u2800\u2800\u2800\u2800\n\u2818\u2801\u2800\u2800\u2840\u2800\u2808\u28bf\u28ff\u28ff\u28f7\u28c4\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2801\u2800\u2800\u2800\u2800\u28fc\u28ff\u287f\u2800\u2800\u2808\u2811\u28a4\u2840\u2800\n\u2800\u2800\u28c0\u28f4\u283f\u2844\u2800\u2800\u2819\u28bf\u28ff\u28ff\u28f7\u28e4\u28c0\u28c0\u2800\u2800\u2800\u2800\u2800\u2880\u28c0\u28e0\u28fe\u28ff\u281f\u2801\u2800\u2800\u2880\u28c0\u28c0\u2808\u2800\n\u2839\u28df\u2889\u2867\u28a4\u2877\u28c0\u2840\u2800\u2800\u2808\u281b\u283f\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u287f\u281b\u2801\u2800\u2800\u2800\u2854\u2809\u2808\u2809\u28b3\u2800\n\u2800\u2800\u287c\u2801\u28f4\u280b\u2801\u2809\u28b3\u2844\u2880\u2800\u2800\u2800\u2808\u2809\u2809\u281b\u281b\u280b\u2809\u2809\u2800\u2800\u2800\u28c0\u28e0\u28e4\u28cc\u28e7\u2840\u2800\u2800\u28f8\u2801\n\u2800\u2800\u2800\u2800\u28bf\u2840\u2800\u2800\u28f8\u285f\u28b8\u28b7\u2840\u2800\u28a2\u2804\u2820\u28e4\u2844\u2800\u2824\u2854\u2802\u2810\u28bf\u2840\u2800\u2800\u2839\u284f\u281b\u281b\u280b\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2819\u2812\u281a\u280b\u2880\u2847\u2808\u28b7\u2840\u284e\u2800\u28fc\u28b8\u28c7\u2800\u2800\u28f7\u2800\u2800\u2808\u28b7\u2840\u2880\u281c\u2801\u2800\u2800\u2800\u2800\u2800\n\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2809\u2801\u2800\u2808\u287f\u2800\u28f0\u2841\u2800\u28bb\u28c6\u28c0\u28ff\u2864\u28b4\u2800\u281a\u2809\u2801\u2800\u2800\u2800\u2800\u2800\u2800\u2800    \n'

spidermanImage = ["""
                   ,,,,            
             ,;) .';;;;',      
 ;;,,_,-.-.,;;'_,|I\;;;/),,_   
  `';;/:|:);{ ;;;|| \;/ /;;;\__                     
      L;/-';/ \;;\',/;\/;;;.') \\                   
      .:`''` - \;;'.__/;;;/  . _'-._                
    .'/   \     \;;;;;;/.'_7:.  '). \_              
  .''/     | '._ );}{;//.'    '-:  '.,L             
.'. /       \  ( |;;;/_/         \._./;\   _,       
 . /        |\ ( /;;/_/             ';;;\,;;_,      
. /         )__(/;;/_/                (;;'''''      
 /        _;:':;;;;:';-._             );            
/        /   \  `'`   --.'-._         \/            
       .'     '.  ,'         '-,                    
      /    /   r--,..__       '.\\                  
    .'    '  .'        '--._     ]                  
    (     :.(;>        _ .' '- ;/            
    |      /:;(    ,_.';(   __.'                    
     '- -'"|;:/    (;;;;-'--'                       
           |;/      ;;(                             
           ''      /;;|          
                   \;;|                             
                    \/                              
"""
]

toygarImage = '''    
 ______   ______     __  __     ______     ______     ______    
/\__  _\ /\  __ \   /\ \_\ \   /\  ___\   /\  __ \   /\  == \   
\/_/\ \/ \ \ \/\ \  \ \____ \  \ \ \__ \  \ \  __ \  \ \  __<   
   \ \_\  \ \_____\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\ 
    \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/ 
                                                                
             ______     ______     ______     __                            
            /\  __ \   /\___  \   /\  ___\   /\ \                           
            \ \ \/\ \  \/_/  /__  \ \  __\   \ \ \____                      
             \ \_____\   /\_____\  \ \_____\  \ \_____\                     
              \/_____/   \/_____/   \/_____/   \/_____/                                                                                     
'''

isGorsunYeterImage = [
"""
                   ,,,,            
             ,;) .';;;;',      
 ;;,,_,-.-.,;;'_,|I\;;;/),,_   
  `';;/:|:);{ ;;;|| \;/ /;;;\__                     
      L;/-';/ \;;\',/;\/;;;.') \\                   
      .:`''` - \;;'.__/;;;/  . _'-._                
    .'/   \     \;;;;;;/.'_7:.  '). \_              
  .''/     | '._ );}{;//.'    '-:  '.,L             
.'. /       \  ( |;;;/_/         \._./;\   _,       
 . /        |\ ( /;;/_/             ';;;\,;;_,      
. /         )__(/;;/_/                (;;'''''      
 /        _;:':;;;;:';-._             );            
/        /   \  `'`   --.'-._         \/            
       .'     '.  ,'         '-,                    
      /    /   r--,..__       '.\\                  
    .'    '  .'        '--._     ]                  
    (     :.(;>        _ .' '- ;/            
    |      /:;(    ,_.';(   __.'                    
     '- -'"|;:/    (;;;;-'--'                       
           |;/      ;;(                             
           ''      /;;|          
                   \;;|                             
                    \/                              
""",
'''
                                                                                               
                                                                                               
        `7MMF'   `7MF'MMP""MM""YMM  .M"""bgd     `7MMF'        .g8""8q.     .g8"""bgd          
          `MA     ,V  P'   MM   `7 ,MI    "Y       MM        .dP'    `YM. .dP'     `M          
           VM:   ,V        MM      `MMb.           MM        dM'      `MM dM'       `          
            MM.  M'        MM        `YMMNq.       MM        MM        MM MM                   
            `MM A'         MM      .     `MM       MM      , MM.      ,MP MM.    `7MMF'        
             :MM;          MM      Mb     dM       MM     ,M `Mb.    ,dP' `Mb.     MM          
              VF         .JMML.    P"Ybmmd"      .JMMmmmmMMM   `"bmmd"'     `"bmmmdPY          
                                                                                               
                                                                                               
                                                                                               
                                                                                               
      db      `7MN.   `7MF'     db      `7MMF'   `YMM'   `MM'MMM"""AMV `7MM"""YMM  `7MM"""Mq.  
     ;MM:       MMN.    M      ;MM:       MM       VMA   ,V  M'   AMV    MM    `7    MM   `MM. 
    ,V^MM.      M YMb   M     ,V^MM.      MM        VMA ,V   '   AMV     MM   d      MM   ,M9  
   ,M  `MM      M  `MN. M    ,M  `MM      MM         VMMP       AMV      MMmmMM      MMmmdM9   
   AbmmmqMA     M   `MM.M    AbmmmqMA     MM      ,   MM       AMV   ,   MM   Y  ,   MM  YM.   
  A'     VML    M     YMM   A'     VML    MM     ,M   MM      AMV   ,M   MM     ,M   MM   `Mb. 
.AMA.   .AMMA..JML.    YM .AMA.   .AMMA..JMMmmmmMMM .JMML.   AMVmmmmMM .JMMmmmmMMM .JMML. .JMM.
                                                                                               
'''                                                                                     
]

acilisResmi = [spidermanImage, toygarImage]

machines = []

def asciiArt(_asciiImage):
    # Split each multiline string by newline
    strings_by_column = [s.split('\n') for s in _asciiImage]

    # Group the split strings by line
    # In this example, all strings are the same, so for each line we
    # will have three copies of the same string.
    strings_by_line = zip(*strings_by_column)

    # Work out how much space we will need for the longest line of
    # each multiline string
    max_length_by_column = [
        max([len(s) for s in col_strings])
        for col_strings in strings_by_column
    ]

    for parts in strings_by_line:
        # Pad strings in each column so they are the same length
        padded_strings = [
            parts[i].ljust(max_length_by_column[i])
            for i in range(len(parts))
        ]
        print(''.join(padded_strings))

def main():

    init(autoreset=True)

    if not os.path.exists(logFilesPath):
        os.makedirs(logFilesPath)
    if not os.path.exists(perfFilesPath):
        os.makedirs(perfFilesPath)

    #print(spidermanImage)
    #print(toygarImage)

    asciiArt(isGorsunYeterImage)

    print(' ' * (os.get_terminal_size().columns - len(contact)//2 - len(author)//2) + author)
    print(' ' * (os.get_terminal_size().columns - len(contact)) + contact)
    print(' ' * (os.get_terminal_size().columns//2 - len(title)//2) + title)

    while True:
        print("\033[36;1mEnter Machine ID(0 for exit): \033[0m", end='')
        _id = input()
        if _id in machines:
            print('Already exists!')
            continue
        if not _id.isdigit():
            print('Invalid ID, just use numbers!')
            continue
        if _id != '0' or len(_id) == 0:
            machines.append(_id)
            continue
        break
        

    allDirs = [name for name in os.listdir(vtsPath) if os.path.isdir(os.path.join(vtsPath, name))]
    dirs = []
    for machine in machines:
        _tmp = [string for string in allDirs if machine in string]
        if len(_tmp) > 0:
            dirs.append(_tmp[0])

    # Get performans files
    for dir in dirs:
        for files in os.listdir(os.path.join(vtsPath, dir)):
            if 'PERF' in files and files.endswith('.xls'):
                print(Fore.YELLOW + os.path.join(vtsPath, dir, files))
                shutil.copy(os.path.join(vtsPath, dir, files), perfFilesPath)
        
    # Get log files
    for logfile in os.listdir(vtsLogPath):
        for machine in machines:
            if machine in logfile and logfile not in os.listdir(logFilesPath):
                print(Fore.LIGHTYELLOW_EX + os.path.join(vtsLogPath, logfile))
                shutil.copy(os.path.join(vtsLogPath, logfile), logFilesPath)


if __name__ == '__main__':
    main()