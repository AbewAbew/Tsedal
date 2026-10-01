"""Apply the tracked LMS source patch once, or fail clearly after upstream drift."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
repo = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / "bench/apps/lms"
patch = root / "patches/lms-branding.patch"

def check(*args):
    return subprocess.run(["git", "-C", str(repo), "apply", "--check", *args, str(patch)],
                          capture_output=True).returncode == 0

if check("--reverse"):
    print("Tsedal LMS branding is already applied.")
elif check():
    subprocess.run(["git", "-C", str(repo), "apply", str(patch)], check=True)
    print("Applied Tsedal LMS branding.")
else:
    raise SystemExit("LMS source differs from the tested version. Review patches/lms-branding.patch before building; no files were changed.")
