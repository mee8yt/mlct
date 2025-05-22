## Значения
К значениям относятся все метки для установки параметров блоков кода. Это все предметы из вкладки "Переменные" в /dev

   - [Значения](values.md)
     - [Игровое значение](#игровое-значение---vvalue-)
     - [Местоположение](#местоположение---lx-y-z-y-p-)
     - [Предмет](#предмет---imaterial-c-m-)
     - [Частица](#частица---particlevariant-)
     - [Зелье](#зелье---vid-d-f-)

### Игровое значение - **``` g`value` ```** [🔝](#значения)
Вид значения, который возвращает какой-либо параметр сущности, мира или события. В кодинге представлен в виде "яблока".

Заполнение:
```js
  var `temp` = g`message`;
//               ^^^^^^^
//                Ключ
```
| **Код** | **Название** |
| --- | --- |
| **Значение сущности** |
| ``` g`health` ``` | Текущее здоровье |
| ``` g`maxHealth` ``` | Максимальное здоровье |
| ``` g`food` ``` | Текущий уровень голода |
| ``` g`saturation` ``` | Текущий уровень сытости |
| ``` g`exhaustion` ``` | Текущий уровень истощения |
| ``` g`xpLevel` ``` | Текущий уровень опыта |
| ``` g`xp` ``` | Текущее значение опыта (%) |
| ``` g`armor` ``` | Текущий уровень защиты |
| ``` g`fire` ``` | Текущее состояние горения |
| ``` g`air` ``` | Текущий уровень воздуха |
| ``` g`maxAir` ``` | Текущий максимум воздуха |
| ``` g`heldSlot` ``` | Текущий слот |
| ``` g`ping` ``` | Пинг игрока |
| ``` g`name` ``` | Имя игрока |
| ``` g`entityType` ``` | Тип сущности |
| ``` g`inventoryType` ``` | Тип открытого инвентаря |
| ``` g`inventoryTitle` ``` | Название открытого инвентаря |
| ``` g`inventorySlots` ``` | Количество слотов инвентаря |
| ``` g`langClient` ``` | Язык клиента |
| ``` g`langServer` ``` | Язык на сервере |
| ``` g`version` ``` | Версия игрока |
| **Значение события** |
| ``` g`damage` ``` | Значение урона |
| ``` g`clickedSlot` ``` | Кликнутый слот |
| ``` g`newSlot` ``` | Новый слот |
| ``` g`oldSlot` ``` | Старый слот |
| ``` g`message` ``` | Сообщение игрока |
| ``` g`eventBlockLocation` ``` | Локация блока из события |
| ``` g`clickedItem` ``` | Кликнутый предмет |
| ``` g`eventBlock` ``` | Блок из события |
| ``` g`fishingState` ``` | Состояние рыбалки |
| ``` g`fishingCaught` ``` | Предмет с рыбалки  |
| ``` g`damageReason` ``` | Причина урона |
| ``` g`deathReason` ``` | Причина смерти |
| ``` g`eventItem` ``` | Предмет события |
| ``` g`interaction` ``` | Тип взаимодействия |
| ``` g`clickType` ``` | Тип клика |
| ``` g`cursorItem` ``` | Предмет в курсоре |
| ``` g`inventoryInteraction` ``` | Действие в инвентаре |
| ``` g`eventSlotType` ``` | Тип слота |
| ``` g`regainHealth` ``` | Количество здоровья |
| ``` g`regainHealthReason` ``` | Причина восстановления здоровья |
| ``` g`expCount` ``` | Количество опыта из события |
| ``` g`purchasedPoints` ``` | Приобретённое количество баллов игры |
| ``` g`goldTransactionCount` ``` | Количество золота из транзакции |
| ``` g`goldTransactionName` ``` | Название транзакции золота |
| ``` g`goldTransactionDisplayName` ``` | Отображаемое название транзакции золота |
| ``` g`shopTransactionKey` ``` | Ключ товара Mineland Studio |
| ``` g`shopTransactionDisplayName` ``` | Отображаемое название товара Mineland Studio |
| **Местоположения** |
| ``` g`location` ``` | Текущее местоположение |
| ``` g`eyeLocation` ``` | Текущее направление взгляда |
| ``` g`facing` ``` | Кардинальное направление |
| ``` g`targetBlockLocation` ``` | Местоположение целевого блока |
| **Предметы** |
| ``` g`mainHandItem` ``` | Предмет из главной руки |
| ``` g`offhandItem` ``` | Предмет из второй руки |
| ``` g`helmet` ``` | Шлем сущности |
| ``` g`chestplate` ``` | Нагрудник сущности |
| ``` g`leggings` ``` | Поножи сущности |
| ``` g`boots` ``` | Ботинки сущности |
| **Значение игры** |
| ``` g`players` ``` | Подсчет количества игроков |
| ``` g`votes` ``` | Количество лайков за игру |
| ``` g`visitors` ``` | Количество уникальных посетителей |
| ``` g`variables` ``` | Количество динамических переменных |
| ``` g`points` ``` | Количество баллов у игры |
| ``` g`blocksLimit` ``` | Оставшееся количество блоков для редактирования |
| ``` g`codeLimit` ``` | Счётчик выполненных действий |
| ``` g`plotId` ``` | Айди игры |

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

### Зелье - **``` g`id d f` ```** [🔝](#значения)
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

   - [Активаторы](activators.md) 
     -  [Событие игрока](activators.md#событие-игрока---playereventevent--none--)
     -  [Событие мира](activators.md#событие-мира---worldeventevent--none--)
     -  [Циклы](activators.md#циклы---loopname-0--none--)
     -  [Функции](activators.md#функции---functionname--none--)
   - [Действия](actions.md)
     - [Действие игрока](actions.md#действие-игрока---playeractionargs-)
     - [Игровое действие](actions.md#игровое-действие---gameactionargs-)
     - [Установить переменную](actions.md#установить-переменную---varactionargs-)
     - [Работа с массивами](actions.md#работа-с-массивами---arrayactionargs-)
     - [Выбрать объект](actions.md#выбрать-объект---selectaction-)
   - [Условия](conditions.md)
     - [Если игрок](conditions.md#если-игрок---ifplayerconditionargs--none--)
     - [Если значение](conditions.md#если-значение---ifvalueconditionargs--none--)
     - [Если существо](conditions.md#если-существо---ifentityconditionargs--none--)
     - [Если игра](conditions.md#если-игра---ifgameconditionargs--none--)
     - [Иначе](conditions.md#иначе---else--none--)
   - [Прочее](other.md)
     - [Константы](other.md#константы-)
     - [Ошибки](other.md#ошибки-)
     - [Комментарии](other.md#комментарии-)
     - [Языковой модуль](other.md#языковой-модуль-)
