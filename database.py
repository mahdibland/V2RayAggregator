import sqlite3
from datetime import datetime

# نام فایل دیتابیس که تمام داده‌ها در آن ذخیره می‌شود
DB_FILE = "aggregator_data.db"

def get_connection():
    """A helper function to get a database connection."""
    return sqlite3.connect(DB_FILE)

def initialize_db():
    """
    Creates the necessary tables if they don't already exist.
    This function should be called once at the start of a workflow.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # --- جدول منابع (Sources) ---
    # برای نگهداری URL های منابع و وضعیت آنها
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sources (
            url TEXT PRIMARY KEY,
            status TEXT NOT NULL CHECK(status IN ('active', 'dead')),
            last_checked TEXT NOT NULL
        )
    ''')

    # --- جدول کانفیگ‌ها (Configs) ---
    # برای نگهداری اطلاعات هر کانفیگ به صورت مجزا
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configs (
            config TEXT PRIMARY KEY,
            source_url TEXT,
            country_code TEXT,
            speed_kbps REAL,
            last_tested TEXT
        )
    ''')

    print("Database initialized successfully.")
    conn.commit()
    conn.close()

def get_all_sources_to_check():
    """Returns all URLs from the sources table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM sources")
    # استخراج نتیجه به صورت یک لیست ساده از رشته‌ها
    urls = [row[0] for row in cursor.fetchall()]
    conn.close()
    return urls

def update_source_status(url: str, status: str):
    """Inserts a new source or updates the status of an existing one."""
    conn = get_connection()
    cursor = conn.cursor()
    now = datetime.utcnow().isoformat()

    # اگر منبع وجود داشت، آپدیت کن، اگر نه، اضافه کن
    cursor.execute('''
        INSERT INTO sources (url, status, last_checked) VALUES (?, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
            status = excluded.status,
            last_checked = excluded.last_checked
    ''', (url, status, now))

    conn.commit()
    conn.close()

def bulk_update_configs(configs_data: list):
    """
    Updates or inserts multiple configs in a single transaction.
    'configs_data' should be a list of tuples:
    [(config_str, source_url, country, speed, timestamp), ...]
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO configs (config, source_url, country_code, speed_kbps, last_tested) VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(config) DO UPDATE SET
            source_url = excluded.source_url,
            country_code = excluded.country_code,
            speed_kbps = excluded.speed_kbps,
            last_tested = excluded.last_tested
    ''', configs_data)

    conn.commit()
    conn.close()
    print(f"Successfully upserted {len(configs_data)} configs into the database.")

def get_configs_by_country(country_code: str, limit: int = None):
    """Fetches fast and recently tested configs for a specific country."""
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT config FROM configs WHERE country_code = ? ORDER BY speed_kbps DESC"
    if limit:
        query += f" LIMIT {limit}"

    cursor.execute(query, (country_code,))
    configs = [row[0] for row in cursor.fetchall()]
    conn.close()
    return configs

# می‌توانید توابع بیشتری در آینده به اینجا اضافه کنید،
# مثلاً برای پاک کردن کانفیگ‌های قدیمی یا گزارش‌گیری.
