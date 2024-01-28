# VocabBuilder
 
## About The Project
<p>Development of the English dictionary using
Django, MySQL database, and integration with
Google Translate API to automatically translate
words from English into Ukrainian. Use of
asynchronous technologies and code
optimization for efficient query processing</p>
<p>Website url: <a href="https://v1van.pythonanywhere.com/">Link</a></p>
<div style="display: flex; flex-direction: row;">
  <div style="display: flex; flex-direction: column; width: 90%;">
    <img src="https://github.com/IvanVoloshanskyi/VocabBuilder/assets/93157729/4bdcaaf6-ef37-4130-a617-a0283664bb18" style="width: 100%;">
    <img src="https://github.com/IvanVoloshanskyi/VocabBuilder/assets/93157729/f4ba9071-8a90-4024-b1ca-75abf1804085" style="width: 100%;">
  </div>
  <div style="width: 29.3%;">
    <img src="https://github.com/IvanVoloshanskyi/VocabBuilder/assets/93157729/0db625ce-7c1d-4bcd-a55a-f0782d7d35b9" style="width: 100%;">
  </div>
</div>
<p>The mobile layout was designed for phones with a 6.1-inch screen.</p>
<p>Best for all iPhones of the "pro" version</p>

### Built With

* Django
* MYSQL
* API


## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/IvanVoloshanskyi/VocabBuilder.git
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Create .env file and enter your data from ".env-samples" file `.env`
   ```python
   DB_NAME=ENTER YOUR DATABASE NAME;
   ```

4. Create migrations to your DB
   ```sh
   python manage.py makemigrations
   ```
   ```sh
   python manage.py migrate
   ```

5. Generate some words to Recommend Page
   ```sh
   python manage.py generate_random_words
   ```

6. Run project
   ```sh
   python manage.py runserver
   ```
