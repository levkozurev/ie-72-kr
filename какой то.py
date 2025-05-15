import flet as ft
import os


def main(page):
    # Настройки окна
    page.title = "Счетчик кликов+"
    page.window_width = 400
    page.window_height = 300
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Файл для сохранения
    SAVE_FILE = "saved_clicks.txt"

    # Загружаем сохраненные клики при старте
    def load_saved():
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                try:
                    return int(f.read())
                except:
                    return 0
        return 0

    saved_count = load_saved()
    current_count = 0

    # Элементы интерфейса
    count_text = ft.Text(value=f"Текущие: 0 | Всего: {saved_count}", size=24)

    # Обновляем текст
    def update_text():
        count_text.value = f"Текущие: {current_count} | Всего: {saved_count}"
        page.update()

    # Кнопка для подсчета
    def click(e):
        nonlocal current_count
        current_count += 1
        update_text()

    # Кнопка сброса
    def reset(e):
        nonlocal current_count
        current_count = 0
        update_text()

    # Кнопка сохранения
    def save(e):
        nonlocal saved_count
        saved_count += current_count
        with open(SAVE_FILE, "w") as f:
            f.write(str(saved_count))
        update_text()

    # Создаем кнопки
    click_btn = ft.ElevatedButton("Клик!", on_click=click, width=200)
    reset_btn = ft.ElevatedButton("Сбросить текущие", on_click=reset, width=200)
    save_btn = ft.ElevatedButton("save", on_click=save, width=200)

    # Добавляем элементы на страницу
    page.add(
        count_text,
        click_btn,
        reset_btn,
        save_btn
    )


# Запускаем приложение
ft.app(target=main)
