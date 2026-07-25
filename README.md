
ThirdParty use
    环境变量中配置

        cmake .. -DCMAKE_PREFIX_PATH=D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/Release -G "MinGW Makefiles"
        mingw32-make.exe  

        $env:PATH = "D:\studio\workspace\c_cpp_workspace2\ThirdParty\install\x86_64-w64-mingw32-release\bin;$env:PATH"

    cmake 配置

        if(WIN32)
        list(APPEND CMAKE_PREFIX_PATH
            "${PROJECT_SOURCE_DIR}/../ThirdParty/install/x86_64-w64-mingw32-release"
        )
        endif()

        if(WIN32)

        add_custom_command(TARGET main POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy_if_different
                $<TARGET_FILE:SDL2::SDL2>
                $<TARGET_FILE_DIR:main>
        )

        endif()

SDL2
    #git clone https://github.com/libsdl-org/SDL.git
    git clone --branch release-2.28.5 https://github.com/libsdl-org/SDL.git

    windows
        build   yes

            cmake -S ThirdParty/source/SDL -B ThirdParty/build/Release/SDL -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/Release
            cmake -S ThirdParty/source/SDL -B ThirdParty/build/Release/SDL -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=/home/sean/workspace/c_cpptest/ThirdParty/install/Release
            cmake --build ThirdParty/build/Release/SDL

            cmake --install ThirdParty/build/Release/SDL


    linux
        build   error
            
        
        install
            sudo apt update
            sudo apt install libsdl2-dev

            dpkg -L libsdl2-dev
            dpkg -s libsdl2-dev

freetype

    # git clone https://github.com/freetype/freetype.git
    git clone --branch VER-2-13-1 https://github.com/freetype/freetype.git

        官网：https://freetype.org 
        官方下载：https://download.savannah.gnu.org/releases/freetype/

    windows

        build       yes

    linux
        build       yes

            -- Install configuration: "Release"
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/ft2build.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftmm.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/ftstdlib.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/ftmodule.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/integer-types.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/mac-support.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/ftheader.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/public-macros.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftmodapi.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftbitmap.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftsynth.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftlcdfil.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftgasp.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/fttrigon.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftrender.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftstroke.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftadvanc.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftbbox.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftlzw.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/fterrdef.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftotval.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftincrem.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftlogging.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftmac.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftcolor.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftsystem.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/tttables.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftgxval.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/fttypes.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/t1tables.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftoutln.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ttnameid.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftpfr.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftchapters.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/fterrors.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftglyph.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftdriver.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftparams.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftimage.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftbzip2.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftwinfnt.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftsizes.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftlist.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftmoderr.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftcache.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftfntfmt.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftbdf.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftgzip.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/otsvg.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/freetype.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftsnames.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/ftcid.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/tttags.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/ftconfig.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/freetype2/freetype/config/ftoption.h
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/pkgconfig/freetype2.pc
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/libfreetype.so.6.20.0
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/libfreetype.so.6
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/libfreetype.so
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/cmake/freetype/freetype-config.cmake
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/cmake/freetype/freetype-config-release.cmake
            -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/cmake/freetype/freetype-config-version.cmake

            ldd main
                linux-vdso.so.1 (0x00007ffe1c9c1000)
                libfreetype.so.6 => /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/libfreetype.so.6 (0x00007d9a3960e000)
                libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007d9a39200000)
                libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007d9a395e1000)
                /lib64/ld-linux-x86-64.so.2 (0x00007d9a396e3000)

        install
            sudo apt update
            sudo apt install libfreetype6-dev

            dpkg -s libfreetype6-dev
lvgl

    git clone --branch v8.3.10 https://github.com/lvgl/lvgl.git
    git clone --branch v8.3.0 https://github.com/lvgl/lv_drivers.git
    

        模拟器仓库  https://github.com/lvgl/lv_port_pc_eclipse
        git clone --branch release/v8.3 https://github.com/lvgl/lv_port_pc_eclipse.git


rlottie

    git clone --branch v0.2 https://github.com/Samsung/rlottie.git

    windows

        build   yes         !!! -DLIB_INSTALL_DIR=lib

            cmake -S source/rlottie -B build/x86_64-w64-mingw32-release/rlottie -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release -DLIB_INSTALL_DIR=lib

            cmake --build build/x86_64-w64-mingw32-release/rlottie
            cmake --install build/x86_64-w64-mingw32-release/rlottie
                -- Install configuration: "Release"
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/lib/pkgconfig/rlottie.pc
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/include/rlottie.h
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/include/rlottie_capi.h
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/include/rlottiecommon.h
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/lib/librlottie.a
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/lib/cmake/rlottie/rlottieTargets.cmake
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/lib/cmake/rlottie/rlottieTargets-release.cmake
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/lib/cmake/rlottie/rlottieConfig.cmake
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/lib/cmake/rlottie/rlottieConfigVersion.cmake
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/lib/liblibrlottie-image-loader.dll.dll.a
                -- Installing: D:/studio/workspace/c_cpp_workspace2/ThirdParty/install/x86_64-w64-mingw32-release/bin/librlottie-image-loader.dll

    linux 
        build   yes           !!! -DLIB_INSTALL_DIR=lib -DCMAKE_CXX_FLAGS="-include limits"
            cmake -S source/rlottie -B build/x86_64-linux-gnu-release/rlottie -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=/home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release -DLIB_INSTALL_DIR=lib -DCMAKE_CXX_FLAGS="-include limits"

            cmake --build build/x86_64-linux-gnu-release/rlottie
            cmake --install build/x86_64-linux-gnu-release/rlottie
                -- Install configuration: "Release"
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/pkgconfig/rlottie.pc
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/rlottie.h
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/rlottie_capi.h
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/include/rlottiecommon.h
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/librlottie.a
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/cmake/rlottie/rlottieTargets.cmake
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/cmake/rlottie/rlottieTargets-release.cmake
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/cmake/rlottie/rlottieConfig.cmake
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/cmake/rlottie/rlottieConfigVersion.cmake
                -- Installing: /home/sean/studio/c_cpp_workspace2/ThirdParty/install/x86_64-linux-gnu-release/lib/librlottie-image-loader.so

ArduinoJson

    git clone --branch v6.21.2 https://github.com/bblanchon/ArduinoJson.git


STM_hal

    #v1.8.6 https://github.com/STMicroelectronics/STM32CubeF1.git       
    git clone --branch 5.4.0 https://github.com/ARM-software/CMSIS_5.git CMSIS/CMSIS_5.4.0
    git clone --branch v1.1.10 https://github.com/STMicroelectronics/stm32f1xx-hal-driver.git
    git clone --branch v4.3.5 https://github.com/STMicroelectronics/cmsis-device-f1.git

    #v1.27.1 https://github.com/STMicroelectronics/STM32CubeF4.git
    # git clone --branch 5.4.0 https://github.com/ARM-software/CMSIS_5.git CMSIS/CMSIS_5.4.0
    git clone --branch v1.8.1 https://github.com/STMicroelectronics/stm32f4xx-hal-driver.git
    git clone --branch v2.6.8 https://github.com/STMicroelectronics/cmsis-device-f4.git

    #v1.11.1 https://github.com/STMicroelectronics/STM32CubeH7.git
    git clone --branch 5.6.0 https://github.com/ARM-software/CMSIS_5.git CMSIS/CMSIS_5.6.0
    git clone --branch v1.11.1 https://github.com/STMicroelectronics/stm32h7xx-hal-driver.git
    git clone --branch v1.10.3 https://github.com/STMicroelectronics/cmsis-device-h7.git

STM_SVD

    #https://github.com/Open-CMSIS-Pack

    STM32H750.svd
        git clone --branch v4.1.3 https://github.com/Open-CMSIS-Pack/STM32H7xx_DFP.git

    STM32F407.svd
        git clone --branch v3.1.1 https://github.com/Open-CMSIS-Pack/STM32F4xx_DFP.git

    STM32F103xx.svd
        git clone --branch v2.4.1 https://github.com/BoaSean/STM32F1xx_DFP.git

rt-thread

    # git clone --branch v4.1.0 https://github.com/RT-Thread/rt-thread.git
    
    git clone --branch v4.1.0 https://github.com/BoaSean/rtt-kernel.git  rtt-kernel-v4.1.0
    git clone --branch v4.1.0 https://github.com/BoaSean/rtt-sdk.git  rtt-sdk-v4.1.0


    # git clone --branch v5.1.0 https://github.com/RT-Thread/rt-thread.git
    
    git clone --branch v5.1.0 https://github.com/BoaSean/rtt-kernel.git 
    git clone --branch v5.1.0 https://github.com/BoaSean/rtt-sdk.git

    4.1.0   
        CPPPATH = Env.get('CPPPATH', ['']) + group.get('LOCAL_CPPPATH', [''])
        CPPDEFINES = Env.get('CPPDEFINES', ['']) + group.get('LOCAL_CPPDEFINES', [''])

        CPPPATH = list(Env.get('CPPPATH', [''])) + group.get('LOCAL_CPPPATH', [''])
        CPPDEFINES = list(Env.get('CPPDEFINES', [''])) + group.get('LOCAL_CPPDEFINES', [''])

art-pi

    git clone --branch 1.3.0 https://github.com/RT-Thread-Studio/sdk-bsp-stm32h750-realthread-artpi.git