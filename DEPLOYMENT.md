# 🚀 Deployment Guide for RentFlow

Complete guide to deploy RentFlow on **Render** (backend), **Netlify** (frontend), and **Neon** (PostgreSQL database).

---

## 📋 Prerequisites

- GitHub account
- Render.com account (free tier available)
- Netlify account (free tier available)
- Neon.tech account (free tier available)

---

## 1️⃣ Database Setup (Neon PostgreSQL)

### Step 1: Create Neon Database

1. Go to [neon.tech](https://neon.tech)
2. Sign up / Log in
3. Click **"Create Project"**
4. Project settings:
   - **Project name**: `rentflow-db`
   - **Region**: Choose closest to your users
   - **PostgreSQL version**: 15
5. Click **"Create Project"**

### Step 2: Get Connection String

1. In your Neon project dashboard, click **"Connection Details"**
2. Copy the **Connection string** (looks like):
   ```
   postgresql://user:password@ep-xxx-xxx.region.aws.neon.tech/rentflow_db?sslmode=require
   ```
3. **Save this URL** - you'll need it for Render!

---

## 2️⃣ Backend Deployment (Render)

### Step 1: Push Code to GitHub

```bash
cd RentFlow
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Create Web Service on Render

1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select **RentFlow** repository

### Step 3: Configure Service

**Basic Settings:**
- **Name**: `rentflow-api`
- **Region**: Oregon (US West) or closest to you
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Environment Variables:**

Click **"Add Environment Variable"** and add:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | *Your Neon connection string from Step 1* |
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | *Generate random string or leave for auto-generate* |
| `ALGORITHM` | `HS256` |

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait 3-5 minutes for deployment
3. Your API will be live at: `https://rentflow-api.onrender.com`

### Step 5: Verify Backend

Visit: `https://rentflow-api.onrender.com/docs`

You should see the **Swagger UI** with all API endpoints!

---

## 3️⃣ Frontend Deployment (Netlify)

### Step 1: Update Frontend Config

Edit `frontend/.env` or create `frontend/.env.production`:

```bash
VITE_API_BASE_URL=https://rentflow-api.onrender.com/api
```

Commit and push:
```bash
git add .
git commit -m "Configure production API URL"
git push
```

### Step 2: Deploy to Netlify

**Option A: Via Netlify Dashboard (Recommended)**

1. Go to [netlify.com](https://netlify.com)
2. Click **"Add new site"** → **"Import an existing project"**
3. Choose **GitHub** and select **RentFlow** repository
4. Configure build settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`
5. Click **"Deploy site"**

**Option B: Via Netlify CLI**

```bash
cd frontend
npm install -g netlify-cli
netlify login
netlify init
netlify deploy --prod
```

### Step 3: Configure Environment Variable

In Netlify dashboard:
1. Go to **Site settings** → **Environment variables**
2. Add variable:
   - **Key**: `VITE_API_BASE_URL`
   - **Value**: `https://rentflow-api.onrender.com/api`
3. Click **"Redeploy"** to apply changes

### Step 4: Configure Custom Domain (Optional)

1. Go to **Domain management**
2. Add your custom domain
3. Configure DNS settings

---

## 4️⃣ Verify Deployment

### Backend Health Check
```bash
curl https://rentflow-api.onrender.com/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "RentFlow API v2.0"
}
```

### Frontend Check

Visit: `https://your-site.netlify.app`

You should see the RentFlow homepage!

### Test API Connection

1. Open browser console (F12)
2. Navigate to Properties page
3. Check Network tab - API calls should go to your Render backend
4. You should see properties loaded from the database

---

## 5️⃣ Post-Deployment

### Initialize Database with Test Data

The database will be automatically populated with test data on first backend startup!

Test credentials will be:
- **Admin**: `login='admin'`, `password='admin123'`
- **Client**: `phone='+79998887766'`, `password='client123'`

### Monitor Your Services

**Render:**
- Dashboard: https://dashboard.render.com
- View logs: Click on your service → "Logs" tab

**Netlify:**
- Dashboard: https://app.netlify.com
- View deployments: Click on your site → "Deploys" tab

**Neon:**
- Dashboard: https://console.neon.tech
- Monitor database usage and performance

---

## 🔧 Troubleshooting

### Backend Issues

**Problem**: Backend crashes on startup
- **Solution**: Check Render logs for error messages
- Common issue: DATABASE_URL not set correctly

**Problem**: Database connection error
- **Solution**: Verify Neon connection string includes `?sslmode=require`

### Frontend Issues

**Problem**: API calls fail (CORS errors)
- **Solution**: Backend CORS is set to allow all origins (`*`)
- Check browser console for actual error

**Problem**: Environment variable not loaded
- **Solution**: Vite requires `VITE_` prefix for env vars
- Redeploy after changing env vars

### Database Issues

**Problem**: Tables not created
- **Solution**: Backend creates tables automatically on startup
- Check Render logs for migration errors

**Problem**: Test data not loaded
- **Solution**: Test data is created on first startup only
- To recreate: In Neon dashboard, drop all tables and restart backend

---

## 📊 Free Tier Limits

### Neon (Database)
- ✅ 512 MB storage
- ✅ 1 project
- ✅ Unlimited compute hours
- ✅ Auto-suspend after 5 minutes of inactivity

### Render (Backend)
- ✅ 750 hours/month (enough for 1 service)
- ✅ 512 MB RAM
- ❌ Spins down after 15 min inactivity (first request takes ~30s)
- ❌ Monthly usage resets

### Netlify (Frontend)
- ✅ 100 GB bandwidth/month
- ✅ 300 build minutes/month
- ✅ Instant cache invalidation
- ✅ Automatic HTTPS

---

## 🎉 Success!

Your RentFlow application is now live!

**Frontend**: `https://your-site.netlify.app`
**Backend API**: `https://rentflow-api.onrender.com`
**API Docs**: `https://rentflow-api.onrender.com/docs`

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Netlify Documentation](https://docs.netlify.com)
- [Neon Documentation](https://neon.tech/docs)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)
- [Vite Deployment Guide](https://vitejs.dev/guide/static-deploy.html)

---

**Need help?** Check the logs in Render/Netlify dashboards or create an issue on GitHub.

🌊 Happy RentFlowing! 🚀
