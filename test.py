from mcstatus import JavaServer

server = JavaServer.lookup("mcac.cc")
status = server.status()
msg = f"服务器在线人数: {status.players.online}, ping: {status.latency}"

print(msg)
