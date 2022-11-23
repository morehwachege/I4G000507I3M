# extract data from application log
# lists, sets, dictionaries
# read the data
# ip_addresses = {
#     '23455498': {
#         'operating_system' :'windows',
#         'browser': 'chrome'
#     }
# }
end_data = {
    '23455498': {
        'operating_system' :'windows',
        'browser': 'chrome'
    }
}

ip_addresses = []

with open("application.log", "r") as extract:
    for line in extract.readlines():
        # line = line.strip(" ")
        line = line.split(" ")
        ip_addresses.append(line[0])
        print(line[14])
ip_addresses = list(set(ip_addresses))

# print(ip_addresses)


