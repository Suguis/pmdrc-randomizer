# pmdrc-randomizer

> **NOTE: Development not active at the moment**

A randomizer for the GBA game "Pokémon Mystery Dungeon: Red Rescue Team".

This is a whole new randomizer, based on the [old](https://github.com/Suguivy/pmdrc-randomizer-old), but includes a GUI and it's more user friendly.

This software is in development. The following checked elements are the features already included, and the unchecked ones are planned to be included:

- [X] Randomize Pokémon in dungeon floors *(Bosses and some parts of the Makuhita's Dojo mazes remain unchanged to prevent crashing)*.
- [ ] Randomize Pokémon moveset.

*...More coming soon...*

## Download and execution

There are two options to run the randomizer, one is by running the executable file, and the other one is by running the source code directly.

### Direct binary release

Go to [Releases](https://github.com/Suguivy/pmdrc-randomizer/releases), and select the more recent version of the executable file. There are two, one for Linux and other for Windows.

### Run from source code

You can also clone the reposity and run the code directly. Make sure you have `git` and `python` installed on your machine:

```
git clone https://github.com/Suguivy/pmdrc-randomizer.git
cd pmdrc-randomizer
python main.py
```

## Usage

**NOTE:** Make sure you are using the US rom. Other versions have not been tested.

**NOTE:** You maybe should make a backup of your game before randomize it.

1. Open the randomizer and click on the *Select rom to randomize* button.
2. Select the rom file.
3. Check the options you want to apply.
4. Click on *Start* and wait for the *DONE!* text.
5. Now you can close the randomizer and play the game!
