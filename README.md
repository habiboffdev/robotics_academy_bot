# Robotics Academy Bot

> **One of my very first programming projects (8th grade)**
>
> A Telegram bot I developed in 8th grade to streamline student registration for my teacher’s private academy lessons. It served as my first hands‑on experience integrating with real‑world users.

## 🚀 Features

- **User Registration:** Students can register for lessons via simple bot commands.
- **Lesson Management:** Admins can create, update, and remove lesson offerings directly through Telegram.
- **Persistent Storage:** All student and lesson data are stored in a local SQLite3 database.
- **Modular Architecture:** Clean code structure for easy extension and maintenance.

---

## 🔧 Technologies

- **Language:** Python 3.8+
- **Telegram API:** pyTelegramBotAPI
- **Database:** SQLite3
- **Environment Variables:** python-dotenv (optional)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/habiboffdev/robotics_academy_bot.git
   cd robotics_academy_bot
   ```
2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the bot**
   - Rename `.env.example` to `.env`
   - Add your `TELEGRAM_BOT_TOKEN` to the `.env` file
5. **Initialize the database**
   ```bash
   python init_db.py
   ```
6. **Run the bot**
   ```bash
   python bot.py
   ```

---

## 📖 Usage

- `/start` — Show welcome message and usage instructions.
- `/lessons` — List available lessons with schedules.
- `/register` — Register the user for a selected lesson.
- `/my_registrations` — Display the user's current lesson registrations.

**Admin Commands (restricted):**
- `/add_lesson` — Create a new lesson offering.
- `/remove_lesson` — Delete an existing lesson.

---

## 🗄️ Database Schema

| Table           | Columns                                        |
|-----------------|------------------------------------------------|
| `students`      | `id` (PK), `telegram_id`, `name`, `registered_at` |
| `lessons`       | `id` (PK), `title`, `description`, `schedule`    |
| `registrations` | `id` (PK), `student_id` (FK), `lesson_id` (FK)` |

---

## 🤝 Contributing

Contributions are welcome! To propose changes:
1. Fork this repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Happy coding!*

