# pmdrc-randomizer

A randomizer for the GBA game "Pokémon Mystery Dungeon: Red Rescue Team".

This software is in development. The following checked elements are the features already included, and the unchecked ones are planned to be included:

- [X] Randomize Pokémon in dungeon floors *(Bosses and some parts of the Makuhita's Dojo mazes remain unchanged to prevent crashing)*.
- [X] Randomize Pokémon moveset.

*...More coming soon...*

## Download and execution

There are two options to run the randomizer, one is by running the executable file, and the other one is by running the source code directly.

### Direct binary release

Go to [Releases](https://github.com/Suguivy/pmdrc-randomizer/releases), and select the more recent version of the executable file. There are two, one for Linux and other for Windows.

### Run from source code

You can also clone the reposity and run the `main.py` file directly. Make sure you have `git` and `python` installed on your machine:

## Building

In Linux, you can build the program by running the `build.sh` script. You need to have the `pyinstaller` package. Install it with `pip3 install pyinstaller`.

## Usage

### Configuration

**NOTE:** Make sure you are using the US rom. Other versions have not been tested.

**NOTE:** You maybe should make a backup of your game before randomize it.

First, edit the `config.json` file. There are two options:
- `"randomizeDungeonPokemon"`: set to `true` if you want to randomize the Pokémon that will appear in the dungeon. Set to `false` otherwise.
- `"randomizePokemonMoves"`: set to `true` if you want to randomize the moves that Pokémon learn by level. Set to `false` otherwise.

### Running

In Windows you can drag and drop the rom file into the executable.

In Linux, open a terminal where the executable is located, and pass the rom file as an argument, like:

```
$ ./pmdrc-randomizer <your-rom-file>
```

If it doesn't work, make sure first to give permisions to run the executable:

```
$ chmod +x pmdrc-randomizer
```

A new rom called "RANDOMIZED <the old rom file name>", will be generated.