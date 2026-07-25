import os
import sys
from pathlib import Path
import subprocess

AARCH64_LINUX_GNU = "aarch64-linux-gnu-release"
ARM_NONE_EABI = "arm-none-eabi-release"
X86_64_LINUX_GNU = "x86_64-linux-gnu-release"
X86_64_MSVC = "x86_64-msvc-release"
X86_64_MINGW32 = "x86_64-w64-mingw32-release"

LIB_SHARED = "share"
LIB_STATIC = "static"

def get_os_name():
    if sys.platform.startswith('win'):
        return 'Windows'
    elif sys.platform.startswith('linux'):
        return 'Linux'
    elif sys.platform.startswith('darwin'):
        return 'macOS'
    else:
        return sys.platform

def get_config_command(build_os:str,build_platform: str, lib_name: str,lib_type: str) -> str:

    lib_dir = f"source/{lib_name}"
    build_dir = f"build/{build_platform}/{lib_name}"
    install_dir = Path(__file__).resolve().parent / "install" /build_platform
    install_dir_str  =install_dir.as_posix()

    # print(f"pwd: {lib_dir}")
    # print(f"pwd: {build_dir}")
    # print(f"pwd: {install_dir_str}")

    if lib_type ==LIB_SHARED:
        lib_type_config = "ON"
    else:
        lib_type_config = "OFF"

    if build_os =="Windows":
        return f'cmake -S {lib_dir} -B {build_dir} -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS={lib_type_config} -DCMAKE_INSTALL_PREFIX={install_dir_str}'
    else:
        return f'cmake -S {lib_dir} -B {build_dir} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS={lib_type_config} -DCMAKE_INSTALL_PREFIX={install_dir_str}'

def get_build_command(build_platform: str, lib_name: str) -> str:

    build_dir = f"build/{build_platform}/{lib_name}"
    return f"cmake --build {build_dir}"

def get_install_command(build_platform: str, lib_name: str) -> str:

    build_dir = f"build/{build_platform}/{lib_name}"
    return f"cmake --install {build_dir}"

def get_command(build_os:str,build_platform: str, lib_name: str,lib_type: str) -> str:

    target_dir = Path.cwd() / "source" / lib_name
    if os.path.isdir(target_dir):
        print(f"lib : {lib_name}")
    else:
        print(f"lib error: {lib_name}")

    print(f"platform: {build_platform}")
    print(f"os: {build_os}")


    cmd_config=get_config_command(build_os,build_platform,lib_name,lib_type)

    cmd_build= get_build_command(build_platform,lib_name)

    cmd_install= get_install_command(build_platform,lib_name)

    print(cmd_config)
    print(cmd_build)
    print(cmd_install)


def main():

    build_os =get_os_name()
    if build_os not in ("Windows", "Linux"):
        print(" os: error")
        sys.exit(1)
    else:
        print(f"os: {build_os}")

    pwd_dir = Path(__file__).resolve().parent
    print(f"pwd: {pwd_dir}")

    """ windows """

    build_platform =  X86_64_MINGW32
    lib_name =  "SDL"
    lib_type =  LIB_SHARED

    get_command(build_os,build_platform,lib_name,lib_type)

    build_platform =  X86_64_MINGW32
    lib_name =  "freetype"
    lib_type =  LIB_SHARED

    get_command(build_os,build_platform,lib_name,lib_type)

    build_platform =  X86_64_MINGW32
    lib_name =  "rlottie"
    lib_type =  LIB_STATIC

    get_command(build_os,build_platform,lib_name,lib_type)

    """ linux """

    # build_platform =  X86_64_LINUX_GNU
    # lib_name =  "freetype"
    # lib_type =  LIB_SHARED

    # get_command(build_os,build_platform,lib_name,lib_type)

    # build_platform =  X86_64_LINUX_GNU
    # lib_name =  "rlottie"
    # lib_type =  LIB_STATIC

    # get_command(build_os,build_platform,lib_name,lib_type)

if __name__ == "__main__":
    main()