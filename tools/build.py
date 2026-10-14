"""Regenerate site and PDF from projects.json; --check rejects stale committed outputs."""
from pathlib import Path
import argparse
import subprocess
import sys
import tempfile
import shutil

root=Path(__file__).resolve().parents[1]
outputs=('index.html','portfolio.css','portfolio.js','portfolio-summary.pdf')
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check',action='store_true')
args=parser.parse_args()
with tempfile.TemporaryDirectory() as directory:
    target=Path(directory) if args.check else root
    if args.check:
        shutil.copytree(root/'tools',target/'tools')
        shutil.copyfile(root/'projects.json',target/'projects.json')
    for script in ('build_site.py','build_pdf.py'):
        subprocess.run([sys.executable,str(target/'tools'/script)],check=True)
    if args.check:
        stale=[name for name in outputs if not (root/name).exists() or (root/name).read_bytes()!=(target/name).read_bytes()]
        if stale:raise SystemExit('Regenerate outputs: '+', '.join(stale))
        print('Canonical metadata and all generated outputs agree')
