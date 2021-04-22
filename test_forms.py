import sys
sys.argv = ['manage.py', 'test', 'catalog.tests.test_forms']
exec(open('manage.py').read())


