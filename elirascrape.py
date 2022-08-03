# elirascrape.py
# ef1500
import argparse
import smule_runner

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='Modules')
smule_parser = subparsers.add_parser('smule', help='smule module')
carrd_parser = subparsers.add_parser('carrd', help='carrd module [UNFINISHED]')
foriio_parser = subparsers.add_parser('foriio', help='foriio module [UNFINISHED]')
tellonym_parser = subparsers.add_parser('tellonym', help='tellonym module [UNFINISHED]')
smule_parser_group = smule_parser.add_mutually_exclusive_group()
smule_parser_group.add_argument("-u", "--username", type=str, help="username to scrape")
smule_parser_group.add_argument("-i", "--id", type=str, help="user ID to scrape")

args = parser.parse_args()

if args.username:
    smule_runner.userLookup_Print(args.username)
if args.id:
    smule_runner.userLookupAPI_Print(args.id)