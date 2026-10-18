
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
<img width="554" height="501" alt="import" src="https://github.com/user-attachments/assets/6a805990-d7f9-4934-a7a1-c959263cf143" />

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

## Список поддерживаемых языков

<details>
<summary><b>Развернуть список доступных направлений перевода</b></summary>

### С английского языка (en-*)

`en-ar` (Арабский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-nl` (Нидерландский) &nbsp;&nbsp;&nbsp; `en-fi` (Финский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-kn` (Каннада)  
`en-az` (Азербайджанский) &nbsp;&nbsp; `en-pl` (Польский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-fr` (Французский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-ko` (Корейский)  
`en-bg` (Болгарский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-pt` (Португальский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-gu` (Гуджарати) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-lt` (Литовский)  
`en-bn` (Бенгальский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-ro` (Румынский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-he` (Иврит) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-lv` (Латышский)  
`en-ca` (Каталанский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-ru` (Русский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-hi` (Хинди) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-ml` (Малаялам)  
`en-cs` (Чешский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-sk` (Словацкий) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-hr` (Хорватский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-ms` (Малайский)  
`en-da` (Датский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-sl` (Словенский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-hu` (Венгерский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-sv` (Шведский)  
`en-de` (Немецкий) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-sq` (Албанский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-id` (Индонезийский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-ta` (Тамильский)  
`en-el` (Греческий) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-tr` (Турецкий) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-is` (Исландский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-te` (Телугу)  
`en-es` (Испанский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-uk` (Украинский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-it` (Итальянский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-zh-Hans` (Китайский)  
`en-et` (Эстонский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-fa` (Персидский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `en-ja` (Японский)  

### На английский язык (*-en)

`ar-en` (Арабский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `el-en` (Греческий) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `it-en` (Итальянский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `pl-en` (Польский)  
`az-en` (Азербайджанский) &nbsp;&nbsp; `es-en` (Испанский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `ja-en` (Японский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `pt-en` (Португальский)  
`be-en` (Белорусский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `et-en` (Эстонский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `kn-en` (Каннада) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `ro-en` (Румынский)  
`bg-en` (Болгарский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fa-en` (Персидский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `ko-en` (Корейский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `ru-en` (Русский)  
`bn-en` (Бенгальский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fi-en` (Финский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `lt-en` (Литовский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sk-en` (Словацкий)  
`bs-en` (Боснийский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fr-en` (Французский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `lv-en` (Латышский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sl-en` (Словенский)  
`ca-en` (Каталанский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `gu-en` (Гуджарати) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `ml-en` (Малаялам) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sq-en` (Албанский)  
`cs-en` (Чешский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `he-en` (Иврит) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `ms-en` (Малайский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sr-en` (Сербский)  
`da-en` (Датский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `hi-en` (Хинди) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `mt-en` (Мальтийский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sv-en` (Шведский)  
`de-en` (Немецкий) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `hr-en` (Хорватский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `nb-en` (Норв. букмол) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `ta-en` (Тамильский)  
`hu-en` (Венгерский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `id-en` (Индонезийский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `nl-en` (Нидерландский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `te-en` (Телугу)  
`is-en` (Исландский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `nn-en` (Норв. нюнорск) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `tr-en` (Турецкий) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `uk-en` (Украинский)  
`vi-en` (Вьетнамский) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `zh-Hans-en` (Китайский)  

</details>



## Полезные ссылки

* [translateLocally](https://github.com/XapaJIaMnu/translateLocally) — оригинальный проект офлайн-переводчика от автора XapaJIaMnu.
* [bergamot-models](https://github.com/mozilla-applied-ml/bergamot-models) — архивный репозиторий моделей Bergamot от Mozilla.
* [firefox-translations-93-pairs](https://huggingface.co/manateelazycat/firefox-translations-93-pairs) — зеркало на Hugging Face, откуда скачивались исходные модели.
