# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Danvasion.py'],
             pathex=['/Users/blainequackenbush/PythonPractice/Danvasion'],
             binaries=[],
             datas=['bacon.png', 'blaine.png','brendan.png', 'bullet.png','cody.png',
              'daniel.png', 'lizzy.png' 'millie.png', 'paige.png', 'rachel.png',
              'sophie.png', 'stars.png', 'pew.wav', 'ow_brendan.wav', 'ow_cody.wav',
                    'ow_daniel.wav', 'ow_lizzy.wav', 'ow_millie.wav', 'ow_paige.wav', 'ow_rachel.wav'
                    'ow_sophie.wav', 'soundtrack.ogg', 'high_score.txt'],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Danvasion',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='Danvasion.app',
             icon=None,
             bundle_identifier=None)
