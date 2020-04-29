# noVNC Display Container

This image is intended to be used for displaying X11 applications from other containers in a browser.

## Image Contents

* [Xvfb](http://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml) - X11 in a virtual framebuffer
* [x11vnc](http://www.karlrunge.com/x11vnc/) - A VNC server that scrapes the above X11 server
* [noNVC](https://kanaka.github.io/noVNC/) - A HTML5 canvas vnc viewer
* [Fluxbox](http://www.fluxbox.org/) - a small window manager
* [xterm](http://invisible-island.net/xterm/) - to demo that it works
* [supervisord](http://supervisord.org) - to keep it all running

## Variables

You can specify the following variables:

* `DISPLAY_WIDTH=<width>` (1024)
* `DISPLAY_HEIGHT=<height>` (768)
* `RUN_XTERM={yes|no}` (yes)
* `RUN_FLUXBOX={yes|no}` (yes)

## Stand-alone Demo

Run:

Replace "mysecret" below with your password of choice. Note that you need to fill out enough of the information in openssl for both a private key and a certificate to be created.

```
$ openssl req -new -x509 -days 365 -nodes -out self-signed.pem -keyout self-signed.pem
```

``` LSF_DOCKER_PORTS='8080:8080' bsub -G compute-ris -Is -R 'select[port8080=1]' -q general-interactive -a 'docker(us.gcr.io/ris-appeng-shared-qa/novnc:latest)' python3 /app/startup.py```
Open a browser and see the `xterm` demo at `http://<IP>:8080/vnc.html`

The IP address can be grabbed from observing which blade the job falls on: ```<<Starting on compute1-exec-187.ris.wustl.edu>>``` would mean the IP would be ```http://compute1-exec-187.ris.wustl.edu:8080/vnc.html```

Some notable features:

* An `x11` network is defined to link the IDE and novnc containers
* The IDE `DISPLAY` environment variable is set using the novnc container name
* The screen size is adjustable to suit your preferences via environment variables
* The only exposed port is for HTTP browser connections

## On DockerHub / GitHub

This container is based on work done by theasp:

* DockerHub [theasp/novnc](https://hub.docker.com/r/theasp/novnc/)
* GitHub [theasp/docker/novnc](https://github.com/theasp/docker)