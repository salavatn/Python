from faker import Faker
import argparse

def get_pswd(level):
    if level == 'hard':
        pswd = fake.password(length=args.len)
    elif level == 'medium':
        pswd = fake.password(length=args.len, special_chars=False)
    elif level == 'easy':
        pswd = fake.password(length=args.len, special_chars=False, digits=False, upper_case=True, lower_case=True)
    return pswd

fake = Faker()

parser = argparse.ArgumentParser(description='Generate passwords of specified length and complexity')
parser.add_argument('--len', help='length of the generated passwords', default=8, type=int,  )
parser.add_argument('--lvl',  help='complexity of the generated passwords', default='easy', choices=['medium', 'hard'], )
parser.add_argument('--cnt',  help='number of passwords to generate',   default=1, type=int)
args = parser.parse_args()

print('\nPassword List:')
while args.cnt > 0:
    args.cnt -= 1
    pswd = get_pswd(level=args.lvl)
    print(f"  {pswd}")

print('\n')
