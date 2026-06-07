servers = ["Server-A", "Server-B", "Server-C"]

for request in range(10):
    print(f"Request {request} -> {servers[request % len(servers)]}")