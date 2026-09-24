#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

TW_VERSION="v3.4.17"

case "$(uname -s)" in
  Linux) os="linux" ;;
  Darwin) os="macos" ;;
  *)
    echo "build-css.sh: unsupported OS: $(uname -s)" >&2
    exit 1
    ;;
esac

case "$(uname -m)" in
  x86_64 | amd64) arch="x64" ;;
  arm64 | aarch64) arch="arm64" ;;
  *)
    echo "build-css.sh: unsupported architecture: $(uname -m)" >&2
    exit 1
    ;;
esac

mkdir -p bin
if [ ! -x bin/tailwindcss ]; then
  url="https://github.com/tailwindlabs/tailwindcss/releases/download/${TW_VERSION}/tailwindcss-${os}-${arch}"
  echo "build-css.sh: downloading ${url}"
  curl -fSL --retry 3 -o bin/tailwindcss "${url}"
  chmod +x bin/tailwindcss
fi

bin/tailwindcss \
  -c tailwind.config.js \
  -i assets/css/tailwind.input.css \
  -o assets/css/tailwind.css \
  --minify \
  "$@"
