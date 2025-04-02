## Активаторы
К активаторам относятся все блоки кода, которые начинают строку. Ими являются все существующие в коде события, циклы и вызываемые функции.

   - [Активаторы](activators.md) 
     -  [Событие игрока](#событие-игрока---playereventevent--none--)
     -  [Событие мира](#событие-мира---worldeventevent--none--)
     -  [Циклы](#циклы---loopname-0--none--)
     -  [Функции](#функции---functionname--none--)

### Событие игрока - **`PlayerEvent(event) { none; }`** [🔝](#активаторы)
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

### Событие мира - **`WorldEvent(event) { none; }`** [🔝](#активаторы)
| **Код** | **Название** |
| --- | --- |
| `WorldEvent(start)` | Запуск мира |
| `WorldEvent(stop)` | Остановка мира |
| `WorldEvent(receiveData)` | Приём данных |
| `WorldEvent(blockIgnite)` | Блок загорелся |
| `WorldEvent(blockBurn)` | Блок сгорел |
| `WorldEvent(blockFade)` | Блок пропал |
| `WorldEvent(pistonExtend)` | Поршень выдвигается |
| `WorldEvent(pistonRetract)` | Поршень вдвигается |
| `WorldEvent(blockExplode)` | Блок взорвался |
| `WorldEvent(entitySpawn)` | Спавн существа |
| `WorldEvent(entityExplode)` | Сущность взорвалась |
| `WorldEvent(entityExplosionPrime)` | Сущность решила взорваться |
| `WorldEvent(leavesDecay)` | Опадение листьев |
| `WorldEvent(treeGrow)` | Дерево выросло |
| `WorldEvent(blockGrow)` | Блок вырос |
| `WorldEvent(blockMoved)` | Блок переместился |
| `WorldEvent(blockBrew)` | Зельеварка приготовила зелье(я) |
| `WorldEvent(brewingStandFuel)` | Зельеварка увеличила уровень топлива |
| `WorldEvent(blockForm)` | Блок сгенерировался |
| `WorldEvent(entityBlockForm)` | Генерация блока из-за сущности |
| `WorldEvent(blockSpread)` | Блок распространился |
| `WorldEvent(blockPhysics)` | Падающий блок приземляется |
| `WorldEvent(portalActivation)` | Создание портала |
| `WorldEvent(notePlay)` | Нотный блок проиграл звук |
| `WorldEvent(blockDispense)` | Блок выкинул предмет |
| `WorldEvent(itemDespawn)` | Предмет пропал |
| `WorldEvent(itemMerge)` | Предметы объединились |
| `WorldEvent(cauldronChange)` | Котел изменил уровень воды |
| `WorldEvent(signChange)` | Табличка была изменена |
| `WorldEvent(blockExp)` | Блок выделил опыт |
| `WorldEvent(itemMoveToInventory)` | Предмет переместился в контейнер |
| `WorldEvent(inventoryPickupItem)` | Воронка подбирает предмет |
| `WorldEvent(furnaceSmelt)` | Печь закончила плавку |
| `WorldEvent(furnaceBurn)` | Печь использует топливо |

### Циклы - **```Loop(`name`, 0) { none; }```** [🔝](#активаторы)

Пример кода:
```js
WorldEvent(start) {
   game.startLoop("give_item");
}

Loop(give_item, 150) {
   player.giveItems<all>(i`stone`);
}
```
При запуске мира будет запускаться цикл, который каждые 150 тиков будет выдавать всем игрокам камень.


### Функции - **```Function(`name`) { none; }```** [🔝](#активаторы)

Пример кода:
```js
WorldEvent(start) {
    game.startFunction("give_item");
}

Function(give_item) {
    player.giveItems<all>(i`stone`);
    game.wait(150);
    game.startFunction("give_item");
} 

```
При запуске мира будет запускаться функция, которая каждые 150 тиков будет выдавать всем игрокам камень. 

>[!TIP]
>Если имя функции или цикла не содержит пробел или спец. символы (кроме цифр и нижних подчёркиваний) то можно писать без спец. символов ``

# Документация 📜
Посмотрите информацию по другим элементам кода.

   - [Действия](documentation/actions.md)
     - [Действие игрока](documentation/actions.md#действие-игрока---playeractionargs-)
     - [Игровое действие](documentation/actions.md#игровое-действие---gameactionargs-)
     - [Установить переменную](documentation/actions.md#установить-переменную---varactionargs-)
     - [Работа с массивами](documentation/actions.md#работа-с-массивами---arrayactionargs-)
     - [Выбрать объект](documentation/actions.md#выбрать-объект---selectaction-)
   - [Условия](documentation/conditions.md)
     - [Если игрок](documentation/conditions.md#если-игрок---ifplayerconditionargs--none--)
     - [Если значение](documentation/conditions.md#если-значение---ifvalueconditionargs--none--)
     - [Если существо](documentation/conditions.md#если-существо---ifentityconditionargs--none--)
     - [Если игра](documentation/conditions.md#если-игра---ifgameconditionargs--none--)
     - [Иначе](documentation/conditions.md#иначе---else--none--)
   - [Значения](documentation/values.md)
     - [Игровое значение](documentation/values.md#игровое-значение---vvalue-)
     - [Местоположение](documentation/values.md#местоположение---lx-y-z-y-p-)
     - [Предмет](documentation/values.md#предмет---imaterial-c-m-)
     - [Частица](documentation/values.md#частица---particlevariant-)
     - [Зелье](documentation/values.md#зелье---vid-d-f-)
   - [Прочее](documentation/other.md)
     - [Константы](documentation/other.md#константы-)
     - [Ошибки](documentation/other.md#ошибки-)
     - [Комментарии](documentation/other.md#комментарии-)
     - [Языковой модуль](documentation/other.md#языковой-модуль-)
