# MLCT
**MLCT** *(**M**ine**L**and **C**ode **T**ranslator)* - Мод, для установки письменного варианта блочного кода на сервере Mineland.

## Содержание

1. [Активаторы](#активаторы)
   -  [Событие игрока](#событие-игрока---playereventname--none-)
   -  [Событие мира]()
   -  [Циклы]()
   -  [Функции]()
2. [Действия]()
   - [Действие игрока]()
   - [Игровое действие]()
   - [Установить переменную]()
   - [Работа с массивами]()
   - [Выбрать объект]()
3. [Условия]()
   - [Если игрок]()
   - [Если значение]()
   - [Если существо]()
   - [Если игра]()
   - [Иначе]()
4. [Примеры]()

## Активаторы
К активаторам относятся все блоки кода, которые начинают строку. Ими являются все существующие в коде события, циклы и вызываемые функции.
### Событие игрока - **`PlayerEvent(name) { none; }`**
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
| `PlayerEvent(closedInventory)` | f |
| `PlayerEvent(editBook)` | f |
| `PlayerEvent(damageItem)` | f |
| `PlayerEvent(breakItem)` | f |
| `PlayerEvent(clickInventory)` | f |
| `PlayerEvent(moveInventory)` | f |
| `PlayerEvent(pickupItem)` | f |
| `PlayerEvent(dropItem)` | f |
| `PlayerEvent(extractFurnace)` | f |
| `PlayerEvent(swapHands)` | f |
| `PlayerEvent(crafted)` | f |
| `PlayerEvent(changeSlot)` | f |
| `PlayerEvent(killPlayer)` | f |
| `PlayerEvent(deathPlayer)` | f |
| `PlayerEvent(damagePlayer)` | f |
| `PlayerEvent(projectileDamagePlayer)` | f |
| `PlayerEvent(takeDamagePlayer)` | f |
| `PlayerEvent(takeFallDamagePlayer)` | f |
| `PlayerEvent(killMobByPlayer)` | f |
| `PlayerEvent(killPlayerByMob)` | f |
| `PlayerEvent(damageMobByPlayer)` | f |
| `PlayerEvent(damagePlayerByMob)` | f |
| `PlayerEvent(projectileDamageMobByPlayer)` | f |
| `PlayerEvent(projectileKillMobByPlayer)` | f |
| `PlayerEvent(deathMob)` | f |
| `PlayerEvent(takeDamageMob)` | f |
| `PlayerEvent(restoredHealthEntity)` | f |
| `PlayerEvent(sneak)` | f |
| `PlayerEvent(unsneak)` | f |
| `PlayerEvent(startSprint)` | f |
| `PlayerEvent(jump)` | f |
| `PlayerEvent(stopSprint)` | f |
| `PlayerEvent(move)` | f |
| `PlayerEvent(rotate)` | f |
| `PlayerEvent(message)` | f |
| `PlayerEvent(launchProjectile)` | f |
| `PlayerEvent(consumeItem)` | f |
| `PlayerEvent(changeFoodLvl)` | f |
