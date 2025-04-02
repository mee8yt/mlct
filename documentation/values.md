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
| **Значение сущности** |
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
| ``` particle`EXPLOSION_LARGE` ``` | Большой взрыв |
| ``` particle`EXPLOSION_HUGE` ``` | Взрыв |
| ``` particle`FIREWORKS_SPARK` ``` | След от фейерверка |
| ``` particle`WATER_BUBBLE` ``` | Пузырьки воды |
| ``` particle`WATER_SPLASH` ``` | Брызги воды |
| ``` particle`WATER_WAKE` ``` | Следы от воды |
| ``` particle`SUSPENDED` ``` | Туман |
| ``` particle`SUSPENDED_DEPTH` ``` | Туман из глубин |
| ``` particle`CRIT` ``` | Критический удар |
| ``` particle`CRIT_MAGIC` ``` | Магический удар |
| ``` particle`SMOKE_NORMAL` ``` | Дым |
| ``` particle`SMOKE_LARGE` ``` | Большой дым |
| ``` particle`SPELL` ``` | Белый аромат |
| ``` particle`SPELL_INSTANT` ``` | Блёстки |
| ``` particle`SPELL_MOB` ``` | Тёмные силы |
| ``` particle`SPELL_MOB_AMBIENT` ``` | Серое воздуховление |
| ``` particle`SPELL_WITCH` ``` | Частицы ведьмы |
| ``` particle`DRIP_WATER` ``` | Капающая вода |
| ``` particle`DRIP_LAVA` ``` | Капающая лава |
| ``` particle`VILLAGER_ANGRY` ``` | Гнев жителя |
| ``` particle`VILLAGER_HAPPY` ``` | Счастье жителя |
| ``` particle`TOWN_AURA` ``` | Туманный бедрок |
| ``` particle`NOTE` ``` | Нота |
| ``` particle`PORTAL` ``` | Портал |
| ``` particle`ENCHANTMENT_TABLE` ``` | Символы стола зачарований |
| ``` particle`FLAME` ``` | Огонёк |
| ``` particle`LAVA` ``` | Капли лавы |
| ``` particle`FOOTSTEP` ``` | Следы |
| ``` particle`CLOUD` ``` | Облачко |
| ``` particle`REDSTONE` ``` | Редстоун |
| ``` particle`SNOWBALL` ``` | Куски снежка |
| ``` particle`SNOW_SHOVEL` ``` | Падающий снег |
| ``` particle`SLIME` ``` | Куски слизи |
| ``` particle`HEART` ``` | Сердце |
| ``` particle`BARRIER` ``` | Барьер |
| ``` particle`WATER_DROP` ``` | Капли воды |
| ``` particle`ITEM_TAKE` ``` | Пустующий предмет |
| ``` particle`MOB_APPEARANCE` ``` | Появление древнего стража |
| ``` particle`DRAGON_BREATH` ``` | Драконье дыхание |
| ``` particle`END_ROD` ``` | Стержень энда |
| ``` particle`DAMAGE_INDICATOR` ``` | Тёмные сердечки |
| ``` particle`SWEEP_ATTACK` ``` | Удар по площади |
| ``` particle`TOTEM` ``` | Таинственный тотем |
| ``` particle`SPIT` ``` | Плевок от ламы |

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
| ``` potion`speed` ``` | Скорость |
| ``` potion`slowness` ``` | Медлительность |
| ``` potion`haste` ``` | Спешка |
| ``` potion`fatigue` ``` | Утомление |
| ``` potion`strength` ``` | Сила |
| ``` potion`healing` ``` | Лечение |
| ``` potion`harming` ``` | Моментальный урон |
| ``` potion`leaping` ``` | Прыжок |
| ``` potion`nausea` ``` | Тошнота |
| ``` potion`regeneration` ``` | Регенерация |
| ``` potion`resistance` ``` | Сопротивление к урону |
| ``` potion`fire_resistance` ``` | Огнестойкость |
| ``` potion`water_breathing` ``` | Подводное дыхание |
| ``` potion`invisible` ``` | Невидимость |
| ``` potion`blindness` ``` | Слепота |
| ``` potion`night_vision` ``` | Ночное видение |
| ``` potion`hunger` ``` | Голод |
| ``` potion`weakness` ``` | Слабость |
| ``` potion`poison` ``` | Отравление |
| ``` potion`wither` ``` | Иссушение |
| ``` potion`health_boost` ``` | Увеличение здоровья |
| ``` potion`absorption` ``` | Поглощение |
| ``` potion`saturation` ``` | Насыщение |
| ``` potion`glowing` ``` | Свечение |
| ``` potion`levitation` ``` | Левитация |
| ``` potion`luck` ``` | Удача |
| ``` potion`bad_luck` ``` | Неудачник! |

# Документация 📜
Посмотрите информацию по другим элементам кода.

   - [Активаторы](documentation/activators.md) 
     -  [Событие игрока](documentation/activators.md#событие-игрока---playereventevent--none--)
     -  [Событие мира](documentation/activators.md#событие-мира---worldeventevent--none--)
     -  [Циклы](documentation/activators.md#циклы---loopname-0--none--)
     -  [Функции](documentation/activators.md#функции---functionname--none--)
   - [Действия](documentation/actions.md)
     - [Действие игрока](documentation/actions.md#действие-игрока---playeractionargs-)
     - [Игровое действие](documentation/actions.md#игровое-действие---gameactionargs-)
     - [Установить переменную](documentation/actions.md#установить-переменную---varactionargs-)
     - [Работа с массивами](documentation/actions.md#работа-с-массивами---arrayactionargs-)
     - [Выбрать объект](documentation/actions.md#выбрать-объект---selectaction-)
   - [Условия](documentation/conditions.md)
     - [Если игрок](documentation/conditions.md#если-игрок---ifplayerconditionargs--none--)
     - [Если значение](documentation/conditions.md#если-значение---ifvalueconditionargs--none--)
     - [Если существо](documentation/conditions.md#если-существо---ifentityconditionargs--none--)
     - [Если игра](documentation/conditions.md#если-игра---ifgameconditionargs--none--)
     - [Иначе](documentation/conditions.md#иначе---else--none--)
   - [Прочее](documentation/other.md)
     - [Константы](documentation/other.md#константы-)
     - [Ошибки](documentation/other.md#ошибки-)
     - [Комментарии](documentation/other.md#комментарии-)
     - [Языковой модуль](documentation/other.md#языковой-модуль-)
