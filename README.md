# 🌊 RentFlow

Система управления арендой недвижимости

---

## 🚀 Деплой на Render + Netlify + Neon

### 1️⃣ База данных (Neon)

1. Регистрируйся: https://neon.tech
2. Создай проект `rentflow-db`
3. **СКОПИРУЙ строку подключения:**
   ```
   postgresql://user:password@ep-xxx.region.aws.neon.tech/rentflow_db?sslmode=require
   ```

### 2️⃣ Бэкенд (Render)

1. Заходи: https://render.com
2. **New +** → **Web Service**
3. Подключи GitHub репозиторий

**Настройки:**
- **Root Directory**: `backend`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Environment Variables:**
- `DATABASE_URL` = *твоя строка из Neon*
- `PYTHON_VERSION` = `3.11.0`

### 3️⃣ Фронтенд (Netlify)

1. Заходи: https://netlify.com
2. **Add new site** → **Import project**
3. Выбери свой репозиторий

**Настройки:**
- **Base directory**: `frontend`
- **Build command**: `npm run build`
- **Publish directory**: `frontend/dist`

**Environment Variables:**
- `VITE_API_BASE_URL` = `https://твой-url.onrender.com/api`

Потом **Trigger deploy** для применения переменной.

---

## ✅ Проверка

### Бэкенд:
```bash
curl https://твой-url.onrender.com/health
curl https://твой-url.onrender.com/docs
```

### Фронтенд:
Открой `https://твой-сайт.netlify.app`

---

## 🧪 Тестовые аккаунты

**Клиент:**
- Телефон: `+79991234567`
- Пароль: `client123`

**Админ:**
- Логин: `admin`
- Пароль: `admin123`

---

## 💻 Локальная разработка

### Бэкенд:
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Отредактируй .env
uvicorn main:app --reload
```

Доступен: http://localhost:8000

### Фронтенд:
```bash
cd frontend
npm install
cp .env.example .env
# Отредактируй .env
npm run dev
```

Доступен: http://localhost:5173

---

## 📊 Что внутри

- ✅ 12 таблиц БД
- ✅ 54+ API эндпоинта
- ✅ Автоматические тестовые данные
- ✅ Тёмная тема
- ✅ Без JWT (для демо)

**API Docs:** http://localhost:8000/docs

---

🌊 RentFlow - готов к деплою!
