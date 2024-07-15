from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

class VannaBot:
    TOKEN: Final = '7294024935:AAG-1Q7iCYQbqnA3d9MtSTa7ENK-APb5l8Q'
    BOT_USERNAME: Final = '@VannaMBFBot'

    def __init__(self):
        self.app = Application.builder().token(self.TOKEN).build()

        # Commands
        self.app.add_handler(CommandHandler('start', self.start_command))
        self.app.add_handler(CommandHandler('help', self.help_command))
        self.app.add_handler(CommandHandler('custom', self.custom_command))

        # Message Handler
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

        # Errors
        self.app.add_error_handler(self.error)

    # Command Handlers
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Welcome to Vbot')

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Welcome to Vbot, What can I help you with?')

    async def custom_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('This is a custom command!')

    # Response Handler
    def handle_response(self, text: str) -> str:
        processed: str = text.lower()

        responses = {
            'hello': 'Hey there!',
            'how are you': 'I am fine, thank you!',
            'i love python': 'Python is awesome!',
            'what is your name': 'I am Vbot!',
            'what can you do': 'I can chat with you!',
            'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
            'who created you': 'I was created by my developer.',
            'what is the weather today': 'I am not sure, but you can check a weather website!',
            'where are you from': 'I am from the internet!',
            'what is your favorite color': 'I love the color blue!',
            'do you like music': 'Yes, music is wonderful!',
            'what is your favorite food': 'I don’t eat, but I hear pizza is great!',
            'how old are you': 'I am timeless!',
            'what is the meaning of life': '42',
            'do you like sports': 'I enjoy watching sports!',
            'what is your favorite sport': 'I like soccer!',
            'can you help me': 'Of course, I am here to help!',
            'do you know any good movies': 'The Matrix is a classic!',
            'what is your hobby': 'Chatting with people like you!',
            'do you have any pets': 'No, but I like cats!',
            'can you dance': 'I wish I could!',
            'do you like games': 'Yes, games are fun!',
            'what is your favorite game': 'I like chess!',
            'can you sing': 'I wish I could!',
            'do you know any jokes': 'Why don’t skeletons fight each other? They don’t have the guts!',
            'can you drive': 'No, I can’t drive.',
            'do you like traveling': 'Yes, I like learning about new places!',
            'what is your favorite place': 'I love virtual worlds!',
            'can you cook': 'No, but I can share recipes!',
            'what is your favorite book': 'I like sci-fi books!',
            'do you like reading': 'Yes, reading is great!',
            'can you help me with my homework': 'I can try to help!',
            'what is your favorite subject': 'I like computer science!',
            'do you know any programming languages': 'Yes, I know Python!',
            'can you code': 'Yes, I can write some code!',
            'do you like robots': 'Yes, robots are cool!',
            'what is your favorite movie': 'I like The Matrix!',
            'do you watch TV': 'No, but I know about TV shows!',
            'can you play instruments': 'No, I can’t play instruments.',
            'what is your favorite instrument': 'I like the piano!',
            'do you know any magic tricks': 'No, but magic is fun!',
            'can you swim': 'No, I can’t swim.',
            'do you like the ocean': 'Yes, the ocean is fascinating!',
            'what is your favorite animal': 'I like dolphins!',
            'do you know any animals': 'Yes, I know many animals!',
            'can you draw': 'No, I can’t draw.',
            'do you like art': 'Yes, art is beautiful!',
            'what is your favorite art': 'I like digital art!',
            'can you help me with math': 'Sure, I can try!',
            'do you like math': 'Yes, math is interesting!',
            'what is your favorite number': 'I like the number 7!',
            'can you help me with science': 'Sure, I can try!',
            'do you like science': 'Yes, science is fascinating!',
            'what is your favorite science': 'I like physics!',
            'can you tell me a fact': 'Sure! Did you know honey never spoils?',
            'do you know any facts': 'Yes, I know many facts!',
            'can you tell me a story': 'Once upon a time...',
            'do you like stories': 'Yes, stories are great!',
            'what is your favorite story': 'I like adventure stories!',
            'can you speak other languages': 'I can understand some!',
            'do you like languages': 'Yes, languages are interesting!',
            'what is your favorite language': 'I like Python!',
            'can you help me with history': 'Sure, I can try!',
            'do you like history': 'Yes, history is important!',
            'what is your favorite historical event': 'I like the moon landing!',
            'can you tell me a quote': 'Sure! "To be or not to be, that is the question."',
            'do you know any quotes': 'Yes, I know many quotes!',
            'can you help me with geography': 'Sure, I can try!',
            'do you like geography': 'Yes, geography is fascinating!',
            'what is your favorite country': 'I like Japan!',
            'can you help me with physics': 'Sure, I can try!',
            'do you like physics': 'Yes, physics is interesting!',
            'what is your favorite physics concept': 'I like quantum mechanics!',
            'can you help me with chemistry': 'Sure, I can try!',
            'do you like chemistry': 'Yes, chemistry is fun!',
            'what is your favorite chemical': 'I like H2O!',
            'can you help me with biology': 'Sure, I can try!',
            'do you like biology': 'Yes, biology is amazing!',
            'what is your favorite biology topic': 'I like genetics!',
            'can you help me with literature': 'Sure, I can try!',
            'do you like literature': 'Yes, literature is great!',
            'what is your favorite book': 'I like 1984 by George Orwell!',
            'can you help me with grammar': 'Sure, I can try!',
            'do you like grammar': 'Yes, grammar is important!',
            'what is your favorite grammar rule': 'I like the Oxford comma!',
            'can you help me with coding': 'Sure, I can try!',
            'do you like coding': 'Yes, coding is fun!',
            'what is your favorite coding language': 'I like Python!',
            'can you help me with algorithms': 'Sure, I can try!',
            'do you like algorithms': 'Yes, algorithms are powerful!',
            'what is your favorite algorithm': 'I like sorting algorithms!',
            'can you help me with data structures': 'Sure, I can try!',
            'do you like data structures': 'Yes, data structures are important!',
            'what is your favorite data structure': 'I like trees!',
            'can you help me with databases': 'Sure, I can try!',
            'do you like databases': 'Yes, databases are essential!',
            'what is your favorite database': 'I like SQLite!',
            'can you help me with networks': 'Sure, I can try!',
            'do you like networks': 'Yes, networks are fascinating!',
            'what is your favorite network protocol': 'I like TCP/IP!',
            'can you help me with security': 'Sure, I can try!',
            'do you like security': 'Yes, security is crucial!',
            'what is your favorite security topic': 'I like encryption!'
        }

        for key in responses:
            if key in processed:
                return responses[key]

        return 'Sorry, I do not understand that.'

    # Message Handler
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_type: str = update.message.chat.type
        text: str = update.message.text

        print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

        if message_type == 'group':
            if self.BOT_USERNAME in text:
                new_text: str = text.replace(self.BOT_USERNAME, '').strip()
                response: str = self.handle_response(new_text)
            else:
                return
        else:
            response = self.handle_response(text)

        print('Bot:', response)
        await update.message.reply_text(response)

    # Error Handler
    async def error(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')

    # Run Bot
    def run(self):
        print('Starting bot...')
        print('Polling...')
        self.app.run_polling(poll_interval=3)

if __name__ == "__main__":
    bot = VannaBot()
    bot.run()
