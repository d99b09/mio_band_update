import serial
# from stm32loader.main import Stm32Loader
from stm32loader import main as loader


if __name__ == '__main__':
    loader.main('-p', 'COM3', '-e', '-w', '-v', 'stm32c8t6_flashing_test_1sec.bin')  # stm32c8t6_flashing_test_1sec

    # '''
    # with open('stm32c8t6_flashing_test.bin', 'rb') as f:
    #     f_bytes = f.read()
    #     f_bytes_amount = len(f_bytes)
    #     packs_with_256_len = int(f_bytes_amount / 256)
    #     left_bytes_amount = f_bytes_amount % 256
    #
    #     # print(f_bytes_amount, packs_with_256_len, left_bytes_amount)
    #
    #     for i in range(packs_with_256_len):
    #         #  calculating first byte crc
    #         #  create the packet then sending it
    #         pass
    #
    #     #  create the packet with left bytes then sending it plus second byte crc
    # '''
