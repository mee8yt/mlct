## Условия
Это специальная конструкция для фильтрации или проверки значений. Если, например, значение переменной проходит через этот фильтр и удовлетворяет условию, то выполняются действия внутри скобок, если не проходит, то запускает другой участок или вообще покидает тело условия.

   - [Условия](conditions.md)
     - [Если игрок](#если-игрок---ifplayerconditionargs--none--)
     - [Если значение](#если-значение---ifvalueconditionargs--none--)
     - [Если существо](#если-существо---ifentityconditionargs--none--)
     - [Если игра](#)
     - [Иначе](#)

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

### Если значение - **`ifValue.condition(args) { none; }`** [🔝](#условия)
| **Код** | **Название** |
| --- | --- |
| `ifValue.equals()` | Значение равно |
| `ifValue.notEquals()` | Значение не равно |
| `ifValue.compareNumber()` | Сравнить числа (облег.) |
| `ifValue.compareInterval()` | Сравнить числа |
| `ifValue.textEquals()` | Текст равняетс |
| `ifValue.textContains()` | Текст содержит |
| `ifValue.exists()` | Переменная существует |
| `ifValue.locationInRegion()` | Если местоположение в регионе |
| `ifValue.textStartWith()` | Текст начинается на |
| `ifValue.textEndWith()` | Текст заканчивается на |

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
