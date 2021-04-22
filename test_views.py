import sys
sys.argv = ['manage.py', 'test', 'catalog.tests.test_views', '--verbosity', '2']
exec(open('manage.py').read())


