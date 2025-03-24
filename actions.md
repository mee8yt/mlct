## Действия
К действиям относятся все блоки, которые позволяют изменять игровой мир,  значения переменных, параметры игроков, а также выбирать этих игроков.



### Действие игрока - **`player.action(args)`**
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
