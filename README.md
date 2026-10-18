
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

<table style="border: none; border-collapse: collapse; width: 100%;" border="0">
<tr style="border: none;">
  <td style="border: none; width: 25%;">`en-ar` (Арабский)</td>
  <td style="border: none; width: 25%;">`en-nl` (Нидерландский)</td>
  <td style="border: none; width: 25%;">`en-fi` (Финский)</td>
  <td style="border: none; width: 25%;">`en-kn` (Каннада)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-az` (Азербайджанский)</td>
  <td style="border: none;">`en-pl` (Польский)</td>
  <td style="border: none;">`en-fr` (Французский)</td>
  <td style="border: none;">`en-ko` (Корейский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-bg` (Болгарский)</td>
  <td style="border: none;">`en-pt` (Португальский)</td>
  <td style="border: none;">`en-gu` (Гуджарати)</td>
  <td style="border: none;">`en-lt` (Литовский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-bn` (Бенгальский)</td>
  <td style="border: none;">`en-ro` (Румынский)</td>
  <td style="border: none;">`en-he` (Иврит)</td>
  <td style="border: none;">`en-lv` (Латышский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-ca` (Каталанский)</td>
  <td style="border: none;">`en-ru` (Русский)</td>
  <td style="border: none;">`en-hi` (Хинди)</td>
  <td style="border: none;">`en-ml` (Малаялам)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-cs` (Чешский)</td>
  <td style="border: none;">`en-sk` (Словацкий)</td>
  <td style="border: none;">`en-hr` (Хорватский)</td>
  <td style="border: none;">`en-ms` (Малайский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-da` (Датский)</td>
  <td style="border: none;">`en-sl` (Словенский)</td>
  <td style="border: none;">`en-hu` (Венгерский)</td>
  <td style="border: none;">`en-sv` (Шведский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-de` (Немецкий)</td>
  <td style="border: none;">`en-sq` (Албанский)</td>
  <td style="border: none;">`en-id` (Индонезийский)</td>
  <td style="border: none;">`en-ta` (Тамильский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-el` (Греческий)</td>
  <td style="border: none;">`en-tr` (Турецкий)</td>
  <td style="border: none;">`en-is` (Исландский)</td>
  <td style="border: none;">`en-te` (Телугу)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-es` (Испанский)</td>
  <td style="border: none;">`en-uk` (Украинский)</td>
  <td style="border: none;">`en-it` (Итальянский)</td>
  <td style="border: none;">`en-zh-Hans` (Китайский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`en-et` (Эстонский)</td>
  <td style="border: none;">`en-fa` (Персидский)</td>
  <td style="border: none;">`en-ja` (Японский)</td>
  <td style="border: none;"></td>
</tr>
</table>

### На английский язык (*-en)

<table style="border: none; border-collapse: collapse; width: 100%;" border="0">
<tr style="border: none;">
  <td style="border: none; width: 25%;">`ar-en` (Арабский)</td>
  <td style="border: none; width: 25%;">`el-en` (Греческий)</td>
  <td style="border: none; width: 25%;">`it-en` (Итальянский)</td>
  <td style="border: none; width: 25%;">`pl-en` (Польский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`az-en` (Азербайджанский)</td>
  <td style="border: none;">`es-en` (Испанский)</td>
  <td style="border: none;">`ja-en` (Японский)</td>
  <td style="border: none;">`pt-en` (Португальский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`be-en` (Белорусский)</td>
  <td style="border: none;">`et-en` (Эстонский)</td>
  <td style="border: none;">`kn-en` (Каннада)</td>
  <td style="border: none;">`ro-en` (Румынский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`bg-en` (Болгарский)</td>
  <td style="border: none;">`fa-en` (Персидский)</td>
  <td style="border: none;">`ko-en` (Корейский)</td>
  <td style="border: none;">`ru-en` (Русский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`bn-en` (Бенгальский)</td>
  <td style="border: none;">`fi-en` (Финский)</td>
  <td style="border: none;">`lt-en` (Литовский)</td>
  <td style="border: none;">`sk-en` (Словацкий)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`bs-en` (Боснийский)</td>
  <td style="border: none;">`fr-en` (Французский)</td>
  <td style="border: none;">`lv-en` (Латышский)</td>
  <td style="border: none;">`sl-en` (Словенский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`ca-en` (Каталанский)</td>
  <td style="border: none;">`gu-en` (Гуджарати)</td>
  <td style="border: none;">`ml-en` (Малаялам)</td>
  <td style="border: none;">`sq-en` (Албанский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`cs-en` (Чешский)</td>
  <td style="border: none;">`he-en` (Иврит)</td>
  <td style="border: none;">`ms-en` (Малайский)</td>
  <td style="border: none;">`sr-en` (Сербский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`da-en` (Датский)</td>
  <td style="border: none;">`hi-en` (Хинди)</td>
  <td style="border: none;">`mt-en` (Мальтийский)</td>
  <td style="border: none;">`sv-en` (Шведский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`de-en` (Немецкий)</td>
  <td style="border: none;">`hr-en` (Хорватский)</td>
  <td style="border: none;">`nb-en` (Норв. букмол)</td>
  <td style="border: none;">`ta-en` (Тамильский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`hu-en` (Венгерский)</td>
  <td style="border: none;">`id-en` (Индонезийский)</td>
  <td style="border: none;">`nl-en` (Нидерландский)</td>
  <td style="border: none;">`te-en` (Телугу)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`is-en` (Исландский)</td>
  <td style="border: none;">`nn-en` (Норв. нюнорск)</td>
  <td style="border: none;">`tr-en` (Турецкий)</td>
  <td style="border: none;">`uk-en` (Украинский)</td>
</tr>
<tr style="border: none;">
  <td style="border: none;">`vi-en` (Вьетнамский)</td>
  <td style="border: none;">`zh-Hans-en` (Китайский)</td>
  <td style="border: none;"></td>
  <td style="border: none;"></td>
</tr>
</table>

</details>




## Полезные ссылки

* [translateLocally](https://github.com/XapaJIaMnu/translateLocally) — оригинальный проект офлайн-переводчика от автора XapaJIaMnu.
* [bergamot-models](https://github.com/mozilla-applied-ml/bergamot-models) — архивный репозиторий моделей Bergamot от Mozilla.
* [firefox-translations-93-pairs](https://huggingface.co/manateelazycat/firefox-translations-93-pairs) — зеркало на Hugging Face, откуда скачивались исходные модели.
