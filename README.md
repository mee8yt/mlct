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
| `PlayerEvent(leave)` | f |
| `PlayerEvent(rejoin)` | f |
| `PlayerEvent(interaction)` | f |
| `PlayerEvent(rightClick)` | f |
| `PlayerEvent(leftClick)` | f |
| `PlayerEvent(rightClickEntity)` | f |
| `PlayerEvent(leashEntity)` | f |
| `PlayerEvent(tameEntity)` | f |
| `PlayerEvent(placeBlock)` | f |
| `PlayerEvent(breakBlock)` | f |
| `PlayerEvent(playerFishing)` | f |
| `PlayerEvent(damageBlock)` | f |
| `PlayerEvent(expChange)` | f |
| `PlayerEvent(like)` | f |
| `PlayerEvent(goldTransaction)` | f |
| `PlayerEvent(buyAdvert)` | f |
| `PlayerEvent(buyPoint)` | f |
| `PlayerEvent(studioTransaction)` | f |
| `PlayerEvent(openedInventory)` | f |
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
