## Действия
К действиям относятся все блоки, которые позволяют изменять игровой мир,  значения переменных, параметры игроков, а также выбирать этих игроков.

   - [Действия](actions.md)
     - [Действие игрока](#действие-игрока---playeractionargs-)
     - [Игровое действие](#игровое-действие---gameactionargs-)
     - [Установить переменную](#установить-переменную---varactionargs-)
     - [Работа с массивами](#работа-с-массивами---arrayactionargs-)
     - [Выбрать объект](#выбрать-объект---selectaction-)

### Действие игрока - **`player.action(args);`** [🔝](#действия)
| **Код** | **Название** |
| --- | --- |
| [`player.giveItems();`](code.md) | Выдать предметы |
| [`player.setItems();`](code.md) | Установить предметы |
| [`player.setItemsEnder();`](code.md) | Установить предметы в эндер сундуке |
| [`player.setArmor();`](code.md) | Установить броню |
| [`player.setItemHand();`](code.md) | Установить предмет в руку |
| [`player.setItemCursor();`](code.md) | Установить предмет в курсор |
| [`player.removeItems();`](code.md) | Удалить предметы |
| [`player.clearInventory();`](code.md) | Очистить инвентарь |
| [`player.clearEnder();`](code.md) | Очистить эндер сундук |
| [`player.setHotbar();`](code.md) | Установить слот в хотбаре |
| [`player.giveRandomItem();`](code.md) | Выдать рандомный предмет |
| [`player.saveInventory();`](code.md) | Сохранить инвентарь |
| [`player.loadInventory();`](code.md) | Загрузить инвентарь |
| [`player.setDelay();`](code.md) | Установить задержку предмета |
| [`player.getItem();`](code.md) | Получить предмет из слота |
| [`player.setItem();`](code.md) | Установить предмет в слот |
| [`player.getItemCooldown();`](code.md) | Получить задержку предмета |
| [`player.send();`](code.md#---playersend-) | Отправить сообщение |
| [`player.sendComponent();`](code.md) | Отправить сообщение (компоненты) |
| [`player.sendDialogue();`](code.md) | Отправить диалог |
| [`player.clearChat();`](code.md) | Очистить чат |
| [`player.playSound();`](code.md) | Проиграть звук |
| [`player.stopSound();`](code.md) | Остановить звук |
| [`player.title();`](code.md) | Отобразить титл |
| [`player.actionbar();`](code.md) | Сообщение в экшн баре |
| [`player.showLink();`](code.md) | Показать книгу с ссылкой |
| [`player.openBook();`](code.md) | Показать книгу |
| [`player.openMenu();`](code.md) | Открыть инвентарное меню |
| [`player.expandMenu();`](code.md) | Расширить инвентарное меню |
| [`player.setItemInMenu();`](code.md) | Установить предмет в меню |
| [`player.setMenuName();`](code.md) | Установить название меню |
| [`player.addLineInMenu();`](code.md) | Добавить строку меню |
| [`player.deleteLineMenu();`](code.md) | Удалить строку меню |
| [`player.closeInventory();`](code.md) | Закрыть инвентарь |
| [`player.openBlock();`](code.md) | Открыть инвентарь блока из игры |
| [`player.openEntity();`](code.md) | Открыть инвентарь сущности из игры |
| [`player.teleport();`](code.md) | Телепортация |
| [`player.rotateToLocation();`](code.md) | Повернуть к местоположению |
| [`player.randomTeleport();`](code.md) | Случайная телепортация |
| [`player.teleportSequence();`](code.md) | Очередь телепортаций |
| [`player.launchVertically();`](code.md) | Запустить вверх/вниз |
| [`player.launchForward();`](code.md) | Запустить вперёд/назад |
| [`player.launchToward();`](code.md) | Запустить в сторону |
| [`player.launchToLocation();`](code.md) | Запустить к местоположению |
| [`player.kick();`](code.md) | Кикнуть игрока |
| [`player.moveToGame();`](code.md) | Переместить в другую игру |
| [`player.damage();`](code.md) | Урон |
| [`player.setHealth();`](code.md) | Установка здоровью |
| [`player.givePotionEffect();`](code.md) | Выдать эффект зелья |
| [`player.clearPotionEffect();`](code.md) | Очистить все эффекты зелий |
| [`player.removePotionEffect();`](code.md) | Удалить эффект зелья |
| [`player.setXpLvl();`](code.md) | Установить уровень опыта |
| [`player.setXpProgress();`](code.md) | Поставить шкалу опыта |
| [`player.setHunger();`](code.md) | Установить уровень голода |
| [`player.setSaturation();`](code.md) | Установить уровень сытости |
| [`player.setExhaustion();`](code.md) | Установить истощение |
| [`player.setMaxHealth();`](code.md) | Установить максимальное здоровье |
| [`player.setOnFire();`](code.md) | Горение |
| [`player.setFlightSpeed();`](code.md) | Установить скорость полёта |
| [`player.setWalkSpeed();`](code.md) | Установить скорость ходьбы |
| [`player.setRemainingAir();`](code.md) | Установить остаток воздуха |
| [`player.setMaximumAir();`](code.md) | Установить максимум воздуха |
| [`player.setName();`](code.md) | Установить имя |
| [`player.setDamage();`](code.md) | Установить урон |
| [`player.setSize();`](code.md) | Установить размер |
| [`player.setSound();`](code.md) | Установить звуки |
| [`player.setGlow();`](code.md) | Установить свечение |
| [`player.setVisibility();`](code.md) | Видимость игрока |
| [`player.setGravity();`](code.md) | Установить гравитацию |
| [`player.setInvincibility();`](code.md) | Установить неуязвимость |
| [`player.deleteEntity();`](code.md) | Удалить сущность |
| [`player.setFlight();`](code.md) | Установить полёт игрока |
| [`player.setGamemode();`](code.md) | Установить режим игрока |
| [`player.setKeepInventory();`](code.md) | Сохранение инвентаря при смерти |
| [`player.showScoreboard();`](code.md) | Показать панель скорборда |
| [`player.hideScoreboard();`](code.md) | Скрыть панель скорборда |
| [`player.showBossbar();`](code.md) | Показать боссбар |
| [`player.hideBossbar();`](code.md) | Скрыть боссбар |
| [`player.layOnBed();`](code.md) | Отображение лежания |
| [`player.wakeUp();`](code.md) | Игрок встаёт с кровати |
| [`player.handAnimation();`](code.md) | Анимация руки |
| [`player.sneakingState();`](code.md) | Сделать игрока приседающим |
| [`player.damageAnimation();`](code.md) | Анимация урона |
| [`player.goldTransaction();`](code.md) | Запросить транзакцию золота |

### Игровое действие - **`game.action(args);`** [🔝](#действия)
| **Код** | **Название** |
| --- | --- |
| `game.spawnEntity();` | Заспавнить моба/сущность |
| `game.spawnNpc();` | Заспавнить NPC |
| `game.spawnItem();` | Заспавнить предмет |
| `game.launchFirework();` | Запустить фейерверк |
| `game.spawnTnt();` | Заспавнить активированный TNT |
| `game.spawnVehicle();` | Заспавнить транспортное средство |
| `game.spawnXpOrb();` | Заспавнить сферу опыта |
| `game.spawnLightning();` | Заспавнить молнию |
| `game.wait();` | Ждать |
| `game.startLoop();` | Запустить цикл |
| `game.stopLoop();` | Остановить цикл |
| `game.cancelEvent();` | Отменить событие |
| `game.callFunction();` | Вызвать функцию |
| `game.setBlock();` | Поставить блок(и) |
| `game.fillRegion();` | Заполнить область блоками |
| `game.breakBlock();` | Сломать блок |
| `game.copyBlock();` | Копировать блоки |
| `game.fillContainer();` | Заполнить контейнер |
| `game.deleteItemFromContainer();` | Удалить предметы из контейнера |
| `game.setItemFromContainer();` | Установить предмет в контейнер |
| `game.clearContainer();` | Очистить контейнер |
| `game.changeSign);` | Изменить табличку |
| `game.changeContainerName();` | Изменить название блока |
| `game.getItemFromContainer();` | Получить предмет из контейнера |
| `game.setItemInEnderChest();` | Установить предметы в эндер сундук |
| `game.getItemFromEnderChest();` | Получить предмет из эндер сундука |
| `game.getItemsFromContainer();` | Получить предметы из контейнера |
| `game.getSignValue();` | Получить значение из таблички |
| `game.createExplosion();` | Создать взрыв |
| `game.playFireworkExplosion();` | Воспроизвести взрыв фейерверка |
| `game.playParticle();` | Воспроизвести частицу |
| `game.playParticleLine();` | Воспроизвести линию из частиц |
| `game.createHologram();` | Создать голограмму |
| `game.deleteHologram();` | Удалить голограмму |
| `game.createScoreboard();` | Создать скорборд |
| `game.deleteScoreboard();` | Удалить скорборд |
| `game.setScoreboardScore();` | Выставить очки скорборда |
| `game.removeScoreboardScore();` | Удалить очки в скорборде |
| `game.setWeather();` | Установить погоду |
| `game.setGameTime();` | Установить время в мире |
| `game.createBossbar();` | Создать боссбар |
| `game.deleteBossbar();` | Удалить боссбар |
| `game.setBossbarTitle();` | Установить титл боссбара |
| `game.setBossbarColor();` | Установить цвет боссбара |
| `game.setBossbarStyle();` | Установить стиль боссбара |
| `game.setBossbarProgress();` | Установить прогресс боссбара |
| `game.readDataFromChannel();` | Считать данные из канала |
| `game.sendDataThroughChannel();` | Отправить данные через канал |
| `game.sendArrayThroughChannel();` | Отправить массив через канал |

### Установить переменную - **`var.action(args);`** [🔝](#действия)
| **Код** | **Название** |
| --- | --- |
| `var.set();` | Установить значение |
| `var.setItemToVariable();` | Установить предмет в переменную|
| `var.setRandomValue();` | Установить случайное значение |
| `var.setTimestamp();` | Установить время в виде даты |
| `var.setUnix();` | Установить время в виде миллисекунд |
| `var.sum();` | Установить сумму |
| `var.difference();` | Установить разность |
| `var.multiply();` | Установить произведение |
| `var.division();` | Установить частное |
| `var.remainder();` | Установить остаток |
| `var.plus();` | Прибавить |
| `var.minus();` | Отнять |
| `var.setRandomNumber();` | Установить случайное число |
| `var.roundNumber();` | Округлить число |
| `var.module();` | Модуль |
| `var.minNumber();` | Минимальное число |
| `var.maxNumber();` | Максимальное число |
| `var.pow();` | Возведение в степень |
| `var.cosinus();` | Косинус |
| `var.sinus();` | Синус |
| `var.tangent();` | Тангенс |
| `var.arcSinus();` | Арксинус |
| `var.arcCosinus();` | Арккосинус |
| `var.arcTangent();` | Арктангенс |
| `var.deg();` | Градусы |
| `var.logarithm();` | Натуральный логарифм |
| `var.sqrt();` | Корень |
| `var.exp();` | Экспонента |
| `var.radians();` | Радианы |
| `var.perlin();` | Шум Перлина |
| `var.simplex();` | Шум Симплекс |
| `var.combine();` | Объединить тексты |
| `var.parseNumber();` | Парсить число |
| `var.truncate();` | Обрезка текста по указанным буквам |
| `var.splitText();` | Разделить текст на элементы |
| `var.getTextLength();` | Получить длину текста |
| `var.replaceText();` | Заменить символы в тексте |
| `var.setTextCase();` | Установить регистр тексту |
| `var.timeFormat();` | Создать формат времени |
| `var.getLocationValue();` | Получить значение из местоположения |
| `var.getLocationDistance();` | Получить расстояние между 2 местоположениями |
| `var.setLocation();` | Установить значения в местоположении |
| `var.getBlock();` | Получить блок из местоположения |
| `var.getItemValue();` | Получить значение из предмета |
| `var.getItemLore();` | Получить описание предмета |
| `var.setItemAmount();` | Установить количество предмета |
| `var.setItemDurability();` | Установить прочность предмета |
| `var.setItemLore();` | Установить описание предмета |
| `var.setItemName();` | Установить название предмета |
| `var.addItemLore();` | Добавить описание предмету |
| `var.deleteItemLore();` | Удалить строку описания предмета |
| `var.getPageBook();` | Получить текст из книги |
| `var.setPageBook();` | Установить текст в книгу |
| `var.setPopupText();` | Установить всплывающий текст |
| `var.setClickEventText();` | Установить событие при клике |
| `var.combineTextComponent();` | Объединить текстовые компоненты |

### Работа с массивами - **`array.action(args);`** [🔝](#действия)
| **Код** | **Название** |
| --- | --- |
| `array.create();` | Очистить/создать массив |
| `array.get();` | Получить элемент массива |
| `array.insert();` | Вставить в массив |
| `array.replace();` | Заменить элемент массива |
| `array.delete();` | Удалить элемент массива |
| `array.put();` | Добавить в конец массива |
| `array.combine();` | Присоединить массив |
| `array.copy();` | Скопировать массив |
| `array.getLength();` | Получить размер массива |
| `array.sort();` | Сортировать массив |
| `array.toString();` | Вывести массив в строку |

### Выбрать объект - **`select.action();`** [🔝](#действия)
Выборка делится на 2 вида: **обычная** и **условная**

Обычная выборка:
| **Код** | **Название** |
| --- | --- |
| `select.default();` | Выбрать игрока по умолчанию |
| `select.defaultEntity()` | Выбрать сущность по умолчанию |
| `select.randomPlayer()` | Выбрать случайного игрока |
| `select.randomMob()` | Выбрать случайного моба |
| `select.randomEntity()` | Выбрать случайную сущность |
| `select.all()` | Выбрать всех игроков |
| `select.allMobs()` | Выбрать всех мобов |
| `select.allEntity()` | Выбрать всех сущностей |
| `select.lastMob()` | Выбрать последнего заспавненого моба |
| `select.randomFilter()` | Выбор фильтра случайным образом |

Условная выборка:
| **Код** | **Название** |
| --- | --- |
| `select.player.ifPlayer.nameEquals();` | Выбрать игрока, если ник игрока равен |
| `select.player.ifValue.equals();` | Выбрать игрока, если значение переменной равно |
| `select.mob.ifEntity.typeEquals();` | Выбрать моба, если тип моба равен |
| `select.entity.ifEntity.isNpc();` | Выбрать сущность, если сущность является НПС |

**Так работает со всеми условиями**

Подробно:
```js
   select.player.ifPlayer.nameEquals();
// ^^^^^^
// Блок действия

   select.player.ifPlayer.nameEquals();
//        ^^^^^^
//        Тип объекта (player,mob,entity)

   select.player.ifPlayer.nameEquals();
//               ^^^^^^^^
//               Тип условия

   select.player.ifPlayer.nameEquals();
//                        ^^^^^^^^^^^^
//                        Само условие для выборки
```

Доступные блоки условий для объектов:
|  **Объект** | **Блоки условий** |
| --- | ---|
| `player` | `ifPlayer`, `ifVar` |
| `mob` | `ifEntity`, `ifVar` |
| `entity` | `ifEntity`, `ifVar` |

# Документация 📜
Посмотрите информацию по другим элементам кода.

   - [Активаторы](activators.md) 
     -  [Событие игрока](activators.md#событие-игрока---playereventevent--none--)
     -  [Событие мира](activators.md#событие-мира---worldeventevent--none--)
     -  [Циклы](activators.md#циклы---loopname-0--none--)
     -  [Функции](activators.md#функции---functionname--none--)
   - [Условия](conditions.md)
     - [Если игрок](conditions.md#если-игрок---ifplayerconditionargs--none--)
     - [Если значение](conditions.md#если-значение---ifvalueconditionargs--none--)
     - [Если существо](conditions.md#если-существо---ifentityconditionargs--none--)
     - [Если игра](conditions.md#если-игра---ifgameconditionargs--none--)
     - [Иначе](conditions.md#иначе---else--none--)
   - [Значения](values.md)
     - [Игровое значение](values.md#игровое-значение---vvalue-)
     - [Местоположение](values.md#местоположение---lx-y-z-y-p-)
     - [Предмет](values.md#предмет---imaterial-c-m-)
     - [Частица](values.md#частица---particlevariant-)
     - [Зелье](values.md#зелье---vid-d-f-)
   - [Прочее](other.md)
     - [Константы](other.md#константы-)
     - [Ошибки](other.md#ошибки-)
     - [Комментарии](other.md#комментарии-)
     - [Языковой модуль](other.md#языковой-модуль-)
