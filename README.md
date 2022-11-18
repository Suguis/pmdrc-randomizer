# pmdrc-randomizer

A randomizer for the GBA game "Pokémon Mystery Dungeon: Red Rescue Team".

This software is in development. The following checked elements are the features already included, and the unchecked ones are planned to be included:

- [X] Randomize Pokémon in dungeon floors *(Bosses and some parts of the Makuhita's Dojo mazes remain unchanged to prevent crashing)*.
- [X] Randomize Pokémon moveset.

*...More coming soon...*

## Download

Go to [Releases](https://github.com/Suguivy/pmdrc-randomizer/releases), and select the more recent version of the executable file. There are two, one for Linux and other for Windows.

## Usage

**NOTE:** Make sure you are using the US rom. Other versions have not been tested.

**NOTE:** You maybe should make a backup of your game before randomize it.

1. Extract the `zip` file. You will find to files: `config.json` in which you can configure what things to randomize, and the executable file `pmdrc-randomizer`.

2. First, edit the `config.json` file to fit your needs. There are two options:
- `"randomizeDungeonPokemon"`: set to `true` if you want to randomize the Pokémon that will appear in the dungeon. Set to `false` otherwise.
- `"randomizePokemonMoves"`: set to `true` if you want to randomize the moves that Pokémon learn by level. Set to `false` otherwise.

3. Then, run the `pmdrc-randomizer` program, and make sure that `config.json` is in the same directory as the executable.

4. A file selection window will pop up. Select the original rom file of the game.

5. Wait a bit, and a file saving window will pop up. Write the name you want for the randomized rom file, and save it.

## Building

You can build the program by running the `build.sh` script. You need to have the `pyinstaller` package. Install it with `pip3 install pyinstaller`. A zip will be generated in the same directory as the build script.