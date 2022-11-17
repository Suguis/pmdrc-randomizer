#!/usr/bin/env python

import randomizers.dungeonPokemon
import randomizers.movesLearned

def randomize(rom_path, config):
    with open(rom_path, 'rb') as rom:
        bs_rom = bytearray(rom.read())

        if config["randomizeDungeonPokemon"]:
            randomizers.dungeonPokemon.randomize(bs_rom)

        if config["randomizePokemonMoves"]:
            randomizers.movesLearned.randomize(bs_rom)

    with open("RANDOMIZED " + rom_path, 'wb') as rom:
        rom.write(bs_rom)