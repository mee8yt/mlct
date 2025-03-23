# MLCT ✨
**MLCT** *(**M**ine**L**and **C**ode **T**ranslator)* - Мод, для установки письменного варианта блочного кода на сервере Mineland.

## Содержание 🗂️

1. [Установка]()
2. [Синтаксис]()
3. [Документация](#документация-)
   - [Активаторы](#активаторы)
     -  [Событие игрока](#событие-игрока---playereventevent--none-)
     -  [Событие мира]()
     -  [Циклы]()
     -  [Функции]()
   - [Действия]()
     - [Действие игрока]()
     - [Игровое действие]()
     - [Установить переменную]()
     - [Работа с массивами]()
     - [Выбрать объект]()
   - [Условия]()
     - [Если игрок]()
     - [Если значение]()
     - [Если существо]()
     - [Если игра]()
     - [Иначе]()
4. [Примеры]()

# Установка 🤙

напиши тут чо та

# Синтаксис 💻

напиши тут чо та

# Документация 📜
Более подробная информация по всем событиям, условиям и действиям кода.
   - [Активаторы](#активаторы)
     -  [Событие игрока](#событие-игрока---playereventevent--none-)
     -  [Событие мира]()
     -  [Циклы]()
     -  [Функции]()
   - [Действия]()
     - [Действие игрока]()
     - [Игровое действие]()
     - [Установить переменную]()
     - [Работа с массивами]()
     - [Выбрать объект]()
   - [Условия]()
     - [Если игрок]()
     - [Если значение]()
     - [Если существо]()
     - [Если игра]()
     - [Иначе]()
## Активаторы
К активаторам относятся все блоки кода, которые начинают строку. Ими являются все существующие в коде события, циклы и вызываемые функции.
### Событие игрока - **`PlayerEvent(event) { none; }`**
| **Код** | **Название** |
| --- | --- |
| `PlayerEvent(join)` | Вход игрока |
| `PlayerEvent(leave)` | Выход игрока |
| `PlayerEvent(rejoin)` | Игрок перезашёл в игру |
| `PlayerEvent(interaction)` | Взаимодействие с блоком |
| `PlayerEvent(rightClick)` | Игрок кликает правой кнопкой |
| `PlayerEvent(leftClick)` | Игрок кликает левой кнопкой |
| `PlayerEvent(rightClickEntity)` | Правый клик по существу |
| `PlayerEvent(leashEntity)` | Игрок привязал сущность |
| `PlayerEvent(tameEntity)` | Игрок приручил сущность |
| `PlayerEvent(placeBlock)` | Игрок поставил блок |
| `PlayerEvent(breakBlock)` | Игрок сломал блок |
| `PlayerEvent(playerFishing)` | Игрок рыбачит |
| `PlayerEvent(damageBlock)` | Игрок дамажит блок |
| `PlayerEvent(expChange)` | Игрок подобрал опыт |
| `PlayerEvent(like)` | Игрок лайкает игру |
| `PlayerEvent(goldTransaction)` | Транзакция золота |
| `PlayerEvent(buyAdvert)` | Покупка рекламы |
| `PlayerEvent(buyPoint)` | Приобретение баллов |
| `PlayerEvent(studioTransaction)` | Транзакция Mineland Studio |
| `PlayerEvent(openedInventory)` | Игрок открыл инвентарь |
| `PlayerEvent(closedInventory)` | Игрок закрыл инвентарь |
| `PlayerEvent(editBook)` | Игрок изменил книгу |
| `PlayerEvent(damageItem)` | Игрок потратил прочность |
| `PlayerEvent(breakItem)` | Игрок сломал предмет |
| `PlayerEvent(clickInventory)` | Игрок кликнул по инвентарю |
| `PlayerEvent(moveInventory)` | Игрок перетащил предметы по слотам |
| `PlayerEvent(pickupItem)` | Игрок поднимает предмет |
| `PlayerEvent(dropItem)` | Игрок выбрасывает предмет |
| `PlayerEvent(extractFurnace)` | Игрок достал предмет из печи |
| `PlayerEvent(swapHands)` | Смена рук |
| `PlayerEvent(crafted)` | Игрок скрафтил предмет |
| `PlayerEvent(changeSlot)` | Игрок сменил слот |
| `PlayerEvent(killPlayer)` | Игрок убил игрока |
| `PlayerEvent(deathPlayer)` | Смерть игрока |
| `PlayerEvent(damagePlayer)` | Игрок нанёс урон игроку |
| `PlayerEvent(projectileDamagePlayer)` | Урон от снаряда |
| `PlayerEvent(takeDamagePlayer)` | Игрок получает урон |
| `PlayerEvent(takeFallDamagePlayer)` | Урон от падения |
| `PlayerEvent(killMobByPlayer)` | Игрок убил моба |
| `PlayerEvent(killPlayerByMob)` | Моб убил игрока |
| `PlayerEvent(damageMobByPlayer)` | Игрок нанёс урон мобу |
| `PlayerEvent(damagePlayerByMob)` | Моб наносит урон игроку |
| `PlayerEvent(projectileDamageMobByPlayer)` | Игрок нанёс урон мобу при помощи снаряда |
| `PlayerEvent(projectileKillMobByPlayer)` | Игрок убил моба при помощи снаряда |
| `PlayerEvent(deathMob)` | Смерть моба |
| `PlayerEvent(takeDamageMob)` | Моб получает урон |
| `PlayerEvent(restoredHealthEntity)` | Сущность восстановила здоровье |
| `PlayerEvent(sneak)` | Игрок крадётся |
| `PlayerEvent(unsneak)` | Игрок перестаёт красться |
| `PlayerEvent(startSprint)` | Игрок бежит |
| `PlayerEvent(jump)` | Игрок прыгает |
| `PlayerEvent(stopSprint)` | Игрок прекратил бежать |
| `PlayerEvent(move)` | Игрок передвигается |
| `PlayerEvent(rotate)` | Игрок повернулся |
| `PlayerEvent(message)` | Игрок написал в чат |
| `PlayerEvent(launchProjectile)` | Игрок запустил снаряд |
| `PlayerEvent(consumeItem)` | Игрок потребляет предмет |
| `PlayerEvent(changeFoodLvl)` | Изменение уровня голода |

### Событие мира - **`WorldEvent(event) { none; }`**
| **Код** | **Название** |
| --- | --- |
| `WorldEvent()` | Запуск мира |
| `WorldEvent()` | Остановка мира |
| `WorldEvent()` | Приём данных |
| `WorldEvent()` | Блок загорелся |
| `WorldEvent()` | Блок сгорел |
| `WorldEvent()` | Блок пропал |
| `WorldEvent()` | Поршень выдвигается |
| `WorldEvent()` | Поршень вдвигается |
| `WorldEvent()` | Блок взорвался |
| `WorldEvent()` | Спавн существа |
| `WorldEvent()` | Сущность взорвалась |
| `WorldEvent()` | Сущность решила взорваться |
| `WorldEvent()` | Опадение листьев |
| `WorldEvent()` | Дерево выросло |
| `WorldEvent()` | Блок вырос |
| `WorldEvent()` | Блок переместился |
| `WorldEvent()` | Зельеварка приготовила зелье(я) |
| `WorldEvent()` | Зельеварка увеличила уровень топлива |
| `WorldEvent()` | Блок сгенерировался |
| `WorldEvent()` | Генерация блока из-за сущности |
| `WorldEvent()` | Блок распространился |
| `WorldEvent()` | Падающий блок приземляется |
| `WorldEvent()` | Создание портала |
| `WorldEvent()` | Нотный блок проиграл звук |
| `WorldEvent()` | Блок выкинул предмет |
| `WorldEvent()` | Предмет пропал |
| `WorldEvent()` | Предметы объединились |
| `WorldEvent()` | Котел изменил уровень воды |
| `WorldEvent()` | Табличка была изменена |
| `WorldEvent()` | Блок выделил опыт |
| `WorldEvent()` | Предмет переместился в контейнер |
| `WorldEvent()` | Воронка подбирает предмет |
| `WorldEvent()` | Печь закончила плавку |
| `WorldEvent()` | Печь использует топливо |

### Циклы - **`Loop(`name`,0) { none; }`**

```
пример кода
```

### Функции - **`Function(`name`) { none; }`**

```
пример кода
```

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
