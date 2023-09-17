import allure
from allure_commons.types import Severity

from tensor_demo_project.pages.main_page import MainPage

main_page = MainPage()


@allure.title('Проверяем логотип')
@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('main_page')
@allure.severity(Severity.CRITICAL)
def test_logo():
    main_page.open()

    main_page.should_be_logo()


@allure.title('Проверяем заголовок страницы')
@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('main_page')
@allure.severity(Severity.CRITICAL)
def test_header():
    main_page.open()

    main_page.should_have_texts_header()


@allure.title('Проверяем заголовок баннера')
@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('main_page')
@allure.severity(Severity.CRITICAL)
def test_banner_title():
    main_page.open()

    main_page.should_have_texts_banner_title(
        'РАЗРАБОТКА\nПРОГРАММНОГО\nОБЕСПЕЧЕНИЯ'
    )


@allure.title('Проверяем блок numbers')
@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('main_page')
@allure.severity(Severity.CRITICAL)
def test_ru_numbers():
    main_page.open()

    main_page.should_have_exacts_texts_numbers(
        '11',
        '100',
        '7 000',
        '4 500 000'
    )


@allure.title('Проверяем подвал страницы')
@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('main_page')
@allure.severity(Severity.CRITICAL)
def test_footer():
    main_page.open()

    main_page.should_have_texts_footer(
        'Направления',
        'О нас',
        'Проекты'
    )
