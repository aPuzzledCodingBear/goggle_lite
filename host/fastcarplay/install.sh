#!/usr/bin/env bash
set -euo pipefail

die() { printf '%s\n' "$*" >&2; exit 1; }
[[ $# -le 1 ]] || die "Usage: bash install.sh [checkout-directory]"
[[ $(uname -s) == Linux && $(uname -m) == aarch64 && $EUID != 0 ]] ||
    die "Run as the normal bench user on 64-bit Raspberry Pi OS."
grep -qx 'VERSION_CODENAME=bookworm' /etc/os-release ||
    die "This installer targets Bookworm."
here=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
checkout=${1:-"$HOME/FastCarPlay"}
origin=https://github.com/niellun/FastCarPlay.git
revision=f483456318344710d2890fc7ee0d67608892dea2
patch_file=$here/ccpa-usb-configuration.patch

sudo apt-get -o APT::Update::Error-Mode=any update
sudo apt-get install -y --no-install-recommends \
    ca-certificates git build-essential xxd pkg-config \
    libsdl2-dev libsdl2-ttf-dev libavformat-dev libavcodec-dev libavutil-dev \
    libswscale-dev libusb-1.0-0-dev libssl-dev ffmpeg usbutils \
    python3-gpiozero python3-evdev python3-libgpiod gpiod

if [[ ! -e "$checkout" && ! -L "$checkout" ]]; then
    git init "$checkout"
    git -C "$checkout" remote add origin "$origin"
fi
[[ -d "$checkout/.git" && ! -L "$checkout" && ! -L "$checkout/.git" ]] ||
    die "Expected a dedicated FastCarPlay checkout: $checkout"
cd -- "$checkout"
exec 9>.goggle-fastcarplay.lock
flock -n 9 || die "Another FastCarPlay setup is active in this checkout."
[[ $(git remote get-url origin) == "$origin" ]] || die "Unexpected FastCarPlay origin."
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
    git fetch --depth=1 origin "$revision"
    git checkout --detach "$revision"
fi
[[ $(git rev-parse HEAD) == "$revision" ]] ||
    die "Checkout has a different revision. Use a fresh directory."
git diff --cached --quiet || die "Checkout has staged source changes."

if git diff --quiet; then
    git apply --check "$patch_file"
    git apply "$patch_file"
fi
git -c diff.algorithm=myers diff --no-ext-diff --no-color --binary --abbrev=7 \
    --src-prefix=a/ --dst-prefix=b/ -U3 HEAD -- |
    cmp -s - "$patch_file" || die "Tracked changes differ from the approved compatibility patch."

make -j1 release
[[ -x out/app ]] || die "Build did not produce out/app."
libraries=$(ldd out/app)
if grep -q 'not found' <<< "$libraries"; then
    printf '%s\n' "$libraries" >&2
    die "Executable has unresolved libraries."
fi
[[ ! -L conf ]] || die "Expected a normal configuration directory."
mkdir -p conf
if [[ ! -e conf/settings.txt && ! -L conf/settings.txt ]]; then
    cp settings.txt conf/settings.txt
fi
[[ -f conf/settings.txt && ! -L conf/settings.txt ]] ||
    die "Expected a normal config file at conf/settings.txt."
printf 'Built %s at %s\n' "$PWD/out/app" "$revision"
