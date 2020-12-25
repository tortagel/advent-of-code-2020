from dataclasses import dataclass
import re

@dataclass
class Passport:
    birth_year: int = None
    issue_year: int = None
    expiration_year: int = None
    height: str = None
    height_unit: str = None
    height_value: int = None
    hair_color: str = None
    eye_color: str = None
    passport_id: str = None
    country_id: str = None

    def is_valid_simple(self):
        return self.birth_year != None and self.issue_year != None \
            and self.expiration_year != None and self.height != None \
            and self.hair_color != None and self.eye_color != None \
            and self.passport_id != None
    
    def is_valid_ex(self):
        return self.is_valid_simple() \
            and 1920 <= self.birth_year <= 2002 \
            and 2010 <= self.issue_year <= 2020 \
            and 2020 <= self.expiration_year <= 2030 \
            and self.height_unit != None \
            and (  (self.height_unit == 'cm' and 150 <= self.height_value <= 193) \
                or (self.height_unit == 'in' and 59 <= self.height_value <= 76)) \
            and re.match(r'^#[a-f0-9]{6}$', self.hair_color) \
            and (self.eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) \
            and re.match(r'^[0-9]{9}$', self.passport_id)

def prepare_puzzle(puzzle):
    passports = []
    passport = Passport()
    for line in puzzle:
        if line == '':
            passports.append(passport)
            passport = Passport()
        else:
            fields = line.split(' ')
            for field in fields:
                data = field.split(':')
                key = data[0]
                value = data[1]
                if key == 'byr':
                    passport.birth_year = int(value)
                elif key == 'iyr':
                    passport.issue_year = int(value)
                elif key == 'eyr':
                    passport.expiration_year = int(value)
                elif key == 'hgt':
                    passport.height = value
                    if (len(value) > 2):
                        passport.height_unit = value[-2:]
                        passport.height_value = int(value[:-2])
                elif key == 'hcl':
                    passport.hair_color = value
                elif key == 'ecl':
                    passport.eye_color = value
                elif key == 'pid':
                    passport.passport_id = value
                elif key == 'cid':
                    passport.country_id = value
    passports.append(passport)

    return passports

def solve_part1(puzzle):
    valid_passports = 0
    for passport in puzzle:
        if passport.is_valid_simple():
            valid_passports += 1
    return valid_passports

def solve_part2(puzzle):
    valid_passports = 0
    for passport in puzzle:
        if passport.is_valid_ex():
            valid_passports += 1
    return valid_passports
