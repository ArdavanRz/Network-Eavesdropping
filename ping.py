from pythonping import ping


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Security prj 1 : {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('\n 9631412')
    print("enter your desired IP for pinging : \n")
    ip = input()
    ping_result = ping(ip, verbose = True) # verbose argument used for reporting the ping result
    print(ping_result)

