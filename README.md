# MLCT
**MLCT** *(**M**ine**L**and **C**ode **T**ranslator)* - Мод, для установки письменного варианта блочного кода на сервере Mineland.

## Содержание

1. [Установка]()
2. [Синтаксис]()
3. [Документация](#документация)
   - [Активаторы](#активаторы)
     -  [Событие игрока](#событие-игрока---playereventname--none-)
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

# Установка

напиши тут чо та

# Синтаксис

напиши тут чо та

# Документация
Более подробная информация по всем событиям, условиям и действиям кода.
   - [Активаторы](#активаторы)
     -  [Событие игрока](#событие-игрока---playereventname--none-)
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
