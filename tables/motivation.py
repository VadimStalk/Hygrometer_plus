"""Auxiliary module for /start"""
desc = {
    0: "прекрасный",
    1: "чудесный",
    2: "дивный",
    3: "великолепный",
    4: "прелестный",
    5: "изумительный",
    6: "чудный",
    7: "восхитительный",
    8: "замечательный",
    9: "превосходный",
}


mot = {
    0: "Прекрасный день, чтобы убить в себе нищеброда!",
    1: "Через год мы пожалеем, что не начали сегодня!",
    2: "Вера в себя создает героев!",
    3: "Вопрос не в том, кто разрешит, а в том, кто остановит!",
    4: "Никогда не поздно стать тем, кем всегда мечтал.",
    5: "Мы рождены, чтобы побеждать.",
    6: "Если мечты не пугают, то они слишком малы.",
    7: "Если будешь соблюдать правила, то упустишь самое интересное.",
    8: "Самый главный соперник – это отражение в зеркале.",
    9: "Если чего-то хочешь, то всегда найдешь способ, а иначе ищешь оправдания.",
    10: "Победа дается тем, кто готов идти до конца.",
    11: "Лучше сожалеть что сделал, чем что-то не попробовал.",
    12: "Идеального времени не будет, ведь ты уже на сцене.",
    13: "В жизни есть что-то, за что стоит бороться!",
    14: "Ты никогда не пересечешь океан, если боишься потерять из виду берег.",
    15: "Как только поверишь в себя, то никогда не будешь прежним.",
    16: "Сделай сегодня что-то такое, о чем завтра подумаешь с улыбкой.",
    17: "Нет ничего крепче в мире настойчивости.",
    18: "Ты способен на все, если только осмелишься.",
    19: "Единственное, что стоит на нашем пути – это наши оправдания.",
    20: "Cтань лучше в этот день!",
    21: "Лучший момент в жизни – это когда стало плевать на то, кто что думает.",
    22: "Единственный, кто сможет тебя остановить – это ты сам.",
    23: "В любом случае приятно знать в старости, что ты приложил все усилия.",
    24: "Месть – это отличный мотиватор.",
    25: "Думаешь если сдашься, то будет легче?",
    26: "Если бы капитан желал сохранить свой корабль, то он бы оставил его в порту.",
    27: "Не быть тем, кто разочаровывает родителей.",
    28: "Будь несчастлив или следуй за мечтами. Твой выбор?",
    29: "Лифта к мечтам нет, но есть лестница.",
    30: "Вероятность осуществить свои мечты делает жизнь интересной.",
    31: "Жизнь как фильм. Придумай свой собственный красочный сценарий.",
    32: "Только я могу изменить свою жизнь, ведь никто за меня этого не сделает.",
    33: "Только когда мы рискуем, наша жизнь становится лучше.",
    34: "Формула успеха проста. Удвой свои усилия, количество поражений и попыток.",
    35: "Победитель – это мечтатель, который не сдался.",
    36: "Сложные времена требуют сложных решений.",
    37: "Возможно это не просто, но это того стоит.",
    38: "То, что ты просыпаешься утром – это уже привилегия, а чего там еще боишься?",
    39: "Мы не знаем на что способны, пока не попробуем.",
    40: "Мотивирующие слова? Ты намного сильнее своих оправданий.",
    41: "Ты можешь построить замок из камней, что кидали в тебя.",
    42: "Когда меняешь свои мечты, то не забывай менять свою реальность.",
    43: "Безусловно можно сдаться, но как ты докажешь своим врагам их неправоту.",
    44: "Никогда не оглядывайся назад, это отвлекает от мечты впереди.",
    45: "Страх проигрыша должен быть меньше азарта победы.",
    46: "Разница мечту мечтами и реальностью только в том, что делаешь.",
    47: "Лучше всего учатся на неудачах, ведь это закаляет характер.",
    48: "Жизнь – это яркое приключение, либо отстой.",
    49: "Каждый чемпион – это соперник, который не сдался.",
    50: "Ты не один против всего мира, ты один против себя самого.",
    51: "Ты не жертва обстоятельств, а продукт своих решений.",
    52: "Единственный способ узнать свои возможности – это попробовать невозможное.",
    53: "Убедись в том, что главный твой враг не находится у тебя между ушами.",
    54: "Лучший способ предсказать будущее – это создать его.",
    55: "Самое сложное – это решить действовать, а все остальное упорство продолжать.",
    56: "Если ты даже не играешь, то ты точно проигрываешь.",
    57: "Плохо, что времени мало. Хорошо, что оно еще есть.",
    58: "Рискуй или потеряй шанс.",
    59: "Живи своими мечтами, а не своим прошлым.",
    60: "Мы сами пишем книгу своей жизни.",
    61: "Делать то, что в глубине души считаешь правильным.",
    62: "Быть продуктивным, а не занятым.",
    63: "Учиться следует так, словно будешь жить вечно, а жить так, словно умрешь завтра.",
    64: "Возможности есть в каждой трудности.",
    65: "Все, что вокруг тебя, было сознано людьми не умнее тебя.",
    66: "Если ничем не рискуешь, то рискуешь еще больше.",
    67: "Удача приходит к тому, кто ее упорно ищет.",
    68: "Поражение и неудача – это первые ступеньки победы.",
    69: "Не бойся отстаивать свое, даже если придется быть одному.",
    70: "Не останавливайся тогда, когда устал. Остановишься, когда сделаешь.",
    71: "Возможности не появляться в двери, ведь нужно вначале самому выбить запертую дверь.",
}
