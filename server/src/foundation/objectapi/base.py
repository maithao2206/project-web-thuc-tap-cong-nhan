import importlib
from flask import Flask, g, session
from foundation.core.datalayer import MongoInterface
from foundation.core.api import BaseAPI
import functools
from foundation.core.api.helper import make_error
from . import config, logger


class ObjectApiServer(Flask):

    def __init__(self, appname, appconfig, **kwargs):
        logger.info('Init ObjectApiServer')

        kwargs.pop('taskapp', None)
        self.modules = kwargs.pop('modules', None)

        datalayer = kwargs.pop('datalayer', MongoInterface)
        self.data = datalayer()

        self.__resource__ = {}
        self.__routes__ = []
        self.__policy__ = []

        self.setup_module()

        config.update(appconfig)

        super(ObjectApiServer, self).__init__(appname)

        self.config.update(config)
        self.init_routes()
        self.init_resource()

    def before_request(self):
        g.user = None
        if session.get("username"):
            g.user = session.get("username")
        if config["AUTH_FIELD"] == "user":
            session["AUTH_FIELD"] = True
        else:
            session["AUTH_FIELD"] = False

    def login_required(self, view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            self.before_request()
            if g.user is None:
                return make_error(status=400, description="You have to login")

            return view(**kwargs)

        return wrapped_view

    def init_routes(self):
        for route_func, args, kwargs in self.__routes__:
            self.route(*args, **kwargs)(route_func)

    def init_resource(self):
        logger.info('Init Resource')
        for name, model in self.__resource__.items():
            baseApi = BaseAPI(self.data, model)

            resource_list = '/' + name
            resource_item = "/%s/<_id>" % name

            self.add_url_rule(resource_list, "get_list_%s" %
                              name, (baseApi.get), methods=['GET'])
            self.add_url_rule(resource_item, "get_item_%s" %
                              name, (baseApi.get_item), methods=['GET'])

            self.add_url_rule(resource_list, "create_%s" %
                              name, self.login_required(baseApi.create), methods=['POST'])
            self.add_url_rule(resource_item, "update_%s" % name,
                              self.login_required(baseApi.update_item), methods=['PATCH'])

            self.add_url_rule(resource_item, "delete_%s" % name,
                              self.login_required(baseApi.delete_item), methods=['DELETE'])

    def setup_module(self):
        modules = config['MODULES']
        modules.extend(self.modules)
        for module_name in modules:
            logger.info('Setup module %r', module_name)
            module = importlib.import_module(module_name)
            module.__setup__(self)

    def resource(self, key, resource):
        # This function use to register a resource for current module
        logger.info('Register resource [%r]', key)
        if key not in self.__resource__:
            self.__resource__[key] = resource
        else:
            logger.info('Resource [%r] already register', key)

    def endpoint(self, *args, **kwargs):
        def _decorator(route_func):
            self.__routes__.append((route_func, args, kwargs))
            return route_func
        return _decorator

    def policy(self):
        # This function use to register a policy for current module
        logger.info('Register policy')
