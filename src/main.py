import os

from bardapi import Bard

TOKEN = "bghi_kny_2mb9-SJzLGhQXNGmdFQLrLOLJyNVZMtoofqzdHSPdPRThuBRtgHUbVPqWKiIg."


def main() -> None:
    bard = Bard(token=TOKEN, timeout=30)
    print(bard.get_answer("2023 Worlds에 대해 알려줘")["content"])


if __name__ == "__main__":
    main()
