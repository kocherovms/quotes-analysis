stock_list = {
    'CBOM': {'name': '"МОСКОВСКИЙ КРЕДИТНЫЙ БАНК" (публичное акционерное общество)', 'type': 'Акция обыкновенная'},
    'ALRS': {'name': 'Акционерная компания "АЛРОСА" (публичное акционерное общество)', 'type': 'Акция обыкновенная'},
    'VTBR': {'name': 'Банк ВТБ (публичное акционерное общество)', 'type': 'Акция обыкновенная'},
    'FIVE': {
        'name': 'Икс 5 Ритейл Груп Н.В. (X5 Retail Group N.V.) (эмитент депозитарных расписок - The Bank of New York Mellon)',
        'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'QIWI': {'name': 'КИВИ ПиЭлСи (QIWI PLC) (эмитент депозитарных расписок - The Bank of New York Mellon)',
             'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'YNDX': {
        'name': 'Компания с ограниченной ответственностью "Яндекс Н.В." (Public Limited Liability Company Yandex N.V.)',
        'type': 'Акции иностранного эмитента'},
    'LNTA': {'name': 'Лента Лтд. (Lenta Ltd.) (эмитент депозитарных расписок - Deutsche Bank Luxembourg S.A.)',
             'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'ENPL': {
        'name': 'Международная компания публичное акционерное общество "ЭН+ ГРУП" (эмитент депозитарных расписок - Citibank N.A. (NYC))',
        'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'BSPB': {'name': 'ПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО "БАНК "САНКТ-ПЕТЕРБУРГ"', 'type': 'Акция обыкновенная'},
    'POLY': {'name': 'Полиметалл Интернэшнл плс (Polymetal International plc)', 'type': 'Акции иностранного эмитента'},
    'AKRN': {'name': 'Публичное акционерное общество "Акрон"', 'type': 'Акция обыкновенная'},
    'AFKS': {'name': 'Публичное акционерное общество "Акционерная финансовая корпорация "Система"',
             'type': 'Акция обыкновенная'},
    'AFLT': {'name': 'Публичное акционерное общество "Аэрофлот – российские авиалинии"', 'type': 'Акция обыкновенная'},
    'GAZP': {'name': 'Публичное акционерное общество "Газпром"', 'type': 'Акция обыкновенная'},
    'GMKN': {'name': 'Публичное акционерное общество "Горно-металлургическая компания "Норильский никель"',
             'type': 'Акция обыкновенная'},
    'PIKK': {'name': 'Публичное акционерное общество "Группа Компаний ПИК"', 'type': 'Акция обыкновенная'},
    'LSRG': {'name': 'Публичное акционерное общество "Группа ЛСР"', 'type': 'Акция обыкновенная'},
    'DSKY': {'name': 'Публичное акционерное общество "Детский мир"', 'type': 'Акция обыкновенная'},
    'IRAO': {'name': 'Публичное акционерное общество "Интер РАО ЕЭС"', 'type': 'Акция обыкновенная'},
    'MVID': {'name': 'Публичное акционерное общество "М.видео"', 'type': 'Акция обыкновенная'},
    'MGNT': {'name': 'Публичное акционерное общество "Магнит"', 'type': 'Акция обыкновенная'},
    'MAGN': {'name': 'Публичное акционерное общество "Магнитогорский металлургический комбинат"',
             'type': 'Акция обыкновенная'},
    'MTLR': {'name': 'Публичное акционерное общество "Мечел"', 'type': 'Акция обыкновенная'},
    'MTLRP': {'name': 'Публичное акционерное общество "Мечел"', 'type': 'Акция привилегированная'},
    'MTSS': {'name': 'Публичное акционерное общество "Мобильные ТелеСистемы"', 'type': 'Акция обыкновенная'},
    'MOEX': {'name': 'Публичное акционерное общество "Московская Биржа ММВБ-РТС"', 'type': 'Акция обыкновенная'},
    'UWGN': {
        'name': 'Публичное акционерное общество "Научно-производственная корпорация "Объединенная Вагонная Компания"',
        'type': 'Акция обыкновенная'},
    'LKOH': {'name': 'Публичное акционерное общество "Нефтяная компания "ЛУКОЙЛ"', 'type': 'Акция обыкновенная'},
    'ROSN': {'name': 'Публичное акционерное общество "Нефтяная компания "Роснефть"', 'type': 'Акция обыкновенная'},
    'NLMK': {'name': 'Публичное акционерное общество "Новолипецкий металлургический комбинат"',
             'type': 'Акция обыкновенная'},
    'PLZL': {'name': 'Публичное акционерное общество "Полюс"', 'type': 'Акция обыкновенная'},
    'RSTI': {'name': 'Публичное акционерное общество "Российские сети"', 'type': 'Акция обыкновенная'},
    'RSTIP': {'name': 'Публичное акционерное общество "Российские сети"', 'type': 'Акция привилегированная'},
    'RTKM': {'name': 'Публичное акционерное общество "Ростелеком"', 'type': 'Акция обыкновенная'},
    'RTKMP': {'name': 'Публичное акционерное общество "Ростелеком"', 'type': 'Акция привилегированная'},
    'SFIN': {'name': 'Публичное акционерное общество "САФМАР Финансовые инвестиции"', 'type': 'Акция обыкновенная'},
    'SBER': {'name': 'Публичное акционерное общество "Сбербанк России"', 'type': 'Акция обыкновенная'},
    'SBERP': {'name': 'Публичное акционерное общество "Сбербанк России"', 'type': 'Акция привилегированная'},
    'CHMF': {'name': 'Публичное акционерное общество "Северсталь"', 'type': 'Акция обыкновенная'},
    'SELG': {'name': 'Публичное акционерное общество "Селигдар"', 'type': 'Акция обыкновенная'},
    'SELGP': {'name': 'Публичное акционерное общество "Селигдар"', 'type': 'Акция привилегированная'},
    'TATN': {'name': 'Публичное акционерное общество "Татнефть" имени В.Д. Шашина', 'type': 'Акция обыкновенная'},
    'TATNP': {'name': 'Публичное акционерное общество "Татнефть" имени В.Д. Шашина', 'type': 'Акция привилегированная'},
    'TGKA': {'name': 'Публичное акционерное общество "Территориальная генерирующая компания №1"',
             'type': 'Акция обыкновенная'},
    'TRNFP': {'name': 'Публичное акционерное общество "Транснефть"', 'type': 'Акция привилегированная'},
    'TRMK': {'name': 'Публичное акционерное общество "Трубная Металлургическая Компания"',
             'type': 'Акция обыкновенная'},
    'HYDR': {'name': 'Публичное акционерное общество "Федеральная гидрогенерирующая компания - РусГидро"',
             'type': 'Акция обыкновенная'},
    'FEES': {'name': 'Публичное акционерное общество "Федеральная сетевая компания Единой энергетической системы"',
             'type': 'Акция обыкновенная'},
    'PHOR': {'name': 'Публичное акционерное общество "ФосАгро"', 'type': 'Акция обыкновенная'},
    'ENRU': {'name': 'Публичное акционерное общество "Энел Россия"', 'type': 'Акция обыкновенная'},
    'UPRO': {'name': 'Публичное акционерное общество "Юнипро"', 'type': 'Акция обыкновенная'},
    'RNFT': {'name': 'Публичное акционерное общество Нефтегазовая компания "РуссНефть"', 'type': 'Акция обыкновенная'},
    'MSNG': {'name': 'Публичное акционерное общество энергетики и электрификации "Мосэнерго"',
             'type': 'Акция обыкновенная'},
    'AGRO': {'name': 'РОС АГРО ПЛС (ROS AGRO PLC) (эмитент депозитарных расписок - The Bank of New York Mellon)',
             'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'RUAL': {'name': 'Юнайтед Компани РУСАЛ Плс (United Company RUSAL Plc)', 'type': 'Акции иностранного эмитента'},
    'NVTK': {'name': 'публичное акционерное общество "НОВАТЭК"', 'type': 'Акция обыкновенная'},
    'MRKU': {'name': 'Открытое акционерное общество "Межрегиональная распределительная сетевая компания Урала"',
             'type': 'Акция обыкновенная'},
    'AQUA': {'name': 'Публичное  акционерное общество "Русская Аквакультура"', 'type': 'Акция обыкновенная'},
    'APTK': {'name': 'Публичное акционерное общество "Аптечная сеть 36,6"', 'type': 'Акция обыкновенная'},
    'AMEZ': {'name': 'Публичное акционерное общество "Ашинский металлургический завод"', 'type': 'Акция обыкновенная'},
    'OGKB': {'name': 'Публичное акционерное общество "Вторая генерирующая компания оптового рынка электроэнергии"',
             'type': 'Акция обыкновенная'},
    'DVEC': {'name': 'Публичное акционерное общество "Дальневосточная энергетическая компания"',
             'type': 'Акция обыкновенная'},
    'KMAZ': {'name': 'Публичное акционерное общество "КАМАЗ"', 'type': 'Акция обыкновенная'},
    'VSMO': {'name': 'Публичное акционерное общество "Корпорация ВСМПО-АВИСМА"', 'type': 'Акция обыкновенная'},
    'MSTT': {'name': 'Публичное акционерное общество "МОСТОТРЕСТ"', 'type': 'Акция обыкновенная'},
    'MRKV': {'name': 'Публичное акционерное общество "Межрегиональная распределительная сетевая компания Волги"',
             'type': 'Акция обыкновенная'},
    'MRKZ': {
        'name': 'Публичное акционерное общество "Межрегиональная распределительная сетевая компания Северо-Запада"',
        'type': 'Акция обыкновенная'},
    'MRKS': {'name': 'Публичное акционерное общество "Межрегиональная распределительная сетевая компания Сибири"',
             'type': 'Акция обыкновенная'},
    'MRKP': {
        'name': 'Публичное акционерное общество "Межрегиональная распределительная сетевая компания Центра и Приволжья"',
        'type': 'Акция обыкновенная'},
    'MRKC': {'name': 'Публичное акционерное общество "Межрегиональная распределительная сетевая компания Центра"',
             'type': 'Акция обыкновенная'},
    'MSRS': {'name': 'Публичное акционерное общество "Московская объединенная электросетевая компания"',
             'type': 'Акция обыкновенная'},
    'OBUV': {'name': 'Публичное акционерное общество "ОР"', 'type': 'Акция обыкновенная'},
    'RASP': {'name': 'Публичное акционерное общество "Распадская"', 'type': 'Акция обыкновенная'},
    'SVAV': {'name': 'Публичное акционерное общество "СОЛЛЕРС"', 'type': 'Акция обыкновенная'},
    'SNGS': {'name': 'Публичное акционерное общество "Сургутнефтегаз"', 'type': 'Акция обыкновенная'},
    'SNGSP': {'name': 'Публичное акционерное общество "Сургутнефтегаз"', 'type': 'Акция привилегированная'},
    'TGKN': {'name': 'Публичное акционерное общество "Территориальная генерирующая компания № 14"',
             'type': 'Акция обыкновенная'},
    'FTRE': {'name': 'Публичное акционерное общество "Финансовая группа БУДУЩЕЕ"', 'type': 'Акция обыкновенная'},
    'WTCM': {'name': 'Публичное акционерное общество "Центр международной торговли"', 'type': 'Акция обыкновенная'},
    'WTCMP': {'name': 'Публичное акционерное общество "Центр международной торговли"',
              'type': 'Акция привилегированная'},
    'TNSE': {'name': 'Публичное акционерное общество Группа компаний "ТНС энерго"', 'type': 'Акция обыкновенная'},
    'RDRB': {'name': '"Российский акционерный коммерческий дорожный банк" (публичное акционерное общество)',
             'type': 'Акция обыкновенная'},
    'RAVN': {'name': 'Raven Property Group Limited (Рейвен Проперти Груп Лимитед)',
             'type': 'Акции иностранного эмитента'},
    'AVAN': {'name': 'Акционерный Коммерческий банк "АВАНГАРД" - публичное акционерное общество',
             'type': 'Акция обыкновенная'},
    'IRGZ': {'name': 'Иркутское публичное акционерное общество энергетики и электрификации',
             'type': 'Акция обыкновенная'},
    'KZOS': {'name': 'Казанское публичное акционерное общество "Органический синтез"', 'type': 'Акция обыкновенная'},
    'KZOSP': {'name': 'Казанское публичное акционерное общество "Органический синтез"',
              'type': 'Акция привилегированная'},
    'LNZL': {'name': 'Ленское золотодобывающее публичное акционерное общество "Лензолото"',
             'type': 'Акция обыкновенная'},
    'LNZLP': {'name': 'Ленское золотодобывающее публичное акционерное общество "Лензолото"',
              'type': 'Акция привилегированная'},
    'KUNF': {'name': 'Открытое  акционерное общество "Каменск-Уральский завод по обработке цветных металлов"',
             'type': 'Акция обыкновенная'},
    'GTLC': {'name': 'Открытое акционерное общество "GTL"', 'type': 'Акция обыкновенная'},
    'BLNG': {'name': 'Открытое акционерное общество "Белон"', 'type': 'Акция обыкновенная'},
    'DZRD': {'name': 'Открытое акционерное общество "Донской завод радиодеталей"', 'type': 'Акция обыкновенная'},
    'DZRDP': {'name': 'Открытое акционерное общество "Донской завод радиодеталей"', 'type': 'Акция привилегированная'},
    'LVHK': {'name': 'Открытое акционерное общество "Левенгук"', 'type': 'Акция обыкновенная'},
    'LPSB': {'name': 'Открытое акционерное общество "Липецкая энергосбытовая компания"', 'type': 'Акция обыкновенная'},
    'MSST': {'name': 'Открытое акционерное общество "Мультисистема"', 'type': 'Акция обыкновенная'},
    'NPOF': {'name': 'Открытое акционерное общество "Научно-производственное объединение "Физика"',
             'type': 'Акция обыкновенная'},
    'MGNZ': {'name': 'Открытое акционерное общество "Соликамский магниевый завод"', 'type': 'Акция обыкновенная'},
    'MGVM': {'name': 'Открытое акционерное общество Медиа группа "Война и Мир"', 'type': 'Акция обыкновенная'},
    'KRKO': {'name': 'Открытое акционерное общество Таганрогский котлостроительный завод "Красный котельщик"',
             'type': 'Акция обыкновенная'},
    'KRKOP': {'name': 'Открытое акционерное общество Таганрогский котлостроительный завод "Красный котельщик"',
              'type': 'Акция привилегированная'},
    'ARSA': {'name': 'ПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО "УПРАВЛЯЮЩАЯ КОМПАНИЯ "АРСАГЕРА"', 'type': 'Акция обыкновенная'},
    'NKNC': {'name': 'Публичное Акционерное Общество "Нижнекамскнефтехим"', 'type': 'Акция обыкновенная'},
    'NKNCP': {'name': 'Публичное Акционерное Общество "Нижнекамскнефтехим"', 'type': 'Акция привилегированная'},
    'SIBG': {'name': 'Публичное Акционерное Общество "Сибирский гостинец"', 'type': 'Акция обыкновенная'},
    'ALNU': {'name': 'Публичное акционерное общество "АЛРОСА-Нюрба"', 'type': 'Акция обыкновенная'},
    'ARMD': {'name': 'Публичное акционерное общество "АРМАДА"', 'type': 'Акция обыкновенная'},
    'ACKO': {'name': 'Публичное акционерное общество "АСКО-СТРАХОВАНИЕ"', 'type': 'Акция обыкновенная'},
    'ABRD': {'name': 'Публичное акционерное общество "Абрау – Дюрсо"', 'type': 'Акция обыкновенная'},
    'UTAR': {'name': 'Публичное акционерное общество "Авиакомпания "ЮТэйр"', 'type': 'Акция обыкновенная'},
    'BANE': {'name': 'Публичное акционерное общество "Акционерная нефтяная Компания "Башнефть"',
             'type': 'Акция обыкновенная'},
    'BANEP': {'name': 'Публичное акционерное общество "Акционерная нефтяная Компания "Башнефть"',
              'type': 'Акция привилегированная'},
    'ASSB': {'name': 'Публичное акционерное общество "Астраханская энергосбытовая компания"',
             'type': 'Акция обыкновенная'},
    'USBN': {'name': 'Публичное акционерное общество "БАНК УРАЛСИБ"', 'type': 'Акция обыкновенная'},
    'BISV': {'name': 'Публичное акционерное общество "Башинформсвязь"', 'type': 'Акция обыкновенная'},
    'BISVP': {'name': 'Публичное акционерное общество "Башинформсвязь"', 'type': 'Акция привилегированная'},
    'BELU': {'name': 'Публичное акционерное общество "Белуга Групп"', 'type': 'Акция обыкновенная'},
    'ALBK': {'name': 'Публичное акционерное общество "Бест Эффортс Банк"', 'type': 'Акция обыкновенная'},
    'BRZL': {'name': 'Публичное акционерное общество "Бурятзолото"', 'type': 'Акция обыкновенная'},
    'VJGZ': {'name': 'Публичное акционерное общество "Варьеганнефтегаз"', 'type': 'Акция обыкновенная'},
    'VJGZP': {'name': 'Публичное акционерное общество "Варьеганнефтегаз"', 'type': 'Акция привилегированная'},
    'VDSB': {'name': 'Публичное акционерное общество "Владимирская энергосбытовая компания"',
             'type': 'Акция обыкновенная'},
    'VLHZ': {'name': 'Публичное акционерное общество "Владимирский химический завод"', 'type': 'Акция обыкновенная'},
    'VGSB': {'name': 'Публичное акционерное общество "Волгоградэнергосбыт"', 'type': 'Акция обыкновенная'},
    'VGSBP': {'name': 'Публичное акционерное общество "Волгоградэнергосбыт"', 'type': 'Акция привилегированная'},
    'VSYD': {'name': 'Публичное акционерное общество "Выборгский судостроительный завод"',
             'type': 'Акция обыкновенная'},
    'VSYDP': {'name': 'Публичное акционерное общество "Выборгский судостроительный завод"',
              'type': 'Акция привилегированная'},
    'GAZA': {'name': 'Публичное акционерное общество "ГАЗ"', 'type': 'Акция обыкновенная'},
    'GAZAP': {'name': 'Публичное акционерное общество "ГАЗ"', 'type': 'Акция привилегированная'},
    'GAZT': {'name': 'Публичное акционерное общество "ГАЗ-Тек"', 'type': 'Акция обыкновенная'},
    'GAZS': {'name': 'Публичное акционерное общество "ГАЗ-сервис"', 'type': 'Акция обыкновенная'},
    'GAZC': {'name': 'Публичное акционерное общество "ГАЗКОН"', 'type': 'Акция обыкновенная'},
    'GTSS': {'name': 'Публичное акционерное общество "ГЕОТЕК Сейсморазведка"', 'type': 'Акция обыкновенная'},
    'GTRK': {'name': 'Публичное акционерное общество "ГЛОБАЛТРАК МЕНЕДЖМЕНТ"', 'type': 'Акция обыкновенная'},
    'RTGZ': {'name': 'Публичное акционерное общество "Газпром газораспределение Ростов-на-Дону"',
             'type': 'Акция обыкновенная'},
    'SIBN': {'name': 'Публичное акционерное общество "Газпром нефть"', 'type': 'Акция обыкновенная'},
    'OGZD': {
        'name': 'Публичное акционерное общество "Газпром" (эмитент депозитарных расписок - The Bank of New York Mellon)',
        'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'HALS': {'name': 'Публичное акционерное общество "Галс-Девелопмент"', 'type': 'Акция обыкновенная'},
    'GRNT': {'name': 'Публичное акционерное общество "Городские Инновационные Технологии"',
             'type': 'Акция обыкновенная'},
    'RLMN': {'name': 'Публичное акционерное общество "Группа Компаний  "Роллман"', 'type': 'Акция обыкновенная'},
    'RLMNP': {'name': 'Публичное акционерное общество "Группа Компаний  "Роллман"', 'type': 'Акция привилегированная'},
    'GCHE': {'name': 'Публичное акционерное общество "Группа Черкизово"', 'type': 'Акция обыкновенная'},
    'DASB': {'name': 'Публичное акционерное общество "Дагестанская энергосбытовая компания"',
             'type': 'Акция обыкновенная'},
    'FESH': {'name': 'Публичное акционерное общество "Дальневосточное морское пароходство"',
             'type': 'Акция обыкновенная'},
    'EELT': {'name': 'Публичное акционерное общество "Европейская Электротехника"', 'type': 'Акция обыкновенная'},
    'ZVEZ': {'name': 'Публичное акционерное общество "ЗВЕЗДА"', 'type': 'Акция обыкновенная'},
    'ZILL': {'name': 'Публичное акционерное общество "Завод имени И.А. Лихачева"', 'type': 'Акция обыкновенная'},
    'IDVP': {'name': 'Публичное акционерное общество "ИНВЕСТ-ДЕВЕЛОПМЕНТ"', 'type': 'Акция обыкновенная'},
    'RUSI': {'name': 'Публичное акционерное общество "ИНВЕСТИЦИОННАЯ КОМПАНИЯ ИК РУСС-ИНВЕСТ"',
             'type': 'Акция обыкновенная'},
    'OPIN': {'name': 'Публичное акционерное общество "ИНГРАД"', 'type': 'Акция обыкновенная'},
    'IGST': {'name': 'Публичное акционерное общество "Ижсталь"', 'type': 'Акция обыкновенная'},
    'IGSTP': {'name': 'Публичное акционерное общество "Ижсталь"', 'type': 'Акция привилегированная'},
    'ISKJ': {'name': 'Публичное акционерное общество "Институт Стволовых Клеток Человека"',
             'type': 'Акция обыкновенная'},
    'KLSB': {'name': 'Публичное акционерное общество "Калужская сбытовая компания"', 'type': 'Акция обыкновенная'},
    'TGKD': {'name': 'Публичное акционерное общество "Квадра - Генерирующая компания"', 'type': 'Акция обыкновенная'},
    'TGKDP': {'name': 'Публичное акционерное общество "Квадра - Генерирующая компания"',
              'type': 'Акция привилегированная'},
    'KSGR': {'name': 'Публичное акционерное общество "Кокс"', 'type': 'Акция обыкновенная'},
    'KOGK': {'name': 'Публичное акционерное общество "Коршуновский горно-обогатительный комбинат"',
             'type': 'Акция обыкновенная'},
    'KMTZ': {'name': 'Публичное акционерное общество "Косогорский металлургический завод"',
             'type': 'Акция обыкновенная'},
    'KTSB': {'name': 'Публичное акционерное общество "Костромская сбытовая компания"', 'type': 'Акция обыкновенная'},
    'KTSBP': {'name': 'Публичное акционерное общество "Костромская сбытовая компания"',
              'type': 'Акция привилегированная'},
    'KZMS': {'name': 'Публичное акционерное общество "Краснокамский завод металлических сеток"',
             'type': 'Акция обыкновенная'},
    'KRSB': {'name': 'Публичное акционерное общество "Красноярскэнергосбыт"', 'type': 'Акция обыкновенная'},
    'KRSBP': {'name': 'Публичное акционерное общество "Красноярскэнергосбыт"', 'type': 'Акция привилегированная'},
    'KBTK': {'name': 'Публичное акционерное общество "Кузбасская Топливная Компания"', 'type': 'Акция обыкновенная'},
    'KAZT': {'name': 'Публичное акционерное общество "КуйбышевАзот"', 'type': 'Акция обыкновенная'},
    'KAZTP': {'name': 'Публичное акционерное общество "КуйбышевАзот"', 'type': 'Акция привилегированная'},
    'KGKC': {'name': 'Публичное акционерное общество "Курганская генерирующая компания"', 'type': 'Акция обыкновенная'},
    'KGKCP': {'name': 'Публичное акционерное общество "Курганская генерирующая компания"',
              'type': 'Акция привилегированная'},
    'MERF': {'name': 'Публичное акционерное общество "МЕРИДИАН"', 'type': 'Акция обыкновенная'},
    'MNFD': {'name': 'Публичное акционерное общество "МН-фонд"', 'type': 'Акция обыкновенная'},
    'MFON': {'name': 'Публичное акционерное общество "МегаФон"', 'type': 'Акция обыкновенная'},
    'ODVA': {'name': 'Публичное акционерное общество "Медиахолдинг"', 'type': 'Акция обыкновенная'},
    'GEMA': {
        'name': 'Публичное акционерное общество "Международный Медицинский Центр Обработки и Криохранения Биоматериалов"',
        'type': 'Акция обыкновенная'},
    'MRKK': {
        'name': 'Публичное акционерное общество "Межрегиональная распределительная сетевая компания Северного Кавказа"',
        'type': 'Акция обыкновенная'},
    'MRKY': {'name': 'Публичное акционерное общество "Межрегиональная распределительная сетевая компания Юга"',
             'type': 'Акция обыкновенная'},
    'MRSB': {'name': 'Публичное акционерное общество "Мордовская энергосбытовая компания"',
             'type': 'Акция обыкновенная'},
    'MORI': {'name': 'Публичное акционерное общество "Морион"', 'type': 'Акция обыкновенная'},
    'MGTS': {'name': 'Публичное акционерное общество "Московская городская телефонная сеть"',
             'type': 'Акция обыкновенная'},
    'MGTSP': {'name': 'Публичное акционерное общество "Московская городская телефонная сеть"',
              'type': 'Акция привилегированная'},
    'KROT': {'name': 'Публичное акционерное общество "Московская кондитерская фабрика "Красный Октябрь"',
             'type': 'Акция обыкновенная'},
    'KROTP': {'name': 'Публичное акционерное общество "Московская кондитерская фабрика "Красный Октябрь"',
              'type': 'Акция привилегированная'},
    'NSVZ': {'name': 'Публичное акционерное общество "Наука-Связь"', 'type': 'Акция обыкновенная'},
    'IRKT': {'name': 'Публичное акционерное общество "Научно-производственная корпорация "Иркут"',
             'type': 'Акция обыкновенная'},
    'NFAZ': {'name': 'Публичное акционерное общество "Нефтекамский автозавод"', 'type': 'Акция обыкновенная'},
    'NKSH': {'name': 'Публичное акционерное общество "Нижнекамскшина"', 'type': 'Акция обыкновенная'},
    'NKHP': {'name': 'Публичное акционерное общество "Новороссийский комбинат хлебопродуктов"',
             'type': 'Акция обыкновенная'},
    'NMTP': {'name': 'Публичное акционерное общество "Новороссийский морской торговый порт"',
             'type': 'Акция обыкновенная'},
    'SATR': {'name': 'Публичное акционерное общество "ОДК-Сатурн"', 'type': 'Акция обыкновенная'},
    'UNAC': {'name': 'Публичное акционерное общество "Объединенная авиастроительная корпорация"',
             'type': 'Акция обыкновенная'},
    'UCSS': {'name': 'Публичное акционерное общество "Объединенные Кредитные Системы"', 'type': 'Акция обыкновенная'},
    'PRTK': {'name': 'Публичное акционерное общество "ПРОТЕК"', 'type': 'Акция обыкновенная'},
    'PAZA': {'name': 'Публичное акционерное общество "Павловский автобус"', 'type': 'Акция обыкновенная'},
    'PMSB': {'name': 'Публичное акционерное общество "Пермская энергосбытовая компания"', 'type': 'Акция обыкновенная'},
    'PMSBP': {'name': 'Публичное акционерное общество "Пермская энергосбытовая компания"',
              'type': 'Акция привилегированная'},
    'PLSM': {'name': 'Публичное акционерное общество "Плазмек"', 'type': 'Акция обыкновенная'},
    'RBCM': {'name': 'Публичное акционерное общество "РБК"', 'type': 'Акция обыкновенная'},
    'CHGZ': {'name': 'Публичное акционерное общество "РН-Западная Сибирь"', 'type': 'Акция обыкновенная'},
    'ROST': {'name': 'Публичное акционерное общество "РОСИНТЕР РЕСТОРАНТС ХОЛДИНГ"', 'type': 'Акция обыкновенная'},
    'RKKE': {'name': 'Публичное акционерное общество "Ракетно-космическая корпорация "Энергия" имени С.П. Королёва"',
             'type': 'Акция обыкновенная'},
    'RSDR': {
        'name': 'Публичное акционерное общество "Российские сети" (эмитент депозитарных расписок - The Bank of New York Mellon)',
        'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'RUGR': {'name': 'Публичное акционерное общество "Русгрэйн Холдинг"', 'type': 'Акция обыкновенная'},
    'ROLO': {'name': 'Публичное акционерное общество "Русолово"', 'type': 'Акция обыкновенная'},
    'RUSP': {'name': 'Публичное акционерное общество "Русполимет"', 'type': 'Акция обыкновенная'},
    'RZSB': {'name': 'Публичное акционерное общество "Рязанская энергетическая сбытовая компания"',
             'type': 'Акция обыкновенная'},
    'KRKN': {'name': 'Публичное акционерное общество "Саратовский нефтеперерабатывающий завод"',
             'type': 'Акция обыкновенная'},
    'KRKNP': {'name': 'Публичное акционерное общество "Саратовский нефтеперерабатывающий завод"',
              'type': 'Акция привилегированная'},
    'SARE': {'name': 'Публичное акционерное общество "Саратовэнерго"', 'type': 'Акция обыкновенная'},
    'SAREP': {'name': 'Публичное акционерное общество "Саратовэнерго"', 'type': 'Акция привилегированная'},
    'SZPR': {'name': 'Публичное акционерное общество "Северо-Западное пароходство"', 'type': 'Акция обыкновенная'},
    'JNOS': {'name': 'Публичное акционерное общество "Славнефть-Ярославнефтеоргсинтез"', 'type': 'Акция обыкновенная'},
    'JNOSP': {'name': 'Публичное акционерное общество "Славнефть-Ярославнефтеоргсинтез"',
              'type': 'Акция привилегированная'},
    'STSB': {'name': 'Публичное акционерное общество "Ставропольэнергосбыт"', 'type': 'Акция обыкновенная'},
    'STSBP': {'name': 'Публичное акционерное общество "Ставропольэнергосбыт"', 'type': 'Акция привилегированная'},
    'VRSB': {'name': 'Публичное акционерное общество "ТНС энерго Воронеж"', 'type': 'Акция обыкновенная'},
    'VRSBP': {'name': 'Публичное акционерное общество "ТНС энерго Воронеж"', 'type': 'Акция привилегированная'},
    'KBSB': {'name': 'Публичное акционерное общество "ТНС энерго Кубань"', 'type': 'Акция обыкновенная'},
    'MISB': {'name': 'Публичное акционерное общество "ТНС энерго Марий Эл"', 'type': 'Акция обыкновенная'},
    'MISBP': {'name': 'Публичное акционерное общество "ТНС энерго Марий Эл"', 'type': 'Акция привилегированная'},
    'NNSB': {'name': 'Публичное акционерное общество "ТНС энерго Нижний Новгород"', 'type': 'Акция обыкновенная'},
    'NNSBP': {'name': 'Публичное акционерное общество "ТНС энерго Нижний Новгород"', 'type': 'Акция привилегированная'},
    'RTSB': {'name': 'Публичное акционерное общество "ТНС энерго Ростов-на-Дону"', 'type': 'Акция обыкновенная'},
    'RTSBP': {'name': 'Публичное акционерное общество "ТНС энерго Ростов-на-Дону"', 'type': 'Акция привилегированная'},
    'YRSB': {'name': 'Публичное акционерное общество "ТНС энерго Ярославль"', 'type': 'Акция обыкновенная'},
    'YRSBP': {'name': 'Публичное акционерное общество "ТНС энерго Ярославль"', 'type': 'Акция привилегированная'},
    'TASB': {'name': 'Публичное акционерное общество "Тамбовская энергосбытовая компания"',
             'type': 'Акция обыкновенная'},
    'TASBP': {'name': 'Публичное акционерное общество "Тамбовская энергосбытовая компания"',
              'type': 'Акция привилегированная'},
    'TANL': {'name': 'Публичное акционерное общество "Тантал"', 'type': 'Акция обыкновенная'},
    'TANLP': {'name': 'Публичное акционерное общество "Тантал"', 'type': 'Акция привилегированная'},
    'TTLK': {'name': 'Публичное акционерное общество "Таттелеком"', 'type': 'Акция обыкновенная'},
    'TGKB': {'name': 'Публичное акционерное общество "Территориальная генерирующая компания №2"',
             'type': 'Акция обыкновенная'},
    'TGKBP': {'name': 'Публичное акционерное общество "Территориальная генерирующая компания №2"',
              'type': 'Акция привилегированная'},
    'TORS': {'name': 'Публичное акционерное общество "Томская распределительная компания"',
             'type': 'Акция обыкновенная'},
    'TORSP': {'name': 'Публичное акционерное общество "Томская распределительная компания"',
              'type': 'Акция привилегированная'},
    'TRFM': {'name': 'Публичное акционерное общество "ТрансФин-М"', 'type': 'Акция обыкновенная'},
    'TMKS': {
        'name': 'Публичное акционерное общество "Трубная Металлургическая Компания" (эмитент депозитарных расписок - The Bank of New York Mellon)',
        'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'TUZA': {'name': 'Публичное акционерное общество "Туймазинский завод автобетоновозов"',
             'type': 'Акция обыкновенная'},
    'TUCH': {'name': 'Публичное акционерное общество "Тучковский комбинат строительных материалов"',
             'type': 'Акция обыкновенная'},
    'UKUZ': {'name': 'Публичное акционерное общество "Угольная компания "Южный Кузбасс"', 'type': 'Акция обыкновенная'},
    'URKA': {'name': 'Публичное акционерное общество "Уралкалий"', 'type': 'Акция обыкновенная'},
    'URKZ': {'name': 'Публичное акционерное общество "Уральская кузница"', 'type': 'Акция обыкновенная'},
    'LIFE': {'name': 'Публичное акционерное общество "Фармсинтез"', 'type': 'Акция обыкновенная'},
    'HKOL': {'name': 'Публичное акционерное общество "ХОРОШИЕ КОЛЕСА"', 'type': 'Акция обыкновенная'},
    'HIMC': {'name': 'Публичное акционерное общество "Химпром"', 'type': 'Акция обыкновенная'},
    'HIMCP': {'name': 'Публичное акционерное общество "Химпром"', 'type': 'Акция привилегированная'},
    'TRCN': {'name': 'Публичное акционерное общество "Центр по перевозке грузов в контейнерах "ТрансКонтейнер"',
             'type': 'Акция обыкновенная'},
    'TCDR': {
        'name': 'Публичное акционерное общество "Центр по перевозке грузов в контейнерах "ТрансКонтейнер" (эмитент депозитарных расписок - The Bank of New York Mellon)',
        'type': 'Депозитарные расписки иностранного эмитента на акции'},
    'CNTL': {'name': 'Публичное акционерное общество "Центральный телеграф"', 'type': 'Акция обыкновенная'},
    'CNTLP': {'name': 'Публичное акционерное общество "Центральный телеграф"', 'type': 'Акция привилегированная'},
    'PRFN': {'name': 'Публичное акционерное общество "Челябинский завод профилированного стального настила"',
             'type': 'Акция обыкновенная'},
    'CHKZ': {'name': 'Публичное акционерное общество "Челябинский кузнечно-прессовый завод"',
             'type': 'Акция обыкновенная'},
    'CHMK': {'name': 'Публичное акционерное общество "Челябинский металлургический комбинат"',
             'type': 'Акция обыкновенная'},
    'CHEP': {'name': 'Публичное акционерное общество "Челябинский трубопрокатный завод"', 'type': 'Акция обыкновенная'},
    'CLSB': {'name': 'Публичное акционерное общество "Челябэнергосбыт"', 'type': 'Акция обыкновенная'},
    'CLSBP': {'name': 'Публичное акционерное общество "Челябэнергосбыт"', 'type': 'Акция привилегированная'},
    'ELTZ': {'name': 'Публичное акционерное общество "Электроцинк"', 'type': 'Акция обыкновенная'},
    'UNKL': {'name': 'Публичное акционерное общество "Южно-Уральский никелевый комбинат"',
             'type': 'Акция обыкновенная'},
    'YAKG': {'name': 'Публичное акционерное общество "Якутская топливно-энергетическая компания"',
             'type': 'Акция обыкновенная'},
    'YKEN': {'name': 'Публичное акционерное общество "Якутскэнерго"', 'type': 'Акция обыкновенная'},
    'YKENP': {'name': 'Публичное акционерное общество "Якутскэнерго"', 'type': 'Акция привилегированная'},
    'VZRZ': {'name': 'Публичное акционерное общество Банк "Возрождение"', 'type': 'Акция обыкновенная'},
    'VZRZP': {'name': 'Публичное акционерное общество Банк "Возрождение"', 'type': 'Акция привилегированная'},
    'KUZB': {'name': 'Публичное акционерное общество Банк "Кузнецкий"', 'type': 'Акция обыкновенная'},
    'DIOD': {'name': 'Публичное акционерное общество Завод экологической техники и экопитания "ДИОД"',
             'type': 'Акция обыкновенная'},
    'MOBB': {'name': 'Публичное акционерное общество МОСКОВСКИЙ ОБЛАСТНОЙ БАНК', 'type': 'Акция обыкновенная'},
    'NAUK': {'name': 'Публичное акционерное общество Научно-производственное объединение "Наука"',
             'type': 'Акция обыкновенная'},
    'OMZZP': {'name': 'Публичное акционерное общество Объединенные машиностроительные заводы (Группа Уралмаш-Ижора)',
              'type': 'Акция привилегированная'},
    'ROSB': {'name': 'Публичное акционерное общество РОСБАНК', 'type': 'Акция обыкновенная'},
    'RGSS': {'name': 'Публичное акционерное общество Страховая Компания "Росгосстрах"', 'type': 'Акция обыкновенная'},
    'KCHE': {'name': 'Публичное акционерное общество энергетики и электрификации "Камчатскэнерго"',
             'type': 'Акция обыкновенная'},
    'KCHEP': {'name': 'Публичное акционерное общество энергетики и электрификации "Камчатскэнерго"',
              'type': 'Акция привилегированная'},
    'LSNG': {'name': 'Публичное акционерное общество энергетики и электрификации "Ленэнерго"',
             'type': 'Акция обыкновенная'},
    'LSNGP': {'name': 'Публичное акционерное общество энергетики и электрификации "Ленэнерго"',
              'type': 'Акция привилегированная'},
    'MAGE': {'name': 'Публичное акционерное общество энергетики и электрификации "Магаданэнерго"',
             'type': 'Акция обыкновенная'},
    'MAGEP': {'name': 'Публичное акционерное общество энергетики и электрификации "Магаданэнерго"',
              'type': 'Акция привилегированная'},
    'SAGO': {'name': 'Публичное акционерное общество энергетики и электрификации "Самараэнерго"',
             'type': 'Акция обыкновенная'},
    'SAGOP': {'name': 'Публичное акционерное общество энергетики и электрификации "Самараэнерго"',
              'type': 'Акция привилегированная'},
    'SLEN': {'name': 'Публичное акционерное общество энергетики и электрификации "Сахалинэнерго"',
             'type': 'Акция обыкновенная'},
    'KUBE': {'name': 'Публичное акционерное общество энергетики и электрификации Кубани', 'type': 'Акция обыкновенная'},
    'PRMB': {'name': 'акционерный коммерческий банк "Приморье" (публичное акционерное общество)',
             'type': 'Акция обыкновенная'},
    'MFGS': {'name': 'открытое акционерное общество "Славнефть - Мегионнефтегаз"', 'type': 'Акция обыкновенная'},
    'MFGSP': {'name': 'открытое акционерное общество "Славнефть - Мегионнефтегаз"', 'type': 'Акция привилегированная'},
    'KMEZ': {'name': 'публичное акционерное общество "Ковровский механический завод"', 'type': 'Акция обыкновенная'},
}
