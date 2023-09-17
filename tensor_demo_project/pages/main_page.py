import allure
from selene import be, browser, have


class MainPage:
    @allure.step('Открываем главную страницу')
    def open(self):
        browser.open('/')

    @allure.step('Проверяем видимость логотипа')
    def should_be_logo(self):
        browser.element('.tensor_ru-Header__logo').should(be.visible)

    @allure.step('Проверяем заголовок страницы')
    def should_have_texts_header(self):
        browser.all(
            '[name=headerMenu]>li:not([class*=--nosep])'
        ).should(have.texts(
            'О компании',
            'Разработка ПО',
            'Работа у нас',
            'Филиалы'
        ))

    @allure.step('Проверяем заголовок баннера на странице')
    def should_have_texts_banner_title(self, text):
        browser.element(
            '.tensor_ru-Index__Banner-title'
        ).should(have.exact_text(text))

    @allure.step('Проверяем блок "numbers"')
    def should_have_exacts_texts_numbers(
            self,
            count_dev_centers,
            count_subsidiarys,
            count_workers,
            count_clients
    ):
        browser.element('.tensor_ru-Numbers').all(
            '.s-Grid-container--space>div'
        ).should(have.exact_texts(
            f'{count_dev_centers}\nцентров разработки',
            f'{count_subsidiarys}\nфилиалов',
            f'{count_workers}\nсотрудников',
            f'{count_clients}\nклиентов'
        ))

    @allure.step('Проверяем подвал страницы')
    def should_have_texts_footer(self, *category_headers):
        browser.element(
            '.tensor_ru-Footer__container'
        ).all(
            '[class$=category-header]'
        ).should(have.texts(
            *category_headers
        ))
