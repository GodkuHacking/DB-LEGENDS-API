
# DB Legends Python Module

![DBLLL](https://github.com/RoseInjector/DB-LEGENDS-API/assets/138173273/d0191e53-9e9b-4881-a654-a30de70600be)

Welcome to the DB Legends Python module! This module allows you to access and retrieve information about Dragon Ball Legends characters from the provided `chars.json` file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RoseInjector/DB-LEGENDS-API.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DB-LEGENDS-API
   ```

3. Run the DB Legends Python script:

   ```bash
   python db_legends.py
   ```

## Usage

To use the DB Legends Python module, follow these steps:

1. Make sure you have the `chars.json` file in the same directory as the script.

2. Run the script and provide the character ID when prompted.

   ```bash
   python db_legends.py
   ```

3. The script will display detailed information about the character with the provided ID, including their name, ID, color, rarity, tags, base stats, and max stats.

## Example

Suppose you want to retrieve information about the character with the ID `DBL51-03U`. Here's how to do it:

```bash
python db_legends.py
Enter the character ID to find (e.g., DBL51-03U): DBL44-01S
```

The script will then display the character's information:

```
 {
    "name": "Jiren: Full Power",
    "id": "DBL44-01S",
    "color": "PUR",
    "rarity": "SPARKING",
    "tags": [
      "Universe 11",
      "Powerful Opponent",
      "Rival Universe",
      "Universe Rep",
      "Male",
      "SPARKING",
      "Ranged Type",
      "PUR",
      "Universe Survival Saga (S)",
      "Jiren",
      "DBL44-01S",
      "Armored Strike Arts",
      "Attack UP (Saiyan)",
      "Ultimate Arts",
      "Special Cover Change (Strike)",
      "Special Cover Change Nullification",
      "Endurance"
    ],
    "main_ability": {
      "name": "It doesn't matter how high you climb; I will not lose!",
      "effect": "Randomly destroys one of your own Cards and draws the Ultimate Arts Card \"Burst Impact\" next.Restores own health by 30% and Ki by 30.Applies Attribute Upgrade \"-50% to enemy's 'Sustained Damage CUT' effects\" to self for 15 timer counts.If enemy is inflicted with Faint, +40% to Ultimate damage inflicted for 15 timer counts.Requirements: 25 timer counts must elapse."
    },
    "unique_ability": {
      "unique_start_abilities": [
        {
          "ability_name": "Burning Ultimate Warrior",
          "ability_effect": "+20% to damage inflicted against \"Tag: Saiyan\" (cannot be cancelled).Applies the following effects to self when battle starts:+90% to damage inflicted (cannot be cancelled).Reduces damage received by 40% (cannot be cancelled).Applies the following effects to self when this character enters the battlefield:Restores Ki by 50.+40% to damage inflicted for 15 timer counts (activates four times).Reduces damage received by 30% for 15 timer counts (activates four times).Cancels Attribute Downgrades and Abnormal Conditions.Restores own health by 35% when 2 allies are defeated."
        },
        {
          "ability_name": "You're nothing in the face of my power!",
          "ability_effect": "Applies the following effects to self when an enemy activates Rising Rush:+40% to damage inflicted (cannot be cancelled) (activates twice).+70% to Ki Recovery (cannot be cancelled) (activates twice).Increases Arts Card Draw Speed by 1 level (cannot be cancelled) (activates once).Restores own health by 30% only once when it reaches 0 (cannot be cancelled) (activates once).Applies Buff Effect \"Nullifies enemy's special actions that activate when changing cover\" for 30 timer counts.Knocks enemy back to long range if a cover change is performed against their Strike Arts attack (activates during assists).[Comboable Arts]Special Move ArtsInflicts enemy with Attribute Downgrade \"+10 to all Arts costs\" for 10 timer counts when enemy switches characters while this character is on the battlefield."
        }
      ]
    },
    "base_stats": {
      "power": 10112,
      "health": 23422,
      "strike_atk": 2653,
      "strike_def": 1641,
      "blast_atk": 2602,
      "blast_def": 1600
    },
    "max_stats": {
      "power": 889457,
      "health": 1430830,
      "strike_atk": 162093,
      "strike_def": 100268,
      "blast_atk": 158928,
      "blast_def": 97730
    },
    "strike": "Strike (Impact)Applies Attribute Upgrade \"-10% to enemy's 'Sustained Damage CUT' effects\" to self for 10 timer counts on hit.*Blast Armor when charging forward.",
    "shot": "Blast (Impact)Restores own Ki by 10 upon activation.",
    "image_url": "https://i.imgur.com/hAmV3G5.png",
    "special_move": {
      "name": "Omegaheat Magnetron",
      "effect": "Deals massive Explode damage.+30% to Special Move damage inflicted for 3 timer counts upon activation.Additional +70% to Special Move damage inflicted for 3 timer counts if enemy is inflicted with Faint."
    },
    "special_skill": {
      "name": "Blazing Fighting Spirit",
      "effect": "Applies the following effects to self upon activation:Restores Ki by 50.+30% to Blast damage inflicted for 20 timer counts.+30% chance for next Strike Arts or Blast Arts to inflict enemy with Faint on hit (cannot be stacked) (activates twice).Gradually restores own health each timer count for 20 timer counts.Destroys all enemy cards on hit.[Comboable Arts]Strike ArtsBlast ArtsSpecial Move ArtsUltimate Arts"
    },
    "ultimate_skill": {
      "name": "Burst Impact",
      "effect": "Deals supreme Impact damage.Applies the following effects to self upon activation:+40% to Ultimate damage inflicted for 3 timer counts.Nullifies enemy's \"Restores own health when it reaches 0\" effects when this character attacks for 3 timer counts.A portion of the damage inflicted will also be dealt to enemy members on standby on hit (this cannot cause them to be defeated).*Blast Armor when charging forward."
    },
    "z_ability": {
      "one": {
        "tags": ["Universe Survival Saga (S)", "Rival Universe"],
        "effect": "+22% to \"Episode: Universe Survival Saga (S)\" or \"Tag: Rival Universe\" base Blast Attack & Strike Defense during battle."
      },
      "two": {
        "tags": [
          "Universe Survival Saga (S)",
          "Rival Universe",
          "Powerful Opponent"
        ],
        "effect": "+26% to \"Episode: Universe Survival Saga (S)\", \"Tag: Rival Universe\", or \"Tag: Powerful Opponent\" base Blast Attack & Strike Defense during battle."
      },
      "three": {
        "tags": [
          "Universe Survival Saga (S)",
          "Rival Universe",
          "Powerful Opponent",
          "Rival Universe"
        ],
        "effect": "+32% to \"Episode: Universe Survival Saga (S)\", \"Tag: Rival Universe\", or \"Tag: Powerful Opponent\" base Blast Attack & Strike Defense and +15% to \"Tag: Rival Universe\" base Blast Defense during battle."
      },
      "four": {
        "tags": [
          "Universe Survival Saga (S)",
          "Rival Universe",
          "Powerful Opponent",
          "Rival Universe"
        ],
        "effect": "+38% to \"Episode: Universe Survival Saga (S)\", \"Tag: Rival Universe\", or \"Tag: Powerful Opponent\" base Blast Attack & Strike Defense and +18% to \"Tag: Rival Universe\" base Blast Defense during battle."
      }
    },
    "is_lf": true,
    "is_tag": false,
    "has_zenkai": false
  }
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Dragon Ball Legends](https://www.dblegends.dragonball-legends.com/en/): For providing the character data.
- [RoseInjector](https://github.com/RoseInjector): For creating this Python module.

Feel free to contribute to this project or report issues if you encounter any problems.
```
