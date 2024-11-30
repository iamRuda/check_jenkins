# Jenkins Pipeline Test Project

## Описание

Этот проект предназначен для проверки и демонстрации работы Jenkins Pipeline с использованием GitHub репозитория. Он включает в себя автоматические тесты с использованием `pytest` и отправку уведомлений в Telegram о результатах выполнения тестов. Основной целью проекта является проверка правильности настроек Jenkins Pipeline, таких как клонирование репозитория, создание виртуального окружения, установка зависимостей, запуск тестов и отправка уведомлений о результатах.

Проект настроен таким образом, чтобы позволить Jenkins пользователю проверить функционирование pipeline в реальном времени, убедившись в том, что pipeline корректно выполняется и взаимодействует с внешними сервисами.

## Структура Pipeline

1. **Клонирование репозитория**: Репозиторий автоматически клонируется из GitHub на Jenkins сервер.
2. **Настройка виртуального окружения**: Виртуальное окружение Python создается для изоляции зависимостей.
3. **Установка зависимостей**: Все зависимости из `requirements.txt` устанавливаются в виртуальное окружение.
4. **Запуск тестов**: Тесты запускаются с использованием `pytest` для проверки функциональности приложения.
5. **Отправка уведомлений**: В зависимости от результата тестов отправляется уведомление через Telegram-бота (успех или неудача).

## Цель проекта

Проект создан для проверки корректности настроек Jenkins Pipeline, включая:
- Клонирование репозитория из GitHub.
- Настройку и использование виртуальных окружений.
- Правильность установки зависимостей Python.
- Правильную настройку тестов с использованием `pytest`.
- Корректную работу с внешними сервисами, такими как Telegram API для отправки уведомлений.

Этот проект служит основой для проверки всех вышеупомянутых шагов и их корректного выполнения в процессе CI/CD pipeline.

## Установка и настройка

### 1. Клонирование репозитория

Для начала необходимо клонировать этот проект на ваш Jenkins сервер или настроить автоматический клон через pipeline.

```bash
git clone https://github.com/iamRuda/check_jenkins.git
