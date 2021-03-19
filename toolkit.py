import pyximport; pyximport.install()
from servel import ServelFiles
import argparse

if __name__ == '__main__':

    action_choices = ['download', 'unlock', 'clear','parse', 'flatten', 'all', 'only_clean', 'full_no_download', 'download_and_clean']
    my_parser = argparse.ArgumentParser(description = 'Toolkit provide methods to parse SERVEL PDFs')

    my_parser.add_argument("-a", "--action_type", choices = action_choices, help = "Perform a action, to process PDF", required = True)

    args = my_parser.parse_args()
   
    action_type = args.action_type

    sf = ServelFiles(__file__)

    if action_type == 'download':
        sf.downloadPDF()
    if action_type == 'unlock':
        sf.unlockPDF()
    if action_type == 'clear':
        sf.clearPDF()
    if action_type == 'parse':
        sf.parsePDF()
        sf.flattenPDF()
    if action_type == 'flatten':
        sf.flattenPDF()
    if action_type == 'full_no_download':
        sf.unlockPDF()
        sf.clearPDF()
        sf.parsePDF()
        sf.flattenPDF()
    if action_type == 'download_and_clean':
        sf.downloadPDF()
        sf.unlockPDF()
        sf.clearPDF()
    if action_type == 'only_clean':
        sf.unlockPDF()
        sf.clearPDF()
    if action_type == 'all':
        sf.downloadPDF()
        sf.unlockPDF()
        sf.clearPDF()
        sf.parsePDF()
        sf.flattenPDF()