from parameters import get_hostname
import random
import sys

# System:
text_red = "\033[31m"
text_green = "\033[32m"
text_default = "\033[0m"

# Default parameters:
count = 0
service_id = [16, 17, 18, 19, 20]
system_arguments_keys = ["-src", "-dst", "-cnt", "-sid", "-help"]
system_arguments_dict = {"src": "random", "dst": "random", "cnt": 1, "sid": "random"}

# User arguments:
user_all_arguments = sys.argv


def checking_args(user_all_args, system_args, system_args_dict):
    """Check for correct name of arguments"""
    incorrect_args = []

    for arg in user_all_args:

        if arg == "-help":
            print("HELP INFO - ling to help function")

        elif arg[0] == "-":
            checking = arg.lower() in system_args
            if checking is True:
                try:
                    index = user_all_args.index(arg)
                    arg_key = arg[1:].lower()
                    arg_value = user_all_args[index + 1]

                    if arg_value[0] != "-":
                        system_args_dict[arg_key] = arg_value

                    elif arg_value[0] == "-":
                        print(f"\n[ ERROR ] Missing argument: {text_red}{arg} *** {text_default}")
                        print(f"\t  For more information:  -help")
                        break

                except IndexError:
                    print(f"\n[ ERROR ] Missing argument: {text_red}{arg} *** {text_default}")
                    print(f"\t  For more information:  -help")
                    break
            else:
                incorrect_args.append(arg)

    if len(incorrect_args) >= 1:
        print(f"\n[ ERROR ] Incorrect argument:\t", text_red, *incorrect_args, text_default)
        print(f"\t  For more information:   -help")

    print(f"\n{text_green}REM CLI:\tpython", *user_all_arguments)
    print(f"{text_green}REM Options:\t{system_args_dict}{text_default}")

    return system_args_dict


def generate_incident():
    system_args_dict = checking_args(user_all_arguments, system_arguments_keys, system_arguments_dict)
    cnt = system_args_dict['cnt']
    user_args_list = list(system_args_dict.values())
    print(user_args_list)

    # if
    # while count <= cnt:

generate_incident()

def get_service_id():
    return service_id[random.randint(0, 4)]


def get_sid():
    sid_value = system_arguments_dict["sid"]

    if sid_value == "any":
        return get_service_id()
    else:
        return sid_value


def get_src():
    src_value = system_arguments_dict["src"]

    if src_value == "any":
        return get_hostname
        # return GET_RANDOM_SOURCE()

    elif src_value.lower() == "hostname":
        return get_hostname

    else:
        return src_value


def get_dst():
    dst_value = system_arguments_dict["dst"]
    if dst_value == "any":
        return get_service_id()
    else:
        return dst_value


def get_cnt():
    cnt_value = system_arguments_dict["cnt"]
    if cnt_value == "any":
        return get_service_id()
    else:
        return cnt_value


# while count <= get_cnt():
#     count += 1
#     print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_dst()} -file get_file() -i {get_sid()}')




# python gen_incidents.py -src any -dst any -chn any -cnt 10
#
# while count <= user_count:
#     count += 1
#
#     if service_id == "any":
#         sid = get_service_id()
#
#
#     if channel == 16:
#         print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_usb()} -file {get_file()} -i {channel}')
#         print(f'timeout {timer} > NUL')
#     elif channel == 17:
#         print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_lan()} -file {get_file()} -i {channel}')
#         print(f'timeout {timer} > NUL')
#     elif channel == 19:
#         print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_printer()} -file {get_file()} -i {channel}')
#         print(f'timeout {timer} > NUL')
#     elif channel == (18 or 21):
#         print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_https()} -file {get_file()} -i {channel}')
#         print(f'timeout {timer} > NUL')


#
# for arg in user_all_args:
#     if arg == "-src":
#         index = user_all_args.index(arg)
#         print(user_all_args[index + 1])
#
#
#
# if len(user_all_args) == 1 or user_all_args[-1] == "-help":
#     print(f"Len(args): \t {len(user_all_args)}")
#     print("Распечатать страницу HELP")
# else:
#     print(f"Len(args): \t {len(user_all_args)}")
#     print("В разработке")


#
# '''
#     16 - Endpoint Removable Media
#     17 - Endpoint LAN
# 18 - Endpoint HTTP
#     19 - Endpoint Printing
# 21 - Endpoint HTTPS
# 60 - HTTP
# 70 - HTTPS
# 80 - FTP
# '''