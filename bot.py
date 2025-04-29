import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define a function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Please send your Instagram username and email.')

# Define a function to handle messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text.split()
    
    if len(user_input) < 2:
        update.message.reply_text('Please provide both your username and email in the format: username email')
        return
    
    username = user_input[0]
    email = user_input[1]

    # Call the API with the provided username and email
    api_url = 'https://followerus.com/free-instagram-followers'
    payload = {
        'username': username,
        'email': email
    }

    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            update.message.reply_text('Your information has been submitted successfully!')
        else:
            update.message.reply_text('There was an error submitting your information. Please try again later.')
    except Exception as e:
        logging.error(f'Error: {e}')
        update.message.reply_text('An error occurred. Please try again later.')

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("7503476485:AAFgneSdofU8QlPJRJ497_pRWoVNMcqwcnA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
