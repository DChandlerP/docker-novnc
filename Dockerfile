FROM ubuntu:latest

# Install git, supervisor, VNC, & X11 packages
RUN set -ex; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      bash \
      emacs \
      git \
      nano \
      net-tools \
      novnc \
      python3\
      supervisor \
      vim \
      x11vnc \
      xfce4 \
      xfce4-terminal \
      xvfb \
      && apt-get clean

# Setup demo environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    DISPLAY=:0.0 \
    DISPLAY_WIDTH=1440 \
    DISPLAY_HEIGHT=900 \
    RUN_XTERM=yes \
    RUN_FLUXBOX=yes

COPY . /app
RUN python3 -m unittest app/test.py
# CMD ["supervisord", "-c", "/app/supervisord.conf"]

