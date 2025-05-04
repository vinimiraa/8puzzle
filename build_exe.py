import os
import subprocess
import sys
import shutil

def build_executable():
    print("Iniciando a criação do executável...")
    
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    try:
        import PIL
    except ImportError:
        print("Pillow não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    
    if os.path.exists("build"):
        print("Removendo diretório 'build' anterior...")
        shutil.rmtree("build")
    
    if os.path.exists("dist"):
        print("Removendo diretório 'dist' anterior...")
        shutil.rmtree("dist")
    
    spec_file = """
block_cipher = None

a = Analysis(
    ['gui/app.py'],  # Alterado para apontar para gui/app.py
    pathex=['.'],  # Adicionar o diretório atual como caminho de busca
    binaries=[],
    datas=[('puzzle/*', 'puzzle'), ('search/*', 'search'), ('heuristics/*', 'heuristics'), ('utils/*', 'utils')],
    hiddenimports=['__future__'],
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
    name='8Puzzle',
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
    icon='icon.ico',
)
    """
    
    with open("8puzzle.spec", "w") as f:
        f.write(spec_file)
    
    print("Executando PyInstaller...")
    subprocess.check_call([
        sys.executable, 
        "-m", 
        "PyInstaller", 
        "8puzzle.spec", 
        "--clean"
    ])
    
    print(f"\nExecutável criado em: {os.path.abspath('dist/8Puzzle.exe')}")
# build_executable

if __name__ == "__main__":
    build_executable()
