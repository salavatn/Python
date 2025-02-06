from faker import Faker


# Section 1: create instance of Faker()
faker = Faker('en_EN')


# Section 2: get the list of attributes and methods
fake_type = dir(faker)


# Section 3: Which data need to find
keyword = "passport"


# Section 4: search the keyword in fake_type
for item in fake_type:
    if keyword in item:
        print(f'\t- {item}')


# Example output:
    # - passport_dates
    # - passport_dob
    # - passport_full
    # - passport_gender
    # - passport_number