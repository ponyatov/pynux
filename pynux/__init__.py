import os

## project name
def project(): return 'pynux'

## project About
def about():
    return 'Cross-Linux build system in Python'

## top directory structure
dirs_ = ['.vscode','bin','doc','lib','inc','src','tmp','ref','mk','root','host','target']

## create directory structure
def dirs():
    for d in dirs_: 
        try: os.mkdir(d)
        except FileExistsError: pass

## generate .gitignores
def gitignore():
    with open('.gitignore','w') as giti: 
        print('''*~\n*.swp\n*.log\n*.pyc\n/doc/html/\n!.gitignore''',file=giti)
    for d in dirs_:
        with open(f'{d}/.gitignore','a') as giti: pass

## ignore some autopep8 rules (a bit more dense code & doxygen)
peps_ = ['E26','E302','E305','E401','E402','E701','E702']

## all `mk/`` file base names
mk_ = ['var','dirs','version','cross','tool','src','cfg','pkg','all','format','rule','doc','install','merge']

def mk():
    with open('Makefile','w') as mk:
        for i in mk_:
            m = f'mk/{i}.mk'
            print(f'include {m}',file=mk)
            with open(m,'w') as mm: pass


## the first command: install infrastructure
def install():
    dirs()
    gitignore()
    mk()
