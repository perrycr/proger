from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
  await message.answer(f'Привет, {message.from_user.first_name}! Я - бот помощник в Python.\nВыберите раздел:', reply_markup=kb.main)

@router.callback_query(F.data == 'study')
async def study(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы выбрали обучение: ', reply_markup=kb.study)

@router.callback_query(F.data == 'backstudy')
async def backstudy(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('Вы вернулись в главное меню: ', reply_markup=kb.main)

@router.callback_query(F.data == 'backstrstudy')
async def bstrstudy(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('Вы вернулись назад в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'strstudy')
async def strstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('str() - от английского string - строка. Функция str() превращает значение в строку. \nПример:\n```\na = "School"\nb = "is"\nc = "cool"\nsumma = a + b + c\nprint(type(summa))\n```\nВывод:\n<class "str">\n\nКак итог мы получаем тип класса - строка (str)', reply_markup=kb.strstudy)

@router.callback_query(F.data == 'fromstrstudy')
async def fstrsudy(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('abs() - от английского absolute value  - абсолютное значение. Функция abs() возвращает число по модулю.\nПример:\n```\na = -5\nprint(abs(a))\n```\nВывод:\n5\n\nКак мы видим вывилось число -5 по модулю, то есть просто 5', reply_markup=kb.absstudy)

@router.callback_query(F.data == 'absstudy')
async def absstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('abs() - от английского absolute value  - абсолютное значение. Функция abs() возвращает число по модулю.\nПример:\n```\na = -5\nprint(abs(a))\n```\nВывод:\n5\n\nКак мы видим вывилось число -5 по модулю, то есть просто 5', reply_markup=kb.absstudy)

@router.callback_query(F.data == 'backfromabs')
async def backfromabs(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('str() - от английского string - строка. Функция str() превращает значение в строку. \nПример:\n```\na = "School"\nb = "is"\nc = "cool"\nsumma = a + b + c\nprint(type(summa))\n```\nВывод:\n<class "str">\n\nКак итог мы получаем тип класса - строка (str)', reply_markup=kb.strstudy)

@router.callback_query(F.data == 'fromabstomenue')
async def absmenue(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись назад в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'nextfromabs')
async def nextfabs(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('input() - от английского input - ввод. Функция input() принимает строковый тип данных.\nПример:\n```\nname = input("Введите имя: ")\nprint(name)\n```\nВывод:\nБудет выведено то имя, которое введет пользователь', reply_markup=kb.inputstudy)



@router.callback_query(F.data == 'inputstudy')
async def inputstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('input() - от английского input - ввод. Функция input() принимает строковый тип данных.\nПример:\n```\nname = input("Введите имя: ")\nprint(name)\n```\nВывод:\nБудет выведено то имя, которое введет пользователь', reply_markup=kb.inputstudy)

@router.callback_query(F.data == 'backfrominputst')
async def bachfrinpst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('abs() - от английского absolute value  - абсолютное значение. Функция abs() возвращает число по модулю.\nПример:\n```\na = -5\nprint(abs(a))\n```\nВывод:\n5\n\nКак мы видим вывилось число -5 по модулю, то есть просто 5', reply_markup=kb.absstudy)

@router.callback_query(F.data == 'frominputtomenue')
async def finpttom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись назад в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'nextfrominputst')
async def nfinpst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('int(input()) - от английского integer - целое число. int(input( )) - принимает целочисленное значение.\nПример:\n```\na = int(input("Введите первое число: "))\nb = int(input("Введите второе число: "))\nprint(a + b)\n```\nВывод:\nБудет выведена сумма двух чисел, которые введет пользователь. На пример, если пользователь ввел 15 и 20, то , будет выведено 35', reply_markup=kb.intinputstudy)


@router.callback_query(F.data == 'intinputstudy')
async def intinputstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('int(input()) - от английского integer - целое число. int(input( )) - принимает целочисленное значение.\nПример:\n```\na = int(input("Введите первое число: "))\nb = int(input("Введите второе число: "))\nprint(a + b)\n```\nВывод:\nБудет выведена сумма двух чисел, которые введет пользователь. На пример, если пользователь ввел 15 и 20, то , будет выведено 35', reply_markup=kb.intinputstudy)

@router.callback_query(F.data == 'backfromintst')
async def backfromintst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('input() - от английского input - ввод. Функция input() принимает строковый тип данных.\nПример:\n```\nname = input("Введите имя: ")\nprint(name)\n```\nВывод:\nБудет выведено то имя, которое введет пользователь', reply_markup=kb.inputstudy)

@router.callback_query(F.data == 'frominttomenue')
async def frominttomenue(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)


@router.callback_query(F.data == 'nextfromintst')
async def nextfromintst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('float(input()) - от английского float - плавать. Функция float предназначена для ввода чисел с плавающей точкой.\nПример:\n```\nfirst = float(input("Введите первое число: "))\nmult = first*2\nprint(mult)\n```\nВывод:\nБыдет выведен результат умножения введенного числа с плавающей точкой на 2. На пример, если пользователь ввел 2.5, то будет выведено 5.0', reply_markup=kb.floatinputstudy)


@router.callback_query(F.data == 'floatinputstudy')
async def floatinst(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('float(input()) - от английского float - плавать. Функция float предназначена для ввода чисел с плавающей точкой.\nПример:\n```\nfirst = float(input("Введите первое число: "))\nmult = first*2\nprint(mult)\n```\nВывод:\nБыдет выведен результат умножения введенного числа с плавающей точкой на 2. На пример, если пользователь ввел 2.5, то будет выведено 5.0', reply_markup=kb.floatinputstudy)

@router.callback_query(F.data == 'backfromfloatst')
async def backffloatlst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('int(input()) - от английского integer - целое число. int(input( )) - принимает целочисленное значение.\nПример:\n```\na = int(input("Введите первое число: "))\nb = int(input("Введите второе число: "))\nprint(a + b)\n```\nВывод:\nБудет выведена сумма двух чисел, которые введет пользователь. На пример, если пользователь ввел 15 и 20, то , будет выведено 35', reply_markup=kb.intinputstudy)

@router.callback_query(F.data == 'fromfloattomenue')
async def fromfloattmenue(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'nextfromfloatst')
async def nextffloatst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('if - от английского if - если. Используется в условиях для проверки, является ли условие истинным или нет.\nПример:\n```\na = 5\nb = int(input("Введите число: "))\n\nif a == b:\n    print("Равны")\nif a > b:\n    print("Первое число больше")\nif a < b:\n    print("Второе число больше")\n```\nВывод:\nЕсли пользователь введет 5, то будет выведено Равны, если меньше, то Первое число больше, а если больше 5, то Второе число больше', reply_markup=kb.ifstudy)

@router.callback_query(F.data == 'ifstudy')
async def ifstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('if - от английского if - если. Используется в условиях для проверки, является ли условие истинным или нет.\nПример:\n```\na = 5\nb = int(input("Введите число: "))\n\nif a == b:\n    print("Равны")\nif a > b:\n    print("Первое число больше")\nif a < b:\n    print("Второе число больше")\n```\nВывод:\nЕсли пользователь введет 5, то будет выведено Равны, если меньше, то Первое число больше, а если больше 5, то Второе число больше', reply_markup=kb.ifstudy)

@router.callback_query(F.data == 'backfromifst')
async def backfromifst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('float(input()) - от английского float - плавать. Функция float предназначена для ввода чисел с плавающей точкой.\nПример:\n```\nfirst = float(input("Введите первое число: "))\nmult = first*2\nprint(mult)\n```\nВывод:\nБыдет выведен результат умножения введенного числа с плавающей точкой на 2. На пример, если пользователь ввел 2.5, то будет выведено 5.0', reply_markup=kb.floatinputstudy)

@router.callback_query(F.data == 'fromiftomenue')
async def fiftomenue(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)


@router.callback_query(F.data == 'nextfromifst')
async def nextfromifst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('elif - от английского сокращения else if (иначе если). Используется для проверки условия, если предыдущее не было истинным.\nПример:\n```\na = int(input("Введите первое число: "))\nb = int(input("Введите второе число: "))\nsumma = a + b\n\nif summa > 15:\n    print("Сумма больше 15")\nelif summa < 14:\n    print("Сумма меньше 14)"\n```\nВывод:\nЕсли сумма чисел (цифр) окажется больше 15, то программа выведет Сумма больше 15, если окажется меньше 14, то выведет Сумма меньше 14', reply_markup=kb.elifstudy)

@router.callback_query(F.data == 'elifstudy')
async def elifstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('elif - от английского сокращения else if (иначе если). Используется для проверки условия, если предыдущее не было истинным.\nПример:\n```\na = int(input("Введите первое число: "))\nb = int(input("Введите второе число: "))\nsumma = a + b\n\nif summa > 15:\n    print("Сумма больше 15")\nelif summa < 14:\n    print("Сумма меньше 14)"\n```\nВывод:\nЕсли сумма чисел (цифр) окажется больше 15, то программа выведет Сумма больше 15, если окажется меньше 14, то выведет Сумма меньше 14', reply_markup=kb.elifstudy)

@router.callback_query(F.data == 'backfromelifst')
async def backfromelst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('if - от английского if - если. Используется в условиях для проверки, является ли условие истинным или нет.\nПример:\n```\na = 5\nb = int(input("Введите число: "))\n\nif a == b:\n    print("Равны")\nif a > b:\n    print("Первое число больше")\nif a < b:\n    print("Второе число больше")\n```\nВывод:\nЕсли пользователь введет 5, то будет выведено Равны, если меньше, то Первое число больше, а если больше 5, то Второе число больше', reply_markup=kb.ifstudy)

@router.callback_query(F.data == 'fromeliftomenue')
async def fromeltome(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'nextfromelifst')
async def nextfelifst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('else - от английского else - иначе. Используется для проверки условия, если предыдущее (или предыдущие) условие не было истинным.\nПример:\n```\na = int(input("Введите первое число: "))\nb = float(input("Введите число с плавающей точкой: "))\n\nif a >=b:\n    print("Yes")\nelse:\n    print("No")\n```\nВывод:\nЕсли пользователь введет первое число больше или равное второму, то будет выведено Yes, иначе - No', reply_markup=kb.elsestudy)

@router.callback_query(F.data == 'backfromelsest')
async def backfelsest(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('elif - от английского сокращения else if (иначе если). Используется для проверки условия, если предыдущее не было истинным.\nПример:\n```\na = int(input("Введите первое число: "))\nb = int(input("Введите второе число: "))\nsumma = a + b\n\nif summa > 15:\n    print("Сумма больше 15")\nelif summa < 14:\n    print("Сумма меньше 14)"\n```\nВывод:\nЕсли сумма чисел (цифр) окажется больше 15, то программа выведет Сумма больше 15, если окажется меньше 14, то выведет Сумма меньше 14', reply_markup=kb.elifstudy)

@router.callback_query(F.data == 'elsestudy')
async def elsestudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('else - от английского else - иначе. Используется для проверки условия, если предыдущее (или предыдущие) условие не было истинным.\nПример:\n```\na = int(input("Введите первое число: "))\nb = float(input("Введите число с плавающей точкой: "))\n\nif a >=b:\n    print("Yes")\nelse:\n    print("No")\n```\nВывод:\nЕсли пользователь введет первое число больше или равное второму, то будет выведено Yes, иначе - No', reply_markup=kb.elsestudy)

@router.callback_query(F.data == 'fromelsetomenue')
async def fromelsetm(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'nextfromelsest')
async def nxtfelsest(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('and - от английского and - и. Имеет смысл логичского умножения. Может использоваться для проверки двух и более условий на истину.\nПример:\n```\nimport random\nfrom random import randint\n\na = random.randint(0, 100)\nb = int(input("Введите число: "))\n\nif a > 0 and b > 0:\n    print(a, ">", 0, "и", b, ">", 0)\nelse:\n    print("Одно или оба числа меньше 0")\n```\nВывод:\nТут мы импортировали библиотеку random, а затем из random импортировали модуль randint. Эта библиотека позоволяет генерировать случайные числа. По этому если случайно сгенерированное число и число, введеное пользователем, окажутся больше 0, то будет выведено, что случайно сгенерированное число > 0 и число, которое ввел пользователь > 0. Иначе будет выведено Одно или оба числа меньше 0', reply_markup=kb.andstudy)

@router.callback_query(F.data == 'backfromandst')
async def backfandst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('else - от английского else - иначе. Используется для проверки условия, если предыдущее (или предыдущие) условие не было истинным.\nПример:\n```\na = int(input("Введите первое число: "))\nb = float(input("Введите число с плавающей точкой: "))\n\nif a >=b:\n    print("Yes")\nelse:\n    print("No")\n```\nВывод:\nЕсли пользователь введет первое число больше или равное второму, то будет выведено Yes, иначе - No', reply_markup=kb.elsestudy)

@router.callback_query(F.data == 'fromandtomenue')
async def fandtom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'andstudy')
async def andstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('and - от английского and - и. Имеет смысл логичского умножения. Может использоваться для проверки двух и более условий на истину.\nПример:\n```\nimport random\nfrom random import randint\n\na = random.randint(0, 100)\nb = int(input("Введите число: "))\n\nif a > 0 and b > 0:\n    print(a, ">", 0, "и", b, ">", 0)\nelse:\n    print("Одно или оба числа меньше 0")\n```\nВывод:\nТут мы импортировали библиотеку random, а затем из random импортировали модуль randint. Эта библиотека позоволяет генерировать случайные числа. По этому если случайно сгенерированное число и число, введеное пользователем, окажутся больше 0, то будет выведено, что случайно сгенерированное число > 0 и число, которое ввел пользователь > 0. Иначе будет выведено Одно или оба числа меньше 0', reply_markup=kb.andstudy)

@router.callback_query(F.data == 'nextfromandst')
async def nextfandst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('or - от английского or - или. Используется для проверки одного из двух или более условий на истину.\nПример:\n```\na = input("Введите слово или предложение: ")\nlength = len(a)\n\nif length == 5 or length > 10:\n    print("Good")\nelse:\n    print("Bad")\n```\nВывод:\nЕсли пользователь введет слово или предложение, состоящее из 5 символов или больше 10 символов, то будет выведено Good, иначе Bad', reply_markup=kb.orstudy)

@router.callback_query(F.data == 'backfromorst')
async def backforst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('and - от английского and - и. Имеет смысл логичского умножения. Может использоваться для проверки двух и более условий на истину.\nПример:\n```\nimport random\nfrom random import randint\n\na = random.randint(0, 100)\nb = int(input("Введите число: "))\n\nif a > 0 and b > 0:\n    print(a, ">", 0, "и", b, ">", 0)\nelse:\n    print("Одно или оба числа меньше 0")\n```\nВывод:\nТут мы импортировали библиотеку random, а затем из random импортировали модуль randint. Эта библиотека позоволяет генерировать случайные числа. По этому если случайно сгенерированное число и число, введеное пользователем, окажутся больше 0, то будет выведено, что случайно сгенерированное число > 0 и число, которое ввел пользователь > 0. Иначе будет выведено Одно или оба числа меньше 0', reply_markup=kb.andstudy)

@router.callback_query(F.data == 'fromortomenue')
async def fortom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'orstudy')
async def orstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('or - от английского or - или. Используется для проверки одного из двух или более условий на истину.\nПример:\n```\na = input("Введите слово или предложение: ")\nlength = len(a)\n\nif length == 5 or length > 10:\n    print("Good")\nelse:\n    print("Bad")\n```\nВывод:\nЕсли пользователь введет слово или предложение, состоящее из 5 символов или больше 10 символов, то будет выведено Good, иначе Bad', reply_markup=kb.orstudy)


@router.callback_query(F.data == 'nextfromorst')
async def nextforst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('in - от английского in - в. Используется для проверки на на наличие элемента в списке, строке, словаре, кортеже, множестве.\nПример:\n```\nusers = ["Admin", "User", "Guest"]\nname = input("Введите имя: ")\n\nif name in users:\n    print("You are welcome!")\nelse:\n'   
'    print("Try again")\n```\nВывод:\nЕсли пользователь введет имя из списка (список называется users), то будет выведено You are welcome!, иначе - Try again', reply_markup=kb.instudy)

@router.callback_query(F.data == 'backfrominst')
async def backfinst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('or - от английского or - или. Используется для проверки одного из двух или более условий на истину.\nПример:\n```\na = input("Введите слово или предложение: ")\nlength = len(a)\n\nif length == 5 or length > 10:\n    print("Good")\nelse:\n    print("Bad")\n```\nВывод:\nЕсли пользователь введет слово или предложение, состоящее из 5 символов или больше 10 символов, то будет выведено Good, иначе Bad', reply_markup=kb.orstudy)

@router.callback_query(F.data == 'fromintomenue')
async def fintom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'instudy')
async def instudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('in - от английского in - в. Используется для проверки на на наличие элемента в списке, строке, словаре, кортеже, множестве.\nПример:\n```\nusers = ["Admin", "User", "Guest"]\nname = input("Введите имя: ")\n\nif name in users:\n    print("You are welcome!")\nelse:\n'   
                                  '    print("Try again")\n```\nВывод:\nЕсли пользователь введет имя из списка (список называется users), то будет выведено You are welcome!, иначе - Try again', reply_markup=kb.instudy)

@router.callback_query(F.data == 'nextfrominst')
async def nextfinst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('not - от английского not - не. Используется в качестве логического отрицания. Может использоваться для проверки списка на отсутсвие элемента.\nПример:\n```\nlist = [1, 2, 3, 4, 5]\ndigit = int(input("Введите число/цифру: "))\n\nif digit not in list:\n    print("Увы")\nelse:\n    print("Вы угадали!")\n```\nВывод:\nЕсли введенная цифра пользователем не окажется в списке, то будет выведено Увы, иначе - Вы угадали!', reply_markup=kb.notstudy)

@router.callback_query(F.data == 'backfromnotst')
async def backfnotst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('in - от английского in - в. Используется для проверки на на наличие элемента в списке, строке, словаре, кортеже, множестве.\nПример:\n```\nusers = ["Admin", "User", "Guest"]\nname = input("Введите имя: ")\n\nif name in users:\n    print("You are welcome!")\nelse:\n'   
                                  '    print("Try again")\n```\nВывод:\nЕсли пользователь введет имя из списка (список называется users), то будет выведено You are welcome!, иначе - Try again', reply_markup=kb.instudy)

@router.callback_query(F.data == 'fromnottomenue')
async def fnotom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'notstudy')
async def notstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('not - от английского not - не. Используется в качестве логического отрицания. Может использоваться для проверки списка на отсутсвие элемента.\nПример:\n```\nlist = [1, 2, 3, 4, 5]\ndigit = int(input("Введите число/цифру: "))\n\nif digit not in list:\n    print("Увы")\nelse:\n    print("Вы угадали!")\n```\nВывод:\nЕсли введенная цифра пользователем не окажется в списке, то будет выведено Увы, иначе - Вы угадали!', reply_markup=kb.notstudy)

@router.callback_query(F.data == 'nextfromnotst')
async def nextfnotst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('try - от английского try - пробовать. try используется вместе с except, но про это чуть позже. В блок try помещается код, который может вызвать ошибку.\nПример:\n```\ntry:\n    name = input("Введите имя: ")\n    password = int(input("Введите пароль: "))\nexcept:\n    print("Имя может содеражать только буквы, а пароль только цифры")\n    print("Попробуйте еще раз")\n    name = input("Введите имя:")\n    password = int(input("Введите пароль: "))\nprint("Добро пожаловать!")\n```\nВывод:\nЕсли пользователь в пароле укажет букву (буквы), то программа попросит ввести имя и пароль еще раз. После правильного ввода будет выведено на экран Добро пожаловать', reply_markup=kb.trystudy)

@router.callback_query(F.data == 'backfromtryst')
async def backftryst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('not - от английского not - не. Используется в качестве логического отрицания. Может использоваться для проверки списка на отсутсвие элемента.\nПример:\n```\nlist = [1, 2, 3, 4, 5]\ndigit = int(input("Введите число/цифру: "))\n\nif digit not in list:\n    print("Увы")\nelse:\n    print("Вы угадали!")\n```\nВывод:\nЕсли введенная цифра пользователем не окажется в списке, то будет выведено Увы, иначе - Вы угадали!', reply_markup=kb.notstudy)

@router.callback_query(F.data == 'fromtrytomenue')
async def fromttom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'trystudy')
async def trystudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('try - от английского try - пробовать. try используется вместе с except, но про это чуть позже. В блок try помещается код, который может вызвать ошибку.\nПример:\n```\ntry:\n    name = input("Введите имя: ")\n    password = int(input("Введите пароль: "))\nexcept:\n    print("Имя может содеражать только буквы, а пароль только цифры")\n    print("Попробуйте еще раз")\n    name = input("Введите имя:")\n    password = int(input("Введите пароль: "))\nprint("Добро пожаловать!")\n```\nВывод:\nЕсли пользователь в пароле укажет букву (буквы), то программа попросит ввести имя и пароль еще раз. После правильного ввода будет выведено на экран Добро пожаловать', reply_markup=kb.trystudy)

@router.callback_query(F.data == 'nextfromtryst')
async def nextftst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('except - от английского except - исключение (кроме). Используется вместе с try. В блок except помещается код, который будет выполнять какие-либо действия в случае ошибки в блоке try.\nПример:\n```\nimport random\nfrom random import randint\n\ntry:\n    a = int(input("Введите число: "))\n    b = random.randint(0, 100)\n    print(a, "/", b, "=", a/b)\nexcept:\n    print("Нельзя делить на 0")\n    a = int(input("Введите число: "))\n    b = random.randint(0, 100)\n    print(a, "/", b, "=", a/b)\n```\nВывод:\nПользователь вводит число, затем программа генерирует случайное число от 0 до 100, а затем делит на него число пользователя. Если случайно сгенерированным числом окажется 0, то будет выведено На 0 делить нельзя и нужно будет еще раз ввести число, а если польше нуля, то выведет оба числа и результат их деления', reply_markup=kb.exceptstudy)

@router.callback_query(F.data == 'backfromexst')
async def backfexc(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('try - от английского try - пробовать. try используется вместе с except, но про это чуть позже. В блок try помещается код, который может вызвать ошибку.\nПример:\n```\ntry:\n    name = input("Введите имя: ")\n    password = int(input("Введите пароль: "))\nexcept:\n    print("Имя может содеражать только буквы, а пароль только цифры")\n    print("Попробуйте еще раз")\n    name = input("Введите имя:")\n    password = int(input("Введите пароль: "))\nprint("Добро пожаловать!")\n```\nВывод:\nЕсли пользователь в пароле укажет букву (буквы), то программа попросит ввести имя и пароль еще раз. После правильного ввода будет выведено на экран Добро пожаловать', reply_markup=kb.trystudy)

@router.callback_query(F.data == 'fromextomenue')
async def fexctom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'exceptstudy')
async def exceptstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('except - от английского except - исключение (кроме). Используется вместе с try. В блок except помещается код, который будет выполнять какие-либо действия в случае ошибки в блоке try.\nПример:\n```\nimport random\nfrom random import randint\n\ntry:\n    a = int(input("Введите число: "))\n    b = random.randint(0, 100)\n    print(a, "/", b, "=", a/b)\nexcept:\n    print("Нельзя делить на 0")\n    a = int(input("Введите число: "))\n    b = random.randint(0, 100)\n    print(a, "/", b, "=", a/b)\n```\nВывод:\nПользователь вводит число, затем программа генерирует случайное число от 0 до 100, а затем делит на него число пользователя. Если случайно сгенерированным числом окажется 0, то будет выведено На 0 делить нельзя и нужно будет еще раз ввести число, а если польше нуля, то выведет оба числа и результат их деления', reply_markup=kb.exceptstudy)


@router.callback_query(F.data == 'nextfromexst')
async def nextfexc(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('finally - от английского finally - окончательно. Используется вместе с try и except. Используется для того, чтобы код выполнился в любом случае, не смотря на ошибки. То есть та часть кода, которая указана в блоке finally будет выполнена в любом случае.\nПример:\n```\ntry:\n    print("У нас есть число 10. На что будем делить?")\n    a = int(input("Введите число: "))\n    print(10, "/", a, "=", 10/a)\nexcept ZeroDivisionError:\n    print("На 0 делить нельзя")\nfinally:\n    print("Спасибо за использование программы!")\n```\nВывод:\nПользователю нужно ввести число, на которое программа будет делить число 10. Если пользователь вводит число больше нуля, то ему показывает результат деления и фразу Спасибо за использование программы! А если пользователь вводит 0, то будет выводиться, что на 0 делить нельзя (После except можно указывать тип ошибки, как это сделал я. Ошибка ZeroDivisionError возникает, если делить на 0. Просто если не указывать тип ошибки, то при любой другой ошибке будет показывть, что нельзя делить на 0), а так же фраза Спасибо за использование программы!', reply_markup=kb.finallystudy)

@router.callback_query(F.data == 'backfromffinst')
async def bfromffinst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('except - от английского except - исключение (кроме). Используется вместе с try. В блок except помещается код, который будет выполнять какие-либо действия в случае ошибки в блоке try.\nПример:\n```\nimport random\nfrom random import randint\n\ntry:\n    a = int(input("Введите число: "))\n    b = random.randint(0, 100)\n    print(a, "/", b, "=", a/b)\nexcept:\n    print("Нельзя делить на 0")\n    a = int(input("Введите число: "))\n    b = random.randint(0, 100)\n    print(a, "/", b, "=", a/b)\n```\nВывод:\nПользователь вводит число, затем программа генерирует случайное число от 0 до 100, а затем делит на него число пользователя. Если случайно сгенерированным числом окажется 0, то будет выведено На 0 делить нельзя и нужно будет еще раз ввести число, а если польше нуля, то выведет оба числа и результат их деления', reply_markup=kb.exceptstudy)

@router.callback_query(F.data == 'fromffintomenue')
async def fromfftm(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'finallystudy')
async def finallystudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('finally - от английского finally - окончательно. Используется вместе с try и except. Используется для того, чтобы код выполнился в любом случае, не смотря на ошибки. То есть та часть кода, которая указана в блоке finally будет выполнена в любом случае.\nПример:\n```\ntry:\n    print("У нас есть число 10. На что будем делить?")\n    a = int(input("Введите число: "))\n    print(10, "/", a, "=", 10/a)\nexcept ZeroDivisionError:\n    print("На 0 делить нельзя")\nfinally:\n    print("Спасибо за использование программы!")\n```\nВывод:\nПользователю нужно ввести число, на которое программа будет делить число 10. Если пользователь вводит число больше нуля, то ему показывает результат деления и фразу Спасибо за использование программы! А если пользователь вводит 0, то будет выводиться, что на 0 делить нельзя (После except можно указывать тип ошибки, как это сделал я. Ошибка ZeroDivisionError возникает, если делить на 0. Просто если не указывать тип ошибки, то при любой другой ошибке будет показывть, что нельзя делить на 0), а так же фраза Спасибо за использование программы!', reply_markup=kb.finallystudy)

@router.callback_query(F.data == 'nextfromffinst')
async def nextfrfinst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('def - от английйского define - определять. Используется для определения (создания) функций. У функции есть свое название, а так же она может принимать параметры.Так же функцию можно вызывать.\nПример:\n```\ndef proger(x):\n    print(x)\nproger("I")\nproger("Love")\nproger("programming")\n```\nВывод:\nI\nLove\nProgramming\n\nМы назвали функцию proger, и наша функция принимает некий параметр x. Внутри функции мы вывели на экран переменную x. А затем вызвали функцию, но уже в скобках написали не x, а то, чему равен x. Каждый раз, когда мы вызывали функцию, мы меняли этот параметр x', reply_markup=kb.defstudy)

@router.callback_query(F.data == 'backfromdefst')
async def backfdefst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('finally - от английского finally - окончательно. Используется вместе с try и except. Используется для того, чтобы код выполнился в любом случае, не смотря на ошибки. То есть та часть кода, которая указана в блоке finally будет выполнена в любом случае.\nПример:\n```\ntry:\n    print("У нас есть число 10. На что будем делить?")\n    a = int(input("Введите число: "))\n    print(10, "/", a, "=", 10/a)\nexcept ZeroDivisionError:\n    print("На 0 делить нельзя")\nfinally:\n    print("Спасибо за использование программы!")\n```\nВывод:\nПользователю нужно ввести число, на которое программа будет делить число 10. Если пользователь вводит число больше нуля, то ему показывает результат деления и фразу Спасибо за использование программы! А если пользователь вводит 0, то будет выводиться, что на 0 делить нельзя (После except можно указывать тип ошибки, как это сделал я. Ошибка ZeroDivisionError возникает, если делить на 0. Просто если не указывать тип ошибки, то при любой другой ошибке будет показывть, что нельзя делить на 0), а так же фраза Спасибо за использование программы!', reply_markup=kb.finallystudy)

@router.callback_query(F.data == 'fromdeftomenue')
async def fromdeftm(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'defstudy')
async def defstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('def - от английйского define - определять. Используется для определения (создания) функций. У функции есть свое название, а так же она может принимать параметры.Так же функцию можно вызывать.\nПример:\n```\ndef proger(x):\n    print(x)\nproger("I")\nproger("Love")\nproger("programming")\n```\nВывод:\nI\nLove\nProgramming\n\nМы назвали функцию proger, и наша функция принимает некий параметр x. Внутри функции мы вывели на экран переменную x. А затем вызвали функцию, но уже в скобках написали не x, а то, чему равен x. Каждый раз, когда мы вызывали функцию, мы меняли этот параметр x', reply_markup=kb.defstudy)

@router.callback_query(F.data == 'nextfromdefst')
async def nextfrdefst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('return - от английского return - возвращать. Используется в функции (def) для возвращения значения из функции, с которым потом можно работать вне функции. А так же return может выполнять выход из функции.\nПример:\n```\ndef summa(x):\n    return x+x\nres = summa(10)\nprint(res)\n```\nВывод:\n20\n\nНаша функция summa() принимает некий параметр x, а затем мы возвращаем из этой функции x+x => теперь мы можем рабоатать со сложением этих иксов вне функции. Далее мы записали нашу функцию в переменную res, но вмето x мы написали чему он будет равен (В нашем случае 10). На следующей строке мы вывели переменную res на экран. (Вывелось 20, так как 10+10=20)', reply_markup=kb.returnstudy)

@router.callback_query(F.data == 'backfromretst')
async def backfretst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('def - от английйского define - определять. Используется для определения (создания) функций. У функции есть свое название, а так же она может принимать параметры.Так же функцию можно вызывать.\nПример:\n```\ndef proger(x):\n    print(x)\nproger("I")\nproger("Love")\nproger("programming")\n```\nВывод:\nI\nLove\nProgramming\n\nМы назвали функцию proger, и наша функция принимает некий параметр x. Внутри функции мы вывели на экран переменную x. А затем вызвали функцию, но уже в скобках написали не x, а то, чему равен x. Каждый раз, когда мы вызывали функцию, мы меняли этот параметр x', reply_markup=kb.defstudy)

@router.callback_query(F.data == 'fromrettomenue')
async def fromrettm(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'returnstudy')
async def returnstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('return - от английского return - возвращать. Используется в функции (def) для возвращения значения из функции, с которым потом можно работать вне функции. А так же return может выполнять выход из функции.\nПример:\n```\ndef summa(x):\n    return x+x\nres = summa(10)\nprint(res)\n```\nВывод:\n20\n\nНаша функция summa() принимает некий параметр x, а затем мы возвращаем из этой функции x+x => теперь мы можем рабоатать со сложением этих иксов вне функции. Далее мы записали нашу функцию в переменную res, но вмето x мы написали чему он будет равен (В нашем случае 10). На следующей строке мы вывели переменную res на экран. (Вывелось 20, так как 10+10=20)', reply_markup=kb.returnstudy)

@router.callback_query(F.data == 'nextfromretst')
async def nextfretst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('class - от английского class - класс. С помощью класса можно описывать однотипные объекты. Так же есть понятие родительский класс и дочерний класс, на пример: птица - это родительский класс, так как это общее понятие, а вот воробей - это дочерний класс, так как это вид птицы.\nПример:\n```\nclass Bird:\n    plumage = True\n    beak = True\n    wings = True\n\nclass Sparrow(Bird):\n    size = "small"\n\nbella = Sparrow()\nrichard = Sparrow()\nrichard.size = "medium"\nprint(bella.size)\nprint(richard.size)\n```\nВывод:\nsmall\nmedium\n\nМы создали родительский класс Bird и записали в него основные характеристики. Затем мы создали дочерний класс Sparrow и в скобках указали, что он относится к классу Bird. В классе Sparrow мы указали размер птицы. Потом создали переменные (имена птиц) и отнесли их к классу Sparrow. Затем мы поменяли размер Ричарда, а потом вывели на экран размер Беллы (small) и размер Ричарда (medium)', 
reply_markup=kb.classstudy)

@router.callback_query(F.data == 'backfromclsst')
async def backfclsst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('return - от английского return - возвращать. Используется в функции (def) для возвращения значения из функции, с которым потом можно работать вне функции. А так же return может выполнять выход из функции.\nПример:\n```\ndef summa(x):\n    return x+x\nres = summa(10)\nprint(res)\n```\nВывод:\n20\n\nНаша функция summa() принимает некий параметр x, а затем мы возвращаем из этой функции x+x => теперь мы можем рабоатать со сложением этих иксов вне функции. Далее мы записали нашу функцию в переменную res, но вмето x мы написали чему он будет равен (В нашем случае 10). На следующей строке мы вывели переменную res на экран. (Вывелось 20, так как 10+10=20)', reply_markup=kb.returnstudy)

@router.callback_query(F.data == 'fromclstomenue')
async def fromclstm(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'classstudy')
async def classstudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('class - от английского class - класс. С помощью класса можно описывать однотипные объекты. Так же есть понятие родительский класс и дочерний класс, на пример: птица - это родительский класс, так как это общее понятие, а вот воробей - это дочерний класс, так как это вид птицы.\nПример:\n```\nclass Bird:\n    plumage = True\n    beak = True\n    wings = True\n\nclass Sparrow(Bird):\n    size = "small"\n\nbella = Sparrow()\nrichard = Sparrow()\nrichard.size = "medium"\nprint(bella.size)\nprint(richard.size)\n```\nВывод:\nsmall\nmedium\n\nМы создали родительский класс Bird и записали в него основные характеристики. Затем мы создали дочерний класс Sparrow и в скобках указали, что он относится к классу Bird. В классе Sparrow мы указали размер птицы. Потом создали переменные (имена птиц) и отнесли их к классу Sparrow. Затем мы поменяли размер Ричарда, а потом вывели на экран размер Беллы (small) и размер Ричарда (medium)',
reply_markup=kb.classstudy)

@router.callback_query(F.data == 'nextfromclsst')
async def nextfclsst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('while - от английского while - пока. while спользуется для написания циклов: пока какое-то условие не истина (или истина) будет выполняться следующее.\nПример:\n```\nlist = [1, 2, 3, 4, 5]\na = int(input("Введите число: "))\nif a not in list:\n____while a not in list:\n________print("Попробуйте еще раз")\n________a = int(input("Введите число: "))\n________if a in list:\n____________print("Добро пожаловать!")\nelse:\n____print("Добро пожаловать!")\n```\nВывод:\nПользователю предлагается ввести число и если его нет в списке list, то будет выполнятся цикл while: пока введенное число пользователем не будет в спике, будет выводиться Попробуйте еще раз и программа будет предлагать ввести число еще раз. Как только пользователь введет число, котрое есть в списке программа выведет Добро пожаловать. А если пользователь сразу ввел число, которое есть в списке, то программа покажет Добро пожаловать!\nP.s не обращайте внимания на нижние подчеркивания, просто Python не дает делать большие отступы', reply_markup=kb.whilestudy)

@router.callback_query(F.data == 'backfromwlst')
async def backfwlst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('class - от английского class - класс. С помощью класса можно описывать однотипные объекты. Так же есть понятие родительский класс и дочерний класс, на пример: птица - это родительский класс, так как это общее понятие, а вот воробей - это дочерний класс, так как это вид птицы.\nПример:\n```\nclass Bird:\n    plumage = True\n    beak = True\n    wings = True\n\nclass Sparrow(Bird):\n    size = "small"\n\nbella = Sparrow()\nrichard = Sparrow()\nrichard.size = "medium"\nprint(bella.size)\nprint(richard.size)\n```\nВывод:\nsmall\nmedium\n\nМы создали родительский класс Bird и записали в него основные характеристики. Затем мы создали дочерний класс Sparrow и в скобках указали, что он относится к классу Bird. В классе Sparrow мы указали размер птицы. Потом создали переменные (имена птиц) и отнесли их к классу Sparrow. Затем мы поменяли размер Ричарда, а потом вывели на экран размер Беллы (small) и размер Ричарда (medium)',
reply_markup=kb.classstudy)

@router.callback_query(F.data == 'fromwltomenue')
async def fwltom(callback: CallbackQuery):
  await callback.answer()
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'whilestudy')
async def whilestudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('while - от английского while - пока. while спользуется для написания циклов: пока какое-то условие не истина (или истина) будет выполняться следующее.\nПример:\n```\nlist = [1, 2, 3, 4, 5]\na = int(input("Введите число: "))\nif a not in list:\n____while a not in list:\n________print("Попробуйте еще раз")\n________a = int(input("Введите число: "))\n________if a in list:\n____________print("Добро пожаловать!")\nelse:\n____print("Добро пожаловать!")\n```\nВывод:\nПользователю предлагается ввести число и если его нет в списке list, то будет выполнятся цикл while: пока введенное число пользователем не будет в спике, будет выводиться Попробуйте еще раз и программа будет предлагать ввести число еще раз. Как только пользователь введет число, котрое есть в списке программа выведет Добро пожаловать. А если пользователь сразу ввел число, которое есть в списке, то программа покажет Добро пожаловать!\nP.s не обращайте внимания на нижние подчеркивания, просто Python не дает делать большие отступы', reply_markup=kb.whilestudy)

@router.callback_query(F.data == 'nextfromwlst')
async def nextfwlst(callback: CallbackQuery):
  await callback.answer('Вы перешли дальше')
  await callback.message.edit_text('for - от английского for - для. i - некая переменная. in - от английского in - в. range - от английского range - диапазон. Цикл for i in range() используется для повторения цикла, некоторое заданное число раз.\nКак может использоваться цикл:\nfor i in range(до скольки ему надо считать)\nfor i in range(от скольки и до скольки считать)\nfor i in range(от скольки, до скольки, с каким шагом)\n\nЭтот цикл, если в скобках указать до скольки считаь, будет считать на единицу меньше, на пример вы указали 10, а он будет счиать до  9. А так же, если указывать только до скольки циклу считать, цикл будет начинать счет от 0.\nПример:\n```\na = int(input("До скольки будем счиать: "))\nfor i in range(a+1):\n    print(i)\n```\nВывод:\nЕсли пользователь введет число 7, то программа будет считать от 0 до 7, так как в диапазоне a+1, это значит, что если бы программа считала в диапазоне a, то она считала бы до 6, а по скольку a+1, то до 7 (6+1=7)', reply_markup=kb.cyclerangestudy)

@router.callback_query(F.data == 'backfromrgst')
async def bfrgst(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('while - от английского while - пока. while спользуется для написания циклов: пока какое-то условие не истина (или истина) будет выполняться следующее.\nПример:\n```\nlist = [1, 2, 3, 4, 5]\na = int(input("Введите число: "))\nif a not in list:\n____while a not in list:\n________print("Попробуйте еще раз")\n________a = int(input("Введите число: "))\n________if a in list:\n____________print("Добро пожаловать!")\nelse:\n____print("Добро пожаловать!")\n```\nВывод:\nПользователю предлагается ввести число и если его нет в списке list, то будет выполнятся цикл while: пока введенное число пользователем не будет в спике, будет выводиться Попробуйте еще раз и программа будет предлагать ввести число еще раз. Как только пользователь введет число, котрое есть в списке программа выведет Добро пожаловать. А если пользователь сразу ввел число, которое есть в списке, то программа покажет Добро пожаловать!\nP.s не обращайте внимания на нижние подчеркивания, просто Python не дает делать большие отступы', reply_markup=kb.whilestudy)

@router.callback_query(F.data == 'fromrgtomenue')
async def frgtom(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы вернулись в меню обучения: ', reply_markup=kb.study)

@router.callback_query(F.data == 'cyclerangestudy')
async def cyclerangestudy(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('for - от английского for - для. i - некая переменная. in - от английского in - в. range - от английского range - диапазон. Цикл for i in range() используется для повторения цикла, некоторое заданное число раз.\nКак может использоваться цикл:\nfor i in range(до скольки ему надо считать)\nfor i in range(от скольки и до скольки считать)\nfor i in range(от скольки, до скольки, с каким шагом)\n\nЭтот цикл, если в скобках указать до скольки считаь, будет считать на единицу меньше, на пример вы указали 10, а он будет счиать до  9. А так же, если указывать только до скольки циклу считать, цикл будет начинать счет от 0.\nПример:\n```\na = int(input("До скольки будем счиать: "))\nfor i in range(a+1):\n    print(i)\n```\nВывод:\nЕсли пользователь введет число 7, то программа будет считать от 0 до 7, так как в диапазоне a+1, это значит, что если бы программа считала в диапазоне a, то она считала бы до 6, а по скольку a+1, то до 7 (6+1=7)', reply_markup=kb.cyclerangestudy)


@router.callback_query(F.data == 'practice')
async def practice(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Вы выбрали практику: ', reply_markup=kb.practice)

@router.callback_query(F.data == 'backpractice')
async def backpractice(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('Вы вернулись в главное меню: ', reply_markup=kb.main)

@router.callback_query(F.data == 'starttest')
async def starttest(callback: CallbackQuery):
  await callback.answer('Вы начали тест')
  await callback.message.edit_text('Вопрос 1:\nКак переводится string?', reply_markup=kb.question1)

@router.callback_query(F.data == 'stoptest1')
async def stoptest1(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)

@router.callback_query(F.data == 'stringpr1')
async def name(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 2:\nЧто выведет на экран эта программа:\n\nname = "Richard"\nprint(type(name))', reply_markup=kb.question2)

@router.callback_query(F.data == 'numberpr1')
async def numberpr1(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - строка.\nВопрос 2:\nЧто выведет на экран эта программа:\n\nname = "Richard"\nprint(type(name))', reply_markup=kb.question2)

@router.callback_query(F.data == 'listpr1')
async def listpr1(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - строка.\nВопрос 2:\nЧто выведет на экран эта программа:\n\nname = "Richard"\nprint(type(name))', reply_markup=kb.question2)

@router.callback_query(F.data == 'tuplepr1')
async def tuplepr1(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - строка.\nВопрос 2:\nЧто выведет на экран эта программа:\n\nname = "Richard"\nprint(type(name))', reply_markup=kb.question2)

@router.callback_query(F.data == 'stoptest2')
async def stoptest2(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)


@router.callback_query(F.data == 'strpr2')
async def strpr2(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 3:\nЧто делает abs()', reply_markup=kb.question3)

@router.callback_query(F.data == 'intpr2')
async def intpr2(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Программа выведет <class "str">\nВопрос 3:\nЧто делает abs()', reply_markup=kb.question3)

@router.callback_query(F.data == 'floatpr2')
async def floatpr2(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Программа выведет <class "str">\nВопрос 3:\nЧто делает abs()', reply_markup=kb.question3)

@router.callback_query(F.data == 'listpr2')
async def listpr2(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Программа выведет <class "str">\nВопрос 3:\nЧто делает abs()', reply_markup=kb.question3)

@router.callback_query(F.data == 'stoptest3')
async def stoptest3(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)

@router.callback_query(F.data == 'module3')
async def module3(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 4:\nКакая функция принимает целые числа:', reply_markup=kb.question4)

@router.callback_query(F.data == 'koren3')
async def koren3(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Выводит модуль числа.\nВопрос 4:\nКакая функция принимает целые числа:', reply_markup=kb.question4)

@router.callback_query(F.data == 'delit3')
async def delit3(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Выводит модуль числа.\nВопрос 4:\nКакая функция принимает целые числа:', reply_markup=kb.question4)

@router.callback_query(F.data == 'rasr3')
async def rasr3(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Выводит модуль числа.\nВопрос 4:\nКакая функция принимает целые числа:', reply_markup=kb.question4)


@router.callback_query(F.data == 'stoptest4')
async def stoptest4(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)

@router.callback_query(F.data == 'int4')
async def int4(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 5:\nЧто выведет на экран эта программа:\n\ndef mult(x, y)\n    return x*y\n\nres = milt(5, 7)\nprint(res)', reply_markup=kb.question5)

@router.callback_query(F.data == 'float4')
async def float4(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - int(input())\nВопрос 5:\nЧто выведет на экран эта программа:\n\ndef mult(x, y)\n    return x*y\n\nres = milt(5, 7)\nprint(res)', reply_markup=kb.question5)


@router.callback_query(F.data == 'stoptest5')
async def stoptest5(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)

@router.callback_query(F.data == 'q35pr5')
async def q35pr5(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 6:\nЧто выведет на экран эта программа:\n\na = "Hello"\nb = len(a)\nif (b >= 5 and b < 10) or b == 7:\n    print("Good")\nelse:\n    print("Bad")', reply_markup=kb.question6)

@router.callback_query(F.data == 'nothing5')
async def nothing5(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - 35.\nВопрос 6:\nЧто выведет на экран эта программа:\n\na = "Hello"\nb = len(a)\nif (b >= 5 and b < 10) or b == 7:\n    print("Good")\nelse:\n    print("Bad")', reply_markup=kb.question6)

@router.callback_query(F.data == 'q12pr5')
async def q12pr5(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - 35.\nВопрос 6:\nЧто выведет на экран эта программа:\n\na = "Hello"\nb = len(a)\nif (b >= 5 and b < 10) or b == 7:\n    print("Good")\nelse:\n    print("Bad")', reply_markup=kb.question6)

@router.callback_query(F.data == 'res5')
async def res5(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - 35.\nВопрос 6:\nЧто выведет на экран эта программа:\n\na = "Hello"\nb = len(a)\nif (b >= 5 and b < 10) or b == 7:\n    print("Good")\nelse:\n    print("Bad")', reply_markup=kb.question6)


@router.callback_query(F.data == 'stoptest6')
async def stoptest6(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)

@router.callback_query(F.data == 'bad6')
async def bad6(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Good.\nВопрос 7:\nЧто обязательно используется вместе с try:', reply_markup=kb.question7)

@router.callback_query(F.data == 'good6')
async def good6(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 7:\nЧто обязательно используется вместе с try:', reply_markup=kb.question7)


@router.callback_query(F.data == 'except7')
async def except7(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 8:\nКак переводится while:', reply_markup=kb.question8)

@router.callback_query(F.data == 'def7')
async def def7(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - except.\nВопрос 8:\nКак переводится while:', reply_markup=kb.question8)

@router.callback_query(F.data == 'while7')
async def while7(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - except.\nВопрос 8:\nКак переводится while:', reply_markup=kb.question8)

@router.callback_query(F.data == 'or7')
async def or7(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - except.\nВопрос 8:\nКак переводится while:', reply_markup=kb.question8)

@router.callback_query(F.data == 'stoptest7')
async def stoptest7(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)


@router.callback_query(F.data == 'while8')
async def while8(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 9:\nКак переводится class:', reply_markup=kb.question9)

@router.callback_query(F.data == 'in8')
async def in8(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Пока.\nВопрос 9:\nКак переводится class:', reply_markup=kb.question9)

@router.callback_query(F.data == 'define8')
async def define8(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Пока.\nВопрос 9:\nКак переводится class:', reply_markup=kb.question9)

@router.callback_query(F.data == 'return8')
async def return8(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Пока.\nВопрос 9:\nКак переводится class:', reply_markup=kb.question9)

@router.callback_query(F.data == 'stoptest8')
async def stoptest8(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)


@router.callback_query(F.data == 'class9')
async def class9(callback: CallbackQuery):
  await callback.answer('Верно!')
  await callback.message.edit_text('Вы ответили верно!\nВопрос 10:\nВам понравился тест?', reply_markup=kb.question10)

@router.callback_query(F.data == 'object9')
async def object9(callback: CallbackQuery):
  await callback.answer('Неверно')
  await callback.message.edit_text('Вы ответили неверно. Правильный ответ - Класс.\nВопрос 10\nВам понравился тест?', reply_markup=kb.question10)

@router.callback_query(F.data == 'stoptest9')
async def stoptest9(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)


@router.callback_query(F.data == 'yes10')
async def yes10(callback: CallbackQuery):
  await callback.answer('Спасибо!')
  await callback.message.edit_text('Спасибо за прохождение теста! Я рад, что вам понравилось. Если у вас есть идеи, как можно доработать бот, перейдите в главном меню в раздел контакты и предложите свою идею', reply_markup=kb.finishtest)

@router.callback_query(F.data == 'no10')
async def no10(callback: CallbackQuery):
  await callback.answer('Будем стараться')
  await callback.message.edit_text('Спасибо за прохождение теста! Очень жаль, что он вам не понравился. Если у вас есть идеи, как можно доработать бот, перейдите в главном меню в раздел контакты и предложите свою идею', reply_markup=kb.finishtest)


@router.callback_query(F.data == 'stoptest10')
async def stoptest10(callback: CallbackQuery):
  await callback.answer('Завершение теста')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)

@router.callback_query(F.data == 'finish')
async def finish(callback: CallbackQuery):
  await callback.answer('Выход в меню')
  await callback.message.edit_text('Вы заврешили тест', reply_markup=kb.practice)


@router.callback_query(F.data == 'contacts')
async def contacts(callback: CallbackQuery):
  await callback.answer('')
  await callback.message.edit_text('Контакты:\nБот обратной связи - @Td_FeedbacKKbot', reply_markup=kb.contactsk)

@router.callback_query(F.data == 'backcontacts')
async def backcontacts(callback: CallbackQuery):
  await callback.answer('Вы вернулись назад')
  await callback.message.edit_text('Вы вернулись в главное меню: ', reply_markup=kb.main)

