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
| 0 | 0 |

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
| `player.setItems();` |  |
| `player.setItemsEnder();` |  |
| `player.setArmor();` |  |
| `player.setItemHand();` |  |
| `player.setItemCursor();` |  |
| `player.removeItem();` |  |
| `player.clearInventory();` |  |
| `player.clearEnder();` |  |
| `player.setHotbar();` |  |
| `player.giveRandomItem();` |  |
| `player.saveInventory();` |  |
| `player.loadInventory();` |  |
| `player.setDelay();` |  |
| `player.getItem();` |  |
| `player.setItem();` |  |
| `player.getItemCooldown();` |  |
| `player.send();` |  |
| `player.sendComponent();` |  |
| `player.sendDialogue();` |  |
| `player.clearChat();` |  |
| `player.playSound();` |  |
| `player.stopSound();` |  |
| `player.title();` |  |
| `player.actionbar();` |  |
| `player.showLink();` |  |
| `player.openBook();` |  |
| `player.openMenu();` |  |
| `player.expandMenu();` |  |
| `player.setItemInMenu();` |  |
| `player.setMenuName();` |  |
| `player.addLineInMenu();` |  |
| `player.deleteLineMenu();` |  |
| `player.closeInventory();` |  |
| `player.openBlock();` |  |
| `player.openEntity();` |  |
| `player.teleport();` |  |
| `player.rotateToLocation();` |  |
| `player.randomTeleport();` |  |
| `player.teleportSequence();` |  |
| `player.launchVertically();` |  |
| `player.launchForward();` |  |
| `player.launchToward();` |  |
| `player.launchToLocation();` |  |
| `player.kick();` |  |
| `player.moveToGame();` |  |
| `player.damage();` |  |
| `player.setHealth();` |  |
| `player.givePotionEffect();` |  |
| `player.clearPotionEffect();` |  |
| `player.removePotionEffect();` |  |
| `player.setXpLvl();` |  |
| `player.setXpProgress();` |  |
| `player.setHunger();` |  |
| `player.setSaturation();` |  |
| `player.setExhaustion();` |  |
| `player.setMaxHealth();` |  |
| `player.setOnFire();` |  |
| `player.setFlightSpeed();` |  |
| `player.setWalkSpeed();` |  |
| `player.setRemainingAir();` |  |
| `player.setMaximumAir();` |  |
| `player.setName();` |  |
| `player.setDamage();` |  |
| `player.setSize();` |  |
| `player.setSound();` |  |
| `player.setGlow();` |  |
| `player.setVisibility();` |  |
| `player.setGravity();` |  |
| `player.setInvincibility();` |  |
| `player.deleteEntity();` |  |
| `player.setFlight();` |  |
| `player.setGamemode();` |  |
| `player.setKeepInventory();` |  |
| `player.showScoreboard();` |  |
| `player.hideScoreboard();` |  |
| `player.showBossbar();` |  |
| `player.hideBossbar();` |  |
| `player.layOnBed();` |  |
| `player.wakeUp();` |  |
| `player.handAnimation();` |  |
| `player.sneakingState();` |  |
| `player.damageAnimation();` |  |
| `player.goldTransaction();` |  |
