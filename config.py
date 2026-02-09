"""
Конфигурационный файл для системы мониторинга экосистемы

Содержит все настройки и параметры для работы системы:
- Пути к директориям
- Пороги для детекции
- Параметры моделей
- Критерии оповещений
"""

import os
from pathlib import Path

# ========== ПУТИ К ДИРЕКТОРИЯМ ==========

# Базовая директория проекта
BASE_DIR = Path(__file__).parent.absolute()

# Директории для данных
DATA_DIR = BASE_DIR / "data"
VIDEO_DIR = DATA_DIR / "videos"
AUDIO_DIR = DATA_DIR / "audio"
IMAGES_DIR = DATA_DIR / "images"
RESULTS_DIR = DATA_DIR / "results"

# Директория для моделей
MODELS_DIR = BASE_DIR / "models"

# Создание директорий если их нет
for directory in [DATA_DIR, VIDEO_DIR, AUDIO_DIR, IMAGES_DIR, RESULTS_DIR, MODELS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


# ========== ПАРАМЕТРЫ YOLOV8 (ВИДЕО АНАЛИЗ) ==========

# Модель YOLOv8 (n - nano, s - small, m - medium, l - large, x - extra large)
YOLO_MODEL = "yolov8n.pt"  # Nano версия для быстрой работы

# Порог уверенности для детекции (0.0 - 1.0)
YOLO_CONFIDENCE_THRESHOLD = 0.25

# IoU порог для Non-Maximum Suppression
YOLO_IOU_THRESHOLD = 0.45

# Классы животных из COCO dataset, которые нас интересуют
ANIMAL_CLASSES = {
    14: 'bird',      # Птица
    15: 'cat',       # Кошка
    16: 'dog',       # Собака
    17: 'horse',     # Лошадь
    18: 'sheep',     # Овца
    19: 'cow',       # Корова
    20: 'elephant',  # Слон
    21: 'bear',      # Медведь
    22: 'zebra',     # Зебра
    23: 'giraffe',   # Жираф
}

# Параметры обработки видео
VIDEO_FPS_SAMPLE = 2  # Обрабатывать каждый N-й кадр (для экономии ресурсов)
VIDEO_RESIZE_FACTOR = 1.0  # Масштаб видео (1.0 = оригинальный размер)


# ========== ПАРАМЕТРЫ YAMNET (АУДИО АНАЛИЗ) ==========

# URL модели YAMNet на TensorFlow Hub
YAMNET_MODEL_URL = "https://tfhub.dev/google/yamnet/1"

# Частота дискретизации для YAMNet
YAMNET_SAMPLE_RATE = 16000

# Порог уверенности для аудио классификации
AUDIO_CONFIDENCE_THRESHOLD = 0.3

# Классы звуков, связанных с природой и животными
NATURE_SOUND_CLASSES = [
    'Bird',
    'Bird vocalization',
    'Bird flight',
    'Chirp',
    'Tweet',
    'Squawk',
    'Animal',
    'Domestic animals',
    'Wild animals',
    'Insect',
    'Cricket',
    'Frog',
    'Wind',
    'Rain',
    'Stream',
    'Ocean',
    'Thunder',
]


# ========== ПАРАМЕТРЫ СИСТЕМЫ ОПОВЕЩЕНИЙ ==========

# Критерии для генерации тревог

# Минимальное количество животных, при котором генерируется оповещение
ALERT_MIN_ANIMALS = 10

# Максимальное количество животных, при котором генерируется оповещение
ALERT_MAX_ANIMALS = 100

# Редкие виды, обнаружение которых всегда генерирует оповещение
ALERT_RARE_SPECIES = ['bear', 'elephant', 'giraffe', 'zebra']

# Критическое снижение активности (% от нормы)
ALERT_ACTIVITY_DROP = 0.5  # 50% снижение

# Необычно высокая активность (кратно от нормы)
ALERT_ACTIVITY_SPIKE = 2.0  # В 2 раза выше нормы


# ========== ПАРАМЕТРЫ ВИЗУАЛИЗАЦИИ ==========

# Размеры графиков
FIGURE_SIZE = (15, 8)
FIGURE_DPI = 100

# Цветовая схема для графиков
COLOR_PALETTE = 'viridis'

# Цвета для bounding boxes по классам
BBOX_COLORS = {
    'bird': (0, 255, 0),       # Зелёный
    'bear': (255, 0, 0),       # Красный
    'deer': (0, 255, 255),     # Голубой
    'default': (255, 255, 0),  # Жёлтый
}


# ========== ПАРАМЕТРЫ ЭКСПОРТА ==========

# Формат для сохранения результатов
EXPORT_FORMAT = 'csv'  # 'csv', 'json', 'excel'

# Формат даты и времени
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# Сохранять ли визуализации
SAVE_VISUALIZATIONS = True

# Формат изображений
IMAGE_FORMAT = 'png'  # 'png', 'jpg'


# ========== ЛОГИРОВАНИЕ ==========

# Уровень логирования
LOG_LEVEL = 'INFO'  # 'DEBUG', 'INFO', 'WARNING', 'ERROR'

# Сохранять ли логи в файл
SAVE_LOGS = True

# Путь к файлу логов
LOG_FILE = BASE_DIR / 'ecosystem_monitor.log'


# ========== ПРОИЗВОДИТЕЛЬНОСТЬ ==========

# Использовать GPU если доступен
USE_GPU = True

# Размер батча для обработки
BATCH_SIZE = 16

# Количество потоков для обработки
NUM_WORKERS = 4


# ========== ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ ==========

# Временная зона
TIMEZONE = 'UTC'

# Язык для отчётов
REPORT_LANGUAGE = 'ru'

# Email для оповещений (опционально)
ALERT_EMAIL = None  # Например: 'ecologist@example.com'

# Telegram bot token для оповещений (опционально)
TELEGRAM_BOT_TOKEN = None
TELEGRAM_CHAT_ID = None


# ========== ИНФОРМАЦИЯ О ВЕРСИИ ==========

VERSION = "1.0.0"
PROJECT_NAME = "Ecosystem Monitoring System"
PROJECT_DESCRIPTION = "Система мониторинга экосистемы с использованием ML"


def print_config():
    """
    Вывод текущей конфигурации системы
    """
    print(f"{'='*60}")
    print(f"{PROJECT_NAME} v{VERSION}")
    print(f"{'='*60}")
    print(f"Базовая директория: {BASE_DIR}")
    print(f"Директория данных: {DATA_DIR}")
    print(f"Модель YOLO: {YOLO_MODEL}")
    print(f"Порог уверенности YOLO: {YOLO_CONFIDENCE_THRESHOLD}")
    print(f"Порог уверенности аудио: {AUDIO_CONFIDENCE_THRESHOLD}")
    print(f"Использование GPU: {USE_GPU}")
    print(f"{'='*60}")


if __name__ == "__main__":
    print_config()
