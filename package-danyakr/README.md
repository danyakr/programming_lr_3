# package-danyakr

## Простой API для получения данных о погоде от OpenWeatherMap

**package-danyakr** - это простой Python-пакет, который позволяет вам получить информацию о погоде для заданного места, используя API OpenWeatherMap.

## Установка

```bash
pip install package-danyakr
```

## Использование

```python
import os
import package-danyakr

os.environ['OWM_API_KEY'] = 'your_api_key'  

weather_data = package-danyakr.get_weather_data('Moscow')

if weather_data:
    print(f"Погода в {weather_data['name']}: {weather_data['feels_like']}°C")
    print(f"Координаты: {weather_data['coord']}")
    print(f"Страна: {weather_data['country']}")
    print(f"Часовой пояс: {weather_data['timezone']}")
```

## Документация

### Функции

* **get_weather_data(place, api_key=None)**

  - **place**: Название места (город, страна).
  - **api_key**: API ключ для OpenWeatherMap. Если не указан, то используется ключ из переменной окружения OWM_API_KEY.

  - Возвращает словарь с данными о погоде:

    ```python
    {
        "name": "Moscow",  # Название места
        "coord": {"lon": 37.6173, "lat": 55.7558},  # Координаты
        "country": "RU",  # Страна
        "feels_like": 15.25,  # Ощущаемая температура
        "timezone": "UTC+3"  # Часовой пояс
    }
    ```
    
    Или None, если произошла ошибка.


## Лицензия

Этот проект лицензирован под лицензией MIT. См. файл LICENSE для получения более подробной информации.

## Контакты

***danyakr***  
*thebrrr2505@gmail.com*

    

