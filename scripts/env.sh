#!/usr/bin/env bash
TSEDAL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export TSEDAL_ROOT
export PATH="$TSEDAL_ROOT/.local/node/node_modules/.bin:$TSEDAL_ROOT/.local/bench-cli/bin:$PATH"
