import argparse
from faker import Faker

def get_pswd(level, len):
    fake = Faker()
    if level == 'hard':
        pswd = fake.password(length=len)
    elif level == 'medium':
        pswd = fake.password(length=len, special_chars=False)
    elif level == 'easy':
        pswd = fake.password(length=len, special_chars=False, digits=False, upper_case=True, lower_case=True)
    return pswd

parser = argparse.ArgumentParser(description='Generate passwords of specified length and complexity')
parser.add_argument('--len', help='length of the generated passwords', default=8, type=int,  )
parser.add_argument('--lvl',  help='complexity of the generated passwords', default='easy', choices=['medium', 'hard'], )
parser.add_argument('--cnt',  help='number of passwords to generate',   default=1, type=int)
args = parser.parse_args()

print('\nPassword List:')
for i in range(args.cnt):
    pswd = get_pswd(level=args.lvl, len=args.len)
    print('  %s' % pswd)

print('\n')
