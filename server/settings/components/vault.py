"""
Vault settings.
"""
import os
import sys

import hvac

from collections import Mapping

from requests.exceptions import RequestException

__all__ = ["VaultSettings", "vault_settings"]


class VaultSettings(Mapping):
    """
        A container for associating key/value pairs that are
        fetched from Hashicorp Vault.

        >>> settings = VaultSettings(url, user, secret, path)
        >>> settings["BRAINTREE_SECRET_KEY"]
        >>> settings.get("STRIPE_SECRET_KEY", "123")

        If there is no such var in Vault - try to find it in env vars
        or return `default` if provided with `.get` method.

    """

    def __init__(self, url, user, secret, path):
        self._config_storage = dict()

        try:
            if not os.getenv("IGNORE_VAULT", "") == "true":
                client = hvac.Client(url=url)
                client.auth_userpass(user, secret)
                self._config_storage = client.read(path)["data"]
        except hvac.exceptions.VaultError as exc:
            sys.stderr.write(
                (
                    "\x1b[1;31m"
                    "Failed to fetch settings storage from vault server. Exception: "
                    "{}. \n"
                    "Using default ENV."
                    "\x1b[0m"
                    "\n"
                ).format(exc)
            )
        except RequestException as exc:
            sys.stderr.write(
                (
                    "\x1b[1;31m"
                    "Failed to connect with a vault server. Exception: "
                    "{}. \n"
                    "Using default ENV."
                    "\x1b[0m"
                    "\n"
                ).format(exc)
            )

    def __getitem__(self, key):
        """
            >>> for var in self: ...
        """
        try:
            return self._config_storage[key]
        except KeyError:
            return os.environ[key]

    def __iter__(self):
        return iter(self._config_storage)

    def __len__(self):
        return len(self._config_storage)

    def get(self, key, default=None):
        """
            >>> self.get("MY_SECRET_KEY", default="123")
        """
        try:
            return self[key]
        except KeyError:
            return default


VAULT_URL = os.getenv("VAULT_URL", "https://vault.example.com:443")
VAULT_USER = os.getenv("VAULT_USER", "")
VAULT_PASSWORD = os.getenv("VAULT_PASSWORD", "")
VAULT_CONFIGPATH = os.getenv("VAULT_CONFIGPATH", "")

vault_settings = VAULT_SETTINGS = VaultSettings(
    VAULT_URL, VAULT_USER, VAULT_PASSWORD, VAULT_CONFIGPATH
)
