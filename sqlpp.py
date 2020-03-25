#########################################
# .: sqlpp :.
# Takes an input of one or more sql files and outputs the sql pretty printed
# .: Sample :.
# sqlpp <sql_file> [<sql_file2>[, ...]]
# .: deploy on linux :.
# % git clone https://github.com/JavaScriptDude/sqlpp.git && cd sqlpp
# % python3 -m pip install -r requirements.txt --user
# % echo "python3 ${PWD}/sqlpp.py \$@" > ${HOME}/.local/bin/sqlpp
# % chmod u+x ${HOME}/.local/bin/sqlpp
# % sqlpp -h
# .: Other :.
# Author: Timothy C. Quinn
# Home: https://github.com/JavaScriptDude/sqlpp
# Licence: https://opensource.org/licenses/MIT
#########################################

import argparse, sqlparse, re, sys, traceback

parser = argparse.ArgumentParser(prog="sqlpp")
parser.add_argument("--verbose", "-v", action='store_true')
parser.add_argument("--stdin", "-s", action='store_true')
parser.add_argument("--comma_first", default=False, action='store_true')

parser.add_argument("file", type=argparse.FileType("r"), nargs="*")

args = parser.parse_args()

def prepend(s, s2): return s2 + re.sub('\n', '\n'+s2, s)

def pprint(sIn, n=-1):
    sOut = sqlparse.format(sIn, reindent=True, keyword_case='upper', use_space_around_operators=True, comma_first=args.comma_first)
    if args.verbose or n > 1: 
        print("File{0}:\n    {1}\n{2}\nFormatted SQL:\n{3}\n".format(
            (' ' + str(i+1) if n > 1 else '')
            ,file.name
            ,("\nOriginal SQL:\n{}\n".format(prepend(sIn, "    ")) 
                    if args.verbose else "")
            ,prepend(sOut, "    ")
        ))
    else:
        print(sOut)
try:
    if args.stdin:
        sb = []
        for line in sys.stdin:
            sb.append(line)

        pprint('\n'.join(sb))

    else:

        n=len(args.file)
        if n== 0:
            parser.print_help()
            print("One or more files required")
        for i, file in enumerate(args.file):
            sIn = file.read().replace('\n', '')
            file.close()
            pprint(sIn, n)
    
    sys.exit(0)

except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    sTB = '\n'.join(traceback.format_tb(exc_traceback))
    print("Fatal exception: {}\n - msg: {}\n stack: {}".format(exc_type, exc_value, sTB))
    sys.exit(1)
