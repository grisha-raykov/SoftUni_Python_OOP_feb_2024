"""
This module is for learning private methods and method name mangling
"""

from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email):
        username, data = email.split('@')
        provider, domain = data.split('.')

        return (self.__is_name_valid(username) and
                self.__is_mail_valid(provider) and
                self.__is_domain_valid(domain))
