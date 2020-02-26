#########################################
# .: sqlpp :.
# Takes an input of one or more sql files and outputs the sql pretty printed
# .: Sample :.
# sqlpp <sql_file> [<sql_file2>[, ...]]
# .: deploy on linux :.
# % git clone https://github.com/JavaScriptDude/sqlpp.git && cd sqlpp
# % echo "python3 ${PWD}/sqlpp.py \$@" > ${HOME}/.local/bin/sqlpp
# % chmod u+x ${HOME}/.local/bin/sqlpp
# .: Other :.
# Author: Timothy C. Quinn
# Home: https://github.com/JavaScriptDude/sqlpp
# Licence: https://opensource.org/licenses/MIT
#########################################

import argparse, sqlparse, re

parser = argparse.ArgumentParser(prog="sqlpp")
parser.add_argument("--verbose", "-v", action='store_true')
parser.add_argument("file", type=argparse.FileType("r"), nargs="+")

args = parser.parse_args()

def prepend(s, s2): return s2 + re.sub('\n', '\n'+s2, s)

# Pretty print input files
n=len(args.file)
for i, file in enumerate(args.file):
    sIn = file.read().replace('\n', '')
    file.close()
    sOut = sqlparse.format(sIn, reindent=True, keyword_case='upper')
    if args.verbose or n > 1: 
        print("File {}:\n    {}\n{}SQL:\n{}\n".format(
            i+1
            ,file.name
            ,("Original SQL:\n{}\n".format(prepend(sIn, "    ")) if args.verbose else "")
            ,prepend(sOut, "    ")
        ))
    else:
        print(sOut)
