# 📦 Create Discord Bot

A clean and modular Discord bot template using Python and `Pycord`.  
Designed to be scalable, maintainable, and suitable for developers who prefer modular organization.

[![Python](https://img.shields.io/badge/Python-3.8-blue.svg?style=flat-square)]()
[![Python](https://img.shields.io/badge/Pycord-2.6.1-blue.svg?style=flat-square)]()

## 🧩 Features

- 🧱 Modular command and event handling system (Cogs)
- 🌍 Support for multilingual extensions (localizations/)
- 🔧 Designed for easy expansion and maintenance
- 📝 Clear project directory structure and layering

---

## 🚀 Getting Started

### 🛠️ Register a Discord bot application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Go to the **Bot** tab and add a bot user to your application.
   - Copy the `TOKEN` (keep this private!).
3. In the **Bot** tab, scroll down and enable:

   - ✅ Presence Intent
   - ✅ Server Members Intent
   - ✅ Message Content Intent

   > For more info:  
   > 👉 [Gateway Intents Documentation](https://discord.com/developers/docs/topics/gateway#gateway-intents)

---

## 🧱 Project Structure

```
📁 pycord-bot-template/
├── cogs/                  # Modular command & event handlers
│   ├── commands/
│   │   └── moderation/    # Moderation commands
│   │       └── message_clean.py
│   │   └── dev.py
│   │── events/     # Custom event handlers
│   └── __init__.py
├── core/
│   ├── bot.py             # Main bot setup
│   └── loader.py          # Cog loader
├── data/                  # (Reserved) Data and cache
├── localizations/
│   ├── get_locale.py      # Locale handling
│   └── locale.json        # Example localization data
├── utils/
│   ├── __init__.py
│   └── utils.py           # Utility functions
├── views/                 # (Optional) Discord UI views
├── .env                   # Token and secrets (DO NOT SHARE)
├── .gitignore
├── main.py                # Entry point
└── requirements.txt       # Python dependencies
```

---

## 🏗️ Views - Discord UI Components

The `views/` folder contains reusable Discord UI components such as:

- Buttons
- SelectMenus
- TextInputs

This allows for centralized management and easy reuse of UI elements, improving maintainability and scalability.

---

## ⚙️ Cogs Auto-Loading

The project features an automatic cog loader that recursively searches through the entire cogs/ directory and its subdirectories.

You can exclude entire directories from being loaded by placing a special `__ignore__` file inside the folder. This provides a simple way to control which cogs are active without modifying code.

## 📦 Install Dependencies

Ensure you have Python 3.8 or higher installed.

Install the required packages with:

```bash
pip install -r requirements.txt
```

OR

```bash
pip install -U py-cord python-dotenv
```

---

## ▶️ Run the Bot

Make sure your bot token is set properly in the `.env` file:

```
TOKEN="your_token_here"
```

Then, run the bot using:

```bash
python main.py
```
