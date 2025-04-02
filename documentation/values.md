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
| ``` v`health` ``` | Текущее здоровье |
| ``` v`maxHealth` ``` | Максимальное здоровье |
| ``` v`food` ``` | Текущий уровень голода |
| ``` v`saturation` ``` | Текущий уровень сытости |
| ``` v`exhaustion` ``` | Текущий уровень истощения |
| ``` v`xpLevel` ``` | Текущий уровень опыта |
| ``` v`xp` ``` | Текущее значение опыта (%) |
| ``` v`armor` ``` | Текущий уровень защиты |
| ``` v`fire` ``` | Текущее состояние горения |
| ``` v`air` ``` | Текущий уровень воздуха |
| ``` v`maxAir` ``` | Текущий максимум воздуха |
| ``` v`heldSlot` ``` | Текущий слот |
| ``` v`ping` ``` | Пинг игрока |
| ``` v`name` ``` | Имя игрока |
| ``` v`entityType` ``` | Тип сущности |
| ``` v`inventoryType` ``` | Тип открытого инвентаря |
| ``` v`inventoryTitle` ``` | Название открытого инвентаря |
| ``` v`inventorySlots` ``` | Количество слотов инвентаря |
| ``` v`langClient` ``` | Язык клиента |
| ``` v`langServer` ``` | Язык на сервере |
| ``` v`version` ``` | Версия игрока |
| ``` v`damage` ``` | Значение урона |
| ``` v`clickedSlot` ``` | Кликнутый слот |
| ``` v`newSlot` ``` | Новый слот |
| ``` v`oldSlot` ``` | Старый слот |
| ``` v`message` ``` | Сообщение игрока |
| ``` v`eventBlockLocation` ``` | Локация блока из события |
| ``` v`clickedItem` ``` | Кликнутый предмет |
| ``` v`eventBlock` ``` | Блок из события |
| ``` v`fishingState` ``` | Состояние рыбалки |
| ``` v`fishingCaught` ``` | Предмет с рыбалки  |
| ``` v`damageReason` ``` | Причина урона |
| ``` v`deathReason` ``` | Причина смерти |
| ``` v`eventItem` ``` | Предмет события |
| ``` v`interaction` ``` | Тип взаимодействия |
| ``` v`clickType` ``` | Тип клика |
| ``` v`cursorItem` ``` | Предмет в курсоре |
| ``` v`inventoryInteraction` ``` | Действие в инвентаре |
| ``` v`eventSlotType` ``` | Тип слота |
| ``` v`regainHealth` ``` | Количество здоровья |
| ``` v`regainHealthReason` ``` | Причина восстановления здоровья |
| ``` v`expCount` ``` | Количество опыта из события |
| ``` v`purchasedPoints` ``` | Приобретённое количество баллов игры |
| ``` v`goldTransactionCount` ``` | Количество золота из транзакции |
| ``` v`goldTransactionName` ``` | Название транзакции золота |
| ``` v`goldTransactionDisplayName` ``` | Отображаемое название транзакции золота |
| ``` v`shopTransactionKey` ``` | Ключ товара Mineland Studio |
| ``` v`shopTransactionDisplayName` ``` | Отображаемое название товара Mineland Studio |
| ``` v`location` ``` | Текущее местоположение |
| ``` v`eyeLocation` ``` | Текущее направление взгляда |
| ``` v`facing` ``` | Кардинальное направление |
| ``` v`targetBlockLocation` ``` | Местоположение целевого блока |
| ``` v`mainHandItem` ``` | Предмет из главной руки |
| ``` v`offhandItem` ``` | Предмет из второй руки |
| ``` v`helmet` ``` | Шлем сущности |
| ``` v`chestplate` ``` | Нагрудник сущности |
| ``` v`leggings` ``` | Поножи сущности |
| ``` v`boots` ``` | Ботинки сущности |
| ``` v`players` ``` | Подсчет количества игроков |
| ``` v`votes` ``` | Количество лайков за игру |
| ``` v`visitors` ``` | Количество уникальных посетителей |
| ``` v`variables` ``` | Количество динамических переменных |
| ``` v`points` ``` | Количество баллов у игры |
| ``` v`blocksLimit` ``` | Оставшееся количество блоков для редактирования |
| ``` v`codeLimit` ``` | Счётчик выполненных действий |
| ``` v`plotId` ``` | Айди игры |

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
