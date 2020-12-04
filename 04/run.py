# %% Imports

import re

# %% Load data

with open('./input.txt', 'r') as fhandle:
    input_data = [line for line in fhandle]

len(input_data)

# %% Parse data


def parse_data(input_data):
    '''
    Parse data and return a list of dictionaries
    '''
    parsed = [{}]
    for line in input_data:
        if line != '\n':
            line_dict = {el.split(':')[0]: el.split(':')[1]
                         for el in line.strip().split()}
            parsed[-1].update(line_dict)
        else:
            parsed.append({})
    return parsed


passports = parse_data(input_data)
print(f'Loaded {len(passports)} passports')

# %% Part 1: Check for necessary fields

all_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
]

required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]


def has_all_fields(data: dict, fields: [str]):
    '''
    Check that a dictionary has all the required fields
    '''
    found_fields = [f in data.keys() for f in fields]
    return all(found_fields)

# %% Check passports


passport_check = [has_all_fields(data, required_fields) for data in passports]

print('Valid passports:', sum(passport_check))
print('Total passports:', len(passport_check))

# %% Part 2: Validate fields


def _is_number(val: str):
    '''
    Helper function: string value is a number
    '''
    try:
        return int(val)
    except:
        return False


def _is_len(val: str, length: int):
    '''
    Helper function: string is a certain length
    '''
    return len(val) == length


def validate_byr(val):
    '''
    Validate birth year
    '''
    return _is_number(val) and _is_len(val, 4) and int(val) >= 1920 and int(val) <= 2002


def validate_iyr(val):
    '''
    Validate issue year
    '''
    return _is_number(val) and _is_len(val, 4) and int(val) >= 2010 and int(val) <= 2020


def validate_eyr(val):
    '''
    Validate expiration year
    '''
    return _is_number(val) and _is_len(val, 4) and int(val) >= 2020 and int(val) <= 2030


def validate_hgt(val):
    '''
    Validate height
    '''
    def _validate_cm_val(aval):
        try:
            in_num = int(aval.split('cm')[0])
            return in_num >= 150 and in_num <= 193
        except:
            return False
    valid_cm = re.search(
        '1[5-9][0-9]cm', val) is not None and _validate_cm_val(val)

    def _validate_inch_val(aval):
        try:
            in_num = int(aval.split('in')[0])
            return in_num >= 59 and in_num <= 76
        except:
            return False
    valid_in = re.search(
        '[5-9][0-9]in', val) is not None and _validate_inch_val(val)
    return valid_cm or valid_in


def validate_hcl(val):
    '''
    Validate hair color
    '''
    return re.search('#[0-9a-f]{6}', val) is not None


def validate_ecl(val):
    '''
    Validate eye color
    '''
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return val in valid_colors


def validate_pid(val):
    '''
    Validate passport id
    '''
    return _is_number(val) and _is_len(val, 9)


validate_field = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
}

print(f'Defined {len(validate_field.keys())} validation functions')


def _validate_field_helper(key: str, val: str):
    '''
    Use the dictionary of functions to validate fields
    '''
    # Ignore extra fields
    if key not in validate_field:
        return True
    # Use validator functions (false on error)
    try:
        return validate_field[key](val)
    except Exception as err:
        return False


def is_valid_passport(data: dict):
    '''
    Is a passport valid? Check that all necessary fields are found and all fields are valid
    '''
    return has_all_fields(data, required_fields) and all([_validate_field_helper(k, v) for k, v in data.items()])

# %% Validate passports


valid_passports = [is_valid_passport(ppt) for ppt in passports]

print('Valid passports:', sum(valid_passports))
print('Total passports:', len(valid_passports))

# %%
