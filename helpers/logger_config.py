"""
Module contains functionality for logger configuration:
    - configure_log(file_name) method sets a config file and updates the file name to store logs;
    - RequestFormatter class overrides logging.Formatter class's format method to update log message view.
"""
import re
import logging
import logging.config
import socket
import sys

import yaml

class LogFiles:
    # files with base for all services logging configuration:

    # purpose: to store logs in CLF format in /etrade/home/logs path
    CLF_CONFIG = 'log_config.yml'

    # purpose: to store logs as is within the framework locally
    CONFIG = 'log_config.yml'

    # files' names, where to store logs for a particular service
    # Note: position_service is a micro service of orders_service. So, its logs are stored where order_service's are.
    zephyr = 'zephyr_service'



def configure_log(log_config_file_name, log_storage_file_name):
    """Set a configuration file for logging and update it with the file name for storing logs.
    :param log_config_file_name: name of the file with logger configuration
    :param log_storage_file_name: name of the file where to store logs
    """
    file_path = r"./logs/{log_file_name}.log"
    log_config = yaml.safe_load(open(log_config_file_name))

    if len(sys.argv) > 1 and sys.argv[1] == "run_in_docker":
        file_path = r"/app/logs/{log_file_name}.log"

    log_config["handlers"]["file"]["filename"] = file_path.format(log_file_name=log_storage_file_name)

    logging.config.dictConfig(log_config)


class RequestFormatter(logging.Formatter):
    """Subclass logging.Formatter class to format the log message view."""

    def format(self, record):
        """Override format() method of logging.Formatter, which in turn formats the specified record as text.
        The aim of the overriding: format the creation time to "Common Log Format".
        :param record: LogRecord instance
        :return: formatted record as text
        """

        # Get the message (bound method object) for the LogRecord class
        message = str(record.getMessage)

        # Get the creation time of the specified LogRecord as formatted text
        log_creation_time = self.formatTime(record, datefmt="[%d/%b/%Y:%X %z]")
        host_name = socket.gethostname()
        ip = socket.gethostbyname('localhost')

        log_creation_time_compile = re.compile(r"\[([A-Za-z0-9\/:\s]+)\]")

        if log_creation_time_compile.search(message):
            updated_message = re.sub(r"\[([A-Za-z0-9//:\s]+)\]", f"{log_creation_time}", message)

            # Split the updated with the formatted time message for the LogRecord class by a comma
            list_updated_message = updated_message.split(",")

            # Create a list from the updated with formatted time message for the LogRecord class and splitted by a comma
            list_from_string = list(list_updated_message[4])

            list_from_string = list_from_string[2:-3]

            # Create a string from a ready to log message
            string_from_list = "".join(list_from_string)

        else:
            string_from_list = re.search(r'".*"', message).group()
            string_from_list = string_from_list.replace(r'"', "")

        if log_creation_time not in string_from_list:
            string_from_list = f"{ip} - - {log_creation_time} {string_from_list}"

        # Update the view of the log message in the logs
        record.msg = string_from_list

        return super().format(record)
