#!/usr/bin/env python

import os
import json

import randomizers.dungeonPokemon
import randomizers.movesLearned

def randomize(ba_rom: bytearray):
    with open('config.json') as config_json:
        config = json.load(config_json)

    if config["randomizeDungeonPokemon"]:
        randomizers.dungeonPokemon.randomize(ba_rom)

    if config["randomizePokemonMoves"]:
        randomizers.movesLearned.randomize(ba_rom)