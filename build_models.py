import os
import json
import shutil
import tempfile
import hashlib

GITHUB_USERNAME = "vadim3121"
GITHUB_REPO = "firefox-translation-models"
GITHUB_BRANCH = "main"

OUTPUT_ARCHIVES_DIR = "models"
os.makedirs(OUTPUT_ARCHIVES_DIR, exist_ok=True)

lang_names = {
    "ar": "Arabic", "az": "Azerbaijani", "be": "Belarusian", "bg": "Bulgarian",
    "bn": "Bengali", "bs": "Bosnian", "ca": "Catalan", "cs": "Czech",
    "da": "Danish", "de": "German", "el": "Greek", "en": "English",
    "es": "Spanish", "et": "Estonian", "fa": "Persian", "fi": "Finnish",
    "fr": "French", "gu": "Gujarati", "he": "Hebrew", "hi": "Hindi",
    "hr": "Croatian", "hu": "Hungarian", "id": "Indonesian", "is": "Icelandic",
    "it": "Italian", "ja": "Japanese", "kn": "Kannada", "ko": "Korean",
    "lt": "Lithuanian", "lv": "Latvian", "ml": "Malayalam", "ms": "Malay",
    "mt": "Maltese", "nb": "Norwegian Bokmål", "nl": "Dutch", "nn": "Norwegian Nynorsk",
    "pl": "Polish", "pt": "Portuguese", "ro": "Romanian", "ru": "Russian",
    "sk": "Slovak", "sl": "Slovenian", "sq": "Albanian", "sr": "Serbian",
    "sv": "Swedish", "ta": "Tamil", "te": "Telugu", "tr": "Turkish",
    "uk": "Ukrainian", "vi": "Vietnamese", "zh": "Chinese"
}

def get_lang_name(code):
    return lang_names.get(code, code.upper())

def get_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

all_models = []

print(f"🚀 Начинаем сканирование папок в {os.getcwd()}...\n")

for folder_name in os.listdir("."):
    if not os.path.isdir(folder_name) or folder_name.startswith(".") or folder_name == OUTPUT_ARCHIVES_DIR:
        continue

    metadata_path = os.path.join(folder_name, "metadata.json")
    
    if not os.path.exists(metadata_path):
        continue

    try:
        with open(metadata_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
            
        src_lang = meta.get("sourceLanguage", "en")
        trg_lang = meta.get("targetLanguage", "uk")
        PAIR_CODE = f"{src_lang}.{trg_lang}"
        
        arch_type = meta.get("architecture", "base")
        
        src_name = get_lang_name(src_lang)
        trg_name = get_lang_name(trg_lang)
        
        MODEL_NAME = f"{src_name}-{trg_name} {arch_type}"
        SHORT_NAME = f"{src_lang}-{trg_lang}-{arch_type}"
        
        OUTPUT_DIR_NAME = f"translatelocally-{src_lang}-{trg_lang}"
        ARCHIVE_FILENAME = f"{OUTPUT_DIR_NAME}.tar.gz"
        ARCHIVE_PATH = os.path.join(OUTPUT_ARCHIVES_DIR, ARCHIVE_FILENAME)
        
        found_model = found_vocab = found_lex = None
        for file in os.listdir(folder_name):
            if file.endswith("intgemm.alphas.bin"):
                found_model = os.path.join(folder_name, file)
            elif file.endswith(".spm"):
                found_vocab = os.path.join(folder_name, file)
            elif file.endswith(".s2t.bin"):
                found_lex = os.path.join(folder_name, file)
                
        if not all([found_model, found_vocab, found_lex]):
            print(f"❌ В папке {folder_name} не хватает файлов. Пропуск.")
            continue

        with tempfile.TemporaryDirectory() as temp_dir:
            work_dir = os.path.join(temp_dir, OUTPUT_DIR_NAME)
            os.makedirs(work_dir)

            shutil.copy2(found_model, os.path.join(work_dir, f"model.{PAIR_CODE}.intgemm.alphas.bin"))
            shutil.copy2(found_vocab, os.path.join(work_dir, f"vocab.{PAIR_CODE}.spm"))
            shutil.copy2(found_lex, os.path.join(work_dir, f"lex.50.50.{PAIR_CODE}.s2t.bin"))

            config_content = f"""relative-paths: true
models:
  - model.{PAIR_CODE}.intgemm.alphas.bin
vocabs:
  - vocab.{PAIR_CODE}.spm
  - vocab.{PAIR_CODE}.spm
shortlist:
  - lex.50.50.{PAIR_CODE}.s2t.bin
  - false
beam-size: 1
normalize: 1.0
word-penalty: 0
max-length-break: 128
mini-batch-words: 1024
workspace: 128
max-length-factor: 2.0
skip-cost: true
cpu-threads: 0
quiet: true
quiet-translation: true
gemm-precision: int8shiftAlphaAll
"""
            with open(os.path.join(work_dir, "config.intgemm8bitalpha.yml"), "w", encoding="utf-8") as f:
                f.write(config_content)

            model_info = {
                "modelName": MODEL_NAME,
                "shortName": SHORT_NAME,
                "type": arch_type,
                "src": src_name,
                "trg": trg_name,
                "version": 1.0,
                "API": 1.0
            }
            with open(os.path.join(work_dir, "model_info.json"), "w", encoding="utf-8") as f:
                json.dump(model_info, f, indent=2, ensure_ascii=False)

            shutil.make_archive(
                base_name=os.path.join(OUTPUT_ARCHIVES_DIR, OUTPUT_DIR_NAME), 
                format="gztar", 
                root_dir=temp_dir, 
                base_dir=OUTPUT_DIR_NAME
            )
            
            print(f"✅ Собран архив: {ARCHIVE_FILENAME}")

            checksum = get_sha256(ARCHIVE_PATH)
            
            github_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{OUTPUT_ARCHIVES_DIR}/{ARCHIVE_FILENAME}"

            model_entry = {
                "modelName": MODEL_NAME,
                "shortName": SHORT_NAME,
                "type": arch_type,
                "src": src_name,
                "trg": trg_name,
                "srcTags": {
                    src_lang: src_name
                },
                "trgTag": trg_lang,
                "repository": "Vadim3121 (GitHub)",
                "version": 1,
                "API": 1,
                "checksum": checksum,
                "url": github_url,
                "name": MODEL_NAME,
                "code": SHORT_NAME
            }
            all_models.append(model_entry)

    except Exception as e:
        print(f"⚠️ Ошибка при обработке {folder_name}: {e}")

if all_models:
    models_json_path = os.path.join(OUTPUT_ARCHIVES_DIR, "models.json")
    final_json = {"models": all_models}
    
    with open(models_json_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)
        
    print(f"\n🎉 Все готово! Собрано моделей: {len(all_models)}")
    print(f"📄 Файл со списком всех моделей сохранен в: {models_json_path}")
else:
    print("\n⚠️ Не удалось собрать ни одной модели.")