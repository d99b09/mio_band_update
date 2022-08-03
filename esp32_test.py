import esptool

if __name__ == '__main__':
    '''
    bootloader_dio_40m.bin - .../.platformio/packages/framework-arduinoespressif32/tools/sdk/bin/bootloader_dio_40m.bin
    partitions.bin - .../project_folder/.pio/build/esp32doit-devkit-v1/partitions.bin (VARIABLE)
    boot_app0.bin - .../.platformio/packages/framework-arduinoespressif32/tools/partitions/boot_app0.bin
    firmware.bin - .../project_folder/.pio/build/esp32doit-devkit-v1/firmware.bin (VARIABLE)
    '''
    

    esptool.main(['-p', 'COM5', '-b', '115200', '--before', 'default_reset', '--after', 'hard_reset', '--chip', 'esp32',
                  'write_flash', '-z', '--flash_mode', 'dio', '--flash_size', 'detect', '--flash_freq', '40m', '0x1000',
                  'bootloader_dio_40m.bin', '0x8000', 'partitions.bin', '0xe000', 'boot_app0.bin', '0x10000',
                  'firmware.bin'])
