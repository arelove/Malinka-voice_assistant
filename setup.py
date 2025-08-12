from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name="Voice Assistant",
    version="1.0",
    # description="Modern Dashboard of Voice Assistant",
    author="Ar3love",
    options={
        'build_exe': {
            'include_files': files,
            'packages': ['numpy']  # Список пакетов для включения
        },
    },
    executables=[target]
)
