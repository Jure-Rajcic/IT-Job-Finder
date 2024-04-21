# ITJobFinder 🌐🔍

Welcome to **ITJobFinder**, a subscription-based web application designed to make the job hunt easier and more efficient for IT professionals. This app scrapes IT job postings from specific Facebook groups that provide transparent information about salaries, and notifies users about new job opportunities directly via WhatsApp.

## Project Status 🚧

- **Back-End**: Work in Progress (Python, Apify, GPT-3, Twilio)
- **Front-End**: Planned (Vue3, Tailwind CSS)
- **Current Version**: Development

## Features 🌟

- **Job Scraping**: Automatically scrapes job postings from [this Facebook group](https://www.facebook.com/groups/2158108910905022) focused on IT jobs with transparent salary disclosures.
- **Real-Time Notifications**: Users receive updates via WhatsApp, ensuring they never miss out on new job opportunities.
- **User Subscriptions**: Allows users to subscribe for specialized notifications tailored to their job preferences and skills.

## Technologies 💻

- **Front-End**: Vue3 + Tailwind CSS (Planned)
- **Back-End**:
  - **Python**: For server-side logic and job scraping automation.
  - **Apify**: To handle the scraping tasks seamlessly.
  - **OpenAI's GPT**: To process and summarize job postings.
  - **Twilio**: For integrating WhatsApp messaging to notify users.

## Setup and Installation 🛠️

> Note: Currently, only the back-end setup is available as the front-end development has not started yet.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ITJobFinder.git
   cd ITJobFinder
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**
   - Copy the `.env.example` file to `.env` and fill in the required API keys and database credentials.

4. **Run the Application**
   ```bash
   python main.py
   ```

## Contribution Guidelines 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.
