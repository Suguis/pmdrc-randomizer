#!/usr/bin/env python

"""
This class represents a binary chunk of the two first bytes of the
correspondent entry of the Pokémon found on a dungeon. These two
bytes together represent the Pokémon ID and the level on which
the Pokémon will be found on the dungeon.

More info about the entry on:
https://datacrystal.romhacking.net/wiki/Pok%C3%A9mon_Mystery_Dungeon:_Red_Rescue_Team:Dungeons_Floors_Data:Pok%C3%A9mon_Found
"""

import random

class DungeonPokemon:
    def __init__(self, p_id, level):
        self.p_id = p_id
        self.level = level

    @staticmethod
    def from_memory(rom, address):
        poke = (rom[address] << 8) | rom[address + 1]
        p_id = (poke >> 8) | ((poke & 0x0001) << 8)
        level = (poke & 0x00ff) >> 1
        return DungeonPokemon(p_id, level)

    @staticmethod
    def is_safe(addr):
        """
        This list represents address positions containing specific Pokémon
        that will not be altered to prevent crashing
        """
        no_randomizable = [
            0x4b626c, # Diglett (Mt. Steel)
            0x4b6274, # Skarmory (Mt. Steel)
            0x4b654c, # Ekands (Sinister Woods)
            0x4b6554, # Gengar (Sinister Woods)
            0x4b655c, # Medicham (Sinister Woods)
            0x4b715c, # Charizard (Mt. Freeze)
            0x4b7164, # Alakazam (Mt. Freeze)
            0x4b716c, # Tyranitar (Mt. Freeze)
            0x4b743c, # Charizard (Magma Cavern)
            0x4b7444, # Tyranitar (Magma Cavern)
            0x4b7464, # Alakazam (Magma Cavern)
            0x4b92ac, # Medicham (Wish Cave)
            0x4bdcd4, # Farfetch'D (Normal Maze)
            0x4bdcdc, # Furret (Normal Maze)
            0x4bdce4, # Zigzagoon (Normal Maze)
            0x4bdd0c, # Ponyta (Fire Maze)
            0x4bdd14, # Slugma (Fire Maze)
            0x4bdd1c, # Magby (Fire Maze)
            0x4bdd3c, # Poliwag (Water Maze)
            0x4bdd9c, # Exeggcute (Grass Maze)
            0x4bdda4, # Sunkern (Grass Maze)
            0x4bddac, # Shroomish (Grass Maze)
            0x4bddb4, # Cacnea (Grass Maze)
            0x4bde04, # Voltorb (Electric Maze)
            0x4bde0c, # Electrike (Electric Maze)
            0x4bde34, # Swinub (Ice Maze)
            0x4bde3c, # Piloswine (Ice Maze)
            0x4bde4c, # Snorunt (Ice Maze)
            0x4bde9c, # Hitmonlee (Fight Maze)
            0x4bdea4, # Tyrogue (Fight Maze)
            0x4bdeac, # Meditite (Fight Maze)
            0x4bdecc, # Diglett (Ground Maze)
            0x4bdedc, # Phanpy (Ground Maze)
            0x4bdf24, # Pidgey (Flying Maze)
            0x4bdf34, # Farfetch'D (Flying Maze)
            0x4bdf3c, # Doduo (Flying Maze)
            0x4bdf64, # Wobbuffet (Psychic Maze)
            0x4bdfac, # Nidoran (Female) (Poison Maze)
            0x4bdfb4, # Nidoran (Male) (Poison Maze)
            0x4bdfdc, # Weedle (Bug Maze)
            0x4bdfe4, # Beedrill (Bug Maze)
            0x4bdfec, # Abra (Bug Maze)
            0x4bdff4, # Pinsir (Bug Maze)
            0x4be04c, # Geodude (Rock Maze)
            0x4be054, # Sudowoodo (Rock Maze)
            0x4be05c, # Pupitar (Rock Maze)
            0x4be084, # Gastly (Ghost Maze)
            0x4be0b4, # Bagon (Dragon Maze)
            0x4be0bc, # Shelgon (Dragon Maze)
            0x4be104, # Murkrow (Dark Maze)
            0x4be10c, # Poochyena (Dark Maze)
            0x4be134, # Aron (Steel Maze)
            0x4be144, # Beldum (Steel Maze)
            0x4be18c, # Nuzleaf (Team Shifty)
            0x4be194, # Shiftry (Team Shifty)
            0x4be1e4, # Tentacruel (Team Constrictor)
            0x4be1ec, # Octillery (Team Constrictor)
            0x4be1f4, # Cradily (Team Constrictor)
            0x4be214, # Blastoise (Team Hydro)
            0x4be224, # Feraligatr (Team Hydro)
            0x4be22c, # Swampert (Team Hydro)
            0x4be27c, # Graveler (Team Rumblerock)
            0x4be284, # Golem (Team Rumblerock)
            0x4be524, # Smeargle (Howling Forest)
        ]

        return not addr in no_randomizable

    def get_p_id(self):
        return self.p_id

    def get_level(self):
        return self.level

    def set_p_id(self, p_id):
        self.p_id = p_id

    def set_level(self, level):
        self.level = level

    def to_bin(self):
        # NOTE: The result is in big endian but we need to
        #       rewrite it in little endian

        poke_be = self.p_id + (self.level << 9)

        first_byte  = (0x00ff & poke_be) << 8
        second_byte = (0xff00 & poke_be) >> 8

        return first_byte | second_byte


    def randomize_p_id(self):
        """
        There are some Pokémon IDs that will not be used, for randomization,
        mainly because they will never appear in the dungeon in normal conditions.
        """
        not_used_p_ids = [
            0x000, # ??????????
            0x097, # Mew (doesnt appear)
            0x179, # Castform (Snowy Form) (better to use normal Castform)
            0x17a, # Castform (Sunny Form) "
            0x17b, # Castform (Rainy Form) "
            0x19e, # Deoxys (Normal Form) (only appears one time)
            0x1a1, # Deoxys (Attack Form) (only appears as a illusion)
            0x1a2, # Deoxys (Defense Form) "
            0x1a3, # Deoxys (Speed Form) "
            0x1a4, # Munchlax
            0x1a5, # Decoy
            0x1a6  # Statue
        ]

        valid_p_ids = [
            p_id for p_id in [*range(0x000, 0x1a7)]
            if p_id not in not_used_p_ids
        ]

        self.p_id = random.choice(valid_p_ids)

    def is_not_zero(self):
        return self.p_id > 0 and self.level > 0

    def can_be_replaced(self):
        """
        There are some Pokémon IDs that will not be changed, to prevent
        crashing, many of them are legendary Pokémon IDs.
        """
        no_replaceable = [
            0x000, # ??????????
            0x090, # Articuno
            0x091, # Zapdos
            0x092, # Moltres
            0x096, # Mewtwo
            0x097, # Mew
            0x10c, # Raikou
            0x10d, # Entei
            0x10e, # Suicune
            0x112, # Lugia
            0x113, # Ho-Oh
            0x114, # Celebi
            0x179, # Castform (Snowy Form)
            0x17a, # Castform (Sunny Form)
            0x17b, # Castform (Rainy Form)
            0x17c, # Kecleon
            0x195, # Regirock
            0x196, # Regice
            0x197, # Registeel
            0x198, # Latias
            0x199, # Latios
            0x19a, # Kyogre
            0x19b, # Groudon
            0x19c, # Rayquaza
            0x19d, # Jirachi
            0x19e, # Deoxys (Normal Form)
            0x1a1, # Deoxys (Attack Form)
            0x1a2, # Deoxys (Defense Form)
            0x1a3, # Deoxys (Speed Form)
            0x1a4, # Munchlax
            0x1a5, # Decoy
            0x1a6, # Statue
            0x1a7, # Rayquaza (cutscene)
        ]
        return not self.p_id in no_replaceable

    def __str__(self):
        return hex(self.to_bin())

    def write(self, rom, address):
        poke_bin = self.to_bin()

        first_byte  = (0xff00 & poke_bin) >> 8
        second_byte = 0x00ff & poke_bin

        rom[address]     = first_byte
        rom[address + 1] = second_byte
