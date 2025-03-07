import CommandLineParser as CLP
import sys


if __name__ == '__main__':
	parser = CLP.CommandLineParser()
	parser.add_command('--key', format = r'\d+', is_required = True)
	parser.add_command('--name', format = r'[a-zA-Z]+')
	parser.add_command('--local', conflicting_command = '--remote', is_flag = True)
	parser.add_command('--remote', conflicting_command = '--local', is_flag = True)
	parser.get_arguments(sys.argv)
