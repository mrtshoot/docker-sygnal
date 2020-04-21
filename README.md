# docker-sygnal
sygnal push gateway for matrix on docker

## Step 1
clone this repository on your system with this command on your owning directory
```
git clone https://github.com/mrtshoot/docker-sygnal.git
```

## Step 2
run this command to go on docker-sygnal root directory
```
cd docker-sygnal
```

## Step 3
run this command and go to sygnal directory and create copy of sygnal.yaml.sample
```
cd sygnal;cp sygnal.yaml.sample sygnal.yaml
```

## Step 4
Change your own Sygnal Configuration.your fcm package name and here should be matched.for more detail go to https://github.com/matrix-org/sygnal

## Step 5
go to root directory and run this command to create your own sygnaldocker image
```
docker build -t sygnal
```

## Step 6
Finally Run this command.
```
docker run -d --name mrtshoot-sygnal --restart always -p 0.0.0.0:5000:5000 sygnal
```
