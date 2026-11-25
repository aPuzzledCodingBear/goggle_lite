#!/usr/bin/env bash
set -euo pipefail

die() { printf '%s\n' "$*" >&2; exit 1; }
[[ $# -le 1 && $EUID != 0 ]] || die "Usage as the normal bench user: bash run-bench.sh [checkout-directory]"
here=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
checkout=${1:-"$HOME/FastCarPlay"}
cd -- "$checkout"
project=$(pwd -P)
exec 9>.goggle-fastcarplay.lock
flock -n 9 || die "Another FastCarPlay setup is active in this checkout."
settings=$project/conf/settings.txt
unit=goggle-fastcarplay-bench.service
rule=/etc/udev/rules.d/70-goggle-ccpa.rules
[[ -x out/app && -f "$settings" && ! -L conf && ! -L "$settings" ]] ||
    die "Run install.sh before starting the bench."
current=$(lsusb -d 1314:1521) || die "Connect the 1314:1521 CarPlay box to USB OTG."
[[ $(grep -c '^Bus ' <<< "$current") == 1 ]] || die "Expected exactly one matching CarPlay box."
id -Gn | tr ' ' '\n' | grep -qx plugdev || die "The bench account needs membership in plugdev."

if [[ -e "$rule" || -L "$rule" ]]; then
    [[ ! -L "$rule" ]] && cmp -s "$here/70-goggle-ccpa.rules" "$rule" || die "Existing USB rule differs: $rule"
else
    sudo install -m 0644 "$here/70-goggle-ccpa.rules" "$rule"
fi
sudo udevadm control --reload-rules
sudo udevadm trigger --action=change --subsystem-match=usb --attr-match=idVendor=1314 --attr-match=idProduct=1521
sudo udevadm settle --timeout=10
node=$(awk '/^Bus / { sub(/:$/, "", $4); print "/dev/bus/usb/" $2 "/" $4 }' <<< "$current")
test -r "$node" && test -w "$node" || die "The bench account cannot read and write $node."

usb_settings=$(grep -E '^[[:space:]]*(vendor-id|product-id)[[:space:]]*=' "$settings" || true)
if [[ -z "$usb_settings" ]]; then
    backup=$settings.before-ccpa
    if [[ -e "$backup" || -L "$backup" ]]; then
        [[ ! -L "$backup" ]] && cmp -s "$settings" "$backup" ||
            die "Existing configuration backup differs: $backup"
    else
        cp -p "$settings" "$backup"
    fi
    pending=$(mktemp "$settings.goggle.XXXXXX")
    trap 'rm -f "$pending"' EXIT
    cp -p "$settings" "$pending"
    { printf '\n'; cat "$here/ccpa-1314-1521.conf"; } >> "$pending"
    mv -f "$pending" "$settings"
else
    [[ $(grep -c -E '^[[:space:]]*vendor-id[[:space:]]*=[[:space:]]*4884([[:space:]]*(#.*)?)$' <<< "$usb_settings") == 1 &&
       $(grep -c -E '^[[:space:]]*product-id[[:space:]]*=[[:space:]]*5409([[:space:]]*(#.*)?)$' <<< "$usb_settings") == 1 &&
       $(wc -l <<< "$usb_settings") -eq 2 ]] || die "Existing USB settings differ. Review $settings."
fi

if systemctl is-active --quiet "$unit"; then
    printf '%s is already running.\n' "$unit"
else
    sudo systemd-run --unit=goggle-fastcarplay-bench --collect --uid="$(id -un)" \
        --working-directory="$project" --setenv=SDL_VIDEODRIVER=KMSDRM \
        "$project/out/app" "$settings"
fi
systemctl is-active "$unit"
