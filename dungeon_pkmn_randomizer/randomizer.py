#!/usr/bin/env python

from dungeon_pkmn_randomizer.dungeon_pokemon import DungeonPokemon

def randomize(rom_path):
    print("Randomizing dungeon pkmns!")

    with open(rom_path, 'rb') as rom:
        bs_rom = bytearray(rom.read())
        addr = 0x4b6064
        end_addr = 0x4c2a9b

        poke = DungeonPokemon.from_memory(bs_rom, addr)
        poke.set_level(100)
        poke.set_p_id(0x019d)
        poke.write(bs_rom, addr)

        while addr < end_addr:
            poke = DungeonPokemon.from_memory(bs_rom, addr)
            if (poke.is_not_zero() and poke.can_be_replaced()
                    and DungeonPokemon.is_safe(addr)):
                poke.set_level(100)
                poke.randomize_p_id()
                poke.write(bs_rom, addr)
            addr += 8


    with open(rom_path, 'wb') as rom:
        rom.write(bs_rom)
