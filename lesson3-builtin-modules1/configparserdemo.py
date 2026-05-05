"""
configparser built-in module
conf = cfp.ConfigParser()
# conf.read(filename) # read the ini file and get the content
# conf.sections() # get all the sections in the ini file and return a list
# conf.options(section) #  return a list of options in that section
# conf.items(section)   #  return all k-v pair in that section
# conf.get(section,option) # get a option from that section in string format
# conf.getint(section,option) # get a option from that section in integer format
# conf.write(filename) # write the config info into a ini file
# conf.add_section() # add a new section
# conf.set(section,option,value) # assign the value ito the option in that section
# conf.remove_section(section) # delete that section
# conf.remove_option(section,option) # remove the option from that section
"""

import configparser as cfp

# we actually us the ConfigParser class from the configparser module to create a instance
conf = cfp.ConfigParser()
def create_ini():
    conf['mysql'] = {
            "host" : "192.169.10.68",
            "port" : "3306",
            "user" : "root",
            "password" : "123456"
        }

    with open('config.ini','w',encoding='utf-8') as f:
        conf.write(f)
# create a ini file
# create_ini() # this will create a config.ini the the current folder

# read data from that ini
print(conf.read("config.ini")) # ['config.ini'],but the data loaded in conf object
print(conf.sections()) # ['mysql']

# print the key and value in each item
# for k,v in conf.items("mysql"):
#     print(f"{k}:{v}")

# get the options
print(conf.options("mysql")) # ['host', 'port', 'user', 'password']

print(conf.get("mysql","host")) # 192.169.10.68

# encapsulate a function
def add_config_tofile(conf,filename):
    conf.add_section("api")
    conf.set("api","name","/user/login")
    conf.set("api","method","get")
    conf.set("api","body","{'username':'admin','password':'123456'}")

    with open(filename,'w') as f:
        conf.write(f) 

# add_config_tofile(conf,"config.ini")

# chage a setting
# conf.set('api','method','post')
# with open('config.ini', 'w') as f:
#      conf.write(f)

# remove a setting,
# conf.remove_option("api","body") # remove a option from a section
# conf.remove_section("api")  # remove the whole section
# with open('config.ini', 'w') as f:
#      conf.write(f)


 