from fabric import Connection
from invoke import Responder
try:
    c = Connection(host='localhost', user='user', port=22,connect_kwargs={
        "password":"password"
    })

    # check uname
    result = c.run('uname -s')
    print(result)

    # check who
    result = c.run("who")
    print(result)

    # check pwd
    result = c.run("pwd")
    print(result)

    # cd and git clone
    #result = c.run("cd ~/Project && git clone https://github.com/litondev/redis-socket.io")
    #print(result)

    #git_watchers = [
        #Responder(pattern = r"Username for .*", response="email\n"), 
        #Responder(pattern = r"Password for .*", response="password\n") 
    #]

    # git pull
    # result = c.run("cd ~/Project/myrepo && git pull origin user", pty=True, watchers=git_watchers)
    # print(result)

    # using strip
    result = c.run("pwd")
    print(result.stdout.strip())
except Exception as e:
    print(e)
    print("Terjadi Kesalahan")
