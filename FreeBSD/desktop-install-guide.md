# FreeBSD Desktop install guide

## bspwm
```sh
pkg install -y bspwm
sh $(dirname "$0")/keylaunch
echo "exec /usr/local/bin/bspwm" >> /root/.xsession
sh $(dirname "$0")/xdm
```

## i3
```sh
pkg install -y i3 i3status
echo "exec /usr/local/bin/i3" >> /root/.xsession
sh $(dirname "$0")/xdm
```

## Gnome 3
```sh
pkg install -y gnome3
sysrc gdm_enable=YES
```

## MATE
```sh
pkg install -y mate
echo "exec /usr/local/bin/mate-session" >> /root/.xsession
sh $(dirname "$0")/xdm
```