from configobj import ConfigObj, flatten_errors
from validate import Validator


class JobConfig:
    """ This class ensures we can control access to our config file """

    def __init__(self, ini_file='application.ini',spec_file='application_spec.ini'):
        self.__config = None
        self.__config = ConfigObj(ini_file, configspec=spec_file)

        # Validate our config
        c_validator = Validator()
        c_result = self.__config.validate(c_validator)

        if not c_result:
            # Create an empty settings if our config is invalid
            self.__config = None

    def aqmp_host(self, default=None):
        if self.__config is not None:
            c_section = self.__config['hosts']
            return c_section.get('amqp_host', default)
        return default


if __name__ == '__main__':
    config = ConfigObj('application.ini',configspec='application_spec.ini')
    validator = Validator()
    result = config.validate(validator)
    if result:
        print(config)
    else:
        print('Config file validation failed!')
        for section_list, key, value in flatten_errors(config, result):
            if key is not None:
                print('The "%s" key in the section "%s" failed validation' % (key, ', '.join(section_list)))
            else:
                print('The following section was missing:%s ' % ', '.join(section_list))
