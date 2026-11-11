# Writes the entry summary to the output directory.
import os, shutil
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'summary.txt')
dst = os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.txt')
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copyfile(src, dst)
