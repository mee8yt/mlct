## Условия
Это специальная конструкция для фильтрации или проверки значений. Если, например, значение переменной проходит через этот фильтр и удовлетворяет условию, то выполняются действия внутри скобок, если не проходит, то запускает другой участок или вообще покидает тело условия.

   - [Условия](conditions.md)
     - [Если игрок](#если-игрок---ifplayerconditionargs--none--)
     - [Если значение](#если-значение---ifvalueconditionargs--none--)
     - [Если существо](#если-существо---ifentityconditionargs--none--)
     - [Если игра](#если-игра---ifgameconditionargs--none--)
     - [Иначе](#иначе---else--none--)

### Если игрок - **`ifPlayer.condition(args) { none; }`** [🔝](#условия)
| **Код** | **Название** |
| --- | --- |
| `ifPlayer.nameEquals()` | Имя равно |
| `ifPlayer.messageEquals()` | Сообщение равно |
| `ifPlayer.interactionType()` | Тип взаимодействия с блоком |
| `ifPlayer.handUsedEquals()` | Тип слота снаряжения |
| `ifPlayer.hasGoldTransaction()` | Имеет транзакцию золота |
| `ifPlayer.gamemodeEquals()` | Проверить режим игры |
| `ifPlayer.havePermissions()` | Проверить права игрока |
| `ifPlayer.holdingItem()` | Держит предмет |
| `ifPlayer.hasItem()` | Имеет предмет |
| `ifPlayer.wearingItem()` | Надет предмет |
| `ifPlayer.itemEquals()` | Предмет равен |
| `ifPlayer.itemInCursorEquals()` | Предмет в курсоре равен |
| `ifPlayer.itemHasDelay()` | Предмет имеет задержку |
| `ifPlayer.clickType()` | Тип клика |
| `ifPlayer.clickedSlotEquals()` | Кликнутый слот равен |
| `ifPlayer.hotbarSlotEquals()` | Выбранный слот равен |
| `ifPlayer.openInventoryNameEquals()` | Название открытого инвентаря равен |
| `ifPlayer.inventoryFull()` | Заполнен ли инвентарь игрока |
| `ifPlayer.lookAtBlock()` | Смотрит на блок |
| `ifPlayer.standOnBlock()` | Стоит на блоке |
| `ifPlayer.nearLocation()` | Находится рядом |
| `ifPlayer.blockEquals()` | Блок равен |
| `ifPlayer.isSneaking()` | Крадётся |
| `ifPlayer.isBlocking()` | Использует щит |
| `ifPlayer.isGliding()` | Летит на элитрах |
| `ifPlayer.isSprinting()` | Бежит |
| `ifPlayer.isFlying()` | Летает |
| `ifPlayer.isSwimming()` | Плавает |
| `ifPlayer.isLiked()` | Голосовал |

### Если значение - **`ifVar.condition(args) { none; }`** [🔝](#условия)
| **Код** | **Название** |
| --- | --- |
| `ifVar.equals()` | Значение равно |
| `ifVar.notEquals()` | Значение не равно |
| `ifVar.compareNumber()` | Сравнить числа (облег.) |
| `ifVar.compareInterval()` | Сравнить числа |
| `ifVar.textEquals()` | Текст равняется |
| `ifVar.textContains()` | Текст содержит |
| `ifVar.exists()` | Переменная существует |
| `ifVar.locationInRegion()` | Если местоположение в регионе |
| `ifVar.textStartWith()` | Текст начинается на |
| `ifVar.textEndWith()` | Текст заканчивается на |

### Если существо - **`ifEntity.condition(args) { none; }`** [🔝](#условия)
| **Код** | **Название** |
| --- | --- |
| `ifEntity.typeEquals()` | Тип равен |
| `ifEntity.nameEquals()` | Имя равно |
| `ifEntity.standOnBlock()` | Стоит на блоке |
| `ifEntity.nearLocation()` | Находится рядом |
| `ifEntity.isMob()` | Является мобом |
| `ifEntity.isNpc()` | Является NPC |
| `ifEntity.isProjectile()` | Является снарядом |
| `ifEntity.hasPotionEffect()` | Имеет эффект |

### Если игра - **`ifGame.condition(args) { none; }`** [🔝](#условия)
| **Код** | **Название** |
| --- | --- |
| `ifGame.blockEquals()` | Блок равен |
| `ifGame.containerHasItem()` | Контейнер имеет предмет |
| `ifGame.signContains()` | Табличка содержит текст |

### Иначе - **`else { none; }`** [🔝](#условия)

Пример кода:
```js
if (...) {
   pass;
} else {
   player.send("Код, если не сработало условие до иначе");
}
```

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
