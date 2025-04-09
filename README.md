# MLCT ✨
[English](README.md) | [Русский](README_ru.md)

**MLCT** *(**M**ine**L**and **C**ode **T**ranslator)* - Mod for installing written version of block code on Mineland server.

## Content 🗂️

This repository is for compilator only

1. [Installation](#installation-)
2. [Syntax](#syntax-)
	1. [Data types](#data-types)
	2. [Setting variables](#setting-variables)
	3. [Calling actions](#calling-actions)
	4. [Selectors](#selectors)
	5. [Events](#events)
	6. [Functions](#functions)
	7. [Loops](#functions)
	8. [Environment variables](#environment-variables)
	9. [Modules](#modules)
3. [Documentation](#documentation-)
4. [Examples](#examples-)
5. [Syntax highlight](#syntax-highlight-)
6. [Translation](#translation-)

# Installation 🤙

1. Install Python version 3.11.1 or above
2. Head to [releases](https://github.com/mee8yt/mlct-compiler/releases/latest) page and click "Download ZIP"
3. Unzip the file
4. Run `Setup.py`

> [!IMPORTANT]
> You won't be able to compile the code without Python installed

>[!NOTE]
> After installation, dont make changes in compilator folder. Dont delete compilator source files

# Syntax 💻

## Data types
```js
123 // Number
"Text" // Text
`Variable` // Variable / "complex" value
```

You can put symbol(s) before variable to convert it in "complex" value:

```js
`Variable` // Dynamic variable
s`Saved variable` // It's now saved variable
a`Array` // Array
as`Saved array` // Array can also be saved
l`Location` // Location: set of 5 numbers
v`Value` // Game value
i`Item` // Any item
potion`Potion` // Potion effect
particle`Particle` // Particle

"Text" // Text
c"Text component" // Text component
cls"Text with no color" // "&" symbol wont covert to "§"
```

These symbols making a value from another one are called value shell.

However, you need to set values with mind. E.g. line break:

```js
"Line break \
 on purpose"
```

Keep in mind that on the new line any symbol up to hard letters (tabulations, spaces and other line breaks) won't be taken into account.

Also, if you don't put backslash ("\\") at the end of first line, compilator will count this text as not finished:

```js
"Line break with
no backslash" 
// -> LexerError: STRING token "Line break with" doesn't have the end
```

From free-form text ("words" not wrapped in variables or strings) and various data types, basic coding structures can be derived. These include code and event blocks, conditional piston notations, and various non-block structures that simplify direct interaction with compilator.

## Setting variables
```js
var `test` = 0;
var s`%player% money` = 0;
```

Setting variables like this is called non-block structure. Later you'll understand why.

## Calling actions
```js
player.send("Greetings!");
```

This line describes "Player action - Send message".

Now let's figure out the structure:

```js
   player.send("Greetings!");
// ^^^^^^
// Block

player.send("Greetings!");
//    ^
//    Separator

player.send("Greetings!");
//     ^^^^
//     Action name

player.send("Greetings!");
//          ^^^^^^^^^^^^
//          Arguments

player.send("Greetings!");
//                       ^
//                       Block end
```

> [!IMPORTANT]
> Every code block must end with semicolon (";")

Based on this, block structure is: `block.type(arguments);`, and non-block structure is: `operation target: arguments;` (e.g. var)

### Arguments

Let's take the "Send title" action for example. It has arguments "text1, text2, number1, number2, number3". You can set them in different ways:

1. Positional
```js
player.title("Hello", "This is my world", 20, 20, 20);
```

2. By name
```js
player.title(text1="Hello", number1=0);
```

3. Combined
```js
player.title(text1="Hello", "This is my world");

// Positional arguments are set on the next unspecified value:
player.title(number2=5, "Hello", "This is my world"); // Same thing as (text1="Hello", text2="This is my world", number2=5);
```

#### Switch
A switch is defined by number representing how many times it's clicked:

```js
player.send(["You've completed the parkour", "Wanna try again? /play"], 2); // The switch will trigger 2 times and will be the "String splitting"
```

#### Value
Arguments that represent the value can
pass multiple values. You need to use the "value list" for this. Put the values in `[]` separated by commas.

```js
player.send(["Player liked the game", "Like it too? /like"]);
```

## Selectors
Player actions and conditions can have selectors (These are when you click <KBD>Shift+RMB</KBD>).

```js
player.send<all>("&fPlayer &e%player%&f has joined the game!"); // Sends the message to all players
```

>[!WARNING]
>You can put selectors only before round brackets

### "Not" parameter
When you need to invert the condition, you use the "Not" parameter (same thing as "Not" arrow):

```js
ifPlayer.nameEquals("Mee8YT") {} // Returns true when player name IS Mee8YT
ifPlayer.nameEquals<not>("Mee8YT") {} // Returns true when player name IS NOT Mee8YT
```

>[!NOTE]
>You can use this parameter with other selectors. The order doesn't matter (`ifPlayer.holdingItem<killer><not>()` and `ifPlayer.holdingItem<not><killer>()` will work the same)

## Events

### Player event

```js
PlayerEvent(join) {} // join - event
```

### World event

```js
WorldEvent(start) {} // start - event
```

## Functions

```js
Function(func) {} // func - name

game.startFunction("func"); // Call the function
```

## Loops
```js
Loop(loop, 20) {} // loop - name, 20 - iteration rate 

game.startLoop("loop"); // Start the loop
```

>[!WARNING]
> For functions, loops, and events that has space in their names, you should use the ``
>
> E.g. for the function "anti fly" you write: \`anti fly\`

## Environment variables

To optimize the code and increase readability, you can use environment variables (constants).

These variables are accessible only for the compilator and don't require additional "Set variable" blocks:

```js
const message = "Made using MLCT"; // Creating the constant

PlayerEvent(join) {
    player.send(@env(message)); // "Made using MLCT"
} 
```

>[!IMPORTANT]
> You can set the constant only before the first code block

Constants can store list of values:

```js
const items = [i`diamond`, i`emerald`];
```

You can use it differently:

```js
player.giveItems(@env(items)); // Diamond and emerald
player.giveItems([@env(items), i`stone`]); // Diamond, emerald, and stone
```

To keep the code clean, you can store constants in `enviroments.json` file:

```json
{
   "message": {
      "token": "STRING",
      "shell": null,
      "value": "Some text"
   }
} 
```

`code.txt`:
```js
PlayerEvent(join) {
  player.send(@env(message)); // "Some text"
}
```

## Modules

Modules can make code even more readable! Module is another code file that'll be compiled with the main file.

To use the code from the module, you need to import it:

`module.txt`:
```js
Function(sayHi) {
   player.send("Hello, %player%!");
}
```

`main.txt`:
```js
import "module.txt"; // Importing the module

PlayerEvent(join) {
   game.startFunction("sayHi"); // "Hello, %player%!"
}
```

> [!IMPORTANT]
>You can use `import` only before the first code block

Compilator replaces import with file code and processes it later. So the final result will look like:

```js
Function(sayHi) {
   player.send("Hello, %player%!");
}

PlayerEvent(join) {
   game.startFunction("sayHi");
}
```

You can also use constants from other modules. 

Sometimes you may need to import the module at the end of the code:


```js
import "module.txt" end; // Module won't replace the import, but will be placed at the end of the code
```

# Documentation 📜
You can find more information about the code here:
   - [Activators](documentation/activators.md) 
     -  [Player event](documentation/activators.md#событие-игрока---playereventevent--none--)
     -  [World event](documentation/activators.md#событие-мира---worldeventevent--none--)
     -  [Loops](documentation/activators.md#циклы---loopname-0--none--)
     -  [Functions](documentation/activators.md#функции---functionname--none--)
   - [Actions](documentation/actions.md)
     - [Player action](documentation/actions.md#действие-игрока---playeractionargs-)
     - [Game action](documentation/actions.md#игровое-действие---gameactionargs-)
     - [Set variable](documentation/actions.md#установить-переменную---varactionargs-)
     - [Working with arrays](documentation/actions.md#работа-с-массивами---arrayactionargs-)
     - [Select the object](documentation/actions.md#выбрать-объект---selectaction-)
   - [Conditions](documentation/conditions.md)
     - [If player](documentation/conditions.md#если-игрок---ifplayerconditionargs--none--)
     - [If value](documentation/conditions.md#если-значение---ifvalueconditionargs--none--)
     - [If entity](documentation/conditions.md#если-существо---ifentityconditionargs--none--)
     - [If game](documentation/conditions.md#если-игра---ifgameconditionargs--none--)
     - [Else](documentation/conditions.md#иначе---else--none--)
   - [Values](documentation/values.md)
     - [Game value](documentation/values.md#игровое-значение---vvalue-)
     - [Location](documentation/values.md#местоположение---lx-y-z-y-p-)
     - [Item](documentation/values.md#предмет---imaterial-c-m-)
     - [Particle](documentation/values.md#частица---particlevariant-)
     - [Potion](documentation/values.md#зелье---vid-d-f-)
   - [Other](documentation/other.md)
     - [Constants](documentation/other.md#константы-)
     - [Errors](documentation/other.md#ошибки-)
     - [Comments](documentation/other.md#комментарии-)
     - [Language module](documentation/other.md#языковой-модуль-)
# Examples 📧

Vector gun:
```js
PlayerEvent(rightClick) {
   ifPlayer.holdingItem(i`golden_hoe`) {
      ifPlayer.itemHasDelay<not>(i`golden_hoe`) {
         ifVar.notEquals(`%player% vector.status`, 1) {
            player.setDelay(i`golden_hoe`, 10);
            var `%player% vector.status` = 1;
            var `%player% vector.speed` = 0;
            var `%player% vector.particle` = particle`CRIT`;
            var `%player% vector.final_pos` = v`targetBlockLocation`;
            var.setLocation(`%player% vector.pos`, v`location`, y_mode = 1, y = 0.6);
            game.callFunction("gun.vector");
            game.callFunction("gun.raycast");
         }
      }
   }
}

Function(`gun.vector`) {
      @comment("GUN / Create vector", 9, "gun.vector", 13, "Creates the &3&l&nvector&f from sight.");

      var `%player% vector.pos.ray_coefficient` = 1;
      var.getLocationValue(`%player% vector.pos.yaw`, `%player% vector.pos`, 3);
      var.getLocationValue(`%player% vector.pos.pitch`, `%player% vector.pos`, 4);
      var.radians(`%player% vector.pos.rad(yaw)`, `%player% vector.pos.yaw`);
      var.radians(`%player% vector.pos.rad(pitch)`, `%player% vector.pos.pitch`);
      var.sinus(`%player% vector.pos.sin(yaw)`, `%player% vector.pos.rad(yaw)`);
      var.sinus(`%player% vector.pos.sin(pitch)`, `%player% vector.pos.rad(pitch)`);
      var.cosinus(`%player% vector.pos.cosinus(yaw)`, `%player% vector.pos.rad(yaw)`);
      var.cosinus(`%player% vector.pos.cosinus(pitch)`, `%player% vector.pos.rad(pitch)`);

      var.multiply(`%player% vector.pos.vector_x`, -1, [`%player% vector.pos.sin(yaw)`, `%player% vector.pos.sin(yaw)`, `%player% vector.pos.cosinus(pitch)`, `%player% vector.pos.ray_coefficient`]);
      var.multiply(`%player% vector.pos.vector_y`, -1, [`%player% vector.pos.sin(pitch)`, `%player% vector.pos.ray_coefficient`]);
      var.multiply(`%player% vector.pos.vector_z`, `%player% vector.pos.cosinus(yaw)`, [`%player% vector.pos.cosinus(pitch)`, `%player% vector.pos.ray_coefficient`]);
}

Function(`gun.raycast`) {
   pass;
}

PlayerEvent(takeDamagePlayer) {
   pass;
}
```

# Syntax highlight 💡

Official syntax highlight is only available in Visual Studio Code. Download [the extenstion](https://marketplace.visualstudio.com/items?itemName=Mee8YT.mlct) to make it work.

You may want to use JavaScript syntax/file type if you're using another code editor as it's the closest to MLCT syntax.

# Translation 📄
| Language | Compilator | Documentation |
|---|:---:|:---:|
| 🇷🇺 Русский | 🟩 | 🟩 |
| 🇬🇧 English | 🟩 | 🟥 |
| 🇮🇹 Italiano | 🟩 | 🟥 |
| 🇵🇹 Português | 🟨 | 🟥 |
| 🇩🇪 Deutsch | 🟩 | 🟥 |
| 🇵🇱 Polski | 🟨 | 🟥 |
| 🇱🇻 Latviešu | 🟨 | 🟥 |
| 🇭🇺 Magyar | 🟩 | 🟥 |
| 🇺🇦 Українська | 🟩 | 🟥 |
| 🇧🇾 Беларуская | 🟩 | 🟥 |
| 🇰🇿 Қазақша | 🟨 | 🟥 |
| 🇨🇳 中国人 | 🟩 | 🟥 |
| 🇮🇳 हिन्दी | 🟨 | 🟥 |
| 🇬🇷 Ελληνικά | 🟨 | 🟥 |
| 🇪🇬 اَلْعَرَبِيَّةُ | 🟩 | 🟥 |

<sup>🟩 - 100% translated, 🟨 - in process, 🟥 - no translation.</sup>
