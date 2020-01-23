# Nginx + Tornado Server + MongoDB Dockers
# Build, run and watch scripts

#### Requirements
* Bash
* Openssl
* Docker
* Gnome-terminal, scripts tested in Ubuntu system.

## First steps

#### Configuration

Vars.sh contains variables. You may want to change "name" variable value for project name. All dockers will get this name as prefix.

Nginx needs certificates for 443 port serving, you can easily bulid cert files with generate_keys.sh script. Just run script in directory and fill the questions.
> cert files adds to docker in building time.


#### Building
First, you need to build dockers and network. Check simple build.sh, you can add # prefix to the line for the disable command.

```
./build.sh
```
Dockers and network created.

#### Network check
You should run the servers and network for getting ip adresses.

```
./run.sh start
```
All servers running and watching windows must be opened. Check network watching window and get servers ip adresses. Now you can fix tornado.server ip adress in nginx.conf and mongo.server ip in server.py file.

Then you need to rebuild nginx docker.
> Add # prefix to mongo and tornado commands in build.sh and run again.


## Running

Start and stop all dockers.
```
./run.sh start
...
./run.sh stop
```

Only Nginx and Mongo.
```
./run.sh start server
...
./run.sh stop server
```

Only Tornado
```
./run.sh start app
...
./run.sh stop app
```

## Deploy Your Project

Copy your static files to the nginx_root and application to the tornado_root directory. Changes affects instantly.
> Nginx cache keeps old versions of files in memory, you should refresh your browser.

## Runtime
You can access docker console wit these commands;
```
docker exec -it <prjname>_nginx.server /bin/bash
docker exec -it <prjname>_tornado.server /bin/bash
docker exec -it <prjname>_mongo.server /bin/bash
```
> < prjname > is you wrote project name in vars.sh "name" value.