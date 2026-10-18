# Firefox Translation Models for TranslateLocally

Репозиторий с готовыми моделями для TranslateLocally. Все архивы собраны из оригинальных моделей Mozilla Firefox (Bergamot).

## Как добавить модели в TranslateLocally

1. Скачайте из папки `/models` любой архив с моделью в формате `.tar.gz`.
2. В TranslateLocally откройте: **Edit** -> **Translator Settings** -> **Languages** -> **Import model**.

## Как добавить все модели сразу через репозиторий

1. Скопируйте ссылку ниже:
   ```text
   https://raw.githubusercontent.com/vadim3121/firefox-translation-models/refs/heads/main/models.json
   ```
2. В TranslateLocally откройте: **Edit** -> **Translator Settings** -> **Repositories** -> **Import repository**.
3. Вставьте скопированный адрес и обновите список моделей на вкладке **Languages**.
<p align="center">
  <img src="[https://github.com/твой_ник/твой_репозиторий/raw/main/имя_картинки.png](https://raw.githubusercontent.com/vadim3121/firefox-translation-models/main/import.png)" width="600" alt="TranslateLocally">
</p>
## Как пересобрать модели самостоятельно

1. Скачайте оригинальные папки с моделями (они должны содержать файлы `metadata.json`, `model.*.bin`, `vocab.*.spm`).
2. Положите скрипт `build_models.py` в корневую директорию рядом с этими папками.
3. Отредактируйте в скрипте переменные окружения: `GITHUB_USERNAME`, `GITHUB_REPO`, `GITHUB_BRANCH`.
4. Запустите сборку:
   ```bash
   python build_models.py
   ```
5. Дождитесь окончания процесса.
6. Готовые архивы моделей и файл `models.json` по умолчанию появятся в папке `/models`.

## Полезные ссылки

* [translateLocally](https://github.com/XapaJIaMnu/translateLocally) — оригинальный проект офлайн-переводчика от автора XapaJIaMnu.
* [bergamot-models](https://github.com/mozilla-applied-ml/bergamot-models) — архивный репозиторий моделей Bergamot от Mozilla.
* [firefox-translations-93-pairs](https://huggingface.co/manateelazycat/firefox-translations-93-pairs) — зеркало на Hugging Face, откуда скачивались исходные модели.
