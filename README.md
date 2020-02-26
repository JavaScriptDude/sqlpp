# sqlpp
SQL Pretty Printer

Takes an input of one or more sql files and outputs the sql pretty printed

usage:
```
sqlpp [-h] [--verbose] file [file ...]
```


Installation on linux:
```
git clone https://github.com/JavaScriptDude/sqlpp.git && cd sqlpp
echo "python3 ${PWD}/sqlpp.py \$@" > ${HOME}/.local/bin/sqlpp
chmod u+x ${HOME}/.local/bin/sqlpp
```
