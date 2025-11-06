# RentFlow Frontend

Vue.js 3 frontend for RentFlow property rental management system.

## Features

- Modern Vue.js 3 with Composition API
- Beautiful dark theme UI
- Responsive design
- State management with Pinia
- Client-side routing with Vue Router
- Pure CSS (no CSS frameworks)

## Tech Stack

- **Vue.js 3** - Progressive framework
- **Composition API** - Modern Vue development
- **Vue Router 4** - Routing
- **Pinia** - State management
- **Axios** - HTTP client
- **Vite** - Build tool
- **Pure CSS** - Custom dark theme

## Setup

1. Install dependencies:
```bash
npm install
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with API URL
```

3. Run development server:
```bash
npm run dev
```

4. Build for production:
```bash
npm run build
```

## Project Structure

```
frontend/
├── src/
│   ├── api/              # API services
│   │   ├── axios.js      # Axios config
│   │   └── services/     # API endpoints
│   ├── components/       # Vue components
│   │   ├── common/       # Reusable components
│   │   └── layout/       # Layout components
│   ├── views/            # Pages
│   │   ├── client/       # Client pages
│   │   ├── admin/        # Admin pages
│   │   └── auth/         # Auth pages
│   ├── stores/           # Pinia stores
│   ├── router/           # Vue Router
│   ├── styles/           # CSS files
│   │   ├── variables.css # Dark theme variables
│   │   ├── components.css
│   │   └── main.css
│   └── main.js           # Entry point
└── index.html
```

## Dark Theme

The frontend features a custom dark theme with:

- **Primary:** Blue (#3b82f6)
- **Background:** Dark blue-gray (#0f172a)
- **Text:** Light gray (#f1f5f9)
- **Components:** Glassmorphism effects
- **Shadows:** Enhanced for dark backgrounds

## Components

### Common Components
- `BaseButton` - Styled button component
- `BaseInput` - Input with validation
- `BaseCard` - Card container
- `BaseModal` - Modal dialog
- `BaseLoader` - Loading spinner

### Layout Components
- `AppHeader` - Application header
- `AppFooter` - Application footer
- `AdminSidebar` - Admin navigation

## Pages

### Client Pages
- `/` - Home page
- `/properties` - Property listings
- `/properties/:id` - Property details
- `/client/profile` - User profile
- `/client/applications` - My applications
- `/client/contracts` - My contracts

### Admin Pages
- `/admin/dashboard` - Dashboard
- `/admin/properties` - Properties management
- `/admin/applications` - Applications management
- `/admin/clients` - Clients management

## Development

```bash
# Run dev server
npm run dev

# Build
npm run build

# Preview build
npm run preview
```

## Deployment

See main README.md for deployment instructions.
