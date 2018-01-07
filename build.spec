# -*- mode: python -*-
import cefpython3, os, fnmatch

block_cipher = None

# add extra files
cefpython3_dir = os.path.dirname(cefpython3.__file__)
extra_files = [
    (os.path.join(cefpython3_dir, 'cef.pak'), '.'),
    (os.path.join(cefpython3_dir, 'cef_100_percent.pak'), '.'),
    (os.path.join(cefpython3_dir, 'cef_200_percent.pak'), '.'),
    (os.path.join(cefpython3_dir, 'cef_extensions.pak'), '.'),
    (os.path.join(cefpython3_dir, 'icudtl.dat'), '.'),
    (os.path.join(cefpython3_dir, 'natives_blob.bin'), '.'),
    (os.path.join(cefpython3_dir, 'subprocess.exe'), '.'),
    (os.path.join(cefpython3_dir, 'locales\zh-CN.pak'), 'locales'),
    (os.path.join(cefpython3_dir, 'locales\en-US.pak'), 'locales'),
    (os.path.join('.', 'resources\index.html'), 'resources')
]

# add bundle js
resources_dir = os.listdir('./resources')  
pattern = "bundle*.js"
for entry in resources_dir:  
    if fnmatch.fnmatch(entry, pattern):
        extra_files.append((os.path.join('.', 'resources\%s' % entry), 'resources'))

a = Analysis(['main.py'],
             binaries=[],
             datas=extra_files,
             hiddenimports=["json"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# remove unused files
binaries = []
for item in a.binaries:
    if item[0] not in ['python36.dll', 'msvcm90.dll', 
                        'msvcp90.dll', 'msvcr90.dll', 
                        'MSVCR100.dll', 'VCRUNTIME140.dll',
                        'cefpython3.cefpython_py36',
                        'cefpython3.cefpython_py35',
                        'cefpython3.cefpython_py34',
                        'bz2', 'pyexpat', 'select', 
                        'unicodedata', 'win32pipe',
                        'pywintypes27.dll', 'ucrtbase.dll',
                        'Microsoft.VC90.CRT.manifest'] \
            and not item[0].startswith('api-ms-win-'):
        binaries.append(item)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='hello',
          debug=False,
          strip=False,
          upx=True,
          console=False)

coll = COLLECT(exe,
               binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='hello')