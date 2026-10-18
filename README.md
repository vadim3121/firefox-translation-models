
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

<table style="border: none; border-collapse: collapse; width: 70%;" border="0">
<tr style="border: none;">
  <td style="border: none; width: 25%;"><code>en-ar</code> (Арабский)</td>
  <td style="border: none; width: 25%;"><code>en-nl</code> (Нидерландский)</td>
  <td style="border: none; width: 25%;"><code>en-fi</code> (Финский)</td>
  <td style="border: none; width: 25%;"><code>en-kn</code> (Каннада)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-az</code> (Азербайджанский)</td>
  <td style="border: none;"><code>en-pl</code> (Польский)</td>
  <td style="border: none;"><code>en-fr</code> (Французский)</td>
  <td style="border: none;"><code>en-ko</code> (Корейский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-bg</code> (Болгарский)</td>
  <td style="border: none;"><code>en-pt</code> (Португальский)</td>
  <td style="border: none;"><code>en-gu</code> (Гуджарати)</td>
  <td style="border: none;"><code>en-lt</code> (Литовский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-bn</code> (Бенгальский)</td>
  <td style="border: none;"><code>en-ro</code> (Румынский)</td>
  <td style="border: none;"><code>en-he</code> (Иврит)</td>
  <td style="border: none;"><code>en-lv</code> (Латышский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-ca</code> (Каталанский)</td>
  <td style="border: none;"><code>en-ru</code> (Русский)</td>
  <td style="border: none;"><code>en-hi</code> (Хинди)</td>
  <td style="border: none;"><code>en-ml</code> (Малаялам)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-cs</code> (Чешский)</td>
  <td style="border: none;"><code>en-sk</code> (Словацкий)</td>
  <td style="border: none;"><code>en-hr</code> (Хорватский)</td>
  <td style="border: none;"><code>en-ms</code> (Малайский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-da</code> (Датский)</td>
  <td style="border: none;"><code>en-sl</code> (Словенский)</td>
  <td style="border: none;"><code>en-hu</code> (Венгерский)</td>
  <td style="border: none;"><code>en-sv</code> (Шведский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-de</code> (Немецкий)</td>
  <td style="border: none;"><code>en-sq`</code> (Албанский)</td>
  <td style="border: none;"><code>en-id</code> (Индонезийский)</td>
  <td style="border: none;"><code>en-ta</code> (Тамильский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-el</code> (Греческий)</td>
  <td style="border: none;"><code>en-tr</code> (Турецкий)</td>
  <td style="border: none;"><code>en-is</code> (Исландский)</td>
  <td style="border: none;"><code>en-te</code> (Телугу)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-es</code> (Испанский)</td>
  <td style="border: none;"><code>en-uk</code> (Украинский)</td>
  <td style="border: none;"><code>en-it</code> (Итальянский)</td>
  <td style="border: none;"><code>en-zh-Hans</code> (Китайский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>en-et</code> (Эстонский)</td>
  <td style="border: none;"><code>en-fa</code> (Персидский)</td>
  <td style="border: none;"><code>en-ja</code> (Японский)</td>
  <td style="border: none;"></td>
</tr>
</table>

### На английский язык (*-en)

<table style="border: none; border-collapse: collapse; width: 70%;" border="0">
<tr style="border: none;">
  <td style="border: none; width: 25%;"><code>ar-en</code> (Арабский)</td>
  <td style="border: none; width: 25%;"><code>el-en</code> (Греческий)</td>
  <td style="border: none; width: 25%;"><code>it-en</code> (Итальянский)</td>
  <td style="border: none; width: 25%;"><code>pl-en</code> (Польский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>az-en</code> (Азербайджанский)</td>
  <td style="border: none;"><code>es-en</code> (Испанский)</td>
  <td style="border: none;"><code>ja-en</code> (Японский)</td>
  <td style="border: none;"><code>pt-en</code> (Португальский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>be-en</code> (Белорусский)</td>
  <td style="border: none;"><code>et-en</code> (Эстонский)</td>
  <td style="border: none;"><code>kn-en</code> (Каннада)</td>
  <td style="border: none;"><code>ro-en</code> (Румынский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>bg-en</code> (Болгарский)</td>
  <td style="border: none;"><code>fa-en`</code> (Персидский)</td>
  <td style="border: none;"><code>ko-en</code> (Корейский)</td>
  <td style="border: none;"><code>ru-en</code> (Русский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>bn-en</code> (Бенгальский)</td>
  <td style="border: none;"><code>fi-en</code> (Финский)</td>
  <td style="border: none;"><code>lt-en</code> (Литовский)</td>
  <td style="border: none;"><code>sk-en`</code> (Словацкий)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>bs-en</code> (Боснийский)</td>
  <td style="border: none;"><code>fr-en</code> (Французский)</td>
  <td style="border: none;"><code>lv-en</code> (Латышский)</td>
  <td style="border: none;"><code>sl-en</code> (Словенский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>ca-en</code> (Каталанский)</td>
  <td style="border: none;"><code>gu-en</code> (Гуджарати)</td>
  <td style="border: none;"><code>ml-en</code> (Малаялам)</td>
  <td style="border: none;"><code>sq-en</code> (Албанский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>cs-en</code> (Чешский)</td>
  <td style="border: none;"><code>he-en</code> (Иврит)</td>
  <td style="border: none;"><code>ms-en</code> (Малайский)</td>
  <td style="border: none;"><code>sr-en</code> (Сербский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>da-en</code> (Датский)</td>
  <td style="border: none;"><code>hi-en</code> (Хинди)</td>
  <td style="border: none;"><code>mt-en</code> (Мальтийский)</td>
  <td style="border: none;"><code>sv-en</code> (Шведский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>de-en</code> (Немецкий)</td>
  <td style="border: none;"><code>hr-en</code> (Хорватский)</td>
  <td style="border: none;"><code>nb-en</code> (Норв. букмол)</td>
  <td style="border: none;"><code>ta-en</code> (Тамильский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>hu-en</code> (Венгерский)</td>
  <td style="border: none;"><code>id-en</code> (Индонезийский)</td>
  <td style="border: none;"><code>nl-en</code> (Нидерландский)</td>
  <td style="border: none;"><code>te-en</code> (Телугу)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>is-en</code> (Исландский)</td>
  <td style="border: none;"><code>nn-en</code> (Норв. нюнорск)</td>
  <td style="border: none;"><code>tr-en</code> (Турецкий)</td>
  <td style="border: none;"><code>uk-en</code> (Украинский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;"><code>vi-en</code> (Вьетнамский)</td>
  <td style="border: none;"><code>zh-Hans-en</code> (Китайский)</td>
  <td style="border: none;"></td>
  <td style="border: none;"></td>
</tr>
</table>

</details>





## Полезные ссылки

* [translateLocally](https://github.com/XapaJIaMnu/translateLocally) — оригинальный проект офлайн-переводчика от автора XapaJIaMnu.
* [bergamot-models](https://github.com/mozilla-applied-ml/bergamot-models) — архивный репозиторий моделей Bergamot от Mozilla.
* [firefox-translations-93-pairs](https://huggingface.co/manateelazycat/firefox-translations-93-pairs) — зеркало на Hugging Face, откуда скачивались исходные модели.
