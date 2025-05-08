import pandas as pd

# === Шаг 1: Загрузка данных ===
df_csv = pd.read_csv("data/dataFile.csv")

# === Шаг 2: Словарь ISO → Название страны + Tier ===
iso_to_country_and_tier = {
    "US": ("United States", "US"),
    "RU": ("Russian Federation", "T3"),
    "CN": ("China (Mainland)", "T2"),
    "CA": ("Canada", "T1"),
    "BR": ("Brazil", "T2"),
    "GB": ("United Kingdom", "T1"),
    "DE": ("Germany", "T1"),
    "PH": ("Philippines", "T3"),
    "VN": ("Vietnam", "T2"),
    "ID": ("Indonesia", "T3"),
    "AU": ("Australia", "T1"),
    "ES": ("Spain", "T1"),
    "FR": ("France", "T1"),
    "PL": ("Poland", "T2"),
    "NL": ("Netherlands", "T1"),
    "UA": ("Ukraine", "T3"),
    "IT": ("Italy", "T1"),
    "TH": ("Thailand", "T3"),
    "MY": ("Malaysia", "T2"),
    "MX": ("Mexico", "T3"),
    "SE": ("Sweden", "T1"),
    "JP": ("Japan", "T1"),
    "AR": ("Argentina", "T3"),
    "TR": ("Turkey", "T2"),
    "DK": ("Denmark", "T1"),
    "SG": ("Singapore", "T2"),
    "HK": ("Hong Kong (China)", "T3"),
    "BY": ("Belarus", "T3"),
    "KZ": ("Kazakhstan", "T3"),
    "KR": ("Korea, Republic of", "T3"),
    "CZ": ("Czech Republic", "T2"),
    "IN": ("India", "T3"),
    "FI": ("Finland", "T1"),
    "RO": ("Romania", "T3"),
    "HU": ("Hungary", "T2"),
    "NZ": ("New Zealand", "T1"),
    "CL": ("Chile", "T2"),
    "BE": ("Belgium", "T1"),
    "RS": ("Serbia", "T3"),
    "NO": ("Norway", "T1"),
    "IL": ("Israel", "T2"),
    "TW": ("Taiwan (China)", "T3"),
    "CO": ("Colombia", "T2"),
    "PT": ("Portugal", "T2"),
    "IE": ("Ireland", "T1"),
    "LT": ("Lithuania", "T3"),
    "LV": ("Latvia", "T2"),
    "PE": ("Peru", "T2"),
    "GE": ("Georgia", "T2"),
    "AT": ("Austria", "T1"),
}

# === Шаг 3: Обогащение таблицы ===
df_csv["Region Name"] = df_csv["Country code"].map(lambda code: iso_to_country_and_tier.get(code, ("Unknown", ""))[0])
df_csv["Tier"] = df_csv["Country code"].map(lambda code: iso_to_country_and_tier.get(code, ("", "Unknown"))[1])

# === Шаг 4: Переупорядочивание колонок ===
columns_order = [
    "Region Name",
    "Country code",
    "Tier",
    "Custom new",
    "Custom returning"
]
df_csv = df_csv[columns_order]

# === Шаг 5: Сохранение результата ===
df_csv.to_excel("data/output_with_tiers.xlsx", index=False)

print("Готово. Файл сохранён как output_with_tiers.xlsx")
