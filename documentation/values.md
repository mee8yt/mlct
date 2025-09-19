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
| **Вид** | **Название** | **Значение** |
| --- | --- | --- |
| **Значение сущности** |
| `health` | Текущее здоровье | Число |
| `maxHealth` | Максимальное здоровье | Число |
| ``` food ``` | Текущий уровень голода | Число |
| ``` saturation ``` | Текущий уровень сытости | Число |
| ``` exhaustion ``` | Текущий уровень истощения | Число |
| ``` xpLevel ``` | Текущий уровень опыта | Число |
| ``` xp ``` | Текущее значение опыта (%) | Число<br/>От 0% до 100% |
| ``` armor ``` | Текущий уровень защиты | Число<br/>От 0 |
| ``` fire ``` | Текущее состояние горения | Число<br/>Если больше 0, то сущность горит |
| ``` air ``` | Текущий уровень воздуха | Число<br/>Если 0, то сущность задыхается |
| ``` maxAir ``` | Текущий максимум воздуха | Число<br/>По умолчанию 300 |
| ``` heldSlot ``` | Текущий слот | Число<br/>От 0 до 8 |
| ``` ping ``` | Пинг игрока | Число<br/>В миллисекундах |
| ``` name ``` | Имя игрока | Текст |
| ``` entityType ``` | Тип сущности | Текст<br/>Тип сущности: "PLAYER", "ZOMBIE", "PIG", "DROPPED_ITEM" и т.д. |
| ``` inventoryTitle ``` | Название открытого инвентаря | Текст |
| ``` inventoryType ``` | Тип открытого инвентаря | Текст<br/>Тип инвентаря: "CRAFTING", "CHEST", "WORKBENCH", "ENCHANTING", "ENDER_CHEST", "SHULKER_BOX", "HOPPER", "DROPPER", "DISPENSER", "BEACON", "" |
| ``` inventorySlots ``` | Количество слотов инвентаря | Число |
| ``` langClient ``` | Язык клиента | Текст<br/>Язык: "ru_RU", "en_US" и т.д. |
| ``` langServer ``` | Язык на сервере | Текст<br/>Язык: "RU", "EN", "UK", "DE" |
| ``` version ``` | Версия игрока | Текст<br/>Версия: MINECRAFT_1_?_? |
| **Значение события** |
| ``` eventDamage ``` | Значение урона | Число |
| ``` eventClickedSlot ``` | Кликнутый слот | Число<br/>От 0. Если -999, то предмет выброшен |
| ``` eventNewSlot ``` | Новый слот | Число<br/>От 0 до 8 |
| ``` eventOldSlot ``` | Старый слот | Число<br/>От 0 до 8 |
| ``` message ``` | Сообщение игрока | Текст |
| ``` eventBlockLocation ``` | Локация блока из события | Местоположение |
| ``` eventClickedItem ``` | Кликнутый предмет | Предмет |
| ``` eventBlock ``` | Блок из события | Предмет |
| ``` eventFishingState ``` | Состояние рыбалки | Текст<br/>Состояние рыбалки: "FISHING", "FAILED_ATTEMPT", "BITE", "CAUGHT_FISH", "CAUGHT_ENTITY", "ON_GROUND" |
| ``` eventFishingCaught ``` | Предмет с рыбалки  | Предмет<br/>Если не воздух, то игрок что-то поймал из воды |
| ``` eventDamageReason ``` | Причина урона | Текст<br/>"block_explosion", "contact", "cramming", "custom", "dragon_breath", "drowning", "entity_attack", "entity_explosion", "entity_sweep_attack", "fall", "falling_block", "fire", "fire_tick", "fly_into_wall", "hot_floor", "lava", "lightning", "magic", "melting", "poison", "projectile", "starvation", "suffocation", "suicide", "thorns", "void", "wither" |
| ``` eventDeathReason ``` | Причина смерти | Текст<br/>block_explosion", "contact", "cramming", "custom" и т.д. | 
| ``` eventItem ``` | Предмет события | Предмет |
| ``` eventInteraction ``` | Тип взаимодействия | Текст<br/>Тип взаимодействия с миром: "LEFT_CLICK_AIR", "LEFT_CLICK_BLOCK", "RIGHT_CLICK_AIR", "RIGHT_CLICK_BLOCK" |
| ``` eventClickType ``` | Тип клика | Текст<br/>Тип клика: "LEFT", "RIGHT", "MIDDLE", "SHIFT_LEFT", "SHIFT_RIGHT", "CREATIVE" |
| ``` eventCursorItem ``` | Предмет в курсоре | Предмет |
| ``` eventInventoryInteraction ``` | Действие в инвентаре | Текст<br/>Тип взаимодействия в инвентаре: "PICKUP_ALL", "PICKUP_HALF", "PLACE_ALL", "PLACE_ONE", "NOTHING", "MOVE_TO_OTHER_INVENTORY" |
| ``` eventSlotType ``` | Тип слота | Текст<br/>Тип слота в инвентаре: "CONTAINER", "QUICKBAR", "ARMOR", "CRAFTING", "RESULT", "FUEL" |
| ``` eventRegainHealth ``` | Количество здоровья | Число<br/>Здоровье, которое было восстановлено |
| ``` eventRegainHealthReason ``` | Причина восстановления здоровья | Текст<br/>Причина восстановления: "SATIATED", "MAGIC" |
| ``` evenTexpCount ``` | Количество опыта из события | Число |
| ``` eventPurchasedPoints ``` | Приобретённое количество баллов игры | Число |
| ``` eventGoldTransactionCount ``` | Количество золота из транзакции | Число |
| ``` eventGoldTransactionName ``` | Название транзакции золота | Текст |
| ``` eventGoldTransactionDisplayName ``` | Отображаемое название транзакции золота | Текст |
| ``` eventShopTransactionKey ``` | Ключ товара Mineland Studio | Текст |
| ``` eventShopTransactionDisplayName ``` | Отображаемое название товара Mineland Studio | Текст |
| **Местоположения** |
| ``` location ``` | Текущее местоположение | Местоположение |
| ``` eyeLocation ``` | Текущее местоположение глаз | Местоположение |
| ``` eyeVector ``` | Текущий вектор взгляда | Вектор |
| ``` facing ``` | Кардинальное направление | Текст<br/>Кардинальное направление: "South", "West", "East", "North" |
| ``` targetBlockLocation ``` | Местоположение целевого блока | Местоположение |
| **Предметы** |
| ``` mainHandItem ``` | Предмет из главной руки | Предмет |
| ``` offhandItem ``` | Предмет из второй руки | Предмет |
| ``` helmet ``` | Шлем сущности | Предмет |
| ``` chestplate ``` | Нагрудник сущности | Предмет |
| ``` leggings ``` | Поножи сущности | Предмет |
| ``` boots ``` | Ботинки сущности | Предмет |
| **Значение игры** |
| ``` players ``` | Подсчет количества игроков | Число<br/>От 1 |
| ``` votes ``` | Количество лайков за игру | Число |
| ``` visitors ``` | Количество уникальных посетителей | Число<br/>От 1 |
| ``` variables ``` | Количество динамических переменных | Число |
| ``` points ``` | Количество баллов у игры | Число |
| ``` blocksLimit ``` | Оставшееся количество блоков для редактирования | Число<br/>В состоянии покоя - 5000 |
| ``` codeLimit ``` | Счётчик выполненных действий | Число |
| ``` plotId ``` | Айди игры | Число |
### Частица - **``` particle(particle: str) ```** [🔝](#значения)
Вид значения, который представляет собой один из вариантов визуальных частиц для игрока. В кодинге представлен в виде незерской звезды
| **Код** | **Название** |
| --- | --- |
| ``` EXPLOSION_LARGE ``` | Большой взрыв |
| ``` EXPLOSION_HUGE ``` | Взрыв |
| ``` FIREWORKS_SPARK ``` | След от фейерверка |
| ``` WATER_BUBBLE ``` | Пузырьки воды |
| ``` WATER_SPLASH ``` | Брызги воды |
| ``` WATER_WAKE ``` | Следы от воды |
| ``` SUSPENDED ``` | Туман |
| ``` SUSPENDED_DEPTH ``` | Туман из глубин |
| ``` CRIT ``` | Критический удар |
| ``` CRIT_MAGIC ``` | Магический удар |
| ``` SMOKE_NORMAL ``` | Дым |
| ``` SMOKE_LARGE ``` | Большой дым |
| ``` SPELL ``` | Белый аромат |
| ``` SPELL_INSTANT ``` | Блёстки |
| ``` SPELL_MOB ``` | Тёмные силы |
| ``` SPELL_MOB_AMBIENT ``` | Серое воздуховление |
| ``` SPELL_WITCH ``` | Частицы ведьмы |
| ``` DRIP_WATER ``` | Капающая вода |
| ``` DRIP_LAVA ``` | Капающая лава |
| ``` VILLAGER_ANGRY ``` | Гнев жителя |
| ``` VILLAGER_HAPPY ``` | Счастье жителя |
| ``` TOWN_AURA ``` | Туманный бедрок |
| ``` NOTE ``` | Нота |
| ``` PORTAL ``` | Портал |
| ``` ENCHANTMENT_TABLE ``` | Символы стола зачарований |
| ``` FLAME ``` | Огонёк |
| ``` LAVA ``` | Капли лавы |
| ``` FOOTSTEP ``` | Следы |
| ``` CLOUD ``` | Облачко |
| ``` REDSTONE ``` | Редстоун |
| ``` SNOWBALL ``` | Куски снежка |
| ``` SNOW_SHOVEL ``` | Падающий снег |
| ``` SLIME ``` | Куски слизи |
| ``` HEART ``` | Сердце |
| ``` BARRIER ``` | Барьер |
| ``` WATER_DROP ``` | Капли воды |
| ``` ITEM_TAKE ``` | Пустующий предмет |
| ``` MOB_APPEARANCE ``` | Появление древнего стража |
| ``` DRAGON_BREATH ``` | Драконье дыхание |
| ``` END_ROD ``` | Стержень энда |
| ``` DAMAGE_INDICATOR ``` | Тёмные сердечки |
| ``` SWEEP_ATTACK ``` | Удар по площади |
| ``` TOTEM ``` | Таинственный тотем |
| ``` SPIT ``` | Плевок от ламы |

### Зелье - **``` potion(potion: str, duration: int, level: int) ```** [🔝](#значения)
Вид значения, который представляет собой эффект зелья игрока. В кодинге представлен в виде пузырька с зельем
| **Код** | **Название** |
| --- | --- |
| ``` speed ``` | Скорость |
| ``` slowness ``` | Медлительность |
| ``` haste ``` | Спешка |
| ``` fatigue ``` | Утомление |
| ``` strength ``` | Сила |
| ``` healing ``` | Лечение |
| ``` harming ``` | Моментальный урон |
| ``` leaping ``` | Прыжок |
| ``` nausea ``` | Тошнота |
| ``` regeneration ``` | Регенерация |
| ``` resistance ``` | Сопротивление к урону |
| ``` fire_resistance ``` | Огнестойкость |
| ``` water_breathing ``` | Подводное дыхание |
| ``` invisible ``` | Невидимость |
| ``` blindness ``` | Слепота |
| ``` night_vision ``` | Ночное видение |
| ``` hunger ``` | Голод |
| ``` weakness ``` | Слабость |
| ``` poison ``` | Отравление |
| ``` wither ``` | Иссушение |
| ``` health_boost ``` | Увеличение здоровья |
| ``` absorption ``` | Поглощение |
| ``` saturation ``` | Насыщение |
| ``` glowing ``` | Свечение |
| ``` levitation ``` | Левитация |
| ``` luck ``` | Удача |
| ``` bad_luck ``` | Неудачник! |

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
