import random

def randomize(bs_rom: bytearray):
    addr     = 0x360c06 # Start address
    end_addr = 0x36799b

    in_tm_space = False

    while addr < end_addr:
        move_id = bs_rom[addr]
        if move_id & 0x80 != 0: # If it's a long move_id
            move_id = (move_id << 8) | bs_rom[addr+1]
            new_move_id = random_long_move_id()
            bs_rom[addr] = (0xff00 & new_move_id) >> 8
            bs_rom[addr+1] = 0x00ff & new_move_id
            addr += 2
            if not in_tm_space:
                addr += 1
        elif move_id != 0: # A short move_id
            bs_rom[addr] = random_short_move_id()
            addr += 1
            if not in_tm_space:
                addr += 1
        else: # A 0x00
            addr += 1
            in_tm_space = not in_tm_space


def random_long_move_id():
    invalid = [
        0x000,
        0x163,
        0x164,
        0x165,
        0x166,
        0x167,
        0x18b,
        0x194,
        0x195,
        0x19b,
        0x169,
        0x16a,
        0x16b,
        0x16c,
        0x16d,
        0x16e,
        0x16f,
        0x170,
        0x171,
        0x172,
        0x173,
        0x174,
        0x175,
        0x176,
        0x177,
        0x178,
        0x179,
        0x17a,
        0x17b,
        0x17c,
        0x17d,
        0x17e,
        0x17f,
        0x180,
        0x181,
        0x182,
        0x183,
        0x184,
        0x185,
        0x186,
        0x187,
        0x188,
        0x189,
        0x18a,
        0x18c,
        0x18d,
        0x18e,
        0x18f,
        0x190,
        0x191,
        0x192,
        0x193,
        0x196,
        0x197,
        0x198,
        0x199,
        0x19a,
        0x19c
    ]

    valid = [
        move_id for move_id in [*range(0x0000, 0x019d)]
        if move_id not in invalid
    ]

    r = random.choice(valid)
    return (r & 0x007f) | ((0x0180 & r) << 1) | 0x8000

def random_short_move_id():
    r = random.randint(0x01, 0x7f)
    return r
