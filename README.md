# AI-Finance Tracker

> Локальний фінансовий помічник з AI: трекер витрат/доходів + інтелектуальні поради.

**Статус:** MVP → AI-повний апгрейд

---

## Швидкий старт (якщо хочеш запустити локально, `fast and dirty`)

```bash
# клонюємо репо
git clone <repo-url>
cd ai_finance_tracker

# створюємо віртуальне оточення
python -m venv .venv
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate      # Windows

# ставимо залежності
pip install -r requirements.txt

# створюємо .env на основі .env.example і кидаємо туди ключі
cp .env.example .env
# відредагуй .env: DATABASE_URL, SECRET_KEY, OPENAI_API_KEY (за потреби)

# запускаємо сервер
uvicorn app.main:app --reload --port 8000

# відкриваємо у браузері
http://localhost:8000/docs  # автогенерована документація FastAPI
```

---

## Що тут всередині (коротко)

* `app/` — основний backend (FastAPI)

  * `models/` — SQLAlchemy / Pydantic моделі
  * `routes/` — API endpoints (auth, transactions, analytics, ai)
  * `services/` — бізнес-логіка
  * `utils/` — db, security, validators
  * `templates/` & `static/` — UI якщо треба

* `ai_models/` — NLP-класифікатор, предиктор витрат, LLM-advisor

* `migrations/` — alembic

* `tests/` — тести

* `config.py`, `.env.example`, `requirements.txt`, `run.py`

---

## Конфіг / .env (мінімум)

```env
# приклад .env
DATABASE_URL=sqlite:///./db.sqlite3
SECRET_KEY=super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
OPENAI_API_KEY=sk-...
# інші ключі для HuggingFace або зовнішніх сервісів
```

---

## API (основні ендпоінти)

> Документація автогенерується у `/docs`, але тут теж коротко.

### Auth

* `POST /api/auth/register` — реєстрація `{ "email": "", "password": "" }`
* `POST /api/auth/login` — логін, повертає JWT

### Transactions

* `POST /api/transactions` — додати транзакцію `{ "amount": 100, "description": "Uber", "date": "2025-09-09" }`
* `GET /api/transactions` — список транзакцій (під JWT)
* `PUT /api/transactions/{id}` — редагувати
* `DELETE /api/transactions/{id}` — видалити

### Analytics

* `GET /api/analytics/categories` — зведення по категоріях
* `GET /api/analytics/chart?from=YYYY-MM-DD&to=YYYY-MM-DD` — дані для графіка

### AI

* `POST /api/ai/categorize` — AI-категоризація тексту транзакції
* `GET /api/ai/predict?months=1` — прогноз витрат
* `POST /api/ai/advice` — отримати поради: `{ "prompt": "Як я можу зекономити?" }`

---

## Як працює AI (коротко)

1. **Categorizer** — простий NLP-класіфікатор (скрипт `ai_models/categorizer.py`) тренується на описах транзакцій і категоріях.
2. **Predictor** — часові ряди (Prophet або sklearn) роблять прогноз майбутніх витрат.
3. **Advisor** — LLM (OpenAI або локальна модель) генерує пояснення і поради, бере на вхід агреговані дані користувача + prompt.

> Мінімальний workflow для AI: транзакції → агрегатні фічі → predictor/categorizer → поради/advice.

---

## Roadmap (MVP → Pro)

**Тиждень 1 — MVP**

* Auth, CRUD транзакцій, прості endpoint’и
* Простий dashboard (HTML/урли) або Postman-колекція

**Тиждень 2 — Basic AI**

* Категоризація на NLP (rule-based + простий sklearn)
* API для категоризації

**Тиждень 3 — Analytics & Predict**

* Графіки, predictor (Prophet), базовий UI

**Тиждень 4 — LLM advisor**

* Інтеграція з OpenAI / HuggingFace
* Чат-подібний endpoint + готові prompt’и

**Pro features**

* Підтягування транзакцій з банківських CSV
* Телеграм-бот / мобільний клієнт
* SaaS: multi-tenant + підписки

---

## Тестування

```bash
# pytest
pytest -q
```

---

## Docker (швидко)

`Dockerfile` і `docker-compose.yml` — рекомендую робити у папці `deploy/`. Базовий `docker-compose` запускає DB + web.

---

## Поради для девелопа (ти — мамкін хакер, але роби як профі)

* Робити маленькі коміти і зрозумілі message
* Писати тести на сервіси (особливо AI logic)
* Відокремлювати конфіги — не пхай ключі у git
* Якщо плануєш масштаб — одразу думай про Postgres + Alembic

---

## Контриб'юція

1. Форкни репо
2. Створи фічеву гілку `feature/awesome-stuff`
3. Пул реквест — описуй фічу коротко

---
