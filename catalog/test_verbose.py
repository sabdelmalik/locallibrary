import sys
sys.argv = ['manage.py', 'test', '--verbosity', '2']
exec(open('manage.py').read())
