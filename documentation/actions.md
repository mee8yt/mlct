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
| `player.giveItems();` | Выдать предметы |
| `player.setItems();` | Установить предметы |
| `player.setItemsEnder();` | Установить предметы в эндер сундуке |
| `player.setArmor();` | Установить броню |
| `player.setItemHand();` | Установить предмет в руку |
| `player.setItemCursor();` | Установить предмет в курсор |
| `player.removeItem();` | Удалить предметы |
| `player.clearInventory();` | Очистить инвентарь |
| `player.clearEnder();` | Очистить эндер сундук |
| `player.setHotbar();` | Установить слот в хотбаре |
| `player.giveRandomItem();` | Выдать рандомный предмет |
| `player.saveInventory();` | Сохранить инвентарь |
| `player.loadInventory();` | Загрузить инвентарь |
| `player.setDelay();` | Установить задержку предмета |
| `player.getItem();` | Получить предмет из слота |
| `player.setItem();` | Установить предмет в слот |
| `player.getItemCooldown();` | Получить задержку предмета |
| `player.send();` | Отправить сообщение |
| `player.sendComponent();` | Отправить сообщение (компоненты) |
| `player.sendDialogue();` | Отправить диалог |
| `player.clearChat();` | Очистить чат |
| `player.playSound();` | Проиграть звук |
| `player.stopSound();` | Остановить звук |
| `player.title();` | Отобразить титл |
| `player.actionbar();` | Сообщение в экшн баре |
| `player.showLink();` | Показать книгу с ссылкой |
| `player.openBook();` | Показать книгу |
| `player.openMenu();` | Открыть инвентарное меню |
| `player.expandMenu();` | Расширить инвентарное меню |
| `player.setItemInMenu();` | Установить предмет в меню |
| `player.setMenuName();` | Установить название меню |
| `player.addLineInMenu();` | Добавить строку меню |
| `player.deleteLineMenu();` | Удалить строку меню |
| `player.closeInventory();` | Закрыть инвентарь |
| `player.openBlock();` | Открыть инвентарь блока из игры |
| `player.openEntity();` | Открыть инвентарь сущности из игры |
| `player.teleport();` | Телепортация |
| `player.rotateToLocation();` | Повернуть к местоположению |
| `player.randomTeleport();` | Случайная телепортация |
| `player.teleportSequence();` | Очередь телепортаций |
| `player.launchVertically();` | Запустить вверх/вниз |
| `player.launchForward();` | Запустить вперёд/назад |
| `player.launchToward();` | Запустить в сторону |
| `player.launchToLocation();` | Запустить к местоположению |
| `player.kick();` | Кикнуть игрока |
| `player.moveToGame();` | Переместить в другую игру |
| `player.damage();` | Урон |
| `player.setHealth();` | Установка здоровью |
| `player.givePotionEffect();` | Выдать эффект зелья |
| `player.clearPotionEffect();` | Очистить все эффекты зелий |
| `player.removePotionEffect();` | Удалить эффект зелья |
| `player.setXpLvl();` | Установить уровень опыта |
| `player.setXpProgress();` | Поставить шкалу опыта |
| `player.setHunger();` | Установить уровень голода |
| `player.setSaturation();` | Установить уровень сытости |
| `player.setExhaustion();` | Установить истощение |
| `player.setMaxHealth();` | Установить максимальное здоровье |
| `player.setOnFire();` | Горение |
| `player.setFlightSpeed();` | Установить скорость полёта |
| `player.setWalkSpeed();` | Установить скорость ходьбы |
| `player.setRemainingAir();` | Установить остаток воздуха |
| `player.setMaximumAir();` | Установить максимум воздуха |
| `player.setName();` | Установить имя |
| `player.setDamage();` | Установить урон |
| `player.setSize();` | Установить размер |
| `player.setSound();` | Установить звуки |
| `player.setGlow();` | Установить свечение |
| `player.setVisibility();` | Видимость игрока |
| `player.setGravity();` | Установить гравитацию |
| `player.setInvincibility();` | Установить неуязвимость |
| `player.deleteEntity();` | Удалить сущность |
| `player.setFlight();` | Установить полёт игрока |
| `player.setGamemode();` | Установить режим игрока |
| `player.setKeepInventory();` | Сохранение инвентаря при смерти |
| `player.showScoreboard();` | Показать панель скорборда |
| `player.hideScoreboard();` | Скрыть панель скорборда |
| `player.showBossbar();` | Показать боссбар |
| `player.hideBossbar();` | Скрыть боссбар |
| `player.layOnBed();` | Отображение лежания |
| `player.wakeUp();` | Игрок встаёт с кровати |
| `player.handAnimation();` | Анимация руки |
| `player.sneakingState();` | Сделать игрока приседающим |
| `player.damageAnimation();` | Анимация урона |
| `player.goldTransaction();` | Запросить транзакцию золота |

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
| `var.remainder();` | Установить проценты |
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

Документация tut
