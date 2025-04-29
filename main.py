import logging

# Configure logging to write to a file
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")
    try:
        x = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        raise

if __name__ == "_main_":
    main()