import argparse

parser = argparse.ArgumentParser(
	prog='Rusted Script',
	description='''
	#Rusted Script is a High-Level embedded programming language...
	''',
	epilog='copyright (c) 2021 Rusted Studio'
	)

parser.add_argument('-p', '--prt', default='[DEFAULT]', help='this is the help of this add_argument')
args = parser.parse_args()

if args.prt != '[DEFAULT]':
	print(args.prt + ': has been printed...')
else:
	print(args.prt + ': DEFAULT')