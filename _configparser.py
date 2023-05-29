import configparser


PATH = ''  # *.ini file
SECTION = ''
OPTION = ''

print('PATH: ', PATH)
print('SECTION: ', SECTION)
print('OPTION: ', OPTION)


config = configparser.ConfigParser()
config.read(PATH)


# list of available sections
print('Sections: ', list(config.keys()))


# check the existence of elements
print('has section: ', config.has_section(SECTION))
print('has option: ', config.has_option(SECTION, OPTION))


# print whole values
for section in config.keys():
    print()
    print(f' {section} '.center(20, '-'))
    for item in config[section]:
        print(f"{item} = <{config.get(section, item)}>")
print()


# get a certain element
item = config[SECTION][OPTION]
item = config.get(SECTION, OPTION)
item = config.getint(SECTION, OPTION)  # .getboolean() | .getfloat()
