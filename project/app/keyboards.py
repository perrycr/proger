from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='Обучение', callback_data='study'), InlineKeyboardButton(text='Практика', callback_data='practice')],
[InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

study = InlineKeyboardMarkup(inline_keyboard= [
[InlineKeyboardButton(text='str()', callback_data='strstudy'), InlineKeyboardButton(text='abs()', callback_data='absstudy')],
[InlineKeyboardButton(text='input()', callback_data='inputstudy'), InlineKeyboardButton(text='int(input())', callback_data='intinputstudy')],
[InlineKeyboardButton(text='float(input())', callback_data='floatinputstudy'), InlineKeyboardButton(text='if', callback_data='ifstudy')],
[InlineKeyboardButton(text='elif', callback_data='elifstudy'), InlineKeyboardButton(text='else', callback_data='elsestudy')],
[InlineKeyboardButton(text='and', callback_data='andstudy'),
InlineKeyboardButton(text='or', callback_data='orstudy')],
[InlineKeyboardButton(text='in', callback_data='instudy'), InlineKeyboardButton(text='not', callback_data='notstudy')],
[InlineKeyboardButton(text='try', callback_data='trystudy'), InlineKeyboardButton(text='except', callback_data='exceptstudy')],
[InlineKeyboardButton(text='return', callback_data='returnstudy'), InlineKeyboardButton(text='finally', callback_data='finallystudy')],
[InlineKeyboardButton(text='def', callback_data='defstudy'), InlineKeyboardButton(text='class', callback_data='classstudy')],
[InlineKeyboardButton(text='while', callback_data='whilestudy'), InlineKeyboardButton(text='for i in range()', callback_data='cyclerangestudy')],
    [InlineKeyboardButton(text='Назад', callback_data='backstudy')],
    
])

strstudy = InlineKeyboardMarkup(inline_keyboard= [
[InlineKeyboardButton(text='В меню', callback_data='backstrstudy'), InlineKeyboardButton(text='Дальше', callback_data='fromstrstudy')]
])

absstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromabs'),
    InlineKeyboardButton(text='Дальше', callback_data='nextfromabs')],
    [InlineKeyboardButton(text='В меню', callback_data='fromabstomenue')]
])

inputstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfrominputst'),
    InlineKeyboardButton(text='Дальше', callback_data='nextfrominputst')],
    [InlineKeyboardButton(text='В меню', callback_data='frominputtomenue')]
])

intinputstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromintst'),
    InlineKeyboardButton(text='Дальше', callback_data='nextfromintst')],
    [InlineKeyboardButton(text='В меню', callback_data='frominttomenue')]
])

floatinputstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromfloatst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromfloatst')],
    [InlineKeyboardButton(text='В меню', callback_data='fromfloattomenue')]
])

ifstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromifst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromifst')],
    [InlineKeyboardButton(text='В меню', callback_data='fromiftomenue')]
])

elifstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromelifst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromelifst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromeliftomenue')]
])

elsestudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromelsest'), InlineKeyboardButton(text='Дальше', callback_data='nextfromelsest')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromelsetomenue')]
])

andstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromandst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromandst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromandtomenue')]
])

orstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromorst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromorst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromortomenue')]
])

instudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfrominst'), InlineKeyboardButton(text='Дальше', callback_data='nextfrominst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromintomenue')]
])

notstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromnotst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromnotst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromnottomenue')]
])

trystudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromtryst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromtryst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromtrytomenue')]
])

exceptstudy = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backfromexst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromexst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromextomenue')]
])

finallystudy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='backfromffinst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromffinst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromffintomenue')]
])

defstudy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='backfromdefst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromdefst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromdeftomenue')]
])

returnstudy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='backfromretst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromretst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromrettomenue')]
])

classstudy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='backfromclsst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromclsst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromclstomenue')]
])

whilestudy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='backfromwlst'), InlineKeyboardButton(text='Дальше', callback_data='nextfromwlst')], 
    [InlineKeyboardButton(text='В меню', callback_data='fromwltomenue')]
])

cyclerangestudy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='backfromrgst'), InlineKeyboardButton(text='В меню', callback_data='fromrgtomenue')]
])


practice = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Начать тест', callback_data='starttest')],
    [InlineKeyboardButton(text='В меню', callback_data='backpractice')]
])

question1 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Строка', callback_data='stringpr1'),
    InlineKeyboardButton(text='Число', callback_data='numberpr1')],
    [InlineKeyboardButton(text='Список', callback_data='listpr1'), 
    InlineKeyboardButton(text='Кортеж', callback_data='tuplepr1')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest1')]
])

question2 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='<class "int">', callback_data='intpr2'),
    InlineKeyboardButton(text='<class "str">', callback_data='strpr2')],
    [InlineKeyboardButton(text='<class "float">', callback_data='floatpr2'), 
    InlineKeyboardButton(text='<class "list">', callback_data='listpr2')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest2')]
])

question3 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Извлекает корень', callback_data='koren3'),
    InlineKeyboardButton(text='Делит на само себя', callback_data='delit3')],
    [InlineKeyboardButton(text='Выводит модуль числа', callback_data='module3'), 
    InlineKeyboardButton(text='Делит на разряды', callback_data='rasr3')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest3')]
])

question4 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='int(input())', callback_data='int4'),
    InlineKeyboardButton(text='float(input())', callback_data='float4')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest4')]
])


question5 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Ничего', callback_data='nothing5'),
    InlineKeyboardButton(text='12', callback_data='q12pr5')],
    [InlineKeyboardButton(text='35', callback_data='q35pr5'), 
    InlineKeyboardButton(text='res', callback_data='res5')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest5')]
])


question6 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Good', callback_data='good6'),
    InlineKeyboardButton(text='Bad', callback_data='bad6')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest6')]
])


question7 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='def', callback_data='def7'),
    InlineKeyboardButton(text='while', callback_data='while7')],
    [InlineKeyboardButton(text='except', callback_data='except7'), 
    InlineKeyboardButton(text='or', callback_data='or7')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest7')]
])

question8 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Пока', callback_data='while8'),
    InlineKeyboardButton(text='В', callback_data='in8')],
    [InlineKeyboardButton(text='Определять', callback_data='define8'), 
    InlineKeyboardButton(text='Возвращать', callback_data='return8')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest8')]
])


question9 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Класс', callback_data='class9'),
    InlineKeyboardButton(text='Объект', callback_data='object9')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest9')]
])


question10 = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Да', callback_data='yes10'),
    InlineKeyboardButton(text='Нет', callback_data='no10')],
    [InlineKeyboardButton(text='Завершить тест', callback_data='stoptest10')]
])

finishtest = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='В меню', callback_data='finish')]
])


contactsk = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Назад', callback_data='backcontacts')]
])