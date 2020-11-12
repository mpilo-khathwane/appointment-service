import os
import re
import getconf
import logging

logger = logging.getLogger(__name__)

class ServiceConfig(object):
    def __init__(self, env_namespace=None, ini_files=None):
        if env_namespace is None:
            env_namespace = getconf.NO_NAMESPACE
        if ini_files is not None and not isinstance(ini_files, list):
            ini_files = [ini_files]
        self.env_namespace = env_namespace

        if ini_files is not None and not isinstance(ini_files, list):
            ini_files = [ini_files]
        self.ini_files = ini_files if ini_files is not None else []
        self._load_config()

    def reload(self, **kwargs):
        """
        Change the environment namespace, config files
        """
        if 'env_namespace' in kwargs:
            env_namespace = kwargs['env_namespace']
            if env_namespace is None:
                env_namespace = getconf.NO_NAMESPACE
            self.env_namespace = env_namespace

        if 'ini_files' in kwargs:
            ini_files = kwargs['ini_files']
            if not isinstance(ini_files, list):
                ini_files = [ini_files]
            self.ini_files = ini_files
        self._load_config()

    def _load_config(self):
        for ini_file in self.ini_files:
            if (ini_file is not None) and (not os.path.exists(ini_file)):
                logger.warning('ini-file does not exist: %s', ini_file)
        self._config = getconf.ConfigGetter(self.env_namespace, config_files=self.ini_files)
        self._service_cache = {}

    def _get_section_setting(self, key):
        """
        Map all preceding dots to underscores, except for the last dot.
        This assumes all .ini section nesting is at most one level
        """
        key_split = re.split('\.|\-', key)
        if len(key_split) > 1:
            setting = key_split.pop(-1)
            setting_prefix = "_".join(key_split)
            key = "{}.{}".format(setting_prefix, setting)
        return key

    def _get(self, key, method):
        key = self._get_section_setting(key)
        return getattr(self._config, method)(key)

    def get(self, key):
        """
        Read a configuration setting and return the value as a string.
        Args:
            key (str): The key of the value to look up, in the format 'section.field'. This will
                look for the environment variable PREFIX_SECTION_FIELD, and if not found, the
                section and field in all config files specified in the constructor, and if not found
                the value in defaults['section']['value'].
        """
        return str(self._get(key, 'getstr'))

    get_str = get

    def get_list(self, key):
        """
        Read a configuration setting and return the value as a list of strings.
        This will split on ','.
        """
        return self._get(key, 'getlist')

    def get_bool(self, key):
        """
        Read a configuration setting and return the value as a boolean.
        """
        return self._get(key, 'getbool')

    def get_int(self, key):
        """
        Read a configuration setting and return the value as an integer.
        """
        return self._get(key, 'getint')

    def get_float(self, key):
        """
        Read a configuration setting and return the value as a float.
        """
        return self._get(key, 'getfloat')

    def get_section(self, section_name):
        """
        Return a dict-like object that can be used to query all fields in the given section.
        """
        return self._get(section_name, 'get_section')
