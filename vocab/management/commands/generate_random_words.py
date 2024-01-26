import asyncio
import aiohttp
from asgiref.sync import sync_to_async
from django.core.management import BaseCommand
from vocab.models import Category, RecommendWord
from vocab.management.commands.google_translate import EasyGoogleTranslate

translator = EasyGoogleTranslate(source_language='en', target_language='uk')


async def fetch_random_word(session):
    async with session.get('https://random-word-api.herokuapp.com/word') as response:
        data = await response.json()
        # Assuming the API returns a JSON array with a single word
        return data[0] if data else None


async def fetch_translated_word(word):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, translator.translate, word)


@sync_to_async
def get_random_category():
    return Category.objects.order_by('?').first()


async def create_word_async(session):
    random_word = await fetch_random_word(session)
    translated_word = await fetch_translated_word(random_word)

    # Select a random category
    category = await get_random_category()

    # Create and save Word object
    await sync_to_async(RecommendWord.objects.create)(
        en_word=random_word[0:19],
        ua_word=translated_word[0:19],
        category=category,
    )
    print(f'Word created - Random word {random_word} and Translated word {translated_word}')


async def generate_dummy_data_async():
    async with aiohttp.ClientSession() as session:
        tasks = [create_word_async(session) for _ in range(15)]  # range - amount of words
        await asyncio.gather(*tasks)


class Command(BaseCommand):
    help = 'Generate random data for your database tables'

    async def async_handle(self, *args, **kwargs):
        await generate_dummy_data_async()

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Generating dummy data (async)...'))
        asyncio.run(self.async_handle())
        self.stdout.write(self.style.SUCCESS('Dummy data generated successfully.'))
