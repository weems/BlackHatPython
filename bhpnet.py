# define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print("BHP Net Tool")
    print("")
    print("Usage: bhpnet.py -t target_host -p port")
    print("-l --listen                - listen on [host]:[port] for\n incoming connections.")
    print("-e --execute=file_to_run   - execute the given file upon\n receiving a connection")
    print("")