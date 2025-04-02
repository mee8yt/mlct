## Значения
К значениям относятся все метки для установки параметров блоков кода. Это все предметы из вкладки "Переменные" в /dev

   - [Значения](values.md)
     - [Игровое значение](#игровое-значение---vvalue-)
     - [Местоположение](#местоположение---lx-y-z-y-p-)
     - [Предмет](#предмет---imaterial-c-m-)
     - [Частица](#частица---particlevariant-)
     - [Зелье](#зелье---vid-d-f-)

### Игровое значение - **``` v`value` ```** [🔝](#значения)
Вид значения, который возвращает какой-либо параметр сущности, мира или события. В кодинге представлен в виде "яблока".

Заполнение:
```js
  var `temp` = v`message`;
//               ^^^^^^^
//                Ключ
```
| **Код** | **Название** |
| --- | --- |
| ``` v`health` ``` |  |
| ``` v`maxHealth` ``` |  |
| ``` v`food` ``` |  |
| ``` v`saturation` ``` |  |
| ``` v`exhaustion` ``` |  |
| ``` v`xpLevel` ``` |  |
| ``` v`xp` ``` |  |
| ``` v`armor` ``` |  |
| ``` v`fire` ``` |  |
| ``` v`air` ``` |  |
| ``` v`maxAir` ``` |  |
| ``` v`heldSlot` ``` |  |
| ``` v`ping` ``` |  |
| ``` v`name` ``` |  |
| ``` v`entityType` ``` |  |
| ``` v`inventoryType` ``` |  |
| ``` v`inventoryTitle` ``` |  |
| ``` v`inventorySlots` ``` |  |
| ``` v`langClient` ``` |  |
| ``` v`langServer` ``` |  |
| ``` v`version` ``` |  |
| ``` v`damage` ``` |  |
| ``` v`clickedSlot` ``` |  |
| ``` v`newSlot` ``` |  |
| ``` v`oldSlot` ``` |  |
| ``` v`message` ``` |  |
| ``` v`eventBlockLocation` ``` |  |
| ``` v`clickedItem` ``` |  |
| ``` v`eventBlock` ``` |  |
| ``` v`fishingState` ``` |  |
| ``` v`fishingCaught` ``` |  |
| ``` v`damageReason` ``` |  |
| ``` v`deathReason` ``` |  |
| ``` v`eventItem` ``` |  |
| ``` v`interaction` ``` |  |
| ``` v`clickType` ``` |  |
| ``` v`cursorItem` ``` |  |
| ``` v`inventoryInteraction` ``` |  |
| ``` v`eventSlotType` ``` |  |
| ``` v`regainHealth` ``` |  |
| ``` v`regainHealthReason` ``` |  |
| ``` v`expCount` ``` |  |
| ``` v`purchasedPoints` ``` |  |
| ``` v`goldTransactionCount` ``` |  |
| ``` v`goldTransactionName` ``` |  |
| ``` v`goldTransactionDisplayName` ``` |  |
| ``` v`shopTransactionKey` ``` |  |
| ``` v`shopTransactionDisplayName` ``` |  |
| ``` v`location` ``` |  |
| ``` v`eyeLocation` ``` |  |
| ``` v`facing` ``` |  |
| ``` v`targetBlockLocation` ``` |  |
| ``` v`mainHandItem` ``` |  |
| ``` v`offhandItem` ``` |  |
| ``` v`helmet` ``` |  |
| ``` v`chestplate` ``` |  |
| ``` v`leggings` ``` |  |
| ``` v`boots` ``` |  |
| ``` v`players` ``` |  |
| ``` v`votes` ``` |  |
| ``` v`visitors` ``` |  |
| ``` v`variables` ``` |  |
| ``` v`points` ``` |  |
| ``` v`blocksLimit` ``` |  |
| ``` v`codeLimit` ``` |  |
| ``` v`plotId` ``` |  |

### Местоположение - **``` l`x y z y p` ```** [🔝](#значения)
Вид значения, который представляет собой конкретную точку на карте /build. В кодинге представлен в виде "бумаги".

Заполнение:
```js
  var `temp` = l`x y z yaw pitch`;
//               ^ ^ ^ ^^^ ^^^^^
//             Параметры местоположения

  var `temp` = l`1 3`;
  player.send(temp); -> "1.00 3.00 0.00 0.00 0.00"
```

### Предмет - **``` i`material c m` ```** [🔝](#значения)
Вид значения, который представляет собой предмет, взятый из креатива.

Заполнение:
```js
  var `temp` = i`material count meta`;
//               ^^^^^^^^ ^^^^^ ^^^^
//        Айди предмета   Колво Дата 

  var `temp` = i`diamond`;
  player.send(temp); -> "ItemStack(Diamond x 1)"
```

### Частица - **``` particle`variant` ```** [🔝](#значения)
Вид значения, который представляет собой один из вариантов визуальных частиц для игрока. В кодинге представлен в виде "незерской звезды".

Заполнение:
```js
  var `temp` = particle`variant`;
//                      ^^^^^^^
//                     Вид частицы

  var `temp` = particle`EXPLOSION_LARGE`;
  player.send(temp); -> "1.00 3.00 0.00 0.00 0.00"
```

| **Код** | **Название** |
| --- | --- |
| ``` particle`EXPLOSION_LARGE` ``` |  |
| ``` particle`EXPLOSION_HUGE` ``` |  |
| ``` particle`FIREWORKS_SPARK` ``` |  |
| ``` particle`WATER_BUBBLE` ``` |  |
| ``` particle`WATER_SPLASH` ``` |  |
| ``` particle`WATER_WAKE` ``` |  |
| ``` particle`SUSPENDED` ``` |  |
| ``` particle`SUSPENDED_DEPTH` ``` |  |
| ``` particle`CRIT` ``` |  |
| ``` particle`CRIT_MAGIC` ``` |  |
| ``` particle`SMOKE_NORMAL` ``` |  |
| ``` particle`SMOKE_LARGE` ``` |  |
| ``` particle`SPELL` ``` |  |
| ``` particle`SPELL_INSTANT` ``` |  |
| ``` particle`SPELL_MOB` ``` |  |
| ``` particle`SPELL_MOB_AMBIENT` ``` |  |
| ``` particle`SPELL_WITCH` ``` |  |
| ``` particle`DRIP_WATER` ``` |  |
| ``` particle`DRIP_LAVA` ``` |  |
| ``` particle`VILLAGER_ANGRY` ``` |  |
| ``` particle`VILLAGER_HAPPY` ``` |  |
| ``` particle`TOWN_AURA` ``` |  |
| ``` particle`NOTE` ``` |  |
| ``` particle`PORTAL` ``` |  |
| ``` particle`ENCHANTMENT_TABLE` ``` |  |
| ``` particle`FLAME` ``` |  |
| ``` particle`LAVA` ``` |  |
| ``` particle`FOOTSTEP` ``` |  |
| ``` particle`CLOUD` ``` |  |
| ``` particle`REDSTONE` ``` |  |
| ``` particle`SNOWBALL` ``` |  |
| ``` particle`SNOW_SHOVEL` ``` |  |
| ``` particle`SLIME` ``` |  |
| ``` particle`HEART` ``` |  |
| ``` particle`BARRIER` ``` |  |
| ``` particle`WATER_DROP` ``` |  |
| ``` particle`ITEM_TAKE` ``` |  |
| ``` particle`MOB_APPEARANCE` ``` |  |
| ``` particle`DRAGON_BREATH` ``` |  |
| ``` particle`END_ROD` ``` |  |
| ``` particle`DAMAGE_INDICATOR` ``` |  |
| ``` particle`SWEEP_ATTACK` ``` |  |
| ``` particle`TOTEM` ``` |  |
| ``` particle`SPIT` ``` |  |

### Зелье - **``` v`id d f` ```** [🔝](#значения)
Вид значения, который представляет собой конкретную точку на карте /build. В кодинге представлен в виде "бумаги".

Заполнение:
```js
  var `temp` = potion`id time force`;
//                    ^^ ^^^^ ^^^^^
//            Айди зелья Время Сила

  var `temp` = potion`speed 120`;
  player.send(temp); -> "SPEED:(120t-0x)"
```

| **Код** | **Название** |
| --- | --- |
| ``` potion`speed` ``` |  |
| ``` potion`slowness` ``` |  |
| ``` potion`haste` ``` |  |
| ``` potion`fatigue` ``` |  |
| ``` potion`strength` ``` |  |
| ``` potion`healing` ``` |  |
| ``` potion`harming` ``` |  |
| ``` potion`leaping` ``` |  |
| ``` potion`nausea` ``` |  |
| ``` potion`regeneration` ``` |  |
| ``` potion`resistance` ``` |  |
| ``` potion`fire_resistance` ``` |  |
| ``` potion`water_breathing` ``` |  |
| ``` potion`invisible` ``` |  |
| ``` potion`blindness` ``` |  |
| ``` potion`night_vision` ``` |  |
| ``` potion`hunger` ``` |  |
| ``` potion`weakness` ``` |  |
| ``` potion`poison` ``` |  |
| ``` potion`wither` ``` |  |
| ``` potion`health_boost` ``` |  |
| ``` potion`absorption` ``` |  |
| ``` potion`saturation` ``` |  |
| ``` potion`glowing` ``` |  |
| ``` potion`levitation` ``` |  |
| ``` potion`luck` ``` |  |
| ``` potion`bad_luck` ``` |  |
