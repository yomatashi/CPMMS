# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('./DB/serviceAccountKey.json', '.'), ('./face_recog_models/shape_predictor_68_face_landmarks.dat', 'face_recognition_models/models'), ('./face_recog_models/shape_predictor_5_face_landmarks.dat', 'face_recognition_models/models'), ('./face_recog_models/mmod_human_face_detector.dat', 'face_recognition_models/models'), ('./face_recog_models/dlib_face_recognition_resnet_model_v1.dat', 'face_recognition_models/models')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
