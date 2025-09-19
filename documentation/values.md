## Значения
К значениям относятся все метки для установки параметров блоков кода. Это все предметы из вкладки "Переменные" в /dev

   - [Значения](values.md)
     - [Фабрики](#фабрики-)
     - [Игровое значение](#игровое-значение---vvalue-)
     - [Частица](#частица---particlevariant-)
     - [Зелье](#зелье---vid-d-f-)

### Фабрики
Это составные значения, принимающие аргументы\
Аргумент со знаком `*` является обязательным
| **Вид** | **Название** | **Аргументы** |
| --- | --- | --- |
| `item()` | Предмет | `id`: текст, `name`: текст, `lore`: список[текст], `count`: число, `damage`: число |
| `location()` | Местоположение | `x`: число*, `y`: число*, `z`: число*, `yaw`: число, `pitch`: число |
| `vector()` | Вектор | `x`: число*, `y`: число*, `z`: число* |
| `value()` | Игровое значение | `value`: значение* |
| `potion()` | Зелье | `potion`: зелье*, `duratiion`: число, `level`: число |
| `particle()` | Частица | `particle`: частица |

### Игровое значение - **``` value(value: str)` ```** [🔝](#значения)
Это параметр сущности или игрока, значение события или игры. На сервере представлено в виде яблока
| **Вид** | **Название** |
| --- | --- |
| **Значение сущности** |
| `health` | Текущее здоровье |
| `maxHealth` | Максимальное здоровье |
| ``` food ``` | Текущий уровень голода |
| ``` saturation ``` | Текущий уровень сытости |
| ``` exhaustion ``` | Текущий уровень истощения |
| ``` xpLevel ``` | Текущий уровень опыта |
| ``` xp ``` | Текущее значение опыта (%) |
| ``` armor ``` | Текущий уровень защиты |
| ``` fire ``` | Текущее состояние горения |
| ``` air ``` | Текущий уровень воздуха |
| ``` maxAir ``` | Текущий максимум воздуха |
| ``` heldSlot ``` | Текущий слот |
| ``` ping ``` | Пинг игрока |
| ``` name ``` | Имя игрока |
| ``` entityType ``` | Тип сущности |
| ``` inventoryType ``` | Тип открытого инвентаря |
| ``` inventoryTitle ``` | Название открытого инвентаря |
| ``` inventorySlots ``` | Количество слотов инвентаря |
| ``` langClient ``` | Язык клиента |
| ``` langServer ``` | Язык на сервере |
| ``` version ``` | Версия игрока |
| **Значение события** |
| ``` eventDamage ``` | Значение урона |
| ``` eventClickedSlot ``` | Кликнутый слот |
| ``` eventNewSlot ``` | Новый слот |
| ``` eventOldSlot ``` | Старый слот |
| ``` message ``` | Сообщение игрока |
| ``` eventBlockLocation ``` | Локация блока из события |
| ``` eventClickedItem ``` | Кликнутый предмет |
| ``` eventBlock ``` | Блок из события |
| ``` eventFishingState ``` | Состояние рыбалки |
| ``` eventFishingCaught ``` | Предмет с рыбалки  |
| ``` eventDamageReason ``` | Причина урона |
| ``` eventDeathReason ``` | Причина смерти |
| ``` eventItem ``` | Предмет события |
| ``` eventInteraction ``` | Тип взаимодействия |
| ``` eventClickType ``` | Тип клика |
| ``` eventCursorItem ``` | Предмет в курсоре |
| ``` eventInventoryInteraction ``` | Действие в инвентаре |
| ``` eventSlotType ``` | Тип слота |
| ``` eventRegainHealth ``` | Количество здоровья |
| ``` eventRegainHealthReason ``` | Причина восстановления здоровья |
| ``` evenTexpCount ``` | Количество опыта из события |
| ``` eventPurchasedPoints ``` | Приобретённое количество баллов игры |
| ``` eventGoldTransactionCount ``` | Количество золота из транзакции |
| ``` eventGoldTransactionName ``` | Название транзакции золота |
| ``` eventGoldTransactionDisplayName ``` | Отображаемое название транзакции золота |
| ``` eventShopTransactionKey ``` | Ключ товара Mineland Studio |
| ``` eventShopTransactionDisplayName ``` | Отображаемое название товара Mineland Studio |
| **Местоположения** |
| ``` location ``` | Текущее местоположение |
| ``` eyeLocation ``` | Текущее направление взгляда |
| ``` facing ``` | Кардинальное направление |
| ``` targetBlockLocation ``` | Местоположение целевого блока |
| **Предметы** |
| ``` mainHandItem ``` | Предмет из главной руки |
| ``` offhandItem ``` | Предмет из второй руки |
| ``` helmet ``` | Шлем сущности |
| ``` chestplate ``` | Нагрудник сущности |
| ``` leggings ``` | Поножи сущности |
| ``` boots ``` | Ботинки сущности |
| **Значение игры** |
| ``` players ``` | Подсчет количества игроков |
| ``` votes ``` | Количество лайков за игру |
| ``` visitors ``` | Количество уникальных посетителей |
| ``` variables ``` | Количество динамических переменных |
| ``` points ``` | Количество баллов у игры |
| ``` blocksLimit ``` | Оставшееся количество блоков для редактирования |
| ``` codeLimit ``` | Счётчик выполненных действий |
| ``` plotId ``` | Айди игры |

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

### Вектор - **``` v`x y z` ```** [🔝](#значения)
Вид значения, который представляет собой направленный отрезок. В кодинге представлен в виде "призмарина".

Заполнение:
```js
  var `temp` = v`x y z`;
//               ^^^^^
//              Координаты

  var `temp` = v`0 0 0`;
  player.send(temp); -> "(0, 0, 0)"
```

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
