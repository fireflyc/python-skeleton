from python_skeleton.lib.log import LogMixin


class Demo(LogMixin):
    def hello(self, name):
        self.logger.info("demo %s", name)
        return "Hello, " + name
