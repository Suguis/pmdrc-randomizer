#!/usr/bin/env python

from dungeon_pkmn_randomizer.dungeon_pokemon import DungeonPokemon

def randomize(rom_path):
    print("Randomizing dungeon pkmns!")

    with open(rom_path, 'rb') as rom:
        bs_rom = bytearray(rom.read())
        addr     = 0x4b6064 # Start address
        end_addr = 0x4c2a9b

        while addr < end_addr:
            poke = DungeonPokemon.from_memory(bs_rom, addr)
            if (poke.is_not_zero() and poke.can_be_replaced()
                    and DungeonPokemon.is_safe(addr)):
                poke.randomize_p_id()
                poke.write(bs_rom, addr)
            addr += 8

    with open(rom_path, 'wb') as rom:
        rom.write(bs_rom)
